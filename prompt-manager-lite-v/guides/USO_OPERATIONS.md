# Guía de Uso: Operations

## 🎯 Objetivo
Estandarizar tareas operativas y runbooks.

## 📁 Ubicación
- Base del repositorio: `prompt-manager-lite-v/`
- Carpeta: `prompt-manager-lite-v/streaming_files/operations/`
- Templates existentes: `prompt-manager-lite-v/streaming_files/operations/template.md`
- Manifiesto local (si aplica): `prompt-manager-lite-v/streaming_files/operations/manifest.json`

## 🧩 Convenciones
- Nombre de archivo sugerido: `op-{slug}.md` o `runbook-{slug}.md`
- Frontmatter recomendado:
```
---
title: "{Nombre de la Tarea}"
status: draft|ready|deprecated
owner: "@usuario"
frequency: ad-hoc|daily|weekly|monthly|on-demand
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/operationalStrategy.json
  - real_structure_documentation/schemas/master_blueprint_parts/deploymentStrategy.json
---
```

## 🔗 Trazabilidad
- Enlaza `DOC028-OperationsRunbook.md` y otros DOCs técnicos.
- Si la operación impacta releases, enlaza `DOC022-ReleaseProcess.md`.

## 🧷 Archivos relacionados obligatorios (consistencia)
- Actualiza si corresponde:
  - Runbook general: `prompt-manager-lite-v/real_structure_documentation/docs/DOC028-OperationsRunbook.md`
  - Proceso de despliegue: `prompt-manager-lite-v/real_structure_documentation/docs/DOC010-Deployment.md`
  - Política de releases: `prompt-manager-lite-v/real_structure_documentation/docs/DOC022-ReleaseProcess.md`
  - Monitoreo/alertas (si aplica): `prompt-manager-lite-v/real_structure_documentation/docs/DOC025-Observability.md`
- Manifest global: `prompt-manager-lite-v/manifests/documentation_manifest.json`.
- Enlaces cruzados con `streaming_files/features/` y `streaming_files/bugs/` impactados por la operación.

## 📎 Rutas ejemplo
- Runbook nuevo: `prompt-manager-lite-v/streaming_files/operations/runbook-cache-warmup.md`
- DOCs relacionados: `prompt-manager-lite-v/real_structure_documentation/docs/DOC028-OperationsRunbook.md`
- Manifest: `prompt-manager-lite-v/manifests/documentation_manifest.json`

## 🔢 IDs y Nombres (manual)
- ID secuencial: tomar el mayor `OP###` existente y sumar 1.
- Carpeta recomendada: `streaming_files/operations/OP###-{slug}/`
- Archivo principal dentro: `runbook.md` (basado en `streaming_files/operations/template.md`)
- Opcionales dentro: `pendingtask.md` (copiado de `template-pendingtask.md`), `notes.md`, `assets/`

## ✅ Checklist
- [ ] Paso a paso claro y reproducible
- [ ] Roles y responsables
- [ ] Riesgos y rollback
- [ ] Validaciones post-ejecución
- [ ] schemaRefs añadidos

## 🧪 Verificación
- `python3 tools/verify_docs_and_schemas.py`
- `python3 tools/verify_integrity.py`
