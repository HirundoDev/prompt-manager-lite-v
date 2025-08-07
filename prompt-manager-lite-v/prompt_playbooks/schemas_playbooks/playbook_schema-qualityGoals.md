# Schema Playbook — qualityGoals

Propósito: establecer objetivos de calidad (medibles) por dimensión y cobertura.

Ubicación: `schemas/master_blueprint_parts/qualityGoals.json`

---

1) Estructura
- `dimensions[]`: { name: reliability|security|usability|performance|maintainability, target, metric, measurement }
- `coverage`: { tests: { unit, integration, e2e }, thresholds }
- `process`: { reviews, gates }

---

2) Procedimiento
1. Seleccionar dimensiones relevantes y targets.
2. Definir cómo se mide cada métrica.
3. Alinear thresholds con CI.

---

3) Ejemplo
```json
{
  "dimensions": [{"name": "performance", "target": "p95<300ms", "metric": "latency_p95", "measurement": "prometheus"}],
  "coverage": {"tests": {"unit": 80, "integration": 60, "e2e": 40}},
  "process": {"reviews": "2 reviewers min", "gates": "bloquear merge si tests < thresholds"}
}
```

---

4) Checklist
- [ ] Metas medibles por dimensión.
- [ ] Cobertura y thresholds.
- [ ] Integración con CI.
