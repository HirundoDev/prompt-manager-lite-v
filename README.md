# Prompt Manager Lite V

Repositorio base para documentación estructurada de proyectos con schemas JSON y playbooks. Esta raíz apunta al paquete principal en `prompt-manager-lite-v/`.

Recursos clave
- README del paquete: `prompt-manager-lite-v/README.md`
- Guías:
  - `prompt-manager-lite-v/guides/CONEXION_SCHEMAS_DOCS.md` (mapeo Schemas ↔ Docs)
  - `prompt-manager-lite-v/guides/USO_PLAYBOOKS_DOCS.md` (uso de playbooks y frontmatter)
- Manifest de documentación:
  - Instancia: `prompt-manager-lite-v/manifests/documentation_manifest.json`
  - Schema: `prompt-manager-lite-v/schemas/master_blueprint_parts/documentationManifest.json`

Verificación rápida (desde `prompt-manager-lite-v/`)
```bash
python3 verify_docs_and_schemas.py   # Checks: manifest, playbooks canónicos, cobertura de schemas y guías
python3 verify_integrity.py          # Estado de archivos vs plantillas
```

Convenciones importantes
- Playbooks canónicos: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC{###}-{Nombre}.md` (sin alias).
- Cada `docs/DOC***.md` puede declarar `schemaRefs` en el frontmatter y además estar reflejado en `manifests/documentation_manifest.json` para trazabilidad.
