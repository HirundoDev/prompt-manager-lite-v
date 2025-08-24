# Ejemplo: Comentarios de un post
GET    /api/v1/posts/:postId/comments
POST   /api/v1/posts/:postId/comments
GET    /api/v1/posts/:postId/comments/:id
```

---


# Especificación de API - Marco de Referencia

**Sesión:** BACKEND-API-SETUP  
**Fecha:** 2025-01-20  
**Marco Universal:** Especificación de API  
**Referencia:** [playbooks/documentation_playbooks/DOC008-APISpecification.md](../../../playbooks/documentation_playbooks/DOC008-APISpecification.md)

---


## ⚠️ Manejo de Errores


## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para la especificación y diseño de APIs, adaptable a cualquier estilo arquitectónico.


## 🏗️ Arquitectura de API


## 📄 Paginación y Filtrado


## 📊 Esquemas de Datos


## 📊 Monitoring y Analytics


## 📝 Documentación


## 🔄 Próximos Pasos


## 🔄 Versionado


## 🔌 Endpoints y Recursos


## 🔐 Autenticación y Autorización


## 🧪 Testing


### Backwards Compatibility
**Decisión:** [Política de compatibilidad]
- **Breaking changes:** [Solo en major versions]
- **Additive changes:** [En minor versions]
- **Bug fixes:** [En patch versions]

---


### Base URL y Estructura
**Decisión:** [Estructura base de la API]
```
Base URL: [DEFINIR]
API Version: [v1, v2, etc.]
Full URL Pattern: [https://api.example.com/v1/resource]
```


### Content Type y Serialización
**Decisión:** [Formato de datos]
- **Request Format:** [JSON, XML, Form Data, etc.]
- **Response Format:** [JSON, XML, etc.]
- **Encoding:** [UTF-8, etc.]

---


### Convenciones de Naming
**Decisión:** [Patrones de naming definidos]
- **Resource naming:** [Plural vs singular]
- **URL structure:** [/users vs /user]
- **Query parameters:** [snake_case, camelCase, etc.]
- **Path parameters:** [Convención elegida]


### Códigos de Estado HTTP
**Decisión:** [Códigos utilizados]
- **200 OK:** Successful GET, PUT, PATCH
- **201 Created:** Successful POST
- **204 No Content:** Successful DELETE
- **400 Bad Request:** Invalid request data
- **401 Unauthorized:** Missing/invalid auth
- **403 Forbidden:** Insufficient permissions
- **404 Not Found:** Resource doesn't exist
- **422 Unprocessable Entity:** Validation errors
- **429 Too Many Requests:** Rate limit exceeded
- **500 Internal Server Error:** Server error


### Decisiones Clave a Capturar
- **Estilo de API** y justificación
- **Estructura de endpoints** y naming conventions
- **Autenticación y autorización** implementada
- **Versionado** y backwards compatibility
- **Documentación** y testing strategy

---


### Diseño de API
- [ ] [Definir recursos principales]
- [ ] [Diseñar esquemas de datos]
- [ ] [Establecer convenciones]


### Documentación y Testing
- [ ] [Setup documentación automática]
- [ ] [Escribir tests de API]
- [ ] [Configurar monitoring]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/DOC008-APISpecification.md`*


### Error Response Format
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": "Additional context",
    "timestamp": "ISO 8601 timestamp",
    "path": "/api/v1/resource",
    "validation_errors": [
      {
        "field": "field_name",
        "message": "Field is required",
        "code": "REQUIRED"
      }
    ]
  }
}
```

---


### Estilo de API
**Decisión:** [Estilo arquitectónico elegido]
- **REST** / **GraphQL** / **gRPC** / **tRPC** / **OpenAPI**
- **Justificación:** [Por qué este estilo]
- **Trade-offs considerados:** [Ventajas y desventajas]


### Estrategia de Auth
**Decisión:** [Método de autenticación implementado]
- **Bearer Token (JWT)** / **API Keys** / **OAuth 2.0** / **Basic Auth**
- **Header format:** [Authorization: Bearer <token>]


### Estrategia de Versionado
**Decisión:** [Método de versionado]
- **URL path:** `/v1/resource`
- **Header:** `Accept: application/vnd.api+json;version=1`
- **Query param:** `?version=1`


### Filtrado y Búsqueda
**Decisión:** [Parámetros de filtro permitidos]
```http
GET /api/v1/resources?filter[status]=active
GET /api/v1/resources?search=query
GET /api/v1/resources?sort=-created_at
GET /api/v1/resources?fields=id,name,email
```


### Headers de Autenticación
```http
Authorization: [FORMAT]
Content-Type: application/json
Accept: application/json
X-API-Version: v1
```


### Herramientas de Documentación
**Decisión:** [Herramienta elegida]
- **OpenAPI/Swagger** / **Postman** / **Insomnia** / **Custom docs**
- **Auto-generation:** [Desde código vs manual]


### Implementación
- [ ] [Setup framework y routing]
- [ ] [Implementar autenticación]
- [ ] [Crear endpoints básicos]


### Información Incluida
- **Endpoint descriptions:** [Descripción detallada]
- **Request/Response examples:** [Ejemplos completos]
- **Authentication examples:** [Cómo autenticarse]
- **Error scenarios:** [Casos de error comunes]
- **Rate limiting info:** [Límites y políticas]


### Logging
**Decisión:** [Información a loggear]
- **Request/Response:** [Headers, body, timing]
- **Authentication:** [User, permissions]
- **Errors:** [Stack traces, context]
- **Business events:** [Domain-specific actions]

---


### Métricas de API
**Decisión:** [Métricas a trackear]
- **Response times:** [Latency por endpoint]
- **Error rates:** [4xx, 5xx por endpoint]
- **Throughput:** [Requests per second]
- **Authentication failures:** [Failed logins]


### Nested Resources
**Decisión:** [Estrategia para recursos anidados]
```http

### Niveles de Autorización
**Decisión:** [Modelo de permisos]
- **Public endpoints:** [Listado]
- **Authenticated endpoints:** [Requieren login]
- **Admin endpoints:** [Requieren permisos especiales]
- **Rate limited:** [Límites por usuario/IP]

---


### Paginación
**Decisión:** [Estrategia de paginación]
- **Cursor-based** / **Offset-based** / **Page-based**


### Política de Deprecation
**Decisión:** [Proceso de deprecación]
- **Notice period:** [6 months, etc.]
- **Deprecation headers:** [Sunset header, etc.]
- **Migration guides:** [Documentación de cambios]


### Recursos Principales
**Decisión:** [Recursos identificados en el sistema]


### Request Schemas
**Decisión:** [Estructura de requests]


### Response Schemas
**Decisión:** [Estructura de responses]


### Sorting
**Decisión:** [Convención de ordenamiento]
```http
GET /api/v1/resources?sort=field_name        # ASC
GET /api/v1/resources?sort=-field_name       # DESC
GET /api/v1/resources?sort=field1,-field2    # Multiple
```

---


### Test Coverage
- [ ] **All endpoints tested:** [200, 400, 401, 404, etc.]
- [ ] **Authentication flows:** [Valid/invalid tokens]
- [ ] **Validation logic:** [Required fields, formats]
- [ ] **Business logic:** [Domain-specific rules]
- [ ] **Error scenarios:** [Edge cases]


### Testing Strategy
**Decisión:** [Estrategia de testing de API]
- **Unit tests:** [Endpoints individuales]
- **Integration tests:** [Flows completos]
- **Contract tests:** [API contracts]


### Testing Tools
**Decisión:** [Herramientas de testing]
- **API Testing:** [Postman, Insomnia, REST Client]
- **Automated testing:** [Jest, PyTest, etc.]
- **Load testing:** [Artillery, JMeter, etc.]

---


### Ubicación de Documentación
**Decisión:** [Dónde está disponible]
- **URL:** [https://api.example.com/docs]
- **Access:** [Público vs privado]
- **Interactive:** [Swagger UI, etc.]

---


#### Collection Response
```json
{
  "data": [
    { "resource_object": "..." }
  ],
  "pagination": {
    "page": "integer",
    "per_page": "integer", 
    "total": "integer",
    "total_pages": "integer"
  },
  "meta": {
    "additional_info": "if needed"
  }
}
```

---


#### Create [Resource] Request
```json
{
  "field1": "string",
  "field2": "integer", 
  "field3": "boolean",
  "nested_object": {
    "sub_field": "string"
  }
}
```


#### Query Parameters
```http
GET /api/v1/resources?page=1&per_page=20
GET /api/v1/resources?offset=0&limit=20
GET /api/v1/resources?cursor=eyJpZCI6MTB9
```


#### Recurso 1: [NOMBRE_RECURSO]
```http
GET    /api/v1/[resource]           # List all
GET    /api/v1/[resource]/:id       # Get specific
POST   /api/v1/[resource]           # Create new
PUT    /api/v1/[resource]/:id       # Update (full)
PATCH  /api/v1/[resource]/:id       # Update (partial)
DELETE /api/v1/[resource]/:id       # Delete
```


#### Recurso 2: [NOMBRE_RECURSO]
```http
GET    /api/v1/[resource]           # List all
POST   /api/v1/[resource]           # Create new
GET    /api/v1/[resource]/:id       # Get specific
PUT    /api/v1/[resource]/:id       # Update
DELETE /api/v1/[resource]/:id       # Delete
```


#### Standard Resource Response
```json
{
  "id": "string/number",
  "field1": "string",
  "field2": "integer",
  "field3": "boolean",
  "created_at": "ISO 8601 timestamp",
  "updated_at": "ISO 8601 timestamp"
}
```


#### Update [Resource] Request
```json
{
  "field1": "string (optional)",
  "field2": "integer (optional)",
  "field3": "boolean (optional)"
}
```