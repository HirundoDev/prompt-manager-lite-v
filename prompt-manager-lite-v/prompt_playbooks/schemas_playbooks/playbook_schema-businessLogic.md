# Schema Playbook — businessLogic

Propósito: capturar reglas y políticas de negocio que afectan decisiones del sistema.

Ubicación: `schemas/master_blueprint_parts/businessLogic.json`

---

1) Alcance y principios
- Debe ser ejecutable o al menos validable: cada regla tiene inputs/outputs y pre/postcondiciones.
- Trazabilidad: vincular cada regla con PRDs/ADRs y fragmentos de código.
- Versionado: cambios en reglas deben registrarse con fecha y autor.

---

2) Estructura del schema (claves obligatorias)
- `rules[]`:
  - `id`: identificador estable (RULE-###)
  - `title`: nombre corto
  - `description`: detalle de la regla
  - `inputs[]`: { name, type, source }
  - `outputs[]`: { name, type, target }
  - `preconditions[]`: condiciones que deben cumplirse
  - `postconditions[]`: garantías tras aplicar la regla
  - `constraints[]`: límites/regulaciones (p. ej., GDPR, límites de tarifa)
  - `examples[]`: casos Given/When/Then
  - `links`: { prd, adr, codeRefs[] }
- `policies[]`:
  - `name`, `scope` (global|module), `enforcement` (hard|soft), `owner`
  - `controls[]`: validaciones/controles automatizables
- `evaluation`:
  - `engine`: decision-table|rules-engine|custom
  - `priority`: tie-breakers cuando múltiples reglas aplican

---

3) Procedimiento paso a paso
1. Levantar PRDs y ADRES relevantes; extraer reglas candidatas.
2. Definir inputs/outputs y pre/postcondiciones por regla.
3. Escribir ejemplos Given/When/Then (3–5 por regla crítica).
4. Asociar `codeRefs` (módulos/funciones) y tests existentes.
5. Definir políticas globales y controles (linters/CI checks) para enforcement.
6. Establecer estrategia de evaluación (orden, prioridad, conflictos).
7. Revisar con stakeholders; versionar cambios.

---

4) Ejemplo completo
```json
{
  "rules": [
    {
      "id": "RULE-001",
      "title": "Descuento VIP",
      "description": "Aplicar 10% si el cliente es VIP y el carrito supera $100",
      "inputs": [
        {"name": "isVip", "type": "boolean", "source": "customerProfile"},
        {"name": "cartTotal", "type": "number", "source": "checkout"}
      ],
      "outputs": [
        {"name": "discount", "type": "number", "target": "pricing"}
      ],
      "preconditions": ["cartTotal >= 0"],
      "postconditions": ["discount >= 0"],
      "constraints": ["maxDiscountPercent:20"],
      "examples": [
        {"given": {"isVip": true, "cartTotal": 150}, "when": "checkout", "then": {"discount": 15}},
        {"given": {"isVip": false, "cartTotal": 150}, "when": "checkout", "then": {"discount": 0}}
      ],
      "links": {"prd": "docs/DOC002-ProductDefinition.md#pricing", "adr": "docs/adr/ADR-001.md", "codeRefs": ["/app/pricing/applyDiscount.ts"]}
    }
  ],
  "policies": [
    {"name": "GDPR-PII", "scope": "global", "enforcement": "hard", "owner": "legal", "controls": ["mask_pii_in_logs"]}
  ],
  "evaluation": {"engine": "decision-table", "priority": "first_match"}
}
```

---

5) Métricas/KPIs
- Cobertura de reglas por tests (% de reglas con tests). 
- Falsos positivos/negativos en decisiones.
- Latencia del motor de reglas.

---

6) Buenas prácticas
- Reglas pequeñas y composables; evitar condiciones monolíticas.
- Ejemplos ejecutables (usarlos como tests de aceptación).
- Mantener `codeRefs` actualizados con PRs.

---

7) Errores comunes
- Ambigüedad entre políticas y reglas operativas.
- Falta de pre/postcondiciones medibles.

---

8) Checklist final
- [ ] Reglas con inputs/outputs claros.
- [ ] Ejemplos Given/When/Then por regla.
- [ ] Controles de enforcement definidos.
- [ ] Trazabilidad PRD/ADR/código.

---

9) Referencias
- `docs/DOC002-ProductDefinition.md`
