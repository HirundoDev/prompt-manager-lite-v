# Guía de Conexión entre Schemas y Docs

Objetivo
- Explicar claramente qué documento (DOCxxx) se alimenta de qué schema(s), cómo extraer la información y cómo validar consistencia.
- Servir como referencia única para mappings, convenciones y verificación.

Rutas clave
- Schemas: `real_structure_documentation/schemas/master_blueprint_parts/*.json` y `real_structure_documentation/schemas/design_system_schema.json`
- Playbooks de schemas: `prompt_playbooks/schemas_playbooks/playbook_schema-*.md`
- Playbooks de docs: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC***.md`
- Documentos: `real_structure_documentation/docs/DOC***.md`
- Manifest meta (schema): `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json`

Convenciones de referencia
- Componentes UI: usar `componentLibrary.components[].id` o `slug` como identificador estable.
- Visual Blueprint: `pages[].componentRefs[]` debe referenciar ids/slug/nombres existentes en `componentLibrary` (preferir id/slug).
- API ↔ Arquitectura: alinear `apiContract.endpoints[]` con `architecture.integrationPoints[]` (usa una clave común, por ejemplo `referenceKey`).
- Diccionario ↔ Data Model: asegurar que `dataModel.namingConventions` y `dataModelDictionary` estén sincronizados.
- Testing ↔ Deployment: `testingStrategy.environments` y gates deben reflejar `deploymentStrategy.pipelines`.
- Design System: canónico `real_structure_documentation/schemas/design_system_schema.json` (rol operativo); `master_blueprint_parts/designSystem.json` se mantiene por compatibilidad.

Mapa Doc → Schemas (núcleo)
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

Recetas de extracción (resumen)
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

Validación y coherencia
1) Ejecutar: `python3 tools/verify_integrity.py`
2) Chequeos manuales:
  - ¿Todos los `componentRefs` resuelven a `componentLibrary`?
  - ¿Endpoints ↔ integrationPoints sincronizados?
  - ¿`namingConventions` concuerda con `dataModelDictionary`?
  - ¿Testing envs/gates reflejan pipelines?
3) Al final: generar `master_blueprint_combined.json` con `combine_schemas.py` y revalidar.

Matriz inversa Schemas → Docs (resumen)
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

Extracción paso a paso (ejemplos prácticos)
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

Consejos de consistencia
- Usa ids/slug estables para todos los cruces UI.
- Documenta `referenceKey` compartido entre API y Arquitectura para mapear endpoints↔integrationPoints.
- Mantén un apéndice de términos desde `dataModelDictionary` para homogeneidad semántica.
- Declara dependencias en el manifest (cuando tengas una instancia) para poder auditar cobertura documental.

Referencias directas
- Schemas (ejemplos):
  - `real_structure_documentation/schemas/master_blueprint_parts/apiContract.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/architecture.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/componentLibrary.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/visualBlueprint.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/testingStrategy.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/deploymentStrategy.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/dataModel.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/dataModelDictionary.json`
  - `real_structure_documentation/schemas/master_blueprint_parts/designPatterns.json`
  - `real_structure_documentation/schemas/design_system_schema.json`
- Docs (ejemplos):
  - `real_structure_documentation/docs/DOC008-APISpecification.md`, `real_structure_documentation/docs/DOC009-DataModel.md`, `real_structure_documentation/docs/DOC010-Deployment.md`, `real_structure_documentation/docs/DOC011-TestingStrategy.md`, `real_structure_documentation/docs/DOC032-FrontendScreenFlow.md`
- Playbooks (schemas): `prompt_playbooks/schemas_playbooks/playbook_schema-*.md`
- Playbooks (docs): `prompt_playbooks/documentation_playbooks/playbook-v2-DOC***.md`

## Relación con el manifest de documentación

- Esta guía establece el mapeo vivo Schemas ↔ Docs. Para trazabilidad formal, cada DOC puede declarar `schemaRefs` en su frontmatter y, además, el `documentation_manifest.json` consolida esas mismas rutas a nivel de inventario.
- Uso recomendado:
  - Mantén este documento como fuente narrativa y de extracción.
  - Replica las referencias en `manifests/documentation_manifest.json` bajo `documents[].schemaRefs` para auditoría.
  - El verificador (`tools/verify_docs_and_schemas.py`) alerta cuándo un schema bajo `real_structure_documentation/schemas/**` no aparece ni en esta guía ni en `schemaRefs` del manifest.

Enlaces
- Manifest (instancia): `manifests/documentation_manifest.json`
- Manifest (schema): `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json`
