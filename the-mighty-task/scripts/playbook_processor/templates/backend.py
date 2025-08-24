"""
Templates Backend
=================

Templates universales para arquitectura backend y dependencias.
"""

def create_backend_architecture_template(theme, date_str, filename):
    """Marco de referencia para arquitectura backend"""
    return f'''# Arquitectura Backend - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Arquitectura Backend  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para arquitecturas backend, adaptable a cualquier stack tecnológico.

### Decisiones Clave a Capturar
- **Patrón arquitectónico** elegido y justificación
- **Stack tecnológico** y razones de elección
- **Estrategia de datos** y persistencia
- **Escalabilidad** y performance
- **Seguridad** y autenticación

---

## 🏗️ Patrón Arquitectónico

### Arquitectura Elegida
**Decisión:** [Patrón arquitectónico principal]

**Opciones consideradas:**
- Monolítico / Microservicios / Serverless
- Layered / Hexagonal / Clean Architecture
- Event-Driven / CQRS / Domain-Driven Design

**Justificación:** [Por qué se eligió este patrón]

### Estructura de Alto Nivel
```
[DEFINIR estructura general de la aplicación]
```

---

## 💻 Stack Tecnológico

### Runtime y Lenguaje
**Decisión:** [Lenguaje y runtime elegidos]
- **Lenguaje:** [Node.js, Python, Java, Go, Rust, etc.]
- **Version:** [Versión específica]
- **Justificación:** [Razones para la elección]

### Framework Principal
**Decisión:** [Framework web elegido]
- **Framework:** [Express, FastAPI, Spring Boot, Gin, Actix, etc.]
- **Alternativas consideradas:** [Otros frameworks evaluados]
- **Razón de elección:** [Criterios de decisión]

### Base de Datos
**Decisión:** [Estrategia de persistencia]

#### Base de Datos Principal
- **Tipo:** [SQL, NoSQL, Graph, etc.]
- **Motor:** [PostgreSQL, MongoDB, Redis, Neo4j, etc.]
- **Justificación:** [Por qué esta elección]

#### Caché y Performance
- **Caché:** [Redis, Memcached, In-memory, etc.]
- **Estrategia:** [Patrón de cache elegido]

---

## 🔌 APIs y Comunicación

### Estilo de API
**Decisión:** [Estilo de API adoptado]
- **REST** / **GraphQL** / **gRPC** / **WebSockets**
- **Justificación:** [Razones para la elección]

### Formato de Datos
**Decisión:** [Formato de intercambio]
- **JSON** / **XML** / **Protocol Buffers** / **MessagePack**
- **Estándares:** [JSON:API, OpenAPI, etc.]

### Documentación de API
**Decisión:** [Herramienta de documentación]
- **Swagger/OpenAPI** / **Postman** / **Insomnia** / **Custom**
- **Ubicación:** [Dónde se encuentra la documentación]

---

## 🔐 Seguridad y Autenticación

### Estrategia de Autenticación
**Decisión:** [Método de autenticación]
- **JWT** / **OAuth 2.0** / **Session-based** / **API Keys**
- **Provider:** [Auth0, Firebase, Custom, etc.]

### Autorización
**Decisión:** [Modelo de autorización]
- **RBAC** / **ABAC** / **Custom permissions**
- **Implementation:** [Cómo se implementa]

### Seguridad de Datos
**Decisión:** [Medidas de seguridad implementadas]
- **Encriptación:** [En tránsito y en reposo]
- **Validación:** [Esquemas y sanitización]
- **Rate limiting:** [Estrategia anti-abuse]

---

## 📊 Datos y Persistencia

### Modelo de Datos
**Decisión:** [Estrategia de modelado]
- **ORM/ODM:** [Prisma, SQLAlchemy, Mongoose, etc.]
- **Migrations:** [Estrategia de migraciones]
- **Seeding:** [Datos iniciales]

### Backup y Recovery
**Decisión:** [Estrategia de backup]
- **Frecuencia:** [Cada cuánto se hace backup]
- **Retención:** [Cuánto tiempo se conservan]
- **Recovery:** [Proceso de recuperación]

---

## ⚡ Performance y Escalabilidad

### Estrategia de Escalabilidad
**Decisión:** [Cómo escalar la aplicación]
- **Horizontal** / **Vertical** / **Híbrido**
- **Load Balancing:** [Estrategia de balanceeo]
- **Auto-scaling:** [Si aplica y cómo]

### Optimizaciones
**Decisión:** [Optimizaciones implementadas]
- **Database indexing:** [Índices definidos]
- **Query optimization:** [Estrategias]
- **Caching layers:** [Niveles de caché]

### Monitoring
**Decisión:** [Herramientas de monitoreo]
- **APM:** [New Relic, DataDog, Elastic APM, etc.]
- **Logs:** [Structured logging, centralized]
- **Metrics:** [Business y technical metrics]

---

## 🐳 Deployment y DevOps

### Containerización
**Decisión:** [Estrategia de contenedores]
- **Docker:** [Sí/No y configuración]
- **Orchestration:** [Kubernetes, Docker Compose, etc.]

### CI/CD
**Decisión:** [Pipeline de deployment]
- **CI Tool:** [GitHub Actions, GitLab CI, Jenkins, etc.]
- **Deployment strategy:** [Blue-green, Rolling, Canary]

### Infrastructure
**Decisión:** [Infraestructura elegida]
- **Cloud Provider:** [AWS, GCP, Azure, Digital Ocean, etc.]
- **IaC:** [Terraform, CloudFormation, Pulumi]

---

## 🧪 Testing

### Estrategia de Testing
**Decisión:** [Niveles de testing implementados]

#### Unit Tests
- **Framework:** [Jest, PyTest, JUnit, etc.]
- **Coverage target:** [Porcentaje objetivo]
- **Mocking strategy:** [Cómo se mockea]

#### Integration Tests
- **Database:** [Cómo se testea persistencia]
- **External APIs:** [Estrategia para APIs externas]
- **End-to-end:** [Si aplica]

### Test Environment
**Decisión:** [Ambiente de testing]
- **Database:** [Testing database strategy]
- **External services:** [Mocks vs real services]

---

## 🔄 Próximos Pasos y Roadmap

### Implementación Inmediata
- [ ] [Tarea 1: Setup inicial]
- [ ] [Tarea 2: Configuración base]
- [ ] [Tarea 3: Primer endpoint]

### Fase de Desarrollo
- [ ] [Milestone 1]
- [ ] [Milestone 2]
- [ ] [Milestone 3]

### Optimización y Scaling
- [ ] [Performance tuning]
- [ ] [Security audit]
- [ ] [Monitoring setup]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''

def create_backend_dependencies_template(theme, date_str, filename):
    """Marco de referencia para dependencias backend"""
    return f'''# Dependencias Backend - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Gestión de Dependencias Backend  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para la gestión de dependencias en proyectos backend.

### Decisiones Clave a Capturar
- **Package manager** y herramientas
- **Dependencias core** del framework
- **Libraries** de terceros elegidas
- **Versionado** y compatibility
- **Security** y vulnerability management

---

## 📦 Gestión de Dependencias

### Herramientas de Package Management
**Decisión:** [Herramienta según el stack]
- **Node.js:** npm, yarn, pnpm
- **Python:** pip, poetry, pipenv
- **Java:** Maven, Gradle
- **Go:** go mod
- **Rust:** Cargo
- **Other:** [Especificar]

### Archivo de Configuración
**Decisión:** [Archivo principal de dependencies]
```
// Ejemplos según stack:
// package.json (Node.js)
// requirements.txt / pyproject.toml (Python) 
// pom.xml / build.gradle (Java)
// go.mod (Go)
// Cargo.toml (Rust)
```

---

## 🏗️ Framework y Core Dependencies

### Framework Principal
**Decisión:** [Framework web elegido]
- **Express** / **FastAPI** / **Spring Boot** / **Gin** / **Actix** / **Other**
- **Versión:** [Versión específica]
- **Justificación:** [Por qué este framework]

### Runtime Essentials
**Decisión:** [Dependencies críticas runtime]
- **HTTP Framework:** [Framework específico]
- **Database Driver/ORM:** [Prisma, SQLAlchemy, etc.]
- **Validation:** [Joi, Zod, Pydantic, etc.]
- **Configuration:** [dotenv, config libraries]

---

## 🗄️ Database y Persistencia

### Database Drivers
**Decisión:** [Drivers de base de datos]
- **SQL:** [PostgreSQL, MySQL, SQLite drivers]
- **NoSQL:** [MongoDB, Redis clients]
- **ORM/ODM:** [Prisma, TypeORM, SQLAlchemy, etc.]

### Migration Tools
**Decisión:** [Herramientas de migración]
- **SQL Migrations:** [Knex, Alembic, Flyway, etc.]
- **Schema Management:** [Herramientas específicas]

---

## 🔐 Autenticación y Seguridad

### Authentication Libraries
**Decisión:** [Librerías de auth]
- **JWT:** [jsonwebtoken, PyJWT, etc.]
- **OAuth:** [passport, authlib, etc.]
- **Session Management:** [express-session, etc.]

### Security Tools
**Decisión:** [Herramientas de seguridad]
- **Encryption:** [bcrypt, argon2, etc.]
- **Rate Limiting:** [express-rate-limit, etc.]
- **CORS:** [cors middleware]
- **Helmet:** [Security headers]

---

## 📊 Monitoring y Logging

### Logging Libraries
**Decisión:** [Solución de logging]
- **Winston** / **Pino** / **Loguru** / **Logback** / **Other**
- **Structured logging:** [JSON, custom format]

### Monitoring y APM
**Decisión:** [Application Performance Monitoring]
- **Metrics:** [Prometheus, StatsD, etc.]
- **Tracing:** [OpenTelemetry, Jaeger, etc.]
- **Health Checks:** [Health check libraries]

---

## 🧪 Testing Framework

### Testing Libraries
**Decisión:** [Stack de testing]
- **Unit Tests:** [Jest, PyTest, JUnit, etc.]
- **Integration Tests:** [Supertest, httpx, etc.]
- **Mocking:** [sinon, unittest.mock, etc.]

### Test Utilities
**Decisión:** [Utilities para testing]
- **Database Testing:** [Test containers, in-memory DBs]
- **API Testing:** [Supertest, requests, etc.]
- **Fixtures:** [Factory libraries]

---

## 🔧 Development Tools

### Code Quality
**Decisión:** [Herramientas de calidad]
- **Linting:** [ESLint, Pylint, Golint, etc.]
- **Formatting:** [Prettier, Black, gofmt, etc.]
- **Pre-commit hooks:** [husky, pre-commit, etc.]

### Development Utilities
**Decisión:** [Herramientas de desarrollo]
- **Hot Reload:** [nodemon, watchdog, etc.]
- **Environment Management:** [dotenv, etc.]
- **API Documentation:** [Swagger, FastAPI docs, etc.]

---

## 📈 Performance y Optimization

### Performance Libraries
**Decisión:** [Librerías de performance]
- **Caching:** [Redis, node-cache, etc.]
- **Connection Pooling:** [Database pool libraries]
- **Compression:** [gzip, brotli middleware]

### Async/Concurrency
**Decisión:** [Manejo de concurrency]
- **Async Libraries:** [asyncio, tokio, etc.]
- **Queue Systems:** [Bull, Celery, etc.]
- **Worker Processes:** [cluster, multiprocessing]

---

## 🏷️ Dependency Categories

### Production Dependencies
```json
// Ejemplo para Node.js - adaptar según stack
{{
  "dependencies": {{
    "// Framework": "",
    "express": "^4.x.x",
    
    "// Database": "",
    "prisma": "^5.x.x",
    "@prisma/client": "^5.x.x",
    
    "// Authentication": "",
    "jsonwebtoken": "^9.x.x",
    "bcrypt": "^5.x.x",
    
    "// Validation": "",
    "joi": "^17.x.x",
    
    "// Utilities": "",
    "dotenv": "^16.x.x",
    "cors": "^2.x.x"
  }}
}}
```

### Development Dependencies
```json
{{
  "devDependencies": {{
    "// Testing": "",
    "jest": "^29.x.x",
    "supertest": "^6.x.x",
    
    "// Code Quality": "",
    "eslint": "^8.x.x",
    "prettier": "^3.x.x",
    
    "// Development": "",
    "nodemon": "^3.x.x",
    "@types/node": "^20.x.x"
  }}
}}
```

---

## 🔒 Security y Updates

### Vulnerability Management
**Decisión:** [Estrategia de security]
- **Audit Tools:** [npm audit, safety, etc.]
- **Automated Scanning:** [Dependabot, Renovate]
- **Security Policies:** [Disclosure, updates]

### Update Strategy
**Decisión:** [Proceso de updates]
- **Major Updates:** [Proceso de evaluación]
- **Security Updates:** [Automated vs manual]
- **Breaking Changes:** [Migration strategy]

---

## 📋 Dependency Checklist

### Evaluación de Nuevas Dependencies
- [ ] **Necessity:** ¿Es realmente necesaria?
- [ ] **Alternatives:** ¿Se evaluaron alternativas?
- [ ] **Maintenance:** ¿Está activamente mantenida?
- [ ] **Security:** ¿Tiene vulnerabilidades conocidas?
- [ ] **Size/Performance:** ¿Impacto en performance?
- [ ] **License:** ¿Compatible con el proyecto?
- [ ] **Documentation:** ¿Tiene buena documentación?

### Mantenimiento Regular
- [ ] **Security Audit:** Review mensual
- [ ] **Updates:** Mantener actualizadas
- [ ] **Unused Dependencies:** Cleanup regular
- [ ] **Performance Impact:** Monitoreo
- [ ] **License Compliance:** Verificación

---

## 🔄 Próximos Pasos

### Setup Inicial
- [ ] [Configurar package manager]
- [ ] [Definir dependencies core]
- [ ] [Setup development tools]

### Configuración
- [ ] [Configurar linting y testing]
- [ ] [Setup CI/CD para dependencies]
- [ ] [Configurar security scanning]

### Mantenimiento
- [ ] [Establecer proceso de updates]
- [ ] [Documentar dependency decisions]
- [ ] [Setup monitoring de dependencies]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
