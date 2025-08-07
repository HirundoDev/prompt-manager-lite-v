# Schema Playbook — testingStrategy

Propósito: definir estrategia de pruebas (tipos, pirámide, responsabilidades, cobertura, datos de test).

Ubicación: `schemas/master_blueprint_parts/testingStrategy.json`

---

1) Estructura
- `pyramid`: { unit, integration, e2e }
- `types[]`: { name, scope, tools[], owner }
- `coverageTargets`: { lines, branches, criticalPaths }
- `testData`: { strategy: synthetic|masked|mixed, generators[] }
- `environments`: { staging, prodLike }
- `testingLevels[]`: { level: Unit|Integration|End-to-End|Performance|Security, framework, coverageTarget }
- `testEnvironments[]`: { name, description }

---

2) Procedimiento
1. Definir objetivos de cobertura y pirámide.
2. Mapear tipos de prueba por capa y owner.
3. Establecer estrategia de datos y entornos.

---

3) Ejemplo
```json
{
  "pyramid": {"unit": 70, "integration": 20, "e2e": 10},
  "types": [{"name": "contract", "scope": "api", "tools": ["pact"], "owner": "backend"}],
  "coverageTargets": {"lines": 80, "branches": 70},
  "testData": {"strategy": "synthetic", "generators": ["faker"]},
  "environments": {"staging": "docker-compose", "prodLike": "k8s"},
  "testingLevels": [{"level": "Unit", "framework": "Jest", "coverageTarget": ">=80%"}],
  "testEnvironments": [{"name": "CI", "description": "Pipeline"}]
}
```

---

4) Checklist
- [ ] Pirámide y metas definidas.
- [ ] Tipos/owners asignados.
- [ ] Datos/entornos de test listos.
