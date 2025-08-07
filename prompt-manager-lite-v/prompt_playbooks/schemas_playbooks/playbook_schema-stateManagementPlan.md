# Schema Playbook — stateManagementPlan

Propósito: definir cómo se maneja el estado (client/server/cache/sync) y sus invariantes.

Ubicación: `schemas/master_blueprint_parts/stateManagementPlan.json`

---

1) Estructura
- `stores[]`: { name, scope: client|server|shared, technology, persistence, description }
- `entities[]`: { name, schemaRef, normalization, cacheTTL }
- `sync`: { strategies[]: { from, to, method, conflictResolution } }
- `invariants[]`: { description, checks[] }

---

2) Procedimiento
1. Inventariar stores y entidades.
2. Definir políticas de cache y sincronización.
3. Establecer invariantes y checks automáticos.

---

3) Ejemplo
```json
{
  "stores": [{"name": "redux", "scope": "client", "technology": "redux-toolkit", "persistence": "localStorage"}],
  "entities": [{"name": "User", "schemaRef": "#/components/schemas/User", "normalization": "byId", "cacheTTL": 300}],
  "sync": {"strategies": [{"from": "server", "to": "client", "method": "SSE", "conflictResolution": "last-write-wins"}]},
  "invariants": [{"description": "userId siempre presente tras login", "checks": ["state.user.id != null"]}]
}
```

---

4) Checklist
- [ ] Stores y entidades mapeadas.
- [ ] Cache/sync definidos.
- [ ] Invariantes y checks.
