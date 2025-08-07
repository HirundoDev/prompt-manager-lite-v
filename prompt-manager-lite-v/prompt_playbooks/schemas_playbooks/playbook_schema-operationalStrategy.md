# Schema Playbook — operationalStrategy

Propósito: definir cómo operamos el sistema en producción (SLOs, alertas, on-call, mantenimiento).

Ubicación: `schemas/master_blueprint_parts/operationalStrategy.json`

---

1) Estructura
- `slos[]`: { service, objective, threshold, window }
- `alerts[]`: { metric, condition, channel, runbook }
- `oncall`: { rotations[], escalation }
- `maintenance`: { windows[], procedures[] }

---

2) Procedimiento
1. Definir SLOs por servicio.
2. Mapear métricas y alertas con umbrales.
3. Establecer rotaciones y escalaciones.
4. Documentar ventanas y procedimientos de mantenimiento.

---

3) Ejemplo
```json
{
  "slos": [{"service": "api", "objective": "availability", "threshold": "99.9%", "window": "30d"}],
  "alerts": [{"metric": "error_rate", "condition": ">2% for 5m", "channel": "slack:#oncall", "runbook": "docs/DOC028-OperationsRunbook.md#errors"}]
}
```

---

4) Checklist
- [ ] SLOs y alertas definidos.
- [ ] On-call y escalaciones documentadas.
- [ ] Runbooks enlazados.
