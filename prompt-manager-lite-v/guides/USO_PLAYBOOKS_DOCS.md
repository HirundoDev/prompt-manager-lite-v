# Guía de Uso de Playbooks de Documentación (DOC)

Propósito
- Establecer cómo usar los playbooks de documentación para completar cada `docs/DOC***.md` de forma consistente, trazable y repetible.

Dónde están
- Playbooks de documentación: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC***.md`
- Documentos destino: `docs/DOC***.md`
- Schemas fuente (para extraer datos): `schemas/**` (principalmente `schemas/master_blueprint_parts/*.json` y `schemas/design_system_schema.json`)

Flujo recomendado por documento
1) Abrir el playbook correspondiente (ej.: `playbook-v2-DOC008-APISpecification.md`).
2) Completar el doc `docs/DOC008-APISpecification.md` siguiendo secciones, ejemplos y checklists del playbook.
3) Extraer datos de los schemas mapeados en la guía de conexión (ver `guides/CONEXION_SCHEMAS_DOCS.md`).
4) Añadir referencias cruzadas en el doc (opcional): frontmatter `schemaRefs: [ ... ]`.
5) Validar con `python3 verify_integrity.py` (para asegurar que no se rompió consistencia global) y revisar el checklist final del playbook.

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
  - schemas/master_blueprint_parts/...
  - schemas/design_system_schema.json
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
3) Ejecuta `python3 verify_integrity.py`.
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
- Schemas: `schemas/**`
