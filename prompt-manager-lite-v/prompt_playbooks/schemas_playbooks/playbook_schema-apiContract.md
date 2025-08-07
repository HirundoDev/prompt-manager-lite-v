# Schema Playbook — apiContract

Propósito: especificación única y verificable de endpoints, parámetros, autenticación y respuestas.

Ubicación: `schemas/master_blueprint_parts/apiContract.json`

Claves:
- Identidad/versionado: `version` (string), `servers[]` (url, description), `tags[]`
- `authentication`: { type: OAuth 2.0 | JWT | API Key | None, details, oauth2?, apiKey?, jwt? }
- `endpoints[]` (por operación):
  - Básico: `path`, `method`, `summary`, `description`, `operationId`, `tags[]`
  - Parámetros: `parameters[]` { name, in(path|query|header|cookie), required, schema, description }
  - Request: `request` { contentTypes[], headers{}, bodySchema }
  - Respuestas: `responses[]` { status, description, headers{}, bodySchema, example }
  - Seguridad por operación: `security` { scopes[], roles[] }
  - Políticas por operación: `idempotencyKey` (bool), `rateLimit` { policy, headers[] }, `caching` { etag, lastModified, cacheControl }, `tracing` { correlationIdHeader }
- Reutilizables: `components` { schemas{}, parameters{}, headers{}, responses{} }
- Políticas globales: `policies` { errorModel{}, pagination{}, rateLimit{}, caching{}, deprecation{}, retries{}, timeouts{}, headersReserved{} }

Pasos:
1) Inventariar rutas/handlers del backend y definir `servers`, `version`, `tags`.
2) Para cada endpoint, definir `operationId`, `summary`, `parameters`, `request`, `responses`.
3) Establecer `security` por operación (scopes/roles) y políticas (`idempotencyKey`, `rateLimit`, `caching`, `tracing`).
4) Normalizar DTOs en `components.schemas` y referencias cruzadas.
5) Validar tipos con `dataModelDictionary` y alinear errores con `policies.errorModel`.
6) Documentar casos de paginación/sorting/filtering en `policies.pagination` y parámetros reservados.

Checklist:
- [ ] `servers` y `version` definidos; `tags` globales.
- [ ] Autenticación definida y detalles por tipo (OAuth2/API Key/JWT).
- [ ] Todos los endpoints listados con `operationId`, `summary`, `tags`.
- [ ] `parameters` completos (path/query/header/cookie) con `required` y `schema`.
- [ ] `request` y `responses` por status con headers y ejemplos.
- [ ] `security` por operación (scopes/roles) cuando aplique.
- [ ] `policies` globales: `errorModel`, `pagination`, `rateLimit`, `caching`, `deprecation`, `retries`, `timeouts`, `headersReserved`.
- [ ] `components` reutilizables poblados (schemas/parameters/headers/responses).
- [ ] Tipos alineados con `dataModelDictionary`.

Ejemplo mínimo:
```json
{
  "authentication": {"type":"JWT","details":"Authorization: Bearer <token>"},
  "endpoints": [
    {"path":"/users/{id}","method":"GET","responseBodySchema":{"type":"object","properties":{"id":{"type":"string"}}}}
  ]
}
```

Ejemplo avanzado (fragmento):
```json
{
  "version": "1.0.0",
  "servers": [{ "url": "https://api.example.com", "description": "prod" }],
  "tags": ["users"],
  "authentication": { "type": "OAuth 2.0", "oauth2": { "flows": ["client_credentials"], "tokenUrl": "https://idp/token", "scopes": ["users:read"] } },
  "components": { "schemas": { "User": { "type": "object" } }, "responses": {}, "parameters": {}, "headers": {} },
  "policies": {
    "errorModel": { "type": "object", "properties": { "code": {"type":"string"}, "message": {"type":"string"} } },
    "pagination": { "style": "page", "defaultPageSize": 20, "maxPageSize": 100 },
    "rateLimit": { "headers": ["X-RateLimit-Limit","X-RateLimit-Remaining"] },
    "caching": { "etag": true, "lastModified": true },
    "deprecation": { "policy": "sunset header 90 días" }
  },
  "endpoints": [
    {
      "path": "/users/{id}",
      "method": "GET",
      "operationId": "getUser",
      "summary": "Get user by id",
      "tags": ["users"],
      "parameters": [ { "name": "id", "in": "path", "required": true, "schema": {"type":"string"} } ],
      "responses": [ { "status": 200, "description": "OK", "bodySchema": {"$ref":"#/components/schemas/User"} } ],
      "security": { "scopes": ["users:read"] },
      "caching": { "etag": true }
    }
  ]
}
```

Referencia avanzada:
- `prompt_playbooks/playbook-apiContract.md` (trazado estático)
- `docs/DOC008-APISpecification.md`
