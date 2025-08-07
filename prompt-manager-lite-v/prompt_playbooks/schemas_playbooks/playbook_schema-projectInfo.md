# Schema Playbook — projectInfo

Propósito: completar y mantener `projectInfo.json` con la metadata esencial del proyecto.

Ubicación del schema: `schemas/master_blueprint_parts/projectInfo.json`

Secciones clave:
- `projectName` (string) — nombre oficial del proyecto.
- `projectDescription` (string) — resumen del propósito/alcance.
- `version` (string) — versión del blueprint (default recomendado: 3.0.0).

Pasos:
1) Definir `projectName` y `projectDescription` claros y únicos.
2) Establecer `version` siguiendo semver.
3) Validar coherencia con `DOC000-ProjectBrief.md`.

Checklist:
- [ ] `projectName` no vacío y único.
- [ ] `projectDescription` concisa (1–3 líneas).
- [ ] `version` en formato semver.

Ejemplo:
```json
{
  "projectName": "Prompt Manager Lite V",
  "projectDescription": "Sistema modular para orquestar documentación y blueprints.",
  "version": "3.0.0"
}
```

Referencias:
- `docs/DOC000-ProjectBrief.md`
- `schemas/master_blueprint_schema.json` (properties.projectInfo)
