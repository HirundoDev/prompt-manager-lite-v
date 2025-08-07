# Schema Playbook — wireframeStates

Propósito: definir estados clave de pantallas (empty/loading/error/success) con reglas de transición y expectativas UX.

Ubicación: `schemas/master_blueprint_parts/wireframeStates.json`

---

1) Estructura
- `screens[]`: { id, title, route, states[] }
- `states[]`: { viewName, componentTree }
- `transitions[]`: { screenId, from, to, guards[], actions[] }
- Nodo (`wireframeNode`): { componentType, id, textContent?, styles{}, children[], state? }

---

2) Procedimiento
1. Catalogar pantallas y estados esperados.
2. Definir transiciones y condiciones.
3. Enlazar referencias visuales (wireframes/figma).

---

3) Ejemplo
```json
{
  "screens": [{"id": "login", "title": "Login", "route": "/login", "states": ["empty", "loading", "error", "success"]}],
  "states": [{"viewName": "Login-Empty", "componentTree": {"componentType": "div", "id": "root", "state": "empty", "children": []}}],
  "transitions": [{"screenId": "login", "from": "empty", "to": "loading", "guards": ["form_valid"], "actions": ["submit"]}]
}

---

4) Checklist
- [ ] Estados por pantalla definidos.
- [ ] Transiciones y condiciones claras.
- [ ] Referencias visuales enlazadas.
