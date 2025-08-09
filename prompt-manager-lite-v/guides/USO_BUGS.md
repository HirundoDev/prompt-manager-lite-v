# Guía de Uso: Bugs

## 🎯 Objetivo
Estandarizar el reporte y documentación de bugs con trazabilidad a schemas.

## 📁 Ubicación
- Base del repositorio: `prompt-manager-lite-v/`
- Carpeta: `prompt-manager-lite-v/streaming_files/bugs/`
- Templates existentes: `prompt-manager-lite-v/streaming_files/bugs/template.md`
- Manifiesto local (si aplica): `prompt-manager-lite-v/streaming_files/bugs/manifest.json`

## 🧩 Convenciones
- Nombre de archivo sugerido: `bug-{id-o-slug}.md`
- Frontmatter recomendado:
```
---
title: "{Resumen del Bug}"
status: open|in-progress|resolved
owner: "@usuario"
severity: low|medium|high|critical
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/bugLifecycle.json
  - real_structure_documentation/schemas/master_blueprint_parts/testingStrategy.json
---
```

## 🔗 Trazabilidad
- Enlaza evidencia (logs, capturas) y referencias a DOCs (p.ej. `DOC031-BugIndex.md`).
- Mantén `schemaRefs` alineados con el manifest si se indexa este bug.

## 🧷 Archivos relacionados obligatorios (consistencia)
- Actualiza si corresponde:
  - Índice de bugs: `prompt-manager-lite-v/real_structure_documentation/docs/DOC031-BugIndex.md`
  - Estrategia de pruebas: `prompt-manager-lite-v/real_structure_documentation/docs/DOC011-TestingStrategy.md`
  - Changelog: `prompt-manager-lite-v/real_structure_documentation/docs/DOC013-ChangeLog.md`
  - Seguridad/Compliance si aplica: `prompt-manager-lite-v/real_structure_documentation/docs/DOC012-SecurityCompliance.md`
- Manifest global: `prompt-manager-lite-v/manifests/documentation_manifest.json`.
- Enlaces cruzados con streaming_files/features/operations relacionadas.

## 📎 Rutas ejemplo
- Bug nuevo: `prompt-manager-lite-v/streaming_files/bugs/bug-123-invalid-state.md`
- Evidencia: `prompt-manager-lite-v/logs/bug-123/console.txt` (opcional)
- Manifest: `prompt-manager-lite-v/manifests/documentation_manifest.json`

## 🔢 IDs y Nombres (manual)
- ID secuencial: tomar el mayor `B###` existente y sumar 1.
- Carpeta recomendada: `streaming_files/bugs/B###-{slug}/`
- Archivo principal dentro: `bug_report.md` (basado en `streaming_files/bugs/template.md`)
- Opcionales dentro: `pendingtask.md` (copiado de `template-pendingtask.md`), `notes.md`, `assets/`

## ✅ Checklist
- [ ] Pasos para reproducir
- [ ] Resultado esperado vs actual
- [ ] Alcance/impacto
- [ ] Criterios de cierre
- [ ] schemaRefs añadidos

## 🧪 Verificación
- `python3 tools/verify_docs_and_schemas.py`
- `python3 tools/verify_integrity.py`
