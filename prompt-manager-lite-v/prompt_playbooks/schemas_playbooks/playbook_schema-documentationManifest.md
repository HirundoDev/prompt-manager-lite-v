# Schema Playbook — documentationManifest

Propósito: inventariar y controlar el estado de toda la documentación del proyecto.

Ubicación: `schemas/master_blueprint_parts/documentationManifest.json`

---

1) Estructura
- `documents[]`: { id, title, path, owner, status: draft|review|approved, lastUpdated }
- `dependencies[]`: { fromDoc, toDoc, relation }
- `reviewCycles`: { frequency, reviewers[] }
- `qualityChecks[]`: { id, description, automated: boolean }

---

2) Procedimiento
1. Extraer lista de docs del repo y registrar metadatos.
2. Definir ciclo de revisiones y responsables.
3. Configurar checks automáticos (lint, links, placeholders).

---

3) Ejemplo
```json
{
  "documents": [
    {"id": "DOC000", "title": "Project Brief", "path": "docs/DOC000-ProjectBrief.md", "owner": "pm", "status": "draft", "lastUpdated": "2025-08-01"}
  ],
  "reviewCycles": {"frequency": "monthly", "reviewers": ["tech-writer", "pm"]},
  "qualityChecks": [{"id": "placeholders-zero", "description": "Sin placeholders"}]
}
```

---

4) Checklist
- [ ] Docs inventariados y con owner.
- [ ] Revisiones calendarizadas.
- [ ] Checks de calidad definidos.
