# Schema Playbook — designSystem

Propósito: definir el sistema de diseño (tokens, tipografías, espacios, colores, componentes base) que gobierna UI/UX.

Ubicación: `schemas/master_blueprint_parts/designSystem.json`

---

1) Estructura del schema
- `tokens`:
  - `color[]`: { name, value, contrastPairs[] }
  - `typography[]`: { name, fontFamily, size, lineHeight, weight }
  - `space[]`: { name, value }
  - `radius[]`: { name, value }
  - `shadow[]`: { name, value }
- `guidelines`: { accessibility, motion, layout, content }
- `foundations`: { grid, breakpoints[] }
- `componentsBase[]`: { name, description, a11yNotes }

---

2) Procedimiento
1. Catalogar tokens actuales (fuente: CSS variables/Theme).
2. Verificar contraste y WCAG.
3. Definir guidelines y foundations.
4. Alinear con `componentLibrary`.

---

3) Ejemplo
```json
{
  "tokens": {
    "color": [{"name": "primary-500", "value": "#3366FF", "contrastPairs": ["#FFFFFF"]}],
    "typography": [{"name": "body", "fontFamily": "Inter", "size": 14, "lineHeight": 20, "weight": 400}],
    "space": [{"name": "s-2", "value": 8}]
  },
  "guidelines": {"accessibility": "WCAG AA"},
  "foundations": {"grid": 12, "breakpoints": [320, 768, 1024]}
}
```

---

4) Checklist
- [ ] Tokens auditados y sin duplicados.
- [ ] Contrastes validados.
- [ ] Foundations definidos.
- [ ] Alineado con `componentLibrary`.
