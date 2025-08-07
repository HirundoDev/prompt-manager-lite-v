# Schema Playbook — designPatterns

Propósito: catalogar patrones de diseño y arquitectura (frontend y backend), con lineamientos de uso, relaciones y ejemplos.

Ubicación: `schemas/master_blueprint_parts/designPatterns.json`

---

1) Estructura
- `patterns[]`: {
  name, category, type, tags[], maturity: experimental|recommended|deprecated,
  description, context, problem, solution,
  adoptionGuidelines?, migrationGuidelines?,
  examples: { frontend?: { framework, components[], codeRef }, backend?: { language, framework, modules[], codeRef } },
  consequences: { pros[], cons[] }, applicability[], triggers[], antiTriggers[],
  antiPatterns[]: { name, description }, references[] (URI), adrs[], diagramRefs[] (URI),
  codeSamples[]: { language, snippetRef }, knownUses[]: { system, component?, link? },
  kpis: { metrics[]: { name, target, measurement } }, risks[], mitigations[],
  compatibility: { compatibleWith[], incompatibleWith[] }, constraints[], assumptions[],
  security: { implications[], threatModelRef? }, compliance: { standards[] },
  versioning: { since, until }, lintRules[]: { tool, rule, severity }
}
- `governance`: { preferredPatterns[], deprecatedPatterns[], usagePolicies[], owners[], reviewProcess }
- `mapping`: { frontend: { patternsUsed[], libraries[] }, backend: { patternsUsed[], frameworks[] }, infrastructure?: { patternsUsed[], platforms[], services[] }, devex?: { patternsUsed[], tools[], scaffolds[] } }
- `relationships[]`: { pattern, relatesTo, relationType: complements|alternative|dependsOn }

---

2) Procedimiento
1. Definir owners y proceso de revisión.
2. Documentar contexto-problema-solución, riesgos/mitigaciones y KPIs.
3. Añadir ejemplos (código y repos), ADRs y diagramas.
4. Mapear compatibilidades/conflictos y uso por stack.
5. Agregar lineamientos de adopción y migración.

---

3) Ejemplo
```json
{
  "patterns": [
    {
      "name": "CQRS",
      "category": "backend",
      "type": "architectural",
      "tags": ["ddd", "event-driven"],
      "maturity": "recommended",
      "description": "Separar comandos y consultas",
      "context": "Altas cargas de lectura y escritura",
      "problem": "Una única capa complica rendimiento y evolución",
      "solution": "Segregar modelos de lectura/escritura",
      "adoptionGuidelines": "Usar cuando lectura y escritura tienen SLA distintos",
      "migrationGuidelines": "Introducir capas de query/read en paralelo",
      "examples": {"backend": {"language": "Node.js", "framework": "NestJS", "modules": ["Commands", "Queries"], "codeRef": "repo://services/order"}},
      "consequences": {"pros": ["Escalabilidad"], "cons": ["Complejidad"]},
      "applicability": ["Múltiples consumidores"],
      "triggers": ["Lecturas dominantes"],
      "antiTriggers": ["CRUD sencillo"],
      "antiPatterns": [{"name": "Overengineering", "description": "Usarlo en sistemas simples"}],
      "references": ["https://martinfowler.com/bliki/CQRS.html"],
      "adrs": ["ADR-001-CQRS.md"],
      "diagramRefs": ["https://diagrams.example/cqrs-overview.png"],
      "codeSamples": [{"language": "ts", "snippetRef": "repo://libs/cqrs/example.ts"}],
      "knownUses": [{"system": "Orders", "component": "OrderService", "link": "repo://services/order"}],
      "kpis": {"metrics": [{"name": "P95 Read Latency", "target": "<150ms", "measurement": "apm"}]},
      "risks": ["Complejidad operativa"],
      "mitigations": ["Automatizar despliegues"],
      "compatibility": {"compatibleWith": ["Event Sourcing"], "incompatibleWith": ["Active Record"]},
      "constraints": ["Consistencia eventual"],
      "assumptions": ["Mensajería confiable"],
      "security": {"implications": ["Más superficies de ataque"], "threatModelRef": "ADR-SEC-010.md"},
      "compliance": {"standards": ["ISO27001"]},
      "versioning": {"since": "v1.2", "until": ""},
      "lintRules": [{"tool": "eslint", "rule": "no-repository-in-controller", "severity": "error"}]
    }
  ],
  "governance": {
    "preferredPatterns": ["Repository", "Adapter", "Saga"],
    "deprecatedPatterns": ["Active Record"],
    "usagePolicies": ["Validar en ADR"],
    "owners": ["Architecture Board"],
    "reviewProcess": "RFC + ADR + PR"
  },
  "mapping": {
    "frontend": { "patternsUsed": ["Adapter"], "libraries": ["redux-toolkit"] },
    "backend": { "patternsUsed": ["Repository", "CQRS"], "frameworks": ["NestJS"] },
    "infrastructure": { "patternsUsed": ["Infrastructure as Code"], "platforms": ["Kubernetes"], "services": ["ArgoCD"] },
    "devex": { "patternsUsed": ["Monorepo"], "tools": ["Nx", "Turborepo"], "scaffolds": ["create-app-template"] }
  },
  "relationships": [{"pattern": "Repository", "relatesTo": "Active Record", "relationType": "alternative"}]
}
```

---

4) Checklist
- [ ] Owners y proceso de revisión definidos.
- [ ] Contexto-problema-solución y KPIs completos.
- [ ] Riesgos/mitigaciones, triggers y anti-triggers.
- [ ] Ejemplos, ADRs, diagramas y samples de código.
- [ ] Compatibilidades/conflictos y mapeo por stack.
- [ ] Lineamientos de adopción y migración.
