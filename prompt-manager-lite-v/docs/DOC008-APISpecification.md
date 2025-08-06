# Plantilla Maestra: Especificación de la API (Estilo OpenAPI)

> **Propósito:** Definir de manera inequívoca el contrato de la API, sirviendo como la única fuente de verdad para los desarrolladores de frontend y backend.
> **Playbook de Referencia:** `playbook-v2-DOC008-APISpecification.md`

<!-- 
  INSTRUCCIONES PARA LA IA (API Architect Agent):
  - Tu misión es documentar cada endpoint de la API basándote en la sección `apiContract` del `master_blueprint.json`.
  - Mantén la estructura similar a la de una especificación OpenAPI para familiaridad.
-->

# Especificación de la API: [Nombre del Proyecto]

**URL Base:** `[URL base de la API, ej. /api/v1]`
**Versión:** `[Versión de la API, ej. 1.0.0]`

---

## 1. Autenticación

[Descripción del método de autenticación, desde `apiContract.authentication.strategy`. Ej. Bearer Token (JWT)]

**Flujo:**
1.  El cliente solicita un token al endpoint `POST /auth/login`.
2.  El servidor valida las credenciales y devuelve un JWT.
3.  El cliente debe incluir el token en la cabecera `Authorization` para todas las peticiones protegidas:
    `Authorization: Bearer <token>`

## 2. Manejo de Errores

La API utiliza códigos de estado HTTP estándar. El cuerpo de la respuesta de error sigue este formato:

```json
{
  "statusCode": 404,
  "message": "Recurso no encontrado",
  "error": "Not Found"
}
```

## 3. Límite de Tasa (Rate Limiting)

[Descripción de la política de límite de tasa, desde `apiContract.rateLimiting`.]

## 4. Endpoints

[Iterar sobre `apiContract.endpoints` para generar una sección para cada uno.]

### `[MÉTODO]` `[ruta]`

> [Descripción del endpoint, desde `endpoint.description`]

**Parámetros de Ruta:**

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `[param.name]` | `[param.type]` | `[param.description]` |

**Cuerpo de la Petición (`requestBody`):

```json
// Desde `endpoint.requestSchema`
```

**Respuesta Exitosa (200 OK):**

```json
// Desde `endpoint.responseSchema`
```