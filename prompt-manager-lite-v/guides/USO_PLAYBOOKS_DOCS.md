# Guía de Uso de Playbooks de Documentación (DOC)

Propósito
- Establecer cómo usar los playbooks de documentación para completar cada `real_structure_documentation/docs/DOC***.md` de forma consistente, trazable y repetible.

Dónde están
- Playbooks de documentación: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC***.md`
- Documentos destino: `real_structure_documentation/docs/DOC***.md`
- Schemas fuente (para extraer datos): `real_structure_documentation/schemas/**` (principalmente `real_structure_documentation/schemas/master_blueprint_parts/*.json` y `real_structure_documentation/schemas/design_system_schema.json`)

Flujo recomendado por documento
1) Abrir el playbook correspondiente (ej.: `playbook-v2-DOC008-APISpecification.md`).
2) Completar el doc `real_structure_documentation/docs/DOC008-APISpecification.md` siguiendo secciones, ejemplos y checklists del playbook.
3) Extraer datos de los schemas mapeados en la guía de conexión (ver `guides/CONEXION_SCHEMAS_DOCS.md`).
4) Añadir referencias cruzadas en el doc (opcional): frontmatter `schemaRefs: [ ... ]`.
5) Validar con `python3 tools/verify_integrity.py` (para asegurar que no se rompió consistencia global) y revisar el checklist final del playbook.

Buenas prácticas
- Mantener la narrativa mínima; priorizar datos provenientes de schemas.
- Usar identificación estable (ids/slug) cuando referencies componentes, endpoints o entidades.
- Mantener consistencia terminológica con `dataModelDictionary`.
- Si el playbook indica ejemplos, adáptalos al dominio y enlaza a la fuente (`schema` o `codeRef`).

Guía rápida por algunos DOCs comunes
- DOC008-APISpecification: seguir secciones de endpoints, auth, rate limiting, caching, tracing; poblar principalmente desde `apiContract.json`.
- DOC009-DataModel: poblar entidades, relaciones, convenciones, y diccionario desde `dataModel.json` + `dataModelDictionary.json`.
- DOC010-Deployment: poblar entornos, pipelines, rollout/rollback y compliance desde `deploymentStrategy.json` (y cruzar con arquitectura/observabilidad cuando aplique).
- DOC011-TestingStrategy: seguir pirámide, targets, datos de prueba, entornos desde `testingStrategy.json` y gates de `deploymentStrategy`.
- DOC032-FrontendScreenFlow: poblar flujo/páginas/estados desde `visualBlueprint.json` + `wireframeStates.json`, y validar componentes con `componentLibrary.json`.

Plantilla de frontmatter recomendada
```yaml
---
docId: DOCxxx-Nombre
ownerAgent: equipo-o-persona
status: draft|review|approved
lastUpdated: YYYY-MM-DD
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/...
  - real_structure_documentation/schemas/design_system_schema.json
relatedDocs:
  - DOC0yy-OtroDocumento
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
