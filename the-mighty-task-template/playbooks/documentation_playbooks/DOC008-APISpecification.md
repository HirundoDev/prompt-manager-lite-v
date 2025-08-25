# Especificación de API - Marco Universal

## Propósito del Documento
Este marco universal proporciona una estructura para diseñar, documentar y especificar APIs de manera consistente y escalable. El documento está diseñado para ser adaptable a cualquier estilo de API (REST, GraphQL, gRPC, etc.) y stack tecnológico.

## 🎯 Objetivos Clave

- Establecer un diseño de API consistente y predecible
- Definir estándares de documentación claros y completos
- Implementar patrones de autenticación y seguridad robustos
- Garantizar una experiencia de desarrollador óptima
- Asegurar performance y escalabilidad de la API

---

## 🌐 Estilo y Arquitectura de API

### Tipo de API
**Decisión:** [Estilo de API elegido]

**Opciones a evaluar:**
- **REST:** Arquitectura basada en recursos
- **GraphQL:** Query language flexible
- **gRPC:** RPC de alto rendimiento
- **WebSocket:** Comunicación en tiempo real
- **Server-Sent Events (SSE):** Push unidireccional
- **Webhook:** Callbacks HTTP

**Criterios de selección:**
- Simplicidad de implementación
- Performance requirements
- Real-time capabilities
- Client diversity
- Ecosystem support

### Versionado
**Decisión:** [Estrategia de versionado]

**Opciones:**
- **URL Path:** `/api/v1/users`
- **Header:** `Accept: application/vnd.api+json;version=1`
- **Query Parameter:** `/api/users?version=1`
- **Media Type:** Content negotiation

**Política de compatibilidad:** [Backward compatibility strategy]

### Especificación
**Decisión:** [Formato de especificación]

- **OpenAPI 3.x:** Para REST APIs
- **GraphQL Schema:** Para GraphQL APIs  
- **Protocol Buffers:** Para gRPC APIs
- **AsyncAPI:** Para APIs asíncronas
- **Custom Documentation:** Para APIs híbridas

---

## 🔐 Autenticación y Seguridad

### Estrategia de Autenticación
**Decisión:** [Método de autenticación]

**Opciones principales:**
- **Bearer Token (JWT):** Stateless authentication
- **OAuth 2.0:** Delegated authorization
- **API Key:** Simple key-based auth
- **Basic Auth:** Username/password
- **Session-based:** Server-side sessions
- **mTLS:** Mutual certificate authentication

**Configuración elegida:**
- Authentication method: [Chosen method]
- Token expiration: [Time period]
- Refresh strategy: [How tokens are refreshed]
- Scopes/Permissions: [Authorization model]

### Seguridad de Transporte
**Decisión:** [Configuración de seguridad]

- **TLS Version:** [1.2 minimum, 1.3 preferred]
- **CORS Policy:** [Cross-origin configuration]
- **CSRF Protection:** [If applicable]
- **Rate Limiting:** [Throttling strategy]
- **IP Filtering:** [If required]

### Manejo de Secrets
**Decisión:** [Gestión de secretos]

- **API Keys:** [Generation and rotation]
- **JWT Secrets:** [Key management]
- **OAuth Credentials:** [Client management]
- **Certificates:** [Certificate lifecycle]

---

## 📜 Diseño de Endpoints

### Convenciones de URL
**Decisión:** [Patrones de URL adoptados]

**Para REST:**
- **Resources:** `/api/v1/users`
- **Nested Resources:** `/api/v1/users/{id}/posts`
- **Actions:** `/api/v1/users/{id}/activate`
- **Collections:** `/api/v1/users?page=1&limit=20`

**Naming conventions:**
- Plural nouns for resources
- Kebab-case for multi-word resources
- Consistent parameter naming

### HTTP Methods y Status Codes
**Decisión:** [Mapeo de métodos HTTP]

**CRUD Operations:**
- **GET:** Retrieve resources (200, 404)
- **POST:** Create resources (201, 400, 409)
- **PUT:** Update resources (200, 404)
- **PATCH:** Partial update (200, 404)
- **DELETE:** Remove resources (204, 404)

**Status Codes Strategy:**
- Success: 2xx range with specific codes
- Client errors: 4xx with detailed messages
- Server errors: 5xx with generic messages

### Content Negotiation
**Decisión:** [Formatos soportados]

- **Request formats:** JSON, XML, form-data
- **Response formats:** JSON, XML, MessagePack
- **Default format:** [Primary format]
- **Headers:** Accept, Content-Type

---

## 📋 Estructura de Request/Response

### Request Format
**Decisión:** [Estructura estándar de requests]

```json
{
  "data": {
    "type": "[resource_type]",
    "attributes": {
      "// Resource fields": ""
    },
    "relationships": {
      "// Related resources": ""
    }
  },
  "meta": {
    "request_id": "[unique_id]",
    "client_version": "[version]"
  }
}
```

### Response Format
**Decisión:** [Estructura estándar de responses]

```json
{
  "data": {
    "// Resource or collection": ""
  },
  "meta": {
    "request_id": "[unique_id]",
    "response_time": "[time_ms]",
    "version": "[api_version]"
  },
  "links": {
    "self": "[current_url]",
    "related": "[related_urls]"
  }
}
```

### Error Format
**Decisión:** [Estructura de errores]

```json
{
  "errors": [
    {
      "code": "[ERROR_CODE]",
      "title": "[Human readable title]",
      "detail": "[Specific error description]",
      "source": {
        "pointer": "[/data/attributes/field]",
        "parameter": "[query_param]"
      },
      "meta": {
        "timestamp": "[ISO 8601]",
        "request_id": "[unique_id]"
      }
    }
  ]
}
```

---

## 🔄 Paginación y Filtrado

### Estrategia de Paginación
**Decisión:** [Tipo de paginación implementado]

**Opciones:**
- **Offset-based:** `?page=1&limit=20`
- **Cursor-based:** `?cursor=xyz&limit=20`
- **Page-based:** `?page=1&per_page=20`

**Metadata de paginación:**
```json
{
  "pagination": {
    "current_page": 1,
    "per_page": 20,
    "total_pages": 10,
    "total_items": 200,
    "has_next": true,
    "has_previous": false
  }
}
```

### Filtrado y Búsqueda
**Decisión:** [Sistema de filtros]

**Query parameters:**
- **Simple filters:** `?status=active&category=tech`
- **Range filters:** `?created_at[gte]=2024-01-01`
- **Search:** `?q=keyword`
- **Sorting:** `?sort=name,-created_at`

**Validación:**
- Whitelist of allowed filter fields
- Type validation for filter values
- Maximum result limits

---

## 🎩 Rate Limiting

### Política de Rate Limiting
**Decisión:** [Estrategia de throttling]

**Algoritmos considerados:**
- **Token Bucket:** Burst allowance
- **Sliding Window:** Time-based limiting
- **Fixed Window:** Period-based limiting

**Configuración:**
- Rate limits por usuario/IP
- Different limits por endpoint
- Tier-based limits (freemium model)

### Headers y Responses
**Decisión:** [Headers informativos]

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642694400
X-RateLimit-Window: 3600
```

**Rate limit exceeded response:**
```json
{
  "errors": [{
    "code": "RATE_LIMIT_EXCEEDED",
    "title": "Rate limit exceeded",
    "detail": "Too many requests. Try again in 60 seconds.",
    "meta": {
      "retry_after": 60,
      "limit": 1000,
      "window": 3600
    }
  }]
}
```

---

## 📊 Monitoreo y Analytics

### Métricas de API
**Decisión:** [KPIs tracked]

**Performance metrics:**
- Response times (P50, P95, P99)
- Request rate (req/sec)
- Error rates by endpoint
- Uptime and availability

**Business metrics:**
- API adoption rates
- Feature usage statistics
- Developer onboarding success
- Support ticket correlation

### Health Checks
**Decisión:** [Health monitoring]

**Endpoints:**
- `/health` - Basic health check
- `/health/detailed` - Component status
- `/metrics` - Prometheus metrics
- `/status` - Public status page

### Logging y Observability
**Decisión:** [Logging strategy]

**Log levels:**
- Request/response logging
- Error logging with stack traces
- Performance metrics logging
- Security event logging

**Structured logging format:**
```json
{
  "timestamp": "2025-01-22T10:30:00Z",
  "level": "info",
  "request_id": "req_123",
  "method": "GET",
  "path": "/api/v1/users",
  "status_code": 200,
  "response_time": 45,
  "user_id": "user_456"
}
```

---

## 📏 Documentación

### Herramientas de Documentación
**Decisión:** [Platform y tools]

**Opciones principales:**
- **Swagger UI:** Interactive OpenAPI docs
- **Redoc:** Alternative OpenAPI renderer
- **Postman:** Collection-based docs
- **GitBook:** Rich documentation platform
- **Custom:** Bespoke documentation site

### Contenido Requerido
**Decisión:** [Sections to include]

**Core sections:**
- Getting started guide
- Authentication setup
- Endpoint reference
- Error codes reference
- SDKs and code examples
- Rate limiting information
- Changelog and migration guides

### Developer Experience
**Decisión:** [DX features]

**Interactive features:**
- Try-it-out functionality
- Code generation
- Authentication testing
- Response validation
- Request/response examples

---

## 🚀 Testing Strategy

### API Testing Levels
**Decisión:** [Testing approach]

**Unit testing:**
- Individual endpoint logic
- Input validation
- Business logic
- Error handling

**Integration testing:**
- Database interactions
- External service calls
- Authentication flows
- End-to-end workflows

**Contract testing:**
- API specification compliance
- Request/response schema validation
- Backward compatibility

### Test Environment
**Decisión:** [Test infrastructure]

- **Staging environment:** Production-like setup
- **Test data:** Realistic datasets
- **Mock services:** External dependencies
- **Load testing:** Performance validation

---

## 🔀 Evolución y Mantenimiento

### Lifecycle Management
**Decisión:** [API lifecycle strategy]

**Versioning lifecycle:**
- Development phase
- Beta/preview release
- Stable release
- Deprecation notice
- End-of-life

### Breaking Changes
**Decisión:** [Change management]

**What constitutes a breaking change:**
- Removing endpoints or fields
- Changing data types
- Modifying authentication
- Altering error responses

**Migration strategy:**
- Advance notice period
- Migration guides
- Dual support period
- Automated migration tools

---

## 📋 Plantilla de Especificación

### OpenAPI Template (REST)
```yaml
openapi: 3.1.0
info:
  title: "[Project Name] API"
  version: "[Version]"
  description: "[API Description]"
  contact:
    name: "[Team Name]"
    email: "[Contact Email]"
    url: "[Support URL]"

servers:
  - url: "[Base URL]"
    description: "[Environment]"

security:
  - bearerAuth: []

paths:
  # Define your endpoints here

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

### GraphQL Schema Template
```graphql
type Query {
  # Read operations
}

type Mutation {
  # Write operations
}

type Subscription {
  # Real-time operations
}

# Define your types here
```

---

## 📋 Checklist de Implementación

### Pre-development
- [ ] API style y architecture defined
- [ ] Authentication strategy chosen
- [ ] URL conventions established
- [ ] Error handling patterns defined
- [ ] Rate limiting policy set

### Development
- [ ] Endpoints implemented per specification
- [ ] Authentication/authorization working
- [ ] Error handling implemented
- [ ] Rate limiting configured
- [ ] Logging and monitoring setup

### Pre-release
- [ ] Documentation complete and tested
- [ ] Security review completed
- [ ] Performance testing passed
- [ ] Integration tests passing
- [ ] SDK/client libraries ready

### Post-release
- [ ] Monitoring and alerting active
- [ ] Developer feedback channels open
- [ ] Support documentation updated
- [ ] Changelog maintained

---

**Versión del Marco:** 3.0 Universal  
**Actualizado:** 2025-01-22  
**Aplicable a:** REST, GraphQL, gRPC, y APIs híbridas  
**Próxima revisión:** [Fecha planificada]
