# Guía de Uso: Features

## 🎯 Objetivo
Documentar funcionalidades usando templates y mantener trazabilidad con schemas y manifest.

## 📁 Ubicación
- Base del repositorio: `prompt-manager-lite-v/`
- Carpeta: `prompt-manager-lite-v/streaming_files/features/`
- Templates existentes: `prompt-manager-lite-v/streaming_files/features/template.md`
- Manifiesto local (si aplica): `prompt-manager-lite-v/streaming_files/features/manifest.json`

## 🧩 Convenciones
- Nombre de archivo sugerido: `feature-{slug}.md`
- Frontmatter recomendado:
```
---
title: "{Nombre de la Feature}"
status: draft|in-progress|done
owner: "@usuario"
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/featureManifest.json
  - real_structure_documentation/schemas/master_blueprint_parts/featureLifecycle.json
---
```

## 🔗 Trazabilidad
- Añade esta feature al `manifests/documentation_manifest.json` si procede (como documento relacionado o en sección de índice).
- Mantén `schemaRefs` consistentes entre frontmatter y manifest (si el manifest la referencia).

## 🧷 Archivos relacionados obligatorios (consistencia)
- Revisa/actualiza DOCs afectados si corresponde:
  - `real_structure_documentation/docs/DOC008-APISpecification.md`
  - `real_structure_documentation/docs/DOC009-DataModel.md`
  - `real_structure_documentation/docs/DOC006-BackendArchitecture.md`
  - `real_structure_documentation/docs/DOC004-FrontendArchitecture.md`
  - `real_structure_documentation/docs/DOC019-CLI-Command-Reference.md`
  - `real_structure_documentation/docs/DOC028-OperationsRunbook.md`
- Manifest global: `prompt-manager-lite-v/manifests/documentation_manifest.json` (agregar/ajustar entrada, owners, status, schemaRefs, path).
- Enlaces cruzados: `streaming_files/proposals/`, `streaming_files/bugs/`, `streaming_files/operations/` que originan o impactan la feature.

## 📎 Rutas ejemplo
- Feature nueva: `prompt-manager-lite-v/streaming_files/features/feature-auth-refactor.md`
- DOCs afectados: `prompt-manager-lite-v/real_structure_documentation/docs/DOC008-APISpecification.md`
- Manifest: `prompt-manager-lite-v/manifests/documentation_manifest.json`

## 🔢 IDs y Nombres (manual)
- ID secuencial: tomar el mayor `F###` existente y sumar 1.
- Carpeta recomendada: `streaming_files/features/F###-{slug}/`
- Archivo principal dentro: `feature.md` (basado en `streaming_files/features/template.md`)
- Opcionales dentro: `pendingtask.md` (copiado de `template-pendingtask.md`), `notes.md`, `assets/`

## ✅ Checklist
- [ ] Título claro y objetivo
- [ ] Contexto y criterios de aceptación
- [ ] Impacto en módulos/sistemas
- [ ] schemaRefs añadidos
- [ ] Enlaces a DOCs relevantes (p.ej. `DOC030-FeatureIndex.md`)

## 🧪 Verificación
- `python3 tools/verify_docs_and_schemas.py`
- `python3 tools/verify_integrity.py`
