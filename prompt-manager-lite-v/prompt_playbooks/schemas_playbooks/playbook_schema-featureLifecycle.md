# Schema Playbook — featureLifecycle

Propósito: modelar el ciclo de vida de features (ideación->GA->sunset) para planificación y trazabilidad.

Ubicación: `schemas/master_blueprint_parts/featureLifecycle.json`

---

1) Estructura
- `[]` (array de features): cada item incluye
  - `featureId`, `status`, `summary`, `path`
  - `stages[]`: { name: Idea|Discovery|MVP|Beta|GA|Sunset, entryChecks[], exitCriteria[] }
  - `transitions[]`: { from, to, guards[], actions[] }
  - `metrics`: { adoption, churn, NPS }
  - `ownership`: { productOwner, techOwner }

---

2) Procedimiento
1. Definir stages y criterios por feature (si aplica globalmente, replicar en las features relevantes).
2. Mapear transiciones y gates (reviews, seguridad).
3. Establecer métricas clave por stage/feature.

---

3) Ejemplo
```json
[
  {
    "featureId": "FEAT-001",
    "status": "In Progress",
    "summary": "Checkout v2",
    "path": "docs/features/FEAT-001.md",
    "stages": [{"name": "MVP", "entryChecks": ["PRD"], "exitCriteria": [">100 MAU"]}],
    "transitions": [{"from": "MVP", "to": "Beta", "guards": ["obs"], "actions": ["announce"]}],
    "metrics": {"adoption": 0},
    "ownership": {"productOwner": "PM", "techOwner": "Lead"}
  }
]
```

---

4) Checklist
- [ ] Stages y criterios documentados.
- [ ] Métricas definidas.
- [ ] Owners asignados.
