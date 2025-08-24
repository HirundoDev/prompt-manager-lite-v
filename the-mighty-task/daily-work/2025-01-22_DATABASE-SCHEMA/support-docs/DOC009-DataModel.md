# Modelado de Datos - Marco de Referencia

**Sesión:** DATABASE-SCHEMA  
**Fecha:** 2025-01-22  
**Marco Universal:** Modelado de Datos  
**Referencia:** [playbooks/documentation_playbooks/DOC009-DataModel.md](../../../playbooks/documentation_playbooks/DOC009-DataModel.md)

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
{
  "_id": "ObjectId",
  "field1": "String (required)",
  "field2": "Number (default: 0)", 
  "field3": "Boolean (default: false)",
  "nested_object": {
    "sub_field": "String",
    "array_field": ["String"]
  },
  "created_at": "ISODate",
  "updated_at": "ISODate"
}
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
const schema = {
  field1: { type: String, required: true, maxLength: 255 },
  field2: { type: Number, min: 0, max: 100 },
  field3: { type: Boolean, default: false },
  email: { type: String, match: /^[^@]+@[^@]+\.[^@]+$/ }
}
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
*Consultar playbook original: `playbooks/documentation_playbooks/DOC009-DataModel.md`*
