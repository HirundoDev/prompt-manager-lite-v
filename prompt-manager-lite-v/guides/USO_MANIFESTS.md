# Guía de Uso: Manifests

## Objetivo
Mantener un índice trazable de documentos y sus referencias a schemas.

## Ubicación
- Base del repositorio: `prompt-manager-lite-v/`
- Carpeta: `prompt-manager-lite-v/manifests/`
- Archivo principal: `prompt-manager-lite-v/manifests/documentation_manifest.json`
- Schema (transicional): `prompt-manager-lite-v/real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json`
- Schema (nuevo destino estable): `prompt-manager-lite-v/real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json`

## Campos Clave (resumen)
- `documents[]`: lista de documentos
  - `id`, `title`, `path`, `owner`, `status`
  - `schemaRefs`: referencias a schemas relevantes (opcional pero recomendado)
- `guides[]` (si aplica), `playbooks[]` (si aplica)

## 🔗 Buenas Prácticas
- Mantén `schemaRefs` alineados entre el manifest y el frontmatter del DOC.
- Usa rutas relativas consistentes.
- Evita duplicados; usa nombres canónicos para playbooks.

## ⏱️ Cuándo actualizar el manifest
- Alta/baja/cambio de un DOC bajo `prompt-manager-lite-v/real_structure_documentation/docs/` (nuevo). Si aún existen en `real_structure_documentation/docs/`, migrar y actualizar el manifest.
- Creación o cambio de estado de una Feature/Bug/Operation/Proposal relevante.
- Cambio de `owner`, `status`, `path` o `schemaRefs` en cualquier artefacto indexado.
- Cambios en guías/playbooks que se quieran referenciar como apoyo.

## 📎 Rutas ejemplo
- Manifest (instancia): `prompt-manager-lite-v/manifests/documentation_manifest.json`
- DOC con frontmatter alineado: `prompt-manager-lite-v/real_structure_documentation/docs/DOC008-APISpecification.md`

## Checklist
- [ ] Cada DOC en `real_structure_documentation/docs/` registrado (id, path, owner, status)
- [ ] `schemaRefs` relevantes añadidos
- [ ] Guías/playbooks referenciados donde ayuden al lector
- [ ] Verificador corre sin advertencias

## Verificación
```bash
python3 tools/verify_docs_and_schemas.py
```
