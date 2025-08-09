# Guía de Uso de Playbooks de Schemas

Propósito
- Explicar cómo usar los playbooks de schemas para crear/expandir schemas con máxima compatibilidad y trazabilidad.
- Establecer el flujo de trabajo recomendado: leer playbook → editar schema → validar integridad → alinear docs.

Ubicación
- Playbooks de schemas: `prompt_playbooks/schemas_playbooks/playbook_schema-*.md`
- Schemas: `real_structure_documentation/schemas/master_blueprint_parts/*.json` y `real_structure_documentation/schemas/design_system_schema.json`
- Herramientas: `tools/verify_integrity.py` (validación) y `combine_schemas.py` (ensamble final cuando corresponda)

Principios clave
- Retrocompatibilidad: añadir solo campos opcionales al extender schemas existentes.
- Identificadores estables: preferir `id`/`slug` para referencias cruzadas (ej.: `componentLibrary`).
- Enlaces cruzados: mantener `$comment` en cada schema apuntando a su playbook.
- Separación de concerns: alinear pero no mezclar dominios (frontend/backend/infrastructure/devex).
- Normalización: describir campos con `description`, usar `enum` y `format` cuando aplique.

Flujo recomendado (por schema)
1) Abrir el playbook correspondiente (ej.: `playbook_schema-apiContract.md`).
2) Revisar objetivos, campos, ejemplos y checklist del playbook.
3) Editar el schema asociado en `real_structure_documentation/schemas/**.json` siguiendo las recomendaciones.
   - Añadir nuevos campos como opcionales.
   - Incluir `description`, `enum` y `format` para validación fuerte.
   - Mantener `$comment` hacia el playbook.
4) Validar:
   - Ejecutar `python3 tools/verify_integrity.py` (comprueba esquema y vínculos básicos).
5) Alinear con documentos consumidores (ver `guides/CONEXION_SCHEMAS_DOCS.md`).
6) Cuando todos los schemas estén completos, generar el combinado con `combine_schemas.py` (si aplica en tu flujo).

Convenciones y patrones
- Referencias UI:
  - `componentLibrary.components[].{id,slug,name}` → usados por `visualBlueprint.pages[].componentRefs[]`. Preferir `id/slug`.
- API ↔ Arquitectura:
  - Introducir/usar una `referenceKey` común entre `apiContract.endpoints[]` y `architecture.integrationPoints[]`.
- Modelo de datos:
  - Alinear `dataModel.namingConventions` con `dataModelDictionary`.
- Testing ↔ Deployment:
  - `testingStrategy.environments` y gates coherentes con `deploymentStrategy.pipelines`.
- Design System:
  - Canónico: `real_structure_documentation/schemas/design_system_schema.json` (especificación operativa). `master_blueprint_parts/designSystem.json` se mantiene por compatibilidad.

Taxonomía de campos recomendada (al extender schemas)
- Siempre opcionales: nuevos campos deben ser `optional` para preservar retrocompatibilidad.
- Documentación: incluir `description` y ejemplos representativos.
- Validación: usar `enum`, `pattern`, `minimum/maximum`, `format` (`uri`, `date-time`, etc.) cuando aplique.
- Versionado: añadir `version` a entidades clave cuando afecte contratos.
- Trazabilidad: considerar `docRefs[]` para enlazar DOCs relevantes.

Recetas de enlaces cruzados
- UI: `visualBlueprint.pages[].componentRefs[]` ↔ `componentLibrary.components[].{id,slug}`.
- API-Arch: `apiContract.endpoints[].referenceKey` ↔ `architecture.integrationPoints[].referenceKey`.
- Datos: `dataModelDictionary.terms[]` ↔ `dataModel.entities[].attributes[]` (alias/sinónimos/constraints).
- DevOps: `deploymentStrategy.pipelines[].gates[]` ↔ `testingStrategy.environments[]`/`types[]`.

Ejemplo de extensión (diff conceptual)
```json
// Antes (fragmento apiContract)
{
  "endpoints": [
    { "method": "GET", "path": "/items", "summary": "List items" }
  ]
}
```
```json
// Después (retrocompatible)
{
  "endpoints": [
    {
      "method": "GET",
      "path": "/items",
      "summary": "List items",
      "referenceKey": "inv_items_list", // para alinear con arquitectura
      "caching": { "strategy": "public", "ttlSeconds": 60 } // opcional
    }
  ],
  "$comment": "Ver prompt_playbooks/schemas_playbooks/playbook_schema-apiContract.md"
}
```

Workflow de PR recomendado
1) Revisa el playbook del schema y justifica la extensión.
2) Aplica cambios manteniendo todos los nuevos campos como opcionales.
3) Actualiza `$comment` con el playbook correspondiente.
4) Ejecuta `python3 tools/verify_integrity.py`.
5) Verifica cruces clave (UI, API-Arch, Datos, DevOps) según esta guía.
6) Anota en la descripción del PR: campos añadidos, motivo, docs afectados.

Schemas principales y sus playbooks
- apiContract → `real_structure_documentation/schemas/master_blueprint_parts/apiContract.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-apiContract.md`
- architecture → `real_structure_documentation/schemas/master_blueprint_parts/architecture.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-architecture.md`
- bugLifecycle → `real_structure_documentation/schemas/master_blueprint_parts/bugLifecycle.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-bugLifecycle.md`
- businessLogic → `real_structure_documentation/schemas/master_blueprint_parts/businessLogic.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-businessLogic.md`
- componentLibrary → `real_structure_documentation/schemas/master_blueprint_parts/componentLibrary.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-componentLibrary.md`
- dataModel → `real_structure_documentation/schemas/master_blueprint_parts/dataModel.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-dataModel.md`
- dataModelDictionary → `real_structure_documentation/schemas/master_blueprint_parts/dataModelDictionary.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-dataModelDictionary.md`
- deepLogicAnalysis → `real_structure_documentation/schemas/master_blueprint_parts/deepLogicAnalysis.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-deepLogicAnalysis.md`
- definitions → `real_structure_documentation/schemas/master_blueprint_parts/definitions.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-definitions.md`
- deploymentStrategy → `real_structure_documentation/schemas/master_blueprint_parts/deploymentStrategy.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-deploymentStrategy.md`
- designPatterns → `real_structure_documentation/schemas/master_blueprint_parts/designPatterns.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-designPatterns.md`
- designSystem (legacy) → `real_structure_documentation/schemas/master_blueprint_parts/designSystem.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-designSystem.md`
- design_system_schema (canónico) → `real_structure_documentation/schemas/design_system_schema.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-design_system_schema.md`
- documentationManifest → `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-documentationManifest.md`
- featureLifecycle → `real_structure_documentation/schemas/master_blueprint_parts/featureLifecycle.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-featureLifecycle.md`
- featureManifest → `real_structure_documentation/schemas/master_blueprint_parts/featureManifest.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-featureManifest.md`
- fileExecutionMap → `real_structure_documentation/schemas/master_blueprint_parts/fileExecutionMap.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-fileExecutionMap.md`
- forensicAudit → `real_structure_documentation/schemas/master_blueprint_parts/forensicAudit.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-forensicAudit.md`
- operationalStrategy → `real_structure_documentation/schemas/master_blueprint_parts/operationalStrategy.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-operationalStrategy.md`
- projectInfo → `real_structure_documentation/schemas/master_blueprint_parts/projectInfo.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-projectInfo.md`
- projectManagement → `real_structure_documentation/schemas/master_blueprint_parts/projectManagement.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-projectManagement.md`
- qualityGoals → `real_structure_documentation/schemas/master_blueprint_parts/qualityGoals.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-qualityGoals.md`
- stateManagementPlan → `real_structure_documentation/schemas/master_blueprint_parts/stateManagementPlan.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-stateManagementPlan.md`
- testingStrategy → `real_structure_documentation/schemas/master_blueprint_parts/testingStrategy.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-testingStrategy.md`
- visualBlueprint → `real_structure_documentation/schemas/master_blueprint_parts/visualBlueprint.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-visualBlueprint.md`
- wireframeStates → `real_structure_documentation/schemas/master_blueprint_parts/wireframeStates.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-wireframeStates.md`
- cli_schema (opcional/placeholder) → `real_structure_documentation/schemas/cli_schema.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-cliSchema.md`
- master_blueprint (meta) → `real_structure_documentation/schemas/master_blueprint_schema.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-masterBlueprint.md`

Verificación y calidad
- Comando de validación:
  - `python3 tools/verify_integrity.py`
- Checklist mínimo por PR:
  - [ ] Todos los nuevos campos son opcionales y documentados.
  - [ ] `$comment` actualizado si cambió el playbook.
  - [ ] Cross-referencias coherentes (ids/slug; referenceKey en API/Arquitectura si aplica).
  - [ ] `tools/verify_integrity.py` en verde.

Relación con documentos
- Consulta `guides/CONEXION_SCHEMAS_DOCS.md` para ver qué docs consumen cada schema y qué extractos llenar.
- Recomendación: añadir `schemaRefs` en frontmatter de los docs consumidores, y (opcional) `docRefs` en schemas.

Resolución de gaps
- Si un playbook de schema recomienda campos no presentes y son necesarios para un doc prioritario, añadirlos como opcionales y documentar en el playbook con ejemplo.

Referencias
- Playbooks de schemas: `prompt_playbooks/schemas_playbooks/`
- Guía de conexión: `guides/CONEXION_SCHEMAS_DOCS.md`
- Playbooks de docs: `prompt_playbooks/documentation_playbooks/`
