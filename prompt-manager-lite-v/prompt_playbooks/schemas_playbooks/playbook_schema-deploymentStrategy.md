# Schema Playbook — deploymentStrategy

Propósito: describir estrategia de despliegue (entornos, pipelines, gates, rollback) para garantizar releases seguras y trazables.

Ubicación: `schemas/master_blueprint_parts/deploymentStrategy.json`

---

1) Estructura del schema
- `environments[]`: { name, url, purpose, protections[], deploymentMethod, ciCdPipeline{ provider, pipelineFile } }
- `pipelines[]`: { id, stages[]: { name, actions[], approvals[] } }
- `releasePolicy`: { cadence, freezeWindows[], versioning }
- `rollout`: { strategy: blue-green|canary|rolling|recreate, metrics[], abortCriteria[] }
- `rollback`: { procedures[], dataBackups, featureFlags[] }
- `compliance`: { checks[], evidence[] }

---

2) Procedimiento
1. Inventariar entornos y condiciones de promoción.
2. Definir stages y gates (QA, security, approvals).
3. Elegir estrategia de rollout y KPIs de control.
4. Especificar rollback paso a paso.
5. Alinear con `DOC010-Deployment`.

---

3) Ejemplo
```json
{
  "environments": [
    {"name": "staging", "url": "https://staging.example.com", "purpose": "testing", "protections": ["read-only db"]}
  ],
  "pipelines": [
    {"id": "ci-cd", "stages": [
      {"name": "build", "actions": ["lint", "test"], "approvals": []},
      {"name": "deploy-staging", "actions": ["helm upgrade"], "approvals": ["qa-lead"]}
    ]}
  ],
  "rollout": {"strategy": "canary", "metrics": ["error_rate", "latency"], "abortCriteria": ["error_rate>2%"]},
  "rollback": {"procedures": ["helm rollback"], "featureFlags": ["disable_new_checkout"]}
}
```

---

4) Checklist
- [ ] Entornos y pipelines definidos.
- [ ] Gates y aprobaciones claras.
- [ ] Rollout/rollback documentados.
- [ ] Métricas de control listas.
