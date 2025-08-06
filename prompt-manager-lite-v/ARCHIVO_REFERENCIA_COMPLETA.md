# 📋 Referencia Completa de Archivos - Prompt Manager Lite v

**🎯 Propósito:** Esta es la guía maestra que explica PARA QUÉ SIRVE cada archivo en el sistema Prompt Manager Lite. Consúltala antes de trabajar con cualquier archivo.

---

## 🗂️ **ESTRUCTURA COMPLETA CON PROPÓSITOS**

```
prompt-manager-lite-v/
├── 📚 ARCHIVOS DE GUÍA Y CONTROL
│   ├── README.md                           # Introducción general al sistema
│   ├── GUIA_COMPLETA_DE_USO.md            # Manual de operación completo
│   ├── initial_prompt.md                   # Prompt de inicio para agentes IA
│   ├── ARCHIVO_REFERENCIA_COMPLETA.md     # ESTE ARCHIVO - Mapa de todo el sistema
│   ├── combine_schemas.py                  # Script para generar master blueprint
│   ├── verify_integrity.py                # Script para verificar estado de archivos
│   └── file_integrity.json                # Estado de archivos (generado automáticamente)
│
├── 📝 DOCUMENTOS DEL PROYECTO (docs/)
│   ├── 🏢 INFORMACIÓN BÁSICA
│   │   ├── DOC000-ProjectBrief.md          # Visión general y objetivos del proyecto
│   │   ├── DOC001-ProjectREADME.md         # README principal con instalación y uso
│   │   └── DOC002-ProductDefinition.md    # Definición detallada del producto
│   │
│   ├── 🎨 DISEÑO Y UX
│   │   ├── DOC003-DesignSystem.md          # Sistema de diseño (colores, fuentes, componentes)
│   │   └── DOC032-FrontendScreenFlow.md   # Flujo de pantallas y navegación
│   │
│   ├── 🏗️ ARQUITECTURA TÉCNICA
│   │   ├── DOC004-FrontendArchitecture.md # Arquitectura del frontend (React, Vue, etc.)
│   │   ├── DOC005-FrontendDependencies.md # Dependencias y librerías del frontend
│   │   ├── DOC006-BackendArchitecture.md  # Arquitectura del backend (API, servicios)
│   │   ├── DOC007-BackendDependencies.md  # Dependencias y librerías del backend
│   │   ├── DOC008-APISpecification.md     # Especificación completa de la API REST/GraphQL
│   │   └── DOC009-DataModel.md            # Modelo de datos y esquemas de BD
│   │
│   ├── 🚀 OPERACIONES Y DESPLIEGUE
│   │   ├── DOC010-Deployment.md           # Guía de despliegue y configuración
│   │   ├── DOC028-OperationsRunbook.md    # Manual operacional y troubleshooting
│   │   └── DOC022-ReleaseProcess.md       # Proceso de releases y versionado
│   │
│   ├── 🔬 TESTING Y CALIDAD
│   │   ├── DOC011-TestingStrategy.md      # Estrategia de testing (unit, integration, e2e)
│   │   └── DOC012-SecurityCompliance.md  # Seguridad y cumplimiento normativo
│   │
│   ├── 📋 GESTIÓN DE PROYECTO
│   │   ├── DOC013-ChangeLog.md            # Registro de cambios por versión
│   │   ├── DOC014-IssueTemplate.md        # Plantillas para reportar issues
│   │   ├── DOC015-PullRequestTemplate.md  # Plantillas para pull requests
│   │   ├── DOC016-Contributing.md         # Guía para contribuidores
│   │   ├── DOC017-ADR-Index.md           # Índice de Architecture Decision Records
│   │   └── DOC020-CodeOfConduct.md       # Código de conducta del proyecto
│   │
│   ├── 📚 DOCUMENTACIÓN TÉCNICA
│   │   ├── DOC019-CLI-Command-Reference.md # Referencia completa de comandos CLI
│   │   ├── DOC021-OnboardingGuide.md      # Guía de onboarding para nuevos desarrolladores
│   │   └── DOC029-ProjectRoadmap.md       # Roadmap y planificación futura
│   │
│   ├── 📊 MANIFIESTOS Y REGISTROS
│   │   ├── DOC023-BackendManifest.md      # Registro de servicios y APIs del backend
│   │   ├── DOC024-DatabaseManifest.md     # Registro de tablas, índices y schemas de BD
│   │   ├── DOC025-FrontendManifest.md     # Registro de componentes y páginas del frontend
│   │   ├── DOC026-ProjectFileManifest.md  # Registro de archivos importantes del proyecto
│   │   ├── DOC027-SharedLibsManifest.md   # Registro de librerías compartidas
│   │   ├── DOC030-FeatureIndex.md         # Índice de funcionalidades implementadas
│   │   └── DOC031-BugIndex.md             # Índice de bugs conocidos y solucionados
│   │
│   ├── 📖 GUÍAS Y TEMPLATES
│   │   ├── GUIDE-batch-update.md          # Guía para actualizaciones masivas
│   │   ├── GUIDE-update-content.md        # Guía para actualizar contenido
│   │   ├── GUIDE-update-metadata.md       # Guía para actualizar metadatos
│   │   ├── template-ADR.md                # Template para Architecture Decision Records
│   │   └── documentation_manifest.json    # Manifiesto de toda la documentación
│
├── ⚙️ SCHEMAS JSON (schemas/)
│   ├── master_blueprint_schema.json       # Schema principal que define la estructura completa
│   ├── cli_schema.json                    # Schema para definición de comandos CLI
│   ├── command_registry_schema.json       # Schema para registro de comandos
│   ├── design_system_schema.json          # Schema para sistema de diseño
│   │
│   └── 🧩 PARTES DEL MASTER BLUEPRINT (master_blueprint_parts/)
│       ├── 🏢 INFORMACIÓN BÁSICA
│       │   ├── projectInfo.json           # Información básica del proyecto (nombre, descripción, versión)
│       │   ├── definitions.json           # Definiciones y glosario de términos
│       │   └── projectManagement.json     # Metodología y herramientas de gestión
│       │
│       ├── 🏗️ ARQUITECTURA Y DISEÑO
│       │   ├── architecture.json          # Arquitectura general del sistema
│       │   ├── designSystem.json          # Sistema de diseño (colores, tipografías, componentes)
│       │   ├── componentLibrary.json      # Biblioteca de componentes reutilizables
│       │   └── wireframeStates.json       # Estados y wireframes de la interfaz
│       │
│       ├── 💾 DATOS Y APIS
│       │   ├── dataModel.json             # Modelo de datos y entidades
│       │   ├── dataModelDictionary.json   # Diccionario detallado del modelo de datos
│       │   └── apiContract.json           # Contratos y especificaciones de API
│       │
│       ├── 💼 LÓGICA DE NEGOCIO
│       │   ├── businessLogic.json         # Reglas de negocio y procesos core
│       │   ├── deepLogicAnalysis.json     # Análisis profundo de lógica compleja
│       │   └── forensicAudit.json         # Auditoría forense del código existente
│       │
│       ├── 🚀 OPERACIONES Y DESPLIEGUE
│       │   ├── deploymentStrategy.json    # Estrategia de despliegue y configuración
│       │   ├── operationalStrategy.json   # Estrategia operacional y monitoreo
│       │   └── fileExecutionMap.json      # Mapa de ejecución y dependencias de archivos
│       │
│       ├── 🔬 TESTING Y CALIDAD
│       │   ├── testingStrategy.json       # Estrategia de testing y QA
│       │   └── qualityGoals.json          # Objetivos y métricas de calidad
│       │
│       ├── 🎯 GESTIÓN DE FUNCIONALIDADES
│       │   ├── featureManifest.json       # Manifiesto de funcionalidades
│       │   ├── featureLifecycle.json      # Ciclo de vida de funcionalidades
│       │   ├── bugLifecycle.json          # Ciclo de vida de bugs
│       │   └── stateManagementPlan.json   # Plan de gestión de estado
│       │
│       ├── 📋 DOCUMENTACIÓN Y MANIFIESTOS
│       │   ├── documentationManifest.json # Manifiesto de toda la documentación
│       │   └── visualBlueprint.json       # Blueprint visual del sistema
│
├── 📚 PLAYBOOKS - GUÍAS PARA COMPLETAR ARCHIVOS (prompt_playbooks/)
│   ├── MASTER_PLAYBOOK_GUIDE.md           # Guía maestra de todos los playbooks
│   │
│   ├── 🏢 PLAYBOOKS PARA INFORMACIÓN BÁSICA
│   │   ├── projectInfo.md                 # Cómo completar projectInfo.json
│   │   ├── definitions.md                 # Cómo completar definitions.json
│   │   └── projectManagement.md           # Cómo completar projectManagement.json
│   │
│   ├── 🏗️ PLAYBOOKS PARA ARQUITECTURA
│   │   ├── architecture.md                # Cómo completar architecture.json
│   │   ├── playbook-architecture.md       # Guía detallada de arquitectura
│   │   ├── componentLibrary.md            # Cómo completar componentLibrary.json
│   │   └── playbook-componentLibrary.md   # Guía detallada de componentes
│   │
│   ├── 💾 PLAYBOOKS PARA DATOS Y APIS
│   │   ├── dataModel.md                   # Cómo completar dataModel.json
│   │   ├── dataModelDictionary.md         # Cómo completar dataModelDictionary.json
│   │   ├── apiContract.md                 # Cómo completar apiContract.json
│   │   └── playbook-apiContract.md        # Guía detallada de APIs
│   │
│   ├── 💼 PLAYBOOKS PARA LÓGICA DE NEGOCIO
│   │   ├── businessLogic.md               # Cómo completar businessLogic.json
│   │   ├── deepLogicAnalysis.md           # Cómo completar deepLogicAnalysis.json
│   │   └── forensicAudit.md               # Cómo completar forensicAudit.json
│   │
│   ├── 🚀 PLAYBOOKS PARA OPERACIONES
│   │   ├── deploymentStrategy.md          # Cómo completar deploymentStrategy.json
│   │   ├── operationalStrategy.md         # Cómo completar operationalStrategy.json
│   │   └── fileExecutionMap.md            # Cómo completar fileExecutionMap.json
│   │
│   ├── 🔬 PLAYBOOKS PARA TESTING
│   │   ├── testingStrategy.md             # Cómo completar testingStrategy.json
│   │   ├── qualityGoals.md                # Cómo completar qualityGoals.json
│   │   └── playbook-testingStrategy.md    # Guía detallada de testing
│   │
│   ├── 🎯 PLAYBOOKS PARA FUNCIONALIDADES
│   │   ├── featureManifest.md             # Cómo completar featureManifest.json
│   │   ├── featureLifecycle.md            # Cómo completar featureLifecycle.json
│   │   ├── bugLifecycle.md                # Cómo completar bugLifecycle.json
│   │   └── stateManagementPlan.md         # Cómo completar stateManagementPlan.json
│   │
│   ├── 🎨 PLAYBOOKS PARA DISEÑO
│   │   ├── designSystem.md                # Cómo completar designSystem.json
│   │   ├── playbook-designSystem.md       # Guía detallada de sistema de diseño
│   │   ├── visualBlueprint.md             # Cómo completar visualBlueprint.json
│   │   └── wireframeStates.md             # Cómo completar wireframeStates.json
│   │
│   ├── 📋 PLAYBOOKS PARA DOCUMENTACIÓN
│   │   ├── documentationManifest.md       # Cómo completar documentationManifest.json
│   │   └── documentation_playbooks/       # Playbooks específicos para cada DOCxxx
│   │       ├── playbook-v2-DOC000-ProjectBrief.md
│   │       ├── playbook-v2-DOC001-ProjectREADME.md
│   │       ├── playbook-v2-DOC002-ProductDefinition.md
│   │       ├── playbook-v2-DOC003-DesignSystem.md
│   │       ├── playbook-v2-DOC004-FrontendArchitecture.md
│   │       ├── playbook-v2-DOC005-FrontendDependencies.md
│   │       ├── playbook-v2-DOC006-BackendArchitecture.md
│   │       ├── playbook-v2-DOC007-BackendDependencies.md
│   │       ├── playbook-v2-DOC008-APISpecification.md
│   │       ├── playbook-v2-DOC009-DataModel.md
│   │       ├── playbook-v2-DOC010-Deployment.md
│   │       ├── playbook-v2-DOC011-TestingStrategy.md
│   │       ├── playbook-v2-DOC012-SecurityCompliance.md
│   │       ├── playbook-v2-DOC013-ChangeLog.md
│   │       ├── playbook-v2-DOC014-IssueTemplate.md
│   │       ├── playbook-v2-DOC015-PullRequestTemplate.md
│   │       ├── playbook-v2-DOC016-Contributing.md
│   │       ├── playbook-v2-DOC017-ADR-Index.md
│   │       ├── playbook-v2-DOC019-CLI-Command-Reference.md
│   │       ├── playbook-v2-DOC020-CodeofConduct.md
│   │       ├── playbook-v2-DOC021-OnboardingGuide.md
│   │       ├── playbook-v2-DOC022-ReleaseProcess.md
│   │       ├── playbook-v2-DOC023-BackendManifest.md
│   │       ├── playbook-v2-DOC024-DatabaseManifest.md
│   │       ├── playbook-v2-DOC025-FrontendManifest.md
│   │       ├── playbook-v2-DOC026-ProjectFileManifest.md
│   │       ├── playbook-v2-DOC027-SharedLibsManifest.md
│   │       ├── playbook-v2-DOC028-OperationsRunbook.md
│   │       ├── playbook-v2-DOC029-ProjectRoadmap.md
│   │       ├── playbook-v2-DOC030-FeatureIndex.md
│   │       ├── playbook-v2-DOC031-BugIndex.md
│   │       ├── playbook-v2-DOC032-FrontendScreenFlow.md
│   │       └── playbook-v2-DOC033-ADRTemplate.md
│
├── 🚀 FUNCIONALIDADES (features/)
│   ├── template.md                         # Template base para crear nuevas funcionalidades
│   ├── manifest.json                       # Manifiesto de funcionalidades del proyecto
│   └── F000-Ejemplo-de-Feature/            # Ejemplo de funcionalidad documentada
│       └── feature_spec.md                 # Especificación completa de la funcionalidad
│
├── 🐛 BUGS (bugs/)
│   ├── template.md                         # Template base para documentar bugs
│   ├── manifest.json                       # Manifiesto de bugs del proyecto
│   └── B000-Ejemplo-de-Bug/                # Ejemplo de bug documentado
│       └── bug_report.md                   # Reporte completo del bug
│
├── 🔧 OPERACIONES (operations/)
│   ├── template.md                         # Template base para documentar tareas
│   ├── manifest.json                       # Manifiesto de tareas del proyecto
│   └── T000-Ejemplo-de-Tarea/              # Ejemplo de tarea documentada
│       └── task_spec.md                    # Especificación completa de la tarea
│
└── 💡 PROPUESTAS (proposals/)
    ├── template.md                         # Template base para documentar ideas
    ├── manifest.json                       # Manifiesto de ideas del proyecto
    └── IDEA000-Ejemplo-de-Idea/            # Ejemplo de idea documentada
        └── idea_spec.md                    # Especificación completa de la idea
```

---

## 🎯 **ARCHIVOS CRÍTICOS QUE DEBES COMPLETAR PRIMERO**

### **🔴 OBLIGATORIOS (Sin estos, no funciona):**
1. **`DOC000-ProjectBrief.md`** - Define QUÉ es tu proyecto
2. **`schemas/master_blueprint_parts/projectInfo.json`** - Información básica estructurada
3. **`schemas/master_blueprint_parts/architecture.json`** - Arquitectura general del sistema

### **🟡 IMPORTANTES (Para funcionalidad completa):**
4. **`DOC008-APISpecification.md`** - Si tienes APIs
5. **`schemas/master_blueprint_parts/dataModel.json`** - Si manejas datos
6. **`schemas/master_blueprint_parts/apiContract.json`** - Contratos de API
7. **`DOC004-FrontendArchitecture.md`** - Si tienes frontend
8. **`DOC006-BackendArchitecture.md`** - Si tienes backend

### **🟢 OPCIONALES (Para completitud):**
9. **`DOC010-Deployment.md`** - Cómo desplegar
10. **`DOC011-TestingStrategy.md`** - Cómo testear
11. **Resto de documentos según necesidades específicas**

---

## 🚀 **FLUJO DE TRABAJO RECOMENDADO**

### **PASO 1: Verificar estado**
```bash
python3 verify_integrity.py
```

### **PASO 2: Completar archivos críticos (en orden)**
1. `DOC000-ProjectBrief.md` (consultar `prompt_playbooks/documentation_playbooks/playbook-v2-DOC000-ProjectBrief.md`)
2. `schemas/master_blueprint_parts/projectInfo.json` (consultar `prompt_playbooks/projectInfo.md`)
3. `schemas/master_blueprint_parts/architecture.json` (consultar `prompt_playbooks/architecture.md`)

### **PASO 3: Completar según necesidades del proyecto**
- ¿Tienes API? → `DOC008-APISpecification.md` + `apiContract.json`
- ¿Tienes frontend? → `DOC004-FrontendArchitecture.md` + `componentLibrary.json`
- ¿Tienes backend? → `DOC006-BackendArchitecture.md` + `businessLogic.json`
- ¿Manejas datos? → `DOC009-DataModel.md` + `dataModel.json`

### **PASO 4: Generar master blueprint**
```bash
python3 combine_schemas.py
```

---

## 💡 **CONSEJOS DE USO**

### **Para cada archivo:**
1. **LEE** su playbook correspondiente antes de editarlo
2. **ENTIENDE** su propósito en el sistema general
3. **COMPLETA** todos los placeholders `[así]`
4. **VERIFICA** que el cambio se refleje en `verify_integrity.py`

### **Archivos que trabajan juntos:**
- `DOC000-ProjectBrief.md` ↔ `projectInfo.json` (misma información, diferentes formatos)
- `DOC008-APISpecification.md` ↔ `apiContract.json` (documentación + schema)
- `DOC004-FrontendArchitecture.md` ↔ `componentLibrary.json` (arquitectura + componentes)
- `DOC009-DataModel.md` ↔ `dataModel.json` (documentación + schema de datos)

---

**🎯 Este archivo es tu mapa completo. Consúltalo siempre que no sepas para qué sirve un archivo específico.**
