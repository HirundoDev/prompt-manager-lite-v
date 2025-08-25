"""
Templates Data
==============

Templates universales para API specifications y modelado de datos.
"""

def create_api_specification_template(theme, date_str, filename):
    """Marco de referencia para especificaciones de API"""
    return f'''# Especificación de API - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Especificación de API  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para la especificación y diseño de APIs, adaptable a cualquier estilo arquitectónico.

### Decisiones Clave a Capturar
- **Estilo de API** y justificación
- **Estructura de endpoints** y naming conventions
- **Autenticación y autorización** implementada
- **Versionado** y backwards compatibility
- **Documentación** y testing strategy

---

## 🏗️ Arquitectura de API

### Estilo de API
**Decisión:** [Estilo arquitectónico elegido]
- **REST** / **GraphQL** / **gRPC** / **tRPC** / **OpenAPI**
- **Justificación:** [Por qué este estilo]
- **Trade-offs considerados:** [Ventajas y desventajas]

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

## 🔌 Endpoints y Recursos

### Convenciones de Naming
**Decisión:** [Patrones de naming definidos]
- **Resource naming:** [Plural vs singular]
- **URL structure:** [/users vs /user]
- **Query parameters:** [snake_case, camelCase, etc.]
- **Path parameters:** [Convención elegida]

### Recursos Principales
**Decisión:** [Recursos identificados en el sistema]

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

### Nested Resources
**Decisión:** [Estrategia para recursos anidados]
```http
# Ejemplo: Comentarios de un post
GET    /api/v1/posts/:postId/comments
POST   /api/v1/posts/:postId/comments
GET    /api/v1/posts/:postId/comments/:id
```

---

## 📊 Esquemas de Datos

### Request Schemas
**Decisión:** [Estructura de requests]

#### Create [Resource] Request
```json
{{
  "field1": "string",
  "field2": "integer", 
  "field3": "boolean",
  "nested_object": {{
    "sub_field": "string"
  }}
}}
```

#### Update [Resource] Request
```json
{{
  "field1": "string (optional)",
  "field2": "integer (optional)",
  "field3": "boolean (optional)"
}}
```

### Response Schemas
**Decisión:** [Estructura de responses]

#### Standard Resource Response
```json
{{
  "id": "string/number",
  "field1": "string",
  "field2": "integer",
  "field3": "boolean",
  "created_at": "ISO 8601 timestamp",
  "updated_at": "ISO 8601 timestamp"
}}
```

#### Collection Response
```json
{{
  "data": [
    {{ "resource_object": "..." }}
  ],
  "pagination": {{
    "page": "integer",
    "per_page": "integer", 
    "total": "integer",
    "total_pages": "integer"
  }},
  "meta": {{
    "additional_info": "if needed"
  }}
}}
```

---

## 🔐 Autenticación y Autorización

### Estrategia de Auth
**Decisión:** [Método de autenticación implementado]
- **Bearer Token (JWT)** / **API Keys** / **OAuth 2.0** / **Basic Auth**
- **Header format:** [Authorization: Bearer <token>]

### Headers de Autenticación
```http
Authorization: [FORMAT]
Content-Type: application/json
Accept: application/json
X-API-Version: v1
```

### Niveles de Autorización
**Decisión:** [Modelo de permisos]
- **Public endpoints:** [Listado]
- **Authenticated endpoints:** [Requieren login]
- **Admin endpoints:** [Requieren permisos especiales]
- **Rate limited:** [Límites por usuario/IP]

---

## 📄 Paginación y Filtrado

### Paginación
**Decisión:** [Estrategia de paginación]
- **Cursor-based** / **Offset-based** / **Page-based**

#### Query Parameters
```http
GET /api/v1/resources?page=1&per_page=20
GET /api/v1/resources?offset=0&limit=20
GET /api/v1/resources?cursor=eyJpZCI6MTB9
```

### Filtrado y Búsqueda
**Decisión:** [Parámetros de filtro permitidos]
```http
GET /api/v1/resources?filter[status]=active
GET /api/v1/resources?search=query
GET /api/v1/resources?sort=-created_at
GET /api/v1/resources?fields=id,name,email
```

### Sorting
**Decisión:** [Convención de ordenamiento]
```http
GET /api/v1/resources?sort=field_name        # ASC
GET /api/v1/resources?sort=-field_name       # DESC
GET /api/v1/resources?sort=field1,-field2    # Multiple
```

---

## ⚠️ Manejo de Errores

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

### Error Response Format
```json
{{
  "error": {{
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": "Additional context",
    "timestamp": "ISO 8601 timestamp",
    "path": "/api/v1/resource",
    "validation_errors": [
      {{
        "field": "field_name",
        "message": "Field is required",
        "code": "REQUIRED"
      }}
    ]
  }}
}}
```

---

## 📝 Documentación

### Herramientas de Documentación
**Decisión:** [Herramienta elegida]
- **OpenAPI/Swagger** / **Postman** / **Insomnia** / **Custom docs**
- **Auto-generation:** [Desde código vs manual]

### Información Incluida
- **Endpoint descriptions:** [Descripción detallada]
- **Request/Response examples:** [Ejemplos completos]
- **Authentication examples:** [Cómo autenticarse]
- **Error scenarios:** [Casos de error comunes]
- **Rate limiting info:** [Límites y políticas]

### Ubicación de Documentación
**Decisión:** [Dónde está disponible]
- **URL:** [https://api.example.com/docs]
- **Access:** [Público vs privado]
- **Interactive:** [Swagger UI, etc.]

---

## 🔄 Versionado

### Estrategia de Versionado
**Decisión:** [Método de versionado]
- **URL path:** `/v1/resource`
- **Header:** `Accept: application/vnd.api+json;version=1`
- **Query param:** `?version=1`

### Política de Deprecation
**Decisión:** [Proceso de deprecación]
- **Notice period:** [6 months, etc.]
- **Deprecation headers:** [Sunset header, etc.]
- **Migration guides:** [Documentación de cambios]

### Backwards Compatibility
**Decisión:** [Política de compatibilidad]
- **Breaking changes:** [Solo en major versions]
- **Additive changes:** [En minor versions]
- **Bug fixes:** [En patch versions]

---

## 🧪 Testing

### Testing Strategy
**Decisión:** [Estrategia de testing de API]
- **Unit tests:** [Endpoints individuales]
- **Integration tests:** [Flows completos]
- **Contract tests:** [API contracts]

### Test Coverage
- [ ] **All endpoints tested:** [200, 400, 401, 404, etc.]
- [ ] **Authentication flows:** [Valid/invalid tokens]
- [ ] **Validation logic:** [Required fields, formats]
- [ ] **Business logic:** [Domain-specific rules]
- [ ] **Error scenarios:** [Edge cases]

### Testing Tools
**Decisión:** [Herramientas de testing]
- **API Testing:** [Postman, Insomnia, REST Client]
- **Automated testing:** [Jest, PyTest, etc.]
- **Load testing:** [Artillery, JMeter, etc.]

---

## 📊 Monitoring y Analytics

### Métricas de API
**Decisión:** [Métricas a trackear]
- **Response times:** [Latency por endpoint]
- **Error rates:** [4xx, 5xx por endpoint]
- **Throughput:** [Requests per second]
- **Authentication failures:** [Failed logins]

### Logging
**Decisión:** [Información a loggear]
- **Request/Response:** [Headers, body, timing]
- **Authentication:** [User, permissions]
- **Errors:** [Stack traces, context]
- **Business events:** [Domain-specific actions]

---

## 🔄 Próximos Pasos

### Diseño de API
- [ ] [Definir recursos principales]
- [ ] [Diseñar esquemas de datos]
- [ ] [Establecer convenciones]

### Implementación
- [ ] [Setup framework y routing]
- [ ] [Implementar autenticación]
- [ ] [Crear endpoints básicos]

### Documentación y Testing
- [ ] [Setup documentación automática]
- [ ] [Escribir tests de API]
- [ ] [Configurar monitoring]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''

def create_data_model_template(theme, date_str, filename):
    """Marco de referencia para modelado de datos"""
    return f'''# Modelado de Datos - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Modelado de Datos  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para el modelado de datos, adaptable a bases de datos SQL, NoSQL y esquemas híbridos.

### Decisiones Clave a Capturar
- **Tipo de base de datos** y justificación
- **Esquema de datos** y relaciones
- **Estrategia de normalización** vs desnormalización
- **Indexing** y optimización
- **Migraciones** y versionado de esquema

---

## 🗄️ Arquitectura de Datos

### Tipo de Base de Datos
**Decisión:** [Tecnología de persistencia elegida]
- **SQL:** PostgreSQL, MySQL, SQLite
- **NoSQL:** MongoDB, DynamoDB, CouchDB
- **Graph:** Neo4j, ArangoDB
- **Key-Value:** Redis, DynamoDB
- **Columnar:** Cassandra, ClickHouse
- **Hybrid:** [Combinación de tecnologías]

**Justificación:** [Por qué esta elección]

### Patrones de Modelado
**Decisión:** [Patrón de modelado adoptado]
- **Relational (SQL):** Normalized, ACID compliance
- **Document (NoSQL):** Embedded vs Referenced
- **Event Sourcing:** Event streams y snapshots
- **CQRS:** Command vs Query models
- **Domain-Driven:** Aggregates y bounded contexts

---

## 📊 Esquema de Datos Principal

### Entidades Core
**Decisión:** [Entidades principales del dominio]

#### Entidad 1: [NOMBRE_ENTIDAD]
```sql
-- Ejemplo SQL
CREATE TABLE [table_name] (
    id SERIAL PRIMARY KEY,
    field1 VARCHAR(255) NOT NULL,
    field2 INTEGER DEFAULT 0,
    field3 BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

```json
// Ejemplo NoSQL/Document
{{
  "_id": "ObjectId",
  "field1": "String (required)",
  "field2": "Number (default: 0)", 
  "field3": "Boolean (default: false)",
  "nested_object": {{
    "sub_field": "String",
    "array_field": ["String"]
  }},
  "created_at": "ISODate",
  "updated_at": "ISODate"
}}
```

#### Entidad 2: [NOMBRE_ENTIDAD]
```sql
CREATE TABLE [table_name] (
    id SERIAL PRIMARY KEY,
    [entity1_id] INTEGER REFERENCES [entity1](id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'active',
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Relaciones entre Entidades
**Decisión:** [Tipo de relaciones implementadas]

#### One-to-Many
- **[Entity1] → [Entity2]:** [Descripción de la relación]
- **Foreign Key:** [entity1_id in entity2 table]

#### Many-to-Many  
- **[Entity1] ↔ [Entity3]:** [Descripción]
- **Join Table:** [entity1_entity3_junction]

#### One-to-One
- **[Entity1] → [Profile]:** [Relación 1:1]

---

## 🔍 Indexing y Performance

### Estrategia de Indexing
**Decisión:** [Índices definidos para optimización]

#### Primary Indexes
```sql
-- Índices primarios automáticos
PRIMARY KEY (id)
```

#### Secondary Indexes
```sql
-- Índices para queries frecuentes
CREATE INDEX idx_[table]_[field] ON [table] ([field]);
CREATE INDEX idx_[table]_[field1_field2] ON [table] ([field1], [field2]);
CREATE INDEX idx_[table]_[partial] ON [table] ([field]) WHERE [condition];
```

#### Composite Indexes
```sql
-- Para queries multi-campo
CREATE INDEX idx_[table]_composite ON [table] ([field1], [field2], [field3]);
```

### Query Optimization
**Decisión:** [Estrategias de optimización identificadas]
- **Most frequent queries:** [Listar queries más comunes]
- **N+1 problem solutions:** [Eager loading, etc.]
- **Pagination strategies:** [Offset vs cursor-based]
- **Caching strategy:** [Query result caching]

---

## 🔄 Normalization vs Denormalization

### Nivel de Normalización
**Decisión:** [Nivel de normalización elegido]
- **1NF, 2NF, 3NF:** [Para datos transaccionales]
- **Denormalized:** [Para read-heavy workloads]
- **Hybrid approach:** [Normalized core + denormalized views]

### Trade-offs Considerados
**Decisión:** [Análisis de trade-offs]
- **Storage space:** [Duplicación vs eficiencia]
- **Query performance:** [Joins vs direct access]
- **Maintenance complexity:** [Updates consistency]
- **Scalability:** [Write vs read optimization]

---

## 📝 Data Validation y Constraints

### Field-Level Constraints
**Decisión:** [Validaciones a nivel de campo]
```sql
-- SQL Constraints
NOT NULL, UNIQUE, CHECK (value > 0)
DEFAULT values, FOREIGN KEY references
```

```javascript
// Application-level validation (ejemplo)
const schema = {{
  field1: {{ type: String, required: true, maxLength: 255 }},
  field2: {{ type: Number, min: 0, max: 100 }},
  field3: {{ type: Boolean, default: false }},
  email: {{ type: String, match: /^[^@]+@[^@]+\\.[^@]+$/ }}
}}
```

### Business Rules
**Decisión:** [Reglas de negocio implementadas]
- **Unique constraints:** [Campos que deben ser únicos]
- **Reference integrity:** [FK constraints]
- **Domain constraints:** [Value ranges, formats]
- **Temporal constraints:** [Date validations]

---

## 🔄 Migrations y Schema Evolution

### Migration Strategy
**Decisión:** [Estrategia de migraciones]
- **Forward-only:** [No rollbacks]
- **Reversible:** [Up/down migrations]
- **Blue-green:** [Schema versioning]

### Migration Tools
**Decisión:** [Herramientas de migración]
- **SQL:** Flyway, Liquibase, native tools
- **ORM-based:** Prisma Migrate, Django Migrations, etc.
- **Custom scripts:** [Scripts específicos]

### Versioning Strategy
```
migration_001_create_users_table.sql
migration_002_add_user_email_index.sql
migration_003_create_orders_table.sql
```

### Zero-downtime Deployments
**Decisión:** [Estrategia para deployments sin downtime]
- **Backward compatibility:** [New columns nullable]
- **Multi-phase rollouts:** [Add, deploy, cleanup]
- **Feature flags:** [Gradual schema adoption]

---

## 💾 Backup y Disaster Recovery

### Backup Strategy
**Decisión:** [Estrategia de respaldo]
- **Full backups:** [Frequency and retention]
- **Incremental backups:** [Change-based backups]
- **Point-in-time recovery:** [Transaction log backups]

### Disaster Recovery
**Decisión:** [Plan de recuperación]
- **RTO (Recovery Time Objective):** [Target downtime]
- **RPO (Recovery Point Objective):** [Data loss tolerance]
- **Failover strategy:** [Primary/secondary setup]

---

## 🔒 Security y Access Control

### Data Encryption
**Decisión:** [Estrategia de encriptación]
- **Encryption at rest:** [Database-level encryption]
- **Encryption in transit:** [SSL/TLS]
- **Field-level encryption:** [Sensitive data fields]

### Access Control
**Decisión:** [Control de acceso a datos]
- **Database users:** [Role-based access]
- **Application-level:** [Permission system]
- **Row-level security:** [Data isolation]

### Audit Trail
**Decisión:** [Auditoría de cambios]
- **Change tracking:** [Modified by, when]
- **Soft deletes:** [Mark as deleted vs hard delete]
- **Event logging:** [Data access logs]

---

## 📊 Monitoring y Maintenance

### Database Monitoring
**Decisión:** [Métricas monitoreadas]
- **Performance metrics:** [Query time, throughput]
- **Resource usage:** [CPU, memory, disk]
- **Connection pooling:** [Active connections]
- **Slow query analysis:** [Query optimization]

### Maintenance Tasks
**Decisión:** [Tareas de mantenimiento regulares]
- **Index maintenance:** [Rebuild/reorganize]
- **Statistics updates:** [Query plan optimization]
- **Cleanup routines:** [Old data purging]
- **Health checks:** [Integrity validation]

---

## 🧪 Testing Strategy

### Data Testing
**Decisión:** [Estrategia de testing de datos]
- **Unit tests:** [Model validation, constraints]
- **Integration tests:** [Database operations]
- **Data quality tests:** [Integrity, consistency]

### Test Data Management
**Decisión:** [Gestión de datos de prueba]
- **Fixtures:** [Static test data]
- **Factories:** [Generated test data]
- **Anonymization:** [Production data sanitization]

---

## 🔄 Próximos Pasos

### Schema Design
- [ ] [Definir entidades principales]
- [ ] [Diseñar relaciones]
- [ ] [Establecer constraints]

### Implementation
- [ ] [Setup database y migrations]
- [ ] [Crear esquema inicial]
- [ ] [Implementar indexes]

### Optimization
- [ ] [Query performance analysis]
- [ ] [Setup monitoring]
- [ ] [Backup strategy implementation]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
