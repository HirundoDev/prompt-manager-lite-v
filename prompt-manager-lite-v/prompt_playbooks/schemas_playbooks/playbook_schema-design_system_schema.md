# Schema Playbook: design_system_schema.json (root)

Status and Scope
- Status: Active. This root schema is used to describe and generate the frontend design system end-to-end (tokens → components → usage).
- Scope: Authoritative for UI token specification and component catalog used by generators, linters, and documentation pipelines.
- Relation: The canonical schema for master blueprint composition remains `schemas/master_blueprint_parts/designSystem.json`. This root file is a superset focused on codegen and design delivery.

Purpose
- Provide a normalized, machine-actionable source of truth for:
  - Design tokens (color, typography, spacing, motion, etc.)
  - Semantic tokens (background, text, interactive, feedback, border, overlay)
  - Component catalog (atoms/molecules), including anatomy, variants, states, propsSchema, a11y, and use-cases
  - Naming conventions and theming strategy (light/dark/brand)
  - Mapping a tokens/components → CSS variables/Design tokens in code, Storybook, and UI libraries

How it’s used (pipeline overview)
1) Validate `schemas/design_system_schema.json`.
2) Transform tokens → CSS variables/TypeScript constants (e.g., `--color-primary-500`, `--radius-md`).
3) Generate component metadata docs (MDX/Storybook) and ESLint style rules if needed.
4) Feed UI builders (e.g., Tailwind theme, CSS-in-JS theme, tokens.json for Figma/Style Dictionary).
5) Publish artifacts: `design-tokens.css`, `tokens.ts`, `storybook` docs.

High-level structure (overview)
- `designSystem.systemInfo`: name, version, description
- `designSystem.philosophyAndBrand`:
  - `designPrinciples`: e.g., Claridad, Consistencia
  - `brandPersonality.keywords`
- `designSystem.designTokens`:
  - `color.palette`: raw palette (e.g., `blue-50`, `neutral-900`)
  - `color.semantic`: semantic tokens grouped by usage: `background`, `text`, `interactive`, `feedback`, `border`, `overlay`
  - `typography`: `fontStack`, `typeScale` (Display, H1, H2, Body, Caption)
  - `layout`: `spacingUnit`, `scale`, `breakpoints`
  - `effects`: `shadows`, `borderRadius`
  - `sizing`: `icon`, `container`
  - `borders`: `width`, `style`
  - `zIndex`: dropdown → tooltip
  - `motion`: `duration`, `easing`
- `designSystem.componentCatalog`:
  - `atoms` and `molecules` with component entries. Each has:
    - `detectionMethod`: visual | inferred
    - `anatomy`: ordered parts (Container, Label, Icon, etc.)
    - `variants`: primary/secondary/…
    - `sizes`: sm/md/lg
    - `states`: default/hover/active/focus-visible/disabled/loading, etc.
    - `propsSchema`: typed prop hints (string/boolean/function)
    - `accessibility`: ARIA and keyboard requirements
    - `useCases`: do/do-not guidance

Conventions and rules
- Token naming:
  - Palette: `color-family-level` (e.g., `blue-50`, `neutral-900`).
  - CSS variable export: `--color-blue-50`, `--text-primary`, `--space-4`.
  - Semantic tokens map to palette but remain stable (avoid hardcoding palette values in components).
- Typography:
  - Scale entries must include `fontSize`, `fontWeight`, `lineHeight`. Use rem/px consistently (recommend rem in exports).
- Layout:
  - `spacingUnit` governs `scale` derivations; ensure monotonic increments.
  - Breakpoints follow mobile-first: `sm < md < lg < xl`.
- Motion:
  - Keep durations short/medium/long within accessible ranges. Provide prefers-reduced-motion guidance in codegen.
- Z-index:
  - Reserve ranges: dropdown(1000) … tooltip(1070). New layers must not collide.
- Components:
  - Each component MUST specify anatomy, states, variants, sizes.
  - Accessibility MUST include ARIA role/label guidance and keyboard interactions.
  - `propsSchema` captures intended API; code generators may map to TS types.

Theming and dark mode
- Strategy: semantic tokens + theme overlays. Provide an optional dark theme map:
  - Example: `text.primary` becomes `#F8F9FA` on dark.
- Out of scope: runtime theme switch implementation; in scope: token definitions and mapping tables.

Design-to-code mapping
- Outputs expected:
  - CSS variables: `:root{ --color-blue-50: #E3F2FD; ... }`
  - tokens.ts: typed exports for design tokens
  - Tailwind theme extension or CSS-in-JS theme object
- Mapping examples:
  - `designTokens.color.semantic.text.primary` → `--text-primary`
  - `layout.scale.space-4` → `--space-4`
  - `effects.borderRadius.md` → `--radius-md`

Examples (snippets)
```json
{
  "designSystem": {
    "designTokens": {
      "color": {
        "palette": { "blue-50": "#E3F2FD", "neutral-900": "#212529" },
        "semantic": {
          "text": { "primary": "#212529", "secondary": "#6C757D" },
          "interactive": { "default": "#0D6EFD", "hover": "#0B5ED7" }
        }
      },
      "typography": {
        "fontStack": { "sans": "Inter, ...", "mono": "Menlo, ..." },
        "typeScale": [
          { "name": "H1", "fontSize": "32px", "fontWeight": 700, "lineHeight": "1.3" }
        ]
      }
    },
    "componentCatalog": {
      "atoms": {
        "Button": {
          "anatomy": ["Container", "Label", "Icon (Opcional)"],
          "variants": ["primary", "secondary", "tertiary", "danger"],
          "states": ["default", "hover", "active", "focus-visible", "disabled", "loading"],
          "propsSchema": { "label": "string", "onClick": "function", "isLoading": "boolean" },
          "accessibility": { "aria-label": "Requerido si no hay texto visible." }
        }
      }
    }
  }
}
```

Validation checklist
- [ ] `systemInfo.name`, `version`, `description` definidos
- [ ] `designTokens.color.palette` contiene familias y niveles coherentes
- [ ] Tokens semánticos cubren background, text, interactive, feedback, border, overlay
- [ ] `typography.typeScale` con propiedades completas y consistentes
- [ ] `layout.spacingUnit`, `scale`, `breakpoints` validados
- [ ] `effects.shadows` y `borderRadius` sin valores ambiguos
- [ ] Componentes con anatomy/variants/states/propsSchema/a11y
- [ ] Z-index sin colisiones; motion dentro de rangos accesibles

Versionado y migración
- Mantén `systemInfo.version` (semver) cuando cambien nombres o semánticas de tokens.
- Provee tablas de migración cuando renombres tokens (e.g., `--color-primary` → `--color-brand-primary`).

Colaboración y contribución
- Cambios de tokens requieren validación visual y aprobaciones de diseño y frontend.
- Añadir componentes sigue este orden: anatomy → variants/sizes/states → props → a11y → usos.
- Documenta breaking changes en `DOC003-DesignSystem.md` y en el changelog.

Relación con master blueprint
- `master_blueprint_parts/designSystem.json` se mantiene para composición global.
- Este archivo raíz es la especificación operativa para generación y entrega de UI.

Metadatos mínimos requeridos
- Asegura `$schema` y `$comment` en `schemas/design_system_schema.json`:
  - `$comment: Playbook: prompt_playbooks/schemas_playbooks/playbook_schema-design_system_schema.md`
