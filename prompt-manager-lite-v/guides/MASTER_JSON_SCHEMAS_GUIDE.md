# Guía Maestra de JSON Schemas - Prompt Manager Lite V

**Propósito:** Documentación completa de todos los schemas JSON del sistema, sus propósitos específicos, cómo leerlos e interpretarlos, y mejores prácticas contextuales basadas en estándares de la industria 2025.

**Fecha de Creación:** 2025-12-08  
**Versión:** 1.0  
**Basado en:** Investigación de mejores prácticas JSON Schema 2025

## 🎯 Introducción

Esta guía proporciona una comprensión completa de los **26 schemas JSON** que forman el núcleo del sistema Prompt Manager Lite V. Cada schema está diseñado para un propósito específico y sigue patrones modernos de la industria.

### 📋 Inventario Completo de Schemas

| # | Schema | Dominio | Propósito | Complejidad |
|---|--------|---------|-----------|-------------|
| 1 | `apiContract.json` | API | Especificación completa de contratos API | Alta |
| 2 | `architecture.json` | Arquitectura | Definición de patrones arquitectónicos | Alta |
| 3 | `dataModel.json` | Datos | Modelado de entidades y relaciones | Alta |
| 4 | `testingStrategy.json` | Testing | Estrategias y niveles de pruebas | Media |
| 5 | `deploymentStrategy.json` | DevOps | Estrategias de despliegue y ambientes | Media |
| 6 | `componentLibrary.json` | UI/UX | Inventario de componentes UI | Media |
| 7 | `visualBlueprint.json` | UI/UX | Blueprints visuales y wireframes | Media |
| 8 | `projectInfo.json` | Gestión | Información básica del proyecto | Baja |
| 9 | `projectManagement.json` | Gestión | Gestión de proyectos y equipos | Media |
| 10 | `businessLogic.json` | Negocio | Lógica de negocio y reglas | Media |
| 11 | `operationalStrategy.json` | Operaciones | Estrategias operativas y runbooks | Media |
| 12 | `soc2Compliance.json` | Seguridad | Marco de cumplimiento SOC 2 | Alta |
| 13 | `forensicAudit.json` | Auditoría | Auditoría y análisis forense | Media |
| 14 | `qualityGoals.json` | Calidad | Objetivos y métricas de calidad | Baja |
| 15 | `designPatterns.json` | Arquitectura | Patrones de diseño aplicados | Media |
| 16 | `designSystem.json` | UI/UX | Sistema de diseño (legacy) | Baja |
| 17 | `stateManagementPlan.json` | Frontend | Gestión de estado en frontend | Media |
| 18 | `wireframeStates.json` | UI/UX | Estados de wireframes y flujos | Baja |
| 19 | `featureManifest.json` | Gestión | Inventario de features | Baja |
| 20 | `featureLifecycle.json` | Gestión | Ciclo de vida de features | Baja |
| 21 | `bugLifecycle.json` | Gestión | Ciclo de vida de bugs | Baja |
| 22 | `fileExecutionMap.json` | Operaciones | Mapeo de archivos y ejecución | Baja |
| 23 | `dataModelDictionary.json` | Datos | Diccionario de términos de datos | Baja |
| 24 | `deepLogicAnalysis.json` | Análisis | Análisis profundo de lógica | Media |
| 25 | `definitions.json` | Meta | Definiciones y términos globales | Baja |
| 26 | `documentationManifest.json` | Meta | Manifest de documentación | Baja |

## 🏗️ Categorización por Dominios

### 🔌 **Dominio API (1 schema)**
Schemas relacionados con especificación y documentación de APIs.

#### `apiContract.json` - Especificación de Contratos API
**Propósito:** Define la especificación completa de una API REST siguiendo patrones OpenAPI 3.1.

**Estructura Clave:**
- `endpoints[]` - Lista de endpoints con métodos, parámetros, y respuestas
- `authentication` - Configuración de autenticación (JWT, OAuth2, API Key)
- `policies` - Políticas transversales (rate limiting, caching, CORS)
- `components` - Componentes reutilizables (schemas, parámetros, respuestas)

**Cómo Leerlo:**
1. Revisar `info` para entender el propósito de la API
2. Analizar `servers[]` para conocer los entornos disponibles
3. Examinar `endpoints[]` para cada operación disponible
4. Verificar `authentication` para entender los requisitos de seguridad
5. Revisar `policies` para políticas operativas

**Mejores Prácticas Aplicadas:**
- Validación estricta de métodos HTTP
- Patrones de URL consistentes
- Versionado semántico
- Documentación automática
- Seguridad por diseño

### 🏛️ **Dominio Arquitectura (2 schemas)**
Schemas que definen la estructura y patrones arquitectónicos del sistema.

#### `architecture.json` - Definición Arquitectónica
**Propósito:** Define los patrones arquitectónicos, stack tecnológico, y decisiones de diseño del sistema.

**Estructura Clave:**
- `architecturalPattern` - Patrón principal (Monolítico, Microservicios, Serverless)
- `technologyStack[]` - Stack tecnológico por capas
- `integrationPoints[]` - Puntos de integración entre sistemas
- `securityArchitecture` - Arquitectura de seguridad
- `observability` - Estrategias de monitoreo y observabilidad

**Cómo Leerlo:**
1. Identificar el patrón arquitectónico principal
2. Revisar el stack tecnológico por capas
3. Analizar puntos de integración y dependencias
4. Examinar la arquitectura de seguridad
5. Verificar estrategias de observabilidad

#### `designPatterns.json` - Patrones de Diseño
**Propósito:** Cataloga los patrones de diseño aplicados en diferentes capas del sistema.

**Estructura Clave:**
- `patterns[]` - Lista de patrones implementados
- `mapping` - Mapeo de patrones a componentes específicos
- `governance` - Políticas de gobierno de patrones
- `compliance` - Cumplimiento y estándares

### 📊 **Dominio Datos (3 schemas)**
Schemas relacionados con modelado, estructura y gestión de datos.

#### `dataModel.json` - Modelo de Datos
**Propósito:** Define el modelo de datos completo incluyendo entidades, atributos, relaciones y constraints.

**Estructura Clave:**
- `entities[]` - Definición de entidades con atributos
- `relationships[]` - Relaciones entre entidades
- `constraints[]` - Restricciones y reglas de negocio
- `namingConventions` - Convenciones de nomenclatura

**Cómo Leerlo:**
1. Revisar `entities[]` para entender las entidades principales
2. Analizar `relationships[]` para comprender las conexiones
3. Examinar `constraints[]` para reglas de negocio
4. Verificar `namingConventions` para consistencia

#### `dataModelDictionary.json` - Diccionario de Datos
**Propósito:** Proporciona definiciones y términos del dominio de datos.

#### `deepLogicAnalysis.json` - Análisis Profundo de Lógica
**Propósito:** Análisis detallado de la lógica de negocio compleja.

### 🧪 **Dominio Testing (2 schemas)**
Schemas relacionados con estrategias y procesos de testing.

#### `testingStrategy.json` - Estrategia de Testing
**Propósito:** Define la estrategia completa de testing incluyendo niveles, herramientas y métricas.

**Estructura Clave:**
- `testingLevels[]` - Niveles de testing (Unit, Integration, E2E)
- `frameworks[]` - Herramientas y frameworks de testing
- `coverageTargets` - Objetivos de cobertura
- `environments[]` - Entornos de testing

#### `qualityGoals.json` - Objetivos de Calidad
**Propósito:** Define métricas y objetivos de calidad del software.

### 🚀 **Dominio DevOps (1 schema)**
Schemas relacionados con despliegue y operaciones.

#### `deploymentStrategy.json` - Estrategia de Despliegue
**Propósito:** Define estrategias de despliegue, ambientes, y pipelines de CI/CD.

**Estructura Clave:**
- `environments[]` - Definición de ambientes (dev, staging, prod)
- `pipelines[]` - Pipelines de CI/CD
- `strategies` - Estrategias de despliegue (blue-green, canary, etc.)
- `rollback` - Procedimientos de rollback

### 🎨 **Dominio UI/UX (4 schemas)**
Schemas relacionados con interfaz de usuario y experiencia.

#### `componentLibrary.json` - Biblioteca de Componentes
**Propósito:** Inventario completo de componentes UI reutilizables.

#### `visualBlueprint.json` - Blueprint Visual
**Propósito:** Define la estructura visual y navegación de la aplicación.

#### `wireframeStates.json` - Estados de Wireframes
**Propósito:** Define estados y transiciones en wireframes.

#### `designSystem.json` - Sistema de Diseño (Legacy)
**Propósito:** Sistema de diseño básico (usar `design_system_schema.json` como canónico).

### 📋 **Dominio Gestión (5 schemas)**
Schemas relacionados con gestión de proyectos y features.

#### `projectInfo.json` - Información del Proyecto
**Propósito:** Información básica y metadatos del proyecto.

#### `projectManagement.json` - Gestión de Proyectos
**Propósito:** Estructura de gestión, equipos, y procesos.

#### `featureManifest.json` - Inventario de Features
**Propósito:** Catálogo de features con estados y ownership.

#### `featureLifecycle.json` - Ciclo de Vida de Features
**Propósito:** Define estados y transiciones de features.

#### `bugLifecycle.json` - Ciclo de Vida de Bugs
**Propósito:** Define estados y transiciones de bugs.

### ⚙️ **Dominio Operaciones (3 schemas)**
Schemas relacionados con operaciones y estrategias operativas.

#### `operationalStrategy.json` - Estrategia Operacional
**Propósito:** Define runbooks, procedimientos operativos, y estrategias de soporte.

#### `fileExecutionMap.json` - Mapeo de Ejecución de Archivos
**Propósito:** Mapea archivos del proyecto a sus contextos de ejecución.

#### `businessLogic.json` - Lógica de Negocio
**Propósito:** Define reglas de negocio y procesos core.

### 🔒 **Dominio Seguridad (2 schemas)**
Schemas relacionados con seguridad y cumplimiento.

#### `soc2Compliance.json` - Cumplimiento SOC 2
**Propósito:** Marco completo de cumplimiento SOC 2 con controles y auditoría.

#### `forensicAudit.json` - Auditoría Forense
**Propósito:** Procesos de auditoría y análisis forense.

### 🔧 **Dominio Meta (2 schemas)**
Schemas que definen la estructura del sistema de documentación.

#### `documentationManifest.json` - Manifest de Documentación
**Propósito:** Inventario y metadatos de toda la documentación del sistema.

#### `definitions.json` - Definiciones Globales
**Propósito:** Términos y definiciones globales del sistema.

### 🎯 **Dominio Frontend (1 schema)**
Schemas específicos para gestión de estado en frontend.

#### `stateManagementPlan.json` - Plan de Gestión de Estado
**Propósito:** Define estrategias de gestión de estado en aplicaciones frontend.

## 📖 Guía de Lectura e Interpretación

### 🔍 **Cómo Leer Cualquier Schema JSON**

#### 1. **Metadatos Básicos**
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.promptmanager.dev/schema-name/v1.0.0",
  "title": "Schema Title",
  "description": "Detailed description of purpose"
}
```

**Qué Buscar:**
- `$schema` - Versión de JSON Schema utilizada
- `$id` - Identificador único del schema
- `title` - Nombre descriptivo
- `description` - Propósito y contexto

#### 2. **Estructura Principal**
```json
{
  "type": "object",
  "required": ["campo1", "campo2"],
  "additionalProperties": false,
  "properties": { ... }
}
```

**Qué Buscar:**
- `type` - Tipo de datos principal
- `required[]` - Campos obligatorios
- `additionalProperties` - Si permite campos adicionales
- `properties` - Definición de campos

#### 3. **Definiciones Reutilizables**
```json
{
  "$defs": {
    "commonType": {
      "type": "object",
      "properties": { ... }
    }
  }
}
```

**Qué Buscar:**
- `$defs` - Definiciones reutilizables
- Referencias `$ref` - Uso de definiciones
- Composición con `allOf`, `anyOf`, `oneOf`

### 🎨 **Patrones de Lectura por Dominio**

#### **Schemas de API**
**Enfoque de Lectura:**
1. Revisar información general (`info`, `servers`)
2. Analizar endpoints por grupos funcionales
3. Examinar modelos de autenticación
4. Verificar políticas transversales

**Campos Críticos:**
- `endpoints[].method` y `endpoints[].path`
- `authentication.type`
- `policies.rateLimit`
- `components.schemas`

#### **Schemas de Arquitectura**
**Enfoque de Lectura:**
1. Identificar patrón arquitectónico principal
2. Revisar stack tecnológico por capas
3. Analizar puntos de integración
4. Examinar decisiones de seguridad

**Campos Críticos:**
- `architecturalPattern`
- `technologyStack[]`
- `integrationPoints[]`
- `securityArchitecture`

#### **Schemas de Datos**
**Enfoque de Lectura:**
1. Mapear entidades principales
2. Identificar relaciones clave
3. Revisar constraints y validaciones
4. Verificar convenciones de nomenclatura

**Campos Críticos:**
- `entities[].name` y `entities[].attributes[]`
- `relationships[]`
- `constraints[]`
- `namingConventions`

#### **Schemas de Testing**
**Enfoque de Lectura:**
1. Identificar niveles de testing
2. Revisar herramientas y frameworks
3. Analizar objetivos de cobertura
4. Examinar estrategias de datos de prueba

**Campos Críticos:**
- `testingLevels[]`
- `frameworks[]`
- `coverageTargets`
- `testData`

## 🚀 Mejores Prácticas por Dominio

### 📡 **APIs - Mejores Prácticas 2025**

**Basado en:** OpenAPI 3.1, REST API Guidelines, GraphQL Best Practices

#### **Estructura de Endpoints**
- **Nomenclatura RESTful:** Usar sustantivos para recursos
- **Versionado:** Incluir versión en URL o headers
- **Métodos HTTP:** Usar métodos semánticamente correctos
- **Códigos de Estado:** Usar códigos HTTP apropiados

#### **Autenticación Moderna**
- **JWT con RS256:** Para APIs distribuidas
- **OAuth 2.0 PKCE:** Para aplicaciones públicas
- **API Keys:** Solo para servicios internos
- **mTLS:** Para comunicación service-to-service

#### **Políticas Operativas**
- **Rate Limiting:** Implementar límites por usuario/IP
- **Caching:** Usar ETags y Cache-Control
- **CORS:** Configurar políticas específicas
- **Compression:** Habilitar gzip/brotli

### 🏗️ **Arquitectura - Mejores Prácticas 2025**

**Basado en:** Cloud Native Patterns, Microservices Patterns, Domain-Driven Design

#### **Patrones Arquitectónicos**
- **Microservicios:** Para sistemas complejos y equipos grandes
- **Modular Monolith:** Para equipos pequeños con complejidad media
- **Serverless:** Para cargas de trabajo variables
- **Event-Driven:** Para sistemas altamente desacoplados

#### **Stack Tecnológico**
- **Frontend:** React 18+, Vue 3, Angular 17+
- **Backend:** Node.js 20+, Python 3.12+, Go 1.21+
- **Bases de Datos:** PostgreSQL 16+, MongoDB 7+
- **Cache:** Redis 7+, Memcached
- **Mensajería:** Apache Kafka, RabbitMQ, AWS SQS

#### **Observabilidad**
- **Métricas:** Prometheus + Grafana
- **Logs:** ELK Stack, Fluentd
- **Tracing:** Jaeger, Zipkin
- **APM:** New Relic, DataDog, Dynatrace

### 📊 **Datos - Mejores Prácticas 2025**

**Basado en:** Data Modeling Best Practices, GDPR Compliance, Modern Database Design

#### **Modelado de Entidades**
- **Normalización:** Aplicar formas normales apropiadas
- **Índices:** Definir índices para consultas frecuentes
- **Constraints:** Usar constraints de base de datos
- **Audit Trail:** Incluir campos de auditoría

#### **Tipos de Datos**
- **UUIDs:** Para identificadores únicos
- **Timestamps:** ISO 8601 con timezone
- **JSON/JSONB:** Para datos semi-estructurados
- **Enums:** Para valores predefinidos

#### **Privacidad y Seguridad**
- **PII Identification:** Marcar datos personales
- **Encryption:** Cifrar datos sensibles
- **Retention:** Definir políticas de retención
- **Access Control:** Implementar RBAC

### 🧪 **Testing - Mejores Prácticas 2025**

**Basado en:** Testing Trophy, Shift-Left Testing, Test-Driven Development

#### **Pirámide de Testing**
- **Unit Tests:** 70% - Rápidos y aislados
- **Integration Tests:** 20% - Componentes integrados
- **E2E Tests:** 10% - Flujos críticos de usuario

#### **Herramientas Modernas**
- **JavaScript:** Jest, Vitest, Playwright
- **Python:** pytest, unittest, Selenium
- **Java:** JUnit 5, TestNG, Mockito
- **Go:** testing package, Testify

#### **Estrategias Avanzadas**
- **Contract Testing:** Pact, Spring Cloud Contract
- **Property-Based Testing:** Hypothesis, fast-check
- **Mutation Testing:** Stryker, PIT
- **Visual Testing:** Percy, Chromatic

### 🚀 **DevOps - Mejores Prácticas 2025**

**Basado en:** GitOps, Infrastructure as Code, Platform Engineering

#### **CI/CD Pipelines**
- **GitHub Actions:** Para proyectos en GitHub
- **GitLab CI:** Para GitLab
- **Jenkins:** Para entornos enterprise
- **Azure DevOps:** Para ecosistema Microsoft

#### **Estrategias de Despliegue**
- **Blue-Green:** Para zero-downtime
- **Canary:** Para validación gradual
- **Rolling:** Para actualizaciones continuas
- **Feature Flags:** Para control de features

#### **Infrastructure as Code**
- **Terraform:** Para multi-cloud
- **AWS CDK:** Para AWS
- **Pulumi:** Para programadores
- **Helm:** Para Kubernetes

### 🎨 **UI/UX - Mejores Prácticas 2025**

**Basado en:** Design Systems, Component-Driven Development, Accessibility Standards

#### **Sistemas de Diseño**
- **Design Tokens:** Para consistencia visual
- **Component Libraries:** Storybook, Bit
- **Accessibility:** WCAG 2.1 AA compliance
- **Responsive Design:** Mobile-first approach

#### **Gestión de Estado**
- **React:** Zustand, Redux Toolkit, Context
- **Vue:** Pinia, Vuex
- **Angular:** NgRx, Akita
- **Vanilla:** MobX, RxJS

## 🔧 Herramientas y Validación

### **Validadores JSON Schema**
- **AJV:** Más rápido para JavaScript/Node.js
- **jsonschema:** Para Python
- **everit-org/json-schema:** Para Java
- **Online:** jsonschemavalidator.net

### **Herramientas de Desarrollo**
- **VS Code Extensions:** JSON Schema validation
- **IntelliJ IDEA:** Built-in JSON Schema support
- **Postman:** API schema validation
- **Insomnia:** REST client with schema support

### **Generación de Documentación**
- **OpenAPI Generator:** Para APIs
- **JSON Schema to Markdown:** Para documentación
- **Redoc:** Para documentación interactiva
- **Swagger UI:** Para exploración de APIs

## 📚 Casos de Uso Comunes

### **Para Proyectos Nuevos**
1. Comenzar con `projectInfo.json` para definir básicos
2. Usar `architecture.json` para decisiones arquitectónicas
3. Definir `dataModel.json` para estructura de datos
4. Especificar `apiContract.json` para contratos API
5. Planificar `testingStrategy.json` para calidad

### **Para Proyectos Existentes**
1. Analizar código existente para extraer patrones
2. Documentar arquitectura actual en `architecture.json`
3. Reverse-engineer modelo de datos a `dataModel.json`
4. Documentar APIs existentes en `apiContract.json`
5. Formalizar estrategias de testing existentes

### **Para Auditorías y Compliance**
1. Usar `soc2Compliance.json` para SOC 2
2. Aplicar `forensicAudit.json` para auditorías
3. Documentar en `qualityGoals.json` métricas
4. Usar `operationalStrategy.json` para procedimientos

## 🔄 Flujos de Trabajo Recomendados

### **Flujo de Creación de Schema**
1. **Identificar Propósito:** ¿Qué problema resuelve?
2. **Investigar Mejores Prácticas:** Buscar estándares del dominio
3. **Definir Estructura:** Usar patrones apropiados
4. **Validar y Probar:** Con datos reales
5. **Documentar:** Crear playbook correspondiente

### **Flujo de Actualización de Schema**
1. **Analizar Impacto:** ¿Qué documentos se afectan?
2. **Mantener Compatibilidad:** Versionado semántico
3. **Actualizar Referencias:** En documentos y manifests
4. **Probar Cambios:** Con verificadores automáticos
5. **Comunicar Cambios:** A stakeholders relevantes

### **Flujo de Validación**
1. **Validación Sintáctica:** JSON válido
2. **Validación Semántica:** Schema válido
3. **Validación de Negocio:** Reglas específicas
4. **Validación de Integración:** Con otros schemas
5. **Validación de Rendimiento:** Tiempo de procesamiento

## 🎯 Troubleshooting Común

### **Errores Frecuentes**
- **Schema Inválido:** Verificar sintaxis JSON
- **Referencias Rotas:** Validar `$ref` paths
- **Tipos Incorrectos:** Verificar `type` declarations
- **Campos Faltantes:** Revisar `required` arrays

### **Problemas de Rendimiento**
- **Schemas Muy Complejos:** Simplificar estructura
- **Referencias Circulares:** Evitar loops infinitos
- **Validación Lenta:** Usar compilación de schemas
- **Memoria Excesiva:** Optimizar tamaño de schemas

### **Problemas de Mantenimiento**
- **Schemas Obsoletos:** Implementar versionado
- **Documentación Desactualizada:** Automatizar generación
- **Inconsistencias:** Usar herramientas de linting
- **Falta de Ejemplos:** Incluir casos de uso reales

## 📈 Evolución y Mantenimiento

### **Versionado de Schemas**
- **Semantic Versioning:** Major.Minor.Patch
- **Breaking Changes:** Incrementar major version
- **Nuevos Campos:** Incrementar minor version
- **Bug Fixes:** Incrementar patch version

### **Migración de Schemas**
- **Backward Compatibility:** Mantener compatibilidad hacia atrás
- **Deprecation Warnings:** Avisar sobre campos obsoletos
- **Migration Guides:** Documentar cambios necesarios
- **Automated Migration:** Scripts para migración automática

### **Monitoreo y Métricas**
- **Validation Success Rate:** % de validaciones exitosas
- **Performance Metrics:** Tiempo de validación
- **Error Patterns:** Tipos de errores más comunes
- **Usage Analytics:** Schemas más utilizados

## 🔗 Referencias y Recursos

### **Estándares Oficiales**
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/schema)
- [OpenAPI 3.1 Specification](https://spec.openapis.org/oas/v3.1.0)
- [RFC 7159 - JSON Data Interchange Format](https://tools.ietf.org/html/rfc7159)

### **Herramientas Recomendadas**
- [AJV - JSON Schema Validator](https://ajv.js.org/)
- [JSON Schema Store](https://schemastore.org/)
- [JSON Schema Validator Online](https://www.jsonschemavalidator.net/)

### **Mejores Prácticas de la Industria**
- [Google JSON Style Guide](https://google.github.io/styleguide/jsoncstyleguide.xml)
- [Microsoft REST API Guidelines](https://github.com/Microsoft/api-guidelines)
- [Stripe API Design](https://stripe.com/docs/api)

---

**Esta guía debe actualizarse cuando:**
- Se agreguen nuevos schemas al sistema
- Se publiquen nuevas versiones de JSON Schema
- Se identifiquen nuevas mejores prácticas de la industria
- Se reciba feedback de usuarios del sistema

**Mantenido por:** Sistema de Documentación Prompt Manager Lite V  
**Próxima Revisión:** 2025-03-08