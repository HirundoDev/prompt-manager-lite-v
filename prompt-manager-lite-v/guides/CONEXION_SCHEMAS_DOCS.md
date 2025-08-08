# Guía de Conexión entre Schemas y Docs

Objetivo
- Explicar claramente qué documento (DOCxxx) se alimenta de qué schema(s), cómo extraer la información y cómo validar consistencia.
- Servir como referencia única para mappings, convenciones y verificación.

Rutas clave
- Schemas: `schemas/master_blueprint_parts/*.json` y `schemas/design_system_schema.json`
- Playbooks de schemas: `prompt_playbooks/schemas_playbooks/playbook_schema-*.md`
- Playbooks de docs: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC***.md`
- Documentos: `docs/DOC***.md`
- Manifest meta (schema): `schemas/master_blueprint_parts/documentationManifest.json`

Convenciones de referencia
- Componentes UI: usar `componentLibrary.components[].id` o `slug` como identificador estable.
- Visual Blueprint: `pages[].componentRefs[]` debe referenciar ids/slug/nombres existentes en `componentLibrary` (preferir id/slug).
- API ↔ Arquitectura: alinear `apiContract.endpoints[]` con `architecture.integrationPoints[]` (usa una clave común, por ejemplo `referenceKey`).
- Diccionario ↔ Data Model: asegurar que `dataModel.namingConventions` y `dataModelDictionary` estén sincronizados.
- Testing ↔ Deployment: `testingStrategy.environments` y gates deben reflejar `deploymentStrategy.pipelines`.
- Design System: canónico `schemas/design_system_schema.json` (rol operativo); `master_blueprint_parts/designSystem.json` se mantiene por compatibilidad.

Mapa Doc → Schemas (núcleo)
- DOC000-ProjectBrief → `projectInfo.json` (+ `projectManagement.json` para snapshot; manifest para owners/reviews)
- DOC001-ProjectREADME → `projectInfo.json`
- DOC002-ProductDefinition → `businessLogic.json`, `definitions.json`, `projectInfo.json`
- DOC003-DesignSystem → `design_system_schema.json` (canónico) y/o `designSystem.json`
- DOC004-FrontendArchitecture → `architecture.json`, `designPatterns.json`
- DOC005-FrontendDependencies → `componentLibrary.json`, `design_system_schema.json` (parcial)
- DOC006-BackendArchitecture → `architecture.json`
- DOC007-BackendDependencies → (parcial) + `architecture.json`, `operationalStrategy.json`
- DOC008-APISpecification → `apiContract.json` (+ `architecture.integrationPoints`, `designPatterns.security`)
- DOC009-DataModel → `dataModel.json` + `dataModelDictionary.json`
- DOC010-Deployment → `deploymentStrategy.json` (+ `architecture.deploymentTopology`, `observability`, `availability`, `designPatterns.mapping.infrastructure/devex`)
- DOC011-TestingStrategy → `testingStrategy.json` (+ `deploymentStrategy.pipelines`)
- DOC012-SecurityCompliance → `architecture.securityArchitecture`, `designPatterns.governance/compliance`, `apiContract.authentication/rateLimiting`
- DOC017-ADR-Index → `architecture.adrReferences` (y manifest cuando exista instancia)
- DOC019-CLI-Command-Reference → `cli_schema.json` (si se mantiene)
- DOC028-OperationsRunbook → `operationalStrategy.json` (+ `deploymentStrategy`, `architecture.observability`)
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
- DOC017 (ADR Index): `architecture.adrReferences[]`
- DOC000 (Brief): `projectInfo.*`

Validación y coherencia
1) Ejecutar: `python3 verify_integrity.py`
2) Chequeos manuales:
   - ¿Todos los `componentRefs` resuelven a `componentLibrary`?
   - ¿Endpoints ↔ integrationPoints sincronizados?
   - ¿`namingConventions` concuerda con `dataModelDictionary`?
  - ¿Testing envs/gates reflejan pipelines?
3) Al final: generar `master_blueprint_combined.json` con `combine_schemas.py` (cuando lo uses en tu flujo) y revalidar.

Matriz inversa Schemas → Docs (resumen)
- projectInfo.json → DOC000, DOC001
- architecture.json → DOC004, DOC006, DOC010, DOC012, DOC017, DOC028
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
- documentationManifest.json (meta) → índice y dependencias de todos los DOCs

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
  - `schemas/master_blueprint_parts/apiContract.json`
  - `schemas/master_blueprint_parts/architecture.json`
  - `schemas/master_blueprint_parts/componentLibrary.json`
  - `schemas/master_blueprint_parts/visualBlueprint.json`
  - `schemas/master_blueprint_parts/testingStrategy.json`
  - `schemas/master_blueprint_parts/deploymentStrategy.json`
  - `schemas/master_blueprint_parts/dataModel.json`
  - `schemas/master_blueprint_parts/dataModelDictionary.json`
  - `schemas/master_blueprint_parts/designPatterns.json`
  - `schemas/design_system_schema.json`
- Docs (ejemplos):
  - `docs/DOC008-APISpecification.md`, `docs/DOC009-DataModel.md`, `docs/DOC010-Deployment.md`, `docs/DOC011-TestingStrategy.md`, `docs/DOC032-FrontendScreenFlow.md`
- Playbooks (schemas): `prompt_playbooks/schemas_playbooks/playbook_schema-*.md`
- Playbooks (docs): `prompt_playbooks/documentation_playbooks/playbook-v2-DOC***.md`
