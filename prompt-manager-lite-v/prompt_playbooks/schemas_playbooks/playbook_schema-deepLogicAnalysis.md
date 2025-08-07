# Schema Playbook — deepLogicAnalysis

Propósito: documentar análisis profundo de la lógica del sistema (flujos, invariantes, decisiones críticas, riesgos y mitigaciones) para reducir deuda cognitiva y fallos sutiles.

Ubicación: `schemas/master_blueprint_parts/deepLogicAnalysis.json`

---

1) Estructura del schema
- `domains[]`: áreas de lógica (autenticación, billing, permisos, etc.)
  - `name`, `description`, `keyInvariants[]`, `edgeCases[]`, `failureModes[]`
  - `decisionPoints[]`: { id, context, alternatives, chosen, rationale, links(adr, code[]) }
- `criticalPaths[]`: secuencias deterministas con pre/postcondiciones
  - { id, steps[], preconditions[], postconditions[], metrics[] }
- `risks[]`: { id, description, likelihood(low|medium|high), impact(low|medium|high), mitigations[] }
- `controls[]`: { type: monitor|alert|test, target, frequency }
- `links`: { adrs[], runbooks[], code[] }

---

2) Procedimiento
1. Identificar dominios lógicos y sus invariantes.
2. Mapear critical paths y edge cases.
3. Documentar decisiones (alternativas y trade-offs) y enlazar ADRs.
4. Catalogar riesgos y controles asociados.
5. Alinear con `businessLogic` y `testingStrategy`.

---

3) Ejemplo
```json
{
  "domains": [
    {
      "name": "auth",
      "description": "Autenticación y sesiones",
      "keyInvariants": ["token válido firma/exp"],
      "edgeCases": ["token revocado en refresh"],
      "failureModes": ["replay attack"],
      "decisionPoints": [
        {
          "id": "AUTH-001",
          "context": "Refresco de tokens",
          "alternatives": ["rotación", "sliding"],
          "chosen": "rotación",
          "rationale": "Menor ventana de ataque",
          "links": {"adr": "docs/adr/ADR-010.md", "code": ["/auth/refresh.ts"]}
        }
      ]
    }
  ],
  "criticalPaths": [
    {"id": "CP-LOGIN", "steps": ["POST /login", "emit token"], "preconditions": ["user exists"], "postconditions": ["session active"], "metrics": ["latency_ms"]}
  ],
  "risks": [{"id": "R-1", "description": "token leak", "likelihood": "low", "impact": "high", "mitigations": ["short ttl", "revoke api"]}],
  "controls": [{"type": "monitor", "target": "failed_logins", "frequency": "5m"}],
  "links": {"runbooks": ["docs/DOC028-OperationsRunbook.md"]}
}
```

---

4) KPIs
- Nº de invariantes cubiertos por tests.
- Latencia/errores en critical paths.
- Incidentes por failure mode (tendencia).

---

5) Buenas prácticas
- Regla de un concepto por decisión: maximiza claridad.
- Alinear invariantes con aserciones en código.

---

6) Checklist
- [ ] Dominios e invariantes definidos.
- [ ] Critical paths con pre/postcondiciones.
- [ ] Riesgos y controles mapeados.
- [ ] ADRs/código enlazado.
