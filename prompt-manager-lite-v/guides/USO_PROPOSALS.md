# Guía de Uso: Proposals

## 🎯 Objetivo
Proponer ideas de mejora con estructura y trazabilidad.

## 📁 Ubicación
- Base del repositorio: `prompt-manager-lite-v/`
- Carpeta: `prompt-manager-lite-v/streaming_files/proposals/`
- Templates existentes: `prompt-manager-lite-v/streaming_files/proposals/template.md`, `prompt-manager-lite-v/streaming_files/proposals/idea_spec.md`
- Manifiesto local (si aplica): `prompt-manager-lite-v/streaming_files/proposals/manifest.json`

## 🧩 Convenciones
- Nombre de archivo sugerido: `proposal-{slug}.md`
- Frontmatter recomendado:
```
---
title: "{Nombre de la Propuesta}"
status: draft|review|approved|rejected
owner: "@usuario"
impact: low|medium|high
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/qualityGoals.json
  - real_structure_documentation/schemas/master_blueprint_parts/projectManagement.json
---
```

## 🔗 Trazabilidad
- Relaciona la propuesta con `streaming_files/features/`, `streaming_files/bugs/`, `streaming_files/operations/` afectadas.
- Vincula DOCs relevantes (roadmap, releases, etc.).

## 🧷 Archivos relacionados obligatorios (consistencia)
- Actualiza si corresponde:
  - Roadmap del proyecto: `prompt-manager-lite-v/real_structure_documentation/docs/DOC029-ProjectRoadmap.md`
  - Índice ADR (si se convierte en decisión): `prompt-manager-lite-v/real_structure_documentation/docs/DOC017-ADR-Index.md`
  - Proceso de releases (si aplica): `prompt-manager-lite-v/real_structure_documentation/docs/DOC022-ReleaseProcess.md`
- Si la propuesta se aprueba → crear `streaming_files/features/feature-*.md` y enlazar ambos sentidos.
- Manifest global: `prompt-manager-lite-v/manifests/documentation_manifest.json`.

## 📎 Rutas ejemplo
- Propuesta nueva: `prompt-manager-lite-v/streaming_files/proposals/proposal-async-cache.md`
- Roadmap: `prompt-manager-lite-v/real_structure_documentation/docs/DOC029-ProjectRoadmap.md`
- Manifest: `prompt-manager-lite-v/manifests/documentation_manifest.json`

## 🔢 IDs y Nombres (manual)
- ID secuencial: tomar el mayor `P###` existente y sumar 1.
- Carpeta recomendada: `streaming_files/proposals/P###-{slug}/`
- Archivo principal dentro: `proposal.md` (basado en `streaming_files/proposals/template.md`)
- Opcionales dentro: `pendingtask.md` (copiado de `template-pendingtask.md`), `notes.md`, `assets/`

## ✅ Checklist
- [ ] Problema y contexto
- [ ] Alternativas consideradas
- [ ] Análisis de impacto y riesgos
- [ ] Plan de implementación y métricas
- [ ] schemaRefs añadidos

## 🧪 Verificación
- `python3 tools/verify_docs_and_schemas.py`
- `python3 tools/verify_integrity.py`
