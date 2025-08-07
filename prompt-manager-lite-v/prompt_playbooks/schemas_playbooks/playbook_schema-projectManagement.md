# Schema Playbook — projectManagement

Propósito: describir estructura de gestión del proyecto (roles, rituales, tableros, cadencias, métricas de entrega).

Ubicación: `schemas/master_blueprint_parts/projectManagement.json`

---

1) Estructura
- `roles[]`: { name, responsibilities[] }
- `rituals[]`: { name, frequency, participants[] }
- `boards[]`: { tool, url, columns[] }
- `cadence`: { sprintLengthDays, planningDay }
- `deliveryMetrics`: { leadTime, cycleTime, throughput }

---

2) Procedimiento
1. Inventariar cómo se trabaja hoy (reuniones, tableros, métricas).
2. Estandarizar roles y cadencias.
3. Publicar tableros y rituales.

---

3) Ejemplo
```json
{
  "roles": [{"name": "PM", "responsibilities": ["priorizar backlog"]}],
  "cadence": {"sprintLengthDays": 14, "planningDay": "Mon"}
}
```

---

4) Checklist
- [ ] Roles claros.
- [ ] Cadencias definidas.
- [ ] Tableros enlazados.
