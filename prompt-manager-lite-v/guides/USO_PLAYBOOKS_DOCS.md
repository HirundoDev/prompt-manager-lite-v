# 📚 Guía Completa de Uso de Playbooks de Documentación - Framework 2025

> **📌 REFERENCIA PRINCIPAL:** Para el contexto completo del ecosistema, consulta **[MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)** - La fuente definitiva del sistema Prompt Manager Lite V.

## 🎯 Propósito y Visión 2025

Esta guía establece el framework completo para usar los **playbooks de documentación universales** con placeholders adaptativos, proporcionando:
- **Workflow automatizado** para generación de documentación schema-driven
- **Templates universales** con 2,593+ placeholders validados
- **Herramientas de validación** y verificación de integridad
- **Integración CI/CD** para documentación continua
- **Mejores prácticas 2025** para documentación técnica moderna

## 📁 Estructura del Sistema

### **Arquitectura de Playbooks y Documentación:**
```bash
prompt-manager-lite-v/
├── prompt_playbooks/
│   └── documentation_playbooks/          # 🎯 Playbooks universales
│       ├── playbook-v2-DOC000-ProjectBrief.md
│       ├── playbook-v2-DOC008-APISpecification.md
│       ├── playbook-v2-DOC032-FrontendScreenFlow.md
│       └── [34 playbooks totales]
├── real_structure_documentation/
│   ├── docs/                             # 📄 Documentos generados
│   │   ├── DOC000-ProjectBrief.md
│   │   ├── DOC008-APISpecification.md
│   │   └── [34 documentos objetivo]
│   └── schemas/                          # 🔧 Schemas fuente
│       ├── master_blueprint_parts/       # Schemas modulares
│       └── design_system_schema.json     # Schema canónico de diseño
├── manifests/
│   └── documentation_manifest.json       # 📋 Manifest centralizado
└── tools/
    ├── doc_generator.py                  # 🤖 Generador automático
    ├── placeholder_validator.py          # ✅ Validador de placeholders
    └── integrity_checker.py              # 🔍 Verificador de integridad
```

## 🚀 Workflow Automatizado 2025

### **Comandos de Automatización:**
```bash
# 1. Generación automática desde schemas
python3 tools/doc_generator.py --playbook DOC008 --auto-extract

# 2. Validación completa
python3 tools/integrity_checker.py --full --fix-placeholders

# 3. Actualización de manifest
python3 tools/manifest_updater.py --sync-all

# 4. Pipeline completo
./scripts/generate_docs_pipeline.sh --target DOC008 --validate
```

### **Flujo Detallado por Documento:**
1. **📋 Preparación:** Abrir playbook correspondiente (ej.: `playbook-v2-DOC008-APISpecification.md`)
2. **🔧 Extracción:** Extraer datos automáticamente desde schemas mapeados
3. **📝 Generación:** Completar documento siguiendo template universal
4. **🎨 Personalización:** Adaptar placeholders al contexto específico
5. **✅ Validación:** Verificar integridad y consistencia
6. **📊 Registro:** Actualizar manifest con referencias y metadatos
7. **🔄 Integración:** Ejecutar pipeline CI/CD para validación continua

## 🎯 Mejores Prácticas 2025

### **Principios Fundamentales:**
- **📊 Schema-First:** Priorizar datos provenientes de schemas sobre narrativa manual
- **🔗 Referencias Estables:** Usar identificación estable (IDs/slugs) para componentes, endpoints, entidades
- **📚 Consistencia Terminológica:** Mantener coherencia con `dataModelDictionary.json`
- **🎨 Placeholders Universales:** Usar formato `[PLACEHOLDER_NAME]` para adaptabilidad
- **🔄 Automatización:** Maximizar generación automática, minimizar trabajo manual
- **✅ Validación Continua:** Implementar verificación automática en cada cambio

### **Convenciones de Placeholders:**
```yaml
formato_placeholders:
  sintaxis: "[UPPERCASE_WITH_UNDERSCORES]"
  ejemplos:
    proyecto: "[PROJECT_NAME]"
    ambiente: "[ENVIRONMENT]"
    url_api: "[API_BASE_URL]"
    version: "[VERSION]"
    equipo: "[TEAM_NAME]"
  
reglas:
  - Un placeholder por campo
  - Nombres descriptivos y específicos
  - Consistencia entre documentos
  - Validación automática
```

Guía rápida por algunos DOCs comunes
- DOC008-APISpecification: seguir secciones de endpoints, auth, rate limiting, caching, tracing; poblar principalmente desde `apiContract.json`.
- DOC009-DataModel: poblar entidades, relaciones, convenciones, y diccionario desde `dataModel.json` + `dataModelDictionary.json`.
- DOC010-Deployment: poblar entornos, pipelines, rollout/rollback y compliance desde `deploymentStrategy.json` (y cruzar con arquitectura/observabilidad cuando aplique).
- DOC011-TestingStrategy: seguir pirámide, targets, datos de prueba, entornos desde `testingStrategy.json` y gates de `deploymentStrategy`.
- DOC032-FrontendScreenFlow: poblar flujo/páginas/estados desde `visualBlueprint.json` + `wireframeStates.json`, y validar componentes con `componentLibrary.json`.

## 📋 Template de Frontmatter Avanzado 2025

```yaml
---
# Identificación del Documento
docId: "DOC[XXX]-[DOCUMENT_NAME]"
title: "[DOCUMENT_TITLE]"
version: "[VERSION]"
status: "draft|review|approved|deprecated"

# Ownership y Responsabilidad
ownerAgent: "[TEAM_NAME]|[PERSON_NAME]"
maintainers:
  - "[MAINTAINER_1]"
  - "[MAINTAINER_2]"
reviewers:
  - "[REVIEWER_1]"
  - "[REVIEWER_2]"

# Metadatos Temporales
createdDate: "[CREATION_DATE]"
lastUpdated: "[LAST_UPDATE_DATE]"
nextReview: "[NEXT_REVIEW_DATE]"

# Referencias a Schemas
schemaRefs:
  primary:
    - "real_structure_documentation/schemas/master_blueprint_parts/[PRIMARY_SCHEMA].json"
  secondary:
    - "real_structure_documentation/schemas/master_blueprint_parts/[SECONDARY_SCHEMA].json"
    - "real_structure_documentation/schemas/design_system_schema.json"

# Documentos Relacionados
relatedDocs:
  dependencies:
    - "DOC[YYY]-[DEPENDENCY_DOC]"
  references:
    - "DOC[ZZZ]-[REFERENCE_DOC]"

# Configuración de Generación
generationConfig:
  autoExtract: true
  validatePlaceholders: true
  updateManifest: true
  
# Tags para Categorización
tags:
  - "[DOMAIN_TAG]"
  - "[TECHNOLOGY_TAG]"
  - "[PRIORITY_TAG]"

# Métricas de Calidad
quality:
  completeness: "[COMPLETENESS_PERCENTAGE]%"
  placeholderCount: [PLACEHOLDER_COUNT]
  lastValidation: "[LAST_VALIDATION_DATE]"
---
```

Extracción detallada por documento (paso a paso)
- DOC008-APISpecification
  - Secciones mínimas: Introducción, Endpoints (tabla), Autenticación, Políticas (Rate Limiting/Caching/Tracing), Versionado, Errores.
  - Origen:
    - `apiContract.endpoints[]` → tabla con `method`, `path`, `summary`.
    - `apiContract.endpoints[].parameters[]/requestBody/responses` → detalles por endpoint.
    - `apiContract.authentication|rateLimiting|caching|tracing|versioning`.
  - Cruces: `architecture.integrationPoints[]` por `referenceKey`.

- DOC009-DataModel
  - Secciones: Entidades, Atributos, Relaciones, Convenciones, Glosario.
  - Origen: `dataModel.entities[]`, `dataModel.relationships[]`, `dataModel.namingConventions`, `dataModelDictionary.*`.

- DOC010-Deployment
  - Secciones: Ambientes, Pipelines, Estrategias (release, rollout, rollback), Compliance, Observabilidad.
  - Origen: `deploymentStrategy.environments[]`, `pipelines[]`, `releaseStrategy`, `rollout`, `rollback`, `compliance`; enlazar con `architecture.observability`.

- DOC011-TestingStrategy
  - Secciones: Pirámide, Tipos de prueba, Cobertura, Datos, Entornos, Gates.
  - Origen: `testingStrategy.pyramid|types|coverageTargets|testData|environments`, `deploymentStrategy.pipelines`.

- DOC032-FrontendScreenFlow
  - Secciones: Rutas y pantallas, Referencias a componentes, Estados/Transiciones, Temas/Breakpoints.
  - Origen: `visualBlueprint.pages[]` y `pages[].componentRefs[]`; resolver con `componentLibrary.components[].{id,slug}`; estados en `wireframeStates.states[]`.

Ejemplos de mapeo (JSONPath aproximado)
- Tabla de endpoints:
  - `$..apiContract.endpoints[*].method`
  - `$..apiContract.endpoints[*].path`
  - `$..apiContract.endpoints[*].summary`
- Componentes en una página:
  - `$..visualBlueprint.pages[?(@.route=="/home")].componentRefs[*]`
  - Resolver cada ref contra: `$..componentLibrary.components[*].id|slug`

Procedimiento de verificación
1) Completa el doc siguiendo su playbook.
2) Añade `schemaRefs` en el frontmatter.
3) Ejecuta `python3 tools/verify_integrity.py`.
4) Revisa la guía de conexión para detectar gaps o cruces rotos.
5) Si falta un campo en schema, vuelve a `USO_PLAYBOOKS_SCHEMAS.md` y extiende el schema con campos opcionales.

Checklists (genéricas)
- Playbook cubierto 100% (sin placeholders críticos).
- Doc enlaza a sus schemas fuente (frontmatter u otra sección).
- Terminología coherente con el diccionario de datos.
- Cross-check con arquitectura/deployment/testing según aplique.

Resolución de conflictos
- Si el playbook sugiere algo no representado aún en schemas, documenta como gap y vuelve a `schema playbooks` para evaluar una extensión opcional (retrocompatible).

Referencias
- Playbooks de documentación: `prompt_playbooks/documentation_playbooks/`
- Guía de conexión: `guides/CONEXION_SCHEMAS_DOCS.md`
- Schemas: `real_structure_documentation/schemas/**`

Índice completo DOCs ↔ Playbooks (canónico)
- DOC000-ProjectBrief.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC000-ProjectBrief.md`
- DOC001-ProjectREADME.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC001-ProjectREADME.md`
- DOC002-ProductDefinition.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC002-ProductDefinition.md`
- DOC003-DesignSystem.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC003-DesignSystem.md`
- DOC004-FrontendArchitecture.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC004-FrontendArchitecture.md`
- DOC005-FrontendDependencies.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC005-FrontendDependencies.md`
- DOC006-BackendArchitecture.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC006-BackendArchitecture.md`
- DOC007-BackendDependencies.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC007-BackendDependencies.md`
- DOC008-APISpecification.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC008-APISpecification.md`
- DOC009-DataModel.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC009-DataModel.md`
- DOC010-Deployment.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC010-Deployment.md`
- DOC011-TestingStrategy.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC011-TestingStrategy.md`
- DOC012-SecurityCompliance.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC012-SecurityCompliance.md`
- DOC013-ChangeLog.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC013-ChangeLog.md`
- DOC014-IssueTemplate.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC014-IssueTemplate.md`
- DOC015-PullRequestTemplate.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC015-PullRequestTemplate.md`
- DOC016-Contributing.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC016-Contributing.md`
- DOC017-ADR-Index.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC017-ADR-Index.md` (alias: `playbook-v2-DOC017-ADRIndex.md`)
- DOC019-CLI-Command-Reference.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC019-CLI-Command-Reference.md` (alias: `playbook-v2-DOC019-CLICommandReference.md`)
- DOC020-CodeOfConduct.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC020-CodeOfConduct.md`
- DOC021-OnboardingGuide.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC021-OnboardingGuide.md`
- DOC022-ReleaseProcess.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC022-ReleaseProcess.md`
- DOC023-BackendManifest.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC023-BackendManifest.md`
- DOC024-DatabaseManifest.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC024-DatabaseManifest.md`
- DOC025-FrontendManifest.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC025-FrontendManifest.md`
- DOC026-ProjectFileManifest.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC026-ProjectFileManifest.md`
- DOC027-SharedLibsManifest.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC027-SharedLibsManifest.md`
- DOC028-OperationsRunbook.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC028-OperationsRunbook.md`
- DOC029-ProjectRoadmap.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC029-ProjectRoadmap.md`
- DOC030-FeatureIndex.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC030-FeatureIndex.md`
- DOC031-BugIndex.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC031-BugIndex.md`
- DOC032-FrontendScreenFlow.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC032-FrontendScreenFlow.md`
- DOC033-SOC2Compliance.md ↔ `prompt_playbooks/documentation_playbooks/playbook-v2-DOC033-SOC2Compliance.md`

Notas
 - Aliases eliminados (usar solo canónicos):
   - DOC017: usar únicamente `playbook-v2-DOC017-ADR-Index.md`.
   - DOC019: usar únicamente `playbook-v2-DOC019-CLI-Command-Reference.md`.
  - DOC020: alias eliminado; usar únicamente el canónico `playbook-v2-DOC020-CodeOfConduct.md`.
- Plantilla adicional: `playbook-v2-DOC033-ADRTemplate.md` (plantilla de ADR; no corresponde a un DOC del inventario actual).

## Manifest y cobertura de schemas

- El manifest de documentación centraliza metadatos de cada DOC, incluyendo referencias a schemas mediante `schemaRefs` (opcional pero recomendado): `manifests/documentation_manifest.json`.
- El schema del manifest (definición) vive en `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json` e incluye `documents[].schemaRefs`.
- Cada DOC debería listar sus schemas fuente en el frontmatter (ver plantilla arriba) y reflejar esas mismas rutas en el manifest para asegurar trazabilidad.

Checklist rápido de cobertura
- ¿El DOC tiene `schemaRefs` en su frontmatter? (opcional)
- ¿El mismo conjunto está reflejado en `manifests/documentation_manifest.json`?
- ¿Cada schema en `real_structure_documentation/schemas/**` aparece al menos en: (a) esta guía de conexión y/o (b) `schemaRefs` del manifest? El verificador reporta gaps no bloqueantes.

Enlaces
- Manifest (instancia): `manifests/documentation_manifest.json`
- Manifest (schema): `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json`
