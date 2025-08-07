# Schema Playbook — featureManifest

Propósito: inventario de features con metadatos para roadmap, flags y trazabilidad.

Ubicación: `schemas/master_blueprint_parts/featureManifest.json`

---

1) Estructura
- `features[]`: { featureId, name, description, owner, status(Planned|In Development|Completed|Deprecated), stage(Idea|Discovery|MVP|Beta|GA|Sunset), userStories[], flags[], deps[], docs[] }
- `relations[]`: { from, to, type: blocks|duplicates|relates }
- `flags[]`: { key, default, environments[] }

---

2) Procedimiento
1. Extraer features del roadmap y del código (flags/rutas).
2. Registrar dependencias y relaciones.
3. Enlazar docs y ownership.

---

3) Ejemplo
```json
{
  "features": [
    {"featureId": "FEAT-100", "name": "Checkout v2", "description": "Nueva versión de checkout", "owner": "web", "status": "Planned", "stage": "Idea", "flags": ["checkout_v2"], "deps": ["payments"], "docs": ["docs/DOC030-FeatureIndex.md"]}
  ],
  "flags": [{"key": "checkout_v2", "default": false, "environments": ["staging"]}],
  "relations": [{"from": "FEAT-100", "to": "FEAT-050", "type": "blocks"}]
}
```

---

4) Checklist
- [ ] Features con owner y stage.
- [ ] Flags y deps registradas.
- [ ] Docs enlazados.
