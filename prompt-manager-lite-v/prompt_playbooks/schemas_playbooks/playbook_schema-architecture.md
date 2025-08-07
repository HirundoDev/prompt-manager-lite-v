# Schema Playbook — architecture

Propósito: definir la arquitectura de software del sistema.

Ubicación: `schemas/master_blueprint_parts/architecture.json`

Claves:
- `architecturalPattern`: Monolithic | Microservices | Serverless | Layered | Event-Driven | Other
- `technologyStack[]`: { layer: Frontend|Backend|Database|Cache|MessageQueue, technology, version }
- `communicationStyle`: REST | GraphQL | gRPC | WebSocket | Message-Based
- `dataFlowDiagram`: descripción o enlace
 - Avanzado:
   - `services[]`: descomposición (name, responsibilities, ownsData, dependencies, communication, runtime, scaling)
   - `deploymentTopology`: entornos y nodos (envs, regions, nodes, ingress, cdn)
   - `dataManagement`: bases de datos, partición/sharding, consistencia, backup/restore
   - `observability`: logging, metrics, tracing, dashboards, alerting
   - `securityArchitecture`: threatModelRef, secrets, networkPolicies, authN/authZ, dataProtection
   - `availability`: sla, slo, rpo, rto, failover
   - `performance`: budgets, capacityPlanning
   - `integrationPoints[]`: externos (name, type, protocol, auth, rateLimits)
   - `eventing`: brokers, topics, schemas, retention, deliverySemantics
   - `configuration`: featureFlags, configs, schema
   - `risks`: riesgos claves, mitigación; `constraints`: restricciones
   - `adrRefs[]`: decisiones relevantes

Pasos:
1) Seleccionar `architecturalPattern` y justificarlo en `description` (si aplica).
2) Completar `technologyStack` por capa con versiones reales.
3) Definir `communicationStyle` principal.
4) Añadir `dataFlowDiagram` o enlace a diagrama.
5) Descomponer en `services` (si aplica), modelar responsabilidades y dependencias.
6) Definir `deploymentTopology` por entorno; incluir regiones, balanceo, ingress y CDN.
7) Completar `dataManagement` (modelos, consistencia, backup/restore, DR).
8) Definir `observability` y `securityArchitecture` transversales.
9) Especificar `availability` y `performance` con objetivos medibles.
10) Documentar `integrationPoints` y `eventing` (si aplica).
11) Registrar `risks`, `constraints` y referencias `adrRefs`.

Checklist:
- [ ] Patrón arquitectónico elegido y consistente con requisitos.
- [ ] Stack por capa completo y con versiones.
- [ ] Estilo de comunicación definido.
- [ ] Flujo de datos referenciado.
- [ ] Servicios descompuestos con responsabilidades y límites claros (si aplica).
- [ ] Topología de despliegue definida por entorno.
- [ ] Estrategia de datos y DR definida.
- [ ] Observabilidad y seguridad transversales documentadas.
- [ ] Disponibilidad y rendimiento con metas (SLA/SLO, RPO/RTO, budgets).
- [ ] Integraciones externas y mensajería documentadas.
- [ ] Riesgos, restricciones y ADRs referenciados.

Ejemplo mínimo:
```json
{
  "architecturalPattern": "Layered",
  "technologyStack": [
    {"layer":"Frontend","technology":"React","version":"18"},
    {"layer":"Backend","technology":"FastAPI","version":"0.110"},
    {"layer":"Database","technology":"PostgreSQL","version":"15"}
  ],
  "communicationStyle": "REST"
}
```

Ejemplo avanzado (fragmento):
```json
{
  "services": [
    {"name":"users","responsibilities":["auth","profile"],"ownsData":true,"dependencies":["email"],"communication":"REST","runtime":"python","scaling":{"min":2,"max":10}}
  ],
  "deploymentTopology": {"environments":[{"name":"prod","regions":["us-west"],"nodes":[{"name":"api","replicas":4}],"ingress":{"type":"alb"},"cdn":true}]},
  "dataManagement": {"databases":[{"name":"main","engine":"postgres","version":"15"}],"consistency":"strong","backup":{"schedule":"daily","retentionDays":30}},
  "observability": {"logging":"json","metrics":["latency","errors"],"tracing":"w3c","dashboards":["api-latency"],"alerting":["p95>300ms"]},
  "securityArchitecture": {"threatModelRef":"docs/STRIDE.md","secrets":"vault","networkPolicies":["zero-trust"],"authN":"OIDC","authZ":"RBAC","dataProtection":{"atRest":"AES-256","inTransit":"TLS1.3"}},
  "availability": {"sla":"99.9%","slo":{"p95LatencyMs":300},"rpo":"15m","rto":"30m","failover":"active-passive"},
  "performance": {"budgets":{"homepageMs":2000},"capacityPlanning":"QPS 500"},
  "integrationPoints": [{"name":"stripe","type":"payment","protocol":"REST","auth":"API Key","rateLimits":"100r/s"}],
  "eventing": {"broker":"kafka","topics":["user.created"],"schemas":{"user.created":{"type":"object"}},"retention":"7d","deliverySemantics":"at-least-once"},
  "configuration": {"featureFlags":["newCheckout"],"configSchema":{"type":"object"}},
  "risks": ["single region"],
  "constraints": ["PCI"],
  "adrRefs": ["docs/adr/0001-architecture.md"]
}
```

Referencias:
- `docs/DOC004-FrontendArchitecture.md`
- `docs/DOC006-BackendArchitecture.md`
