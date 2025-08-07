# Schema Playbook — componentLibrary

Propósito: definir catálogo de componentes UI reutilizables y sus contratos.

Ubicación: `schemas/master_blueprint_parts/componentLibrary.json`

---

1) Alcance y principios
- Contratos estables: cada componente describe props, eventos y slots con tipos y semántica.
- Trazabilidad con el Design System: tokens y variantes deben existir en `designSystem`.
- Ejemplos ejecutables (Storybook/MDX) preferidos.
 - Identificadores estables: usar `id` y/o `slug` para enlazar desde `visualBlueprint.pages[].componentRefs[]`.

---

2) Estructura del schema (claves obligatorias)
- `components[]`:
  - `id?`, `slug?` (para referencias cruzadas desde visualBlueprint)
  - `name`, `description`
  - `status`: draft|stable|deprecated
  - `props[]`: { name, type, required, default, description }
  - `events[]`: { name, payloadSchema, description }
  - `slots[]`: { name, description }
  - `accessibility`: { ariaRoles[], keyboardNav, contrast }
  - `examples[]`: { title, code, screenshot? }
  - `codeRefs[]`: rutas a implementación
  - opcionales: `version`, `tags[]`, `dependencies[]`, `deprecations` { replacedBy, since }, `usageGuidelines`
- `theming`:
  - `tokens[]`: { name, type: color|space|radius|font, description }
  - `variants[]`: { name, appliesTo: [componentNames], tokens: [tokenNames] }
- Root opcionales: `repository`, `workflows[]`, `contributionGuidelines`

---

3) Procedimiento paso a paso
1. Inventariar componentes existentes por carpetas/repos.
2. Definir contrato de cada componente (props/eventos/slots) y estado (stable/deprecated).
3. Conectar tokens/variantes del design system; listar gaps.
4. Añadir ejemplos mínimos y enlaces a historias.
5. Asegurar criterios de accesibilidad.
6. Revisar dependencias y patrón de composición/container-presentational si aplica.
7. Asignar `id/slug` y usar esos valores en `visualBlueprint.pages[].componentRefs[]`.

---

4) Ejemplo completo
```json
{
  "components": [
    {
      "id": "cmp-button",
      "slug": "button",
      "name": "Button",
      "description": "Botón primario",
      "status": "stable",
      "props": [
        {"name": "variant", "type": "'primary'|'secondary'|'link'", "required": false, "default": "primary", "description": "Estilo"},
        {"name": "disabled", "type": "boolean", "required": false, "default": false}
      ],
      "events": [{"name": "click", "payloadSchema": {"type": "object", "properties": {"mouseX": {"type": "number"}}}}],
      "slots": [{"name": "default", "description": "Contenido del botón"}],
      "accessibility": {"ariaRoles": ["button"], "keyboardNav": "enter/space", "contrast": ">=4.5:1"},
      "examples": [{"title": "Primario", "code": "<Button>Guardar</Button>"}],
      "codeRefs": ["/ui/components/Button.tsx"],
      "version": "1.2.0",
      "tags": ["form", "action"],
      "dependencies": ["Popover"],
      "deprecations": {"replacedBy": "ButtonV2", "since": "2024-12"},
      "usageGuidelines": "Usar para acciones primarias."
    }
  ],
  "theming": {
    "tokens": [
      {"name": "color-primary", "type": "color", "description": "Color marca"}
    ],
    "variants": [
      {"name": "primary", "appliesTo": ["Button"], "tokens": ["color-primary"]}
    ]
  },
  "repository": "https://git.example.com/ui-library",
  "workflows": ["build", "lint", "visual-regression"],
  "contributionGuidelines": "Ver CONTRIBUTING.md"
}
```

---

5) Métricas/KPIs
- % de componentes con ejemplos y props tipadas.
- Issues de accesibilidad por release.
- Reutilización (nº de repos/módulos que consumen el componente).

---

6) Buenas prácticas
- Props controladas vs no controladas bien documentadas.
- Eventos con payloads tipados y estables.
- Evitar variantes ad-hoc; centralizar en tokens.

---

7) Errores comunes
- Props ambiguas o redundantes.
- Ausencia de ejemplos y de criterios de A11y.

---

8) Checklist final
- [ ] Props/eventos/slots documentados y tipados.
- [ ] Estado (stable/deprecated) asignado.
- [ ] Tokens/variantes enlazados al design system.
- [ ] Accesibilidad cubierta.
- [ ] Ejemplos presentes.
 - [ ] `id/slug` asignados y usados en visualBlueprint.

---

9) Referencias
- `docs/DOC003-DesignSystem.md`
