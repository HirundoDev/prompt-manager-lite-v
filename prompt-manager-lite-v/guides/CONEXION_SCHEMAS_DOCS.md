# 🔗 Guía Completa de Conexión: JSON Schemas ↔️ Documentación - 2025

> **📌 REFERENCIA PRINCIPAL:** Para el contexto completo del ecosistema, consulta **[MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)** - La fuente definitiva del sistema Prompt Manager Lite V.

## 🎯 Propósito y Visión 2025

Esta guía establece el framework completo de mapeo bidireccional entre JSON schemas y documentación, proporcionando:
- **Mapeo exhaustivo** de cada documento (DOCxxx) con sus schemas correspondientes
- **Workflows automatizados** para extracción, transformación y validación de datos
- **Herramientas de sincronización** para mantener consistencia en tiempo real
- **Mejores prácticas 2025** para schema-driven documentation

## 📁 Estructura y Organización

### **Arquitectura de Schemas y Documentación:**
```bash
prompt-manager-lite-v/
├── real_structure_documentation/
│   ├── schemas/
│   │   ├── master_blueprint_parts/     # Schemas modulares
│   │   │   ├── apiContract.json        # Contratos API
│   │   │   ├── architecture.json       # Arquitectura del sistema
│   │   │   ├── componentLibrary.json   # Biblioteca de componentes
│   │   │   ├── dataModel.json          # Modelo de datos
│   │   │   ├── deploymentStrategy.json # Estrategia de despliegue
│   │   │   ├── testingStrategy.json    # Estrategia de testing
│   │   │   └── [30+ schemas más]
│   │   └── design_system_schema.json   # Schema del sistema de diseño
│   └── docs/
│       └── DOC***.md                   # Documentos generados/mantenidos
├── prompt_playbooks/
│   ├── schemas_playbooks/              # Playbooks para schemas
│   │   └── playbook_schema-*.md
│   └── documentation_playbooks/        # Playbooks para docs
│       └── playbook-v2-DOC***.md
├── manifests/
│   └── documentation_manifest.json     # Manifest de documentación
└── tools/
    ├── schema_to_doc.py               # Generador de docs desde schemas
    ├── doc_to_schema.py               # Extractor de schemas desde docs
    ├── sync_validator.py              # Validador de sincronización
    └── mapping_analyzer.py            # Analizador de mapeos
```

## 🔑 Convenciones y Estándares 2025

### **Sistema de Referencias Universal:**
```yaml
identificadores:
  componentes:
    primary: "id"          # UUID único
    secondary: "slug"      # Nombre readable
    fallback: "name"       # Nombre humano
  
  endpoints:
    primary: "referenceKey" # Clave única compartida
    secondary: "path"       # Ruta del endpoint
    
  entidades:
    primary: "entityId"    # ID de entidad
    secondary: "tableName"  # Nombre de tabla
    
  features:
    primary: "featureId"   # ID de feature
    secondary: "featureKey" # Clave de feature flag

convenciones_mapeo:
  - "Use bracketed placeholders: [PLACEHOLDER_NAME]"
  - "Maintain bidirectional references"
  - "Version all schema changes"
  - "Document breaking changes"
```

### **Reglas de Sincronización:**
1. **Componentes UI:** `componentLibrary.components[].id` → `visualBlueprint.componentRefs[]`
2. **API ↔ Arquitectura:** `apiContract.endpoints[].referenceKey` ↔ `architecture.integrationPoints[].referenceKey`
3. **Data Model:** `dataModel.namingConventions` ↔ `dataModelDictionary.terms[]`
4. **Testing ↔ Deployment:** `testingStrategy.environments[]` ↔ `deploymentStrategy.pipelines[].stages[]`
5. **Design System:** `design_system_schema.json` (canonical) → `componentLibrary.components[].designTokens`

## 📊 Matriz Completa de Mapeo Doc → Schemas

### **Mapeo Detallado con Ejemplos:**
 - DOC000-ProjectBrief → `projectInfo.json` (+ `projectManagement.json` para snapshot; manifest para owners/reviews)
 - DOC001-ProjectREADME → `projectInfo.json`
 - DOC002-ProductDefinition → `businessLogic.json`, `definitions.json`, `projectInfo.json`
 - DOC003-DesignSystem → `design_system_schema.json` (canónico) y/o `designSystem.json`
 - DOC004-FrontendArchitecture → `architecture.json`, `designPatterns.json`, `stateManagementPlan.json` (parcial)
 - DOC005-FrontendDependencies → `componentLibrary.json`, `design_system_schema.json` (parcial)
 - DOC006-BackendArchitecture → `architecture.json`, `deepLogicAnalysis.json` (parcial)
 - DOC007-BackendDependencies → (parcial) + `architecture.json`, `operationalStrategy.json`
 - DOC008-APISpecification → `apiContract.json` (+ `architecture.integrationPoints`, `designPatterns.security`)
 - DOC009-DataModel → `dataModel.json` + `dataModelDictionary.json`
 - DOC010-Deployment → `deploymentStrategy.json` (+ `architecture.deploymentTopology`, `observability`, `availability`, `designPatterns.mapping.infrastructure/devex`, `qualityGoals.json`)
 - DOC011-TestingStrategy → `testingStrategy.json` (+ `deploymentStrategy.pipelines`, `qualityGoals.json`)
 - DOC012-SecurityCompliance → `architecture.securityArchitecture`, `designPatterns.governance/compliance`, `apiContract.authentication/rateLimiting`, `forensicAudit.json` (parcial)
 - DOC013-ChangeLog → (manual, plantilla); sin schema, validar con playbook correspondiente
 - DOC014-IssueTemplate → (manual, plantilla); sin schema, validar con playbook correspondiente
 - DOC015-PullRequestTemplate → (manual, plantilla); sin schema, validar con playbook correspondiente
 - DOC016-Contributing → (manual, política); opcional `projectManagement.json` para roles/flujo
 - DOC017-ADR-Index → `architecture.adrReferences` (y manifest cuando exista instancia)
 - DOC019-CLI-Command-Reference → `cli_schema.json` (si se mantiene)
 - DOC020-CodeOfConduct → (manual, política); sin schema, validar con playbook correspondiente
 - DOC021-OnboardingGuide → (manual) + opcional `projectManagement.json` (equipos, ownership, onboarding)
 - DOC022-ReleaseProcess → `deploymentStrategy.json` (+ `projectManagement.json`)
 - DOC023-BackendManifest → `featureManifest.json` (+ `architecture.json`, `operationalStrategy.json`)
 - DOC024-DatabaseManifest → `dataModel.json` (subconjunto) + `architecture.deploymentTopology` (parcial)
 - DOC025-FrontendManifest → `componentLibrary.json` (+ `stateManagementPlan.json` parcial)
 - DOC026-ProjectFileManifest → `fileExecutionMap.json`
 - DOC027-SharedLibsManifest → (manual) + opcional `projectManagement.json` (gobernanza/ownership)
 - DOC028-OperationsRunbook → `operationalStrategy.json` (+ `deploymentStrategy`, `architecture.observability`, `forensicAudit.json` parcial)
 - DOC029-ProjectRoadmap → `projectManagement.json` (hitos/roadmap)
 - DOC030-FeatureIndex → `featureManifest.json`, `featureLifecycle.json`
 - DOC031-BugIndex → `bugLifecycle.json`
 - DOC032-FrontendScreenFlow → `visualBlueprint.json` + `wireframeStates.json` + `componentLibrary.json`
 - DOC033-SOC2Compliance → `soc2Compliance.json` (+ `architecture.json`, `forensicAudit.json`)

## 🔧 Workflows de Extracción y Transformación

### **Proceso Automatizado de Generación:**
- DOC008 (API):
  - Endpoints: `apiContract.endpoints[]` (método, path, summary, params, requestBody, responses)
  - Políticas: `authentication`, `rateLimiting`, `caching`, `tracing`, `versioning`
  - Integración: cruzar con `architecture.integrationPoints[]` por `referenceKey`
- DOC009 (Data Model):
  - Entidades/atributos: `dataModel.entities[]`
  - Relaciones: `dataModel.relationships[]`
  - Convenciones y diccionario: `dataModel.namingConventions` + `dataModel.dictionaryRef`/`dataModelDictionary.*`
- DOC010 (Deployment):
  - Envs: `deploymentStrategy.environments[]`
  - Pipelines y gates: `deploymentStrategy.pipelines[]`, `releaseStrategy`, `rollout`, `rollback`, `compliance`
  - Infra/devex: `designPatterns.mapping.infrastructure/devex`
- DOC011 (Testing):
  - Niveles/targets/datos: `testingStrategy.*` (pyramid, coverageTargets, testData, environments)
- DOC032 (Screen Flow):
  - Páginas y refs: `visualBlueprint.pages[]`, `componentRefs[]`
  - Estados/wireframes: `wireframeStates.states[]`
  - Componentes base: `componentLibrary.components[]` (resolver por id/slug)
- DOC012 (Security Compliance):
  - Arquitectura de seguridad: `architecture.securityArchitecture.*`
  - Políticas API: `apiContract.authentication`, `rateLimiting`, `caching`
  - Gobierno/compliance: `designPatterns.governance`, `compliance`
  - Auditoría/forensics (si aplica): `forensicAudit.*`
- DOC017 (ADR Index):
  - Entradas ADR: `architecture.adrReferences[]` (id, título, fecha, status, link)
- DOC019 (CLI Reference):
  - Comandos/flags: `cli_schema.commands[]`, `options[]`, `examples[]`
- DOC022 (Release Process):
  - Pipelines/gates: `deploymentStrategy.pipelines[]`
  - Estrategias: `releaseStrategy`, `rollout`, `rollback`
  - Roles/owner (opcional): `projectManagement.*`
- DOC023 (Backend Manifest):
  - Features/servicios: `featureManifest.features[]` (id, nombre, owner, status)
  - Alineación arquitectura/ops: `architecture.*`, `operationalStrategy.*`
- DOC024 (Database Manifest):
  - Entidades/tablas: `dataModel.entities[]`
  - Relaciones/constraints: `dataModel.relationships[]`
- DOC025 (Frontend Manifest):
  - Componentes: `componentLibrary.components[]` (id, slug, status, dependencias)
  - Estado (opcional): `stateManagementPlan.*`
- DOC026 (Project File Manifest):
  - Entradas: `fileExecutionMap.files[]` (path, tipo, owner, triggeredBy)
- DOC027 (Shared Libs Manifest):
  - Manual: listar librerías compartidas, versión, repositorios y ownership
  - Gobernanza/owners (opcional): `projectManagement.*`
- DOC028 (Operations Runbook):
  - Runbooks/procedimientos: `operationalStrategy.runbooks[]`
  - Observabilidad: `architecture.observability.*`
  - Integración con despliegue: `deploymentStrategy.*`
  - Forensics (opcional): `forensicAudit.*`
- DOC029 (Project Roadmap):
  - Hitos/roadmap: `projectManagement.milestones[]`, `timeline`, `risks`
- DOC030 (Feature Index):
  - Features: `featureManifest.features[]`
  - Ciclo de vida: `featureLifecycle.*`
- DOC031 (Bug Index):
  - Flujos/estados: `bugLifecycle.statuses[]`, `transitions[]`
- DOC013 (ChangeLog) [manual]:
  - Fuentes: tags de release, historia de commits; mantener formato del playbook
- DOC014 (Issue Template) [manual]:
  - Verificar secciones mínimas (título, descripción, pasos, severidad, etiquetas)
- DOC015 (PR Template) [manual]:
  - Verificar checklist, pruebas, riesgos, rollback, links a issues/ADRs
- DOC016 (Contributing) [manual]:
  - Roles/procesos, guía de estilo, acuerdos de contribución (opcional `projectManagement`)
- DOC020 (Code of Conduct) [manual]:
  - Política estándar y canales de contacto; mantener versión y enlace de referencia
- DOC021 (Onboarding Guide) [manual]:
  - Checklist de onboarding, accesos, owners (opcional `projectManagement`)
- DOC000 (Brief): `projectInfo.*`

## ✅ Validación y Testing Automatizado

### **Suite Completa de Validación:**
```bash
# 1. Validación de integridad básica
python3 tools/verify_integrity.py --full

# 2. Análisis de mapeos
python3 tools/mapping_analyzer.py --report

# 3. Validación de referencias cruzadas
python3 tools/sync_validator.py --check-all

# 4. Generación de reporte de cobertura
python3 tools/schema_coverage.py --output coverage.html

# 5. Validación de schemas contra JSON Schema
python3 tools/validate_schemas.py --strict

# 6. Generación de blueprint combinado
python3 tools/combine_schemas.py --output master_blueprint_combined.json

# 7. Validación final del blueprint
python3 tools/validate_blueprint.py master_blueprint_combined.json
```

### **Checklist de Validación Manual:**
- [ ] Todos los `componentRefs` resuelven a `componentLibrary`
- [ ] Endpoints y integrationPoints sincronizados vía `referenceKey`
- [ ] `namingConventions` consistente con `dataModelDictionary`
- [ ] Testing environments alineados con deployment pipelines
- [ ] Versiones de schemas documentadas
- [ ] Breaking changes identificados
- [ ] Placeholders universales aplicados

## 🔄 Matriz Inversa: Schemas → Documentación

### **Mapeo Completo con Impacto:**
 - projectInfo.json → DOC000, DOC001
 - businessLogic.json → DOC002
 - definitions.json → DOC002
 - projectManagement.json → DOC000, DOC021, DOC022, DOC027 (parcial), DOC029
 - architecture.json → DOC004, DOC006, DOC010, DOC012, DOC017, DOC028
 - deepLogicAnalysis.json → DOC006 (parcial)
 - apiContract.json → DOC008, DOC012
 - dataModel.json → DOC009, DOC024
 - dataModelDictionary.json → DOC009 (glosario/convenciones)
 - deploymentStrategy.json → DOC010, DOC011, DOC022, DOC028
 - testingStrategy.json → DOC011
 - componentLibrary.json → DOC005, DOC025, DOC032
 - visualBlueprint.json → DOC032
 - wireframeStates.json → DOC032
 - designPatterns.json → DOC004, DOC006, DOC010, DOC012
 - soc2Compliance.json → DOC033
 - operationalStrategy.json → DOC007, DOC028
 - featureManifest.json → DOC023, DOC030
 - featureLifecycle.json → DOC030
 - bugLifecycle.json → DOC031
 - fileExecutionMap.json → DOC026
 - cli_schema.json → DOC019
 - stateManagementPlan.json → DOC004 (parcial), DOC025 (parcial), DOC032 (estados)
 - qualityGoals.json → DOC010, DOC011
 - forensicAudit.json → DOC012 (parcial), DOC028 (parcial)
 - designSystem.json (legacy) → DOC003 (opcional)
 - design_system_schema.json (canónico) → DOC003, DOC005 (parcial)
 - master_blueprint_schema.json (meta) → combinador/estructura general (no directo a un DOC)
 - documentationManifest.json (meta) → índice/owners/dependencias de todos los DOCs

## 📝 Ejemplos Prácticos de Extracción

### **Workflows Detallados con Comandos:**
- DOC008-APISpecification desde apiContract.json
  1) Lista de endpoints: leer `endpoints[]` y tabular `method`, `path`, `summary`.
  2) Parámetros y cuerpos: para cada endpoint, usar `parameters[]`, `requestBody`, `responses`.
  3) Políticas transversales: `authentication`, `rateLimiting`, `caching`, `tracing`, `versioning`.
  4) Vincular con arquitectura: cruzar con `architecture.integrationPoints[]` por `referenceKey`.

- DOC009-DataModel desde dataModel.json + dataModelDictionary.json
  1) Entidades: `entities[].name`, `attributes[]` (nombre, tipo, nullability, default).
  2) Relaciones: `relationships[]` (source, target, cardinalidad, constraints).
  3) Convenciones: `namingConventions` y términos del `dataModelDictionary` (definiciones/apéndice).

- DOC010-Deployment desde deploymentStrategy.json (+ arquitectura/designPatterns)
  1) Ambientes: `environments[]` (nombres, variables, secretos gestionados).
  2) Pipelines: `pipelines[]` (stages, gates, artefactos, aprobaciones).
  3) Estrategias: `releaseStrategy`, `rollout`, `rollback`, `compliance`.
  4) Infra/devex: mapear `designPatterns.mapping.infrastructure/devex` a plataformas/servicios/herramientas.

- DOC011-TestingStrategy desde testingStrategy.json (+ deploymentStrategy)
  1) Pirámide y tipos: `pyramid`, `types[]`.
  2) Cobertura/objetivos: `coverageTargets`.
  3) Datos de prueba: `testData`.
  4) Entornos: `environments[]` y su alineación con `deploymentStrategy.pipelines`.

- DOC032-FrontendScreenFlow desde visualBlueprint.json + wireframeStates.json + componentLibrary.json
  1) Páginas/flows: `pages[]` con `title`, `route`, `layout`.
  2) Referencias de componentes: `pages[].componentRefs[]` resolviendo contra `componentLibrary.components[].{id,slug,name}` (preferir id/slug).
  3) Estados/wireframes: `wireframeStates.states[]` por `viewName` y árbol de nodos.
  4) Activos/temas: `assets[]`, `themes[]`, `breakpoints[]` si aplica.

## 🚀 Scripts de Automatización

### **Generador de Documentación desde Schemas:**
```python
# tools/schema_to_doc.py
import json
import yaml
from pathlib import Path

def generate_doc_from_schema(schema_path, doc_template, output_path):
    """
    Genera documentación desde un schema JSON
    """
    with open(schema_path) as f:
        schema = json.load(f)
    
    # Transform schema to documentation
    doc_content = transform_schema_to_doc(schema, doc_template)
    
    # Write documentation
    with open(output_path, 'w') as f:
        f.write(doc_content)
    
    return output_path

# Uso:
# python3 tools/schema_to_doc.py apiContract.json DOC008-template.md DOC008-APISpecification.md
```

### **Sincronizador Bidireccional:**
```python
# tools/bidirectional_sync.py
def sync_schema_and_doc(schema_path, doc_path):
    """
    Mantiene schemas y docs sincronizados
    """
    # Detect changes
    schema_changes = detect_schema_changes(schema_path)
    doc_changes = detect_doc_changes(doc_path)
    
    # Apply bidirectional sync
    if schema_changes:
        update_doc_from_schema(schema_changes, doc_path)
    
    if doc_changes:
        update_schema_from_doc(doc_changes, schema_path)
    
    # Validate consistency
    validate_sync(schema_path, doc_path)
```

### **Analizador de Cobertura:**
```bash
# Comando para análisis de cobertura
python3 tools/coverage_analyzer.py \
  --schemas real_structure_documentation/schemas/ \
  --docs real_structure_documentation/docs/ \
  --output coverage_report.json

# Genera dashboard HTML
python3 tools/coverage_dashboard.py coverage_report.json
```

## 💡 Mejores Prácticas 2025

### **DO's:**
- ✅ Mantener mapeos bidireccionales actualizados
- ✅ Versionar todos los cambios de schema
- ✅ Usar placeholders universales [PLACEHOLDER]
- ✅ Automatizar validación en CI/CD
- ✅ Documentar breaking changes
- ✅ Generar docs desde schemas cuando sea posible
- ✅ Mantener un source of truth único

### **DON'Ts:**
- ❌ Duplicar información manualmente
- ❌ Ignorar warnings de validación
- ❌ Hacer cambios sin actualizar mapeos
- ❌ Usar referencias hardcodeadas
- ❌ Omitir tests de sincronización

## 📈 Métricas y Monitoreo

### **KPIs de Sincronización:**
```yaml
metricas:
  cobertura:
    target: ">95% de docs con schemas"
    actual: "[COVERAGE_PERCENTAGE]"
  
  consistencia:
    target: "100% referencias válidas"
    actual: "[CONSISTENCY_PERCENTAGE]"
  
  automatizacion:
    target: ">80% generación automática"
    actual: "[AUTOMATION_PERCENTAGE]"
  
  validacion:
    target: "0 errores en CI/CD"
    actual: "[VALIDATION_ERRORS]"
```

### **Dashboard de Estado:**
```markdown
## 📊 Schema-Doc Sync Status

| Document | Schema Coverage | Last Sync | Status |
|----------|----------------|-----------|--------|
| DOC008-API | 100% | 2025-01-18 | ✅ Synced |
| DOC009-DataModel | 95% | 2025-01-17 | ⚠️ Needs Update |
| DOC010-Deployment | 100% | 2025-01-18 | ✅ Synced |
```

## 🔍 Troubleshooting Común

### **Problema: Referencias rotas**
```bash
# Diagnóstico
python3 tools/find_broken_refs.py --fix

# Solución automática
python3 tools/repair_references.py --auto
```

### **Problema: Schemas desincronizados**
```bash
# Detectar diferencias
python3 tools/diff_detector.py schema.json doc.md

# Aplicar sincronización
python3 tools/sync_apply.py --force-schema-to-doc
```

### **Problema: Validación fallida**
```bash
# Debug detallado
python3 tools/validate_debug.py --verbose

# Generar reporte
python3 tools/validation_report.py --format html
```

## 🛠️ Herramientas y Utilidades

### **CLI para Gestión de Mapeos:**
```bash
# Schema Manager CLI
schema-manager [command] [options]

Commands:
  validate    Validate schema-doc mappings
  sync        Synchronize schemas and docs
  generate    Generate docs from schemas
  analyze     Analyze coverage and consistency
  report      Generate status reports
  fix         Auto-fix common issues

Examples:
  schema-manager validate --all
  schema-manager sync DOC008 apiContract.json
  schema-manager generate --schema dataModel.json --output DOC009.md
  schema-manager analyze --coverage --output report.html
  schema-manager fix --broken-refs --auto
```

### **GitHub Actions Workflow:**
```yaml
# .github/workflows/schema-doc-sync.yml
name: Schema-Doc Synchronization
on:
  push:
    paths:
      - 'real_structure_documentation/schemas/**'
      - 'real_structure_documentation/docs/**'
  pull_request:
    paths:
      - 'real_structure_documentation/schemas/**'
      - 'real_structure_documentation/docs/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Validate mappings
        run: python3 tools/mapping_analyzer.py --ci
      
      - name: Check sync status
        run: python3 tools/sync_validator.py --check-all
      
      - name: Generate coverage report
        run: python3 tools/schema_coverage.py --output coverage.json
      
      - name: Upload coverage
        uses: actions/upload-artifact@v3
        with:
          name: coverage-report
          path: coverage.json
      
      - name: Comment PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const coverage = require('./coverage.json');
            // Post coverage stats as PR comment
```

## 📋 Integración con Manifest de Documentación

### **Estructura del Manifest:**
```json
{
  "version": "2.0",
  "lastUpdated": "[TIMESTAMP]",
  "documents": [
    {
      "id": "DOC008",
      "title": "API Specification",
      "path": "real_structure_documentation/docs/DOC008-APISpecification.md",
      "schemaRefs": [
        "real_structure_documentation/schemas/master_blueprint_parts/apiContract.json",
        "real_structure_documentation/schemas/master_blueprint_parts/architecture.json"
      ],
      "coverage": "100%",
      "lastSync": "[TIMESTAMP]",
      "status": "synced"
    }
  ],
  "schemas": [
    {
      "path": "real_structure_documentation/schemas/master_blueprint_parts/apiContract.json",
      "version": "1.0.0",
      "documentRefs": ["DOC008", "DOC012"],
      "lastModified": "[TIMESTAMP]"
    }
  ],
  "mappings": [
    {
      "type": "bidirectional",
      "source": "apiContract.endpoints",
      "target": "DOC008.endpoints",
      "syncStrategy": "automatic",
      "validation": "required"
    }
  ]
}
```

### **Comandos de Gestión del Manifest:**
```bash
# Actualizar manifest
python3 tools/update_manifest.py --scan-all

# Validar manifest
python3 tools/validate_manifest.py manifests/documentation_manifest.json

# Generar reporte desde manifest
python3 tools/manifest_report.py --format markdown > MANIFEST_STATUS.md
```

## 🎯 Casos de Uso Avanzados

### **1. Generación Automática de API Docs:**
```bash
# Desde OpenAPI/Swagger
python3 tools/openapi_to_schema.py swagger.yaml apiContract.json
python3 tools/schema_to_doc.py apiContract.json DOC008-APISpecification.md
```

### **2. Sincronización con Base de Datos:**
```bash
# Desde DDL SQL
python3 tools/sql_to_schema.py database.sql dataModel.json
python3 tools/schema_to_doc.py dataModel.json DOC009-DataModel.md
```

### **3. Integración con Design Systems:**
```bash
# Desde Figma/Storybook
python3 tools/design_system_sync.py --source figma --output design_system_schema.json
python3 tools/schema_to_doc.py design_system_schema.json DOC003-DesignSystem.md
```

## 📚 Referencias y Recursos

### **Documentación Principal:**
- **Master Guide:** [MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)
- **JSON Schemas Guide:** [MASTER_JSON_SCHEMAS_GUIDE.md](./MASTER_JSON_SCHEMAS_GUIDE.md)
- **Manifest Documentation:** `manifests/documentation_manifest.json`

### **Herramientas:**
- **Verificador Principal:** `tools/verify_docs_and_schemas.py`
- **Sincronizador:** `tools/sync_validator.py`
- **Generador:** `tools/schema_to_doc.py`
- **Analizador:** `tools/mapping_analyzer.py`

### **Schemas Clave:**
- `real_structure_documentation/schemas/master_blueprint_parts/*.json`
- `real_structure_documentation/schemas/design_system_schema.json`
- `real_structure_documentation/schemas/master_blueprint_schema.json`

---

**Última Actualización:** 2025-01-18
**Versión:** 3.0 (Enhanced con automatización y mejores prácticas 2025)
**Próxima Revisión:** Quincenal para mantener sincronización
