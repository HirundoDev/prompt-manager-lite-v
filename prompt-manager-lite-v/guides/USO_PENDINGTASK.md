# Guía de Uso: Pending Task Template

## 🎯 Objetivo
Estandarizar tareas pendientes pequeñas o puntuales usando `template-pendingtask.md`.

## 📄 Template
- Base del repositorio: `prompt-manager-lite-v/`
- Ubicación del template: `prompt-manager-lite-v/template-pendingtask.md` (raíz del repo)
- Copia el archivo y muévelo a la carpeta correspondiente según el contexto o mantenlo en un backlog de tareas.

## 🧩 Convenciones
- Nombre sugerido: `pending-{fecha}-{slug}.md`
- Frontmatter recomendado (si aplica):
```
---
title: "{Tarea Pendiente}"
status: todo|doing|done
owner: "@usuario"
related:
  - real_structure_documentation/docs/DOC0xx-*.md
  - streaming_files/features/feature-*.md
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/projectManagement.json
---
```

## 🔗 Trazabilidad
- Enlaza a DOCs/Features/Bugs/Operations relacionados.
- Si la tarea impacta documentación oficial, refleja el cambio en el manifest y ejecuta el verificador.

## 🧷 Archivos relacionados obligatorios (consistencia)
- Si la tarea genera o modifica documentación oficial:
  - Actualiza `prompt-manager-lite-v/manifests/documentation_manifest.json`.
  - Ajusta `schemaRefs` en el frontmatter del DOC afectado.
- Si deriva en artefactos formales:
  - Crear feature/bug/operation/proposal correspondiente y enlazar bidireccionalmente.
- Registrar cambios relevantes en índice/changelog si aplica.

## 📎 Rutas ejemplo
- Template: `prompt-manager-lite-v/template-pendingtask.md`
- Tarea creada: `prompt-manager-lite-v/tasks/pending-2025-08-08-cleanup.md` (o en la carpeta del dominio correspondiente)
- Manifest: `prompt-manager-lite-v/manifests/documentation_manifest.json`

## ✅ Checklist
- [ ] Descripción clara y resultado esperado
- [ ] Due date/responsable (si aplica)
- [ ] Enlaces a elementos relacionados
- [ ] Estado actualizado

## 🧪 Verificación
- `python3 tools/verify_docs_and_schemas.py`
- `python3 tools/verify_integrity.py`
