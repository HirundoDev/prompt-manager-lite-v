# Schema Playbook — bugLifecycle

Propósito: definir el flujo de vida de bugs (estado, transiciones, SLA, responsables).

Ubicación: `schemas/master_blueprint_parts/bugLifecycle.json`

---

1) Alcance y principios
- El lifecycle debe ser determinista, auditable y medible (SLA, aging, throughput).
- Debe mapear 1:1 con la herramienta operativa (GitHub Issues/Jira) y con `featureLifecycle`.
- Todas las transiciones deben tener guardas (condiciones) y side-effects (asignación, etiquetas, notificaciones).

---

2) Estructura del schema (claves obligatorias)
- `states[]`: lista ordenada de estados válidos.
  - `name`: string (Open|Triaged|InProgress|QA|Done|Reopened|Closed)
  - `entryChecks[]`: validaciones al entrar (p. ej., reproducible, logs adjuntos)
  - `exitCriteria[]`: condiciones para salir (p. ej., PR merged, tests verdes)
- `transitions[]`: reglas de cambio de estado.
  - `from`: string (estado origen)
  - `to`: string (estado destino)
  - `guards[]`: condiciones requeridas (p. ej., tener assignee, etiqueta `severity:*`)
  - `actions[]`: efectos (asignar owner, set label, comentar, notificar)
- `priorities`: definición y políticas por prioridad.
  - `levels[]`: { name: P0|P1|P2|P3, description }
  - `slaHoursByPriority`: { P0: 24, P1: 72, ... }
- `ownershipRules`:
  - `defaultOwner`: equipo/usuario por defecto
  - `routing`: { area:"frontend" -> team:"web-ui" }
- `reopenPolicy`: condiciones para reabrir y a qué estado vuelve (QA->Reopened->InProgress)
- `duplicatePolicy`: cómo marcar y cerrar duplicados (link al primario)
- `labels`: taxonomía requerida (severity, area, type)
- `notifications`:
  - `onTransition[]`: { from, to, channels: ["slack:#bugs"], templateId }

---

3) Procedimiento paso a paso
1. Descubrimiento: inventariar estados reales usados hoy en el tracker (query por label/status) y normalizarlos.
2. Definir estados canónicos y su orden; documentar entry/exit checks.
3. Enumerar transiciones válidas; para cada transición, definir `guards` y `actions` (asignación, labels, comentario automático).
4. Establecer prioridades (P0–P3) con criterios y SLAs en horas. Alinear con `operations`/`on-call`.
5. Definir ownershipRules y routing por área/módulo (mapea paths/rutas de código a equipos).
6. Políticas: reopen (quién puede, evidencia requerida), duplicate (link y cierre), wontfix (justificación), invalid.
7. Notificaciones: definir canales por transición crítica (Open->Triaged P0 notifica on-call).
8. Validar el ciclo contra `featureLifecycle` (estados y transiciones compatibles para issues relacionados a features).
9. Publicar el schema y sincronizar automations (workflows/bots) del repo.

---

4) Ejemplo completo
```json
{
  "states": [
    {"name": "Open", "entryChecks": ["has_title", "has_description"], "exitCriteria": ["has_assignee"]},
    {"name": "Triaged", "entryChecks": ["has_severity", "has_area"], "exitCriteria": ["has_priority"]},
    {"name": "InProgress", "entryChecks": ["assignee_acknowledged"], "exitCriteria": ["pr_linked"]},
    {"name": "QA", "entryChecks": ["fix_deployed_to_stage"], "exitCriteria": ["tests_passed", "no_regressions"]},
    {"name": "Done"},
    {"name": "Reopened"},
    {"name": "Closed"}
  ],
  "transitions": [
    {"from": "Open", "to": "Triaged", "guards": ["assignee_set"], "actions": ["add_label:triaged"]},
    {"from": "Triaged", "to": "InProgress", "guards": ["priority_set"], "actions": ["notify:slack:#bugs"]},
    {"from": "InProgress", "to": "QA", "guards": ["pr_linked"], "actions": ["assign:qa_team"]},
    {"from": "QA", "to": "Done", "guards": ["tests_passed"], "actions": ["comment:ready_to_close"]},
    {"from": "Done", "to": "Closed"},
    {"from": "Done", "to": "Reopened", "guards": ["bug_reproducible"], "actions": ["add_label:reopened"]}
  ],
  "priorities": {
    "levels": [
      {"name": "P0", "description": "Caída total / data-loss"},
      {"name": "P1", "description": "Impacto alto, workaround limitado"},
      {"name": "P2", "description": "Impacto medio, workaround existe"},
      {"name": "P3", "description": "Bajo impacto / cosmetic"}
    ],
    "slaHoursByPriority": {"P0": 24, "P1": 72, "P2": 168, "P3": 336}
  },
  "ownershipRules": {
    "defaultOwner": "core-engineering",
    "routing": {"area:frontend": "web-ui", "area:backend": "platform"}
  },
  "reopenPolicy": {"allowedFrom": ["Done", "Closed"], "reopenTo": "Reopened", "requirements": ["repro_steps", "env_info"]},
  "duplicatePolicy": {"action": "close", "label": "duplicate", "linkRequired": true},
  "labels": ["severity:P0", "area:frontend", "type:bug"],
  "notifications": {"onTransition": [{"from": "Triaged", "to": "InProgress", "channels": ["slack:#bugs"], "templateId": "triaged_to_wip"}]}
}
```

---

5) Métricas y KPIs
- Lead time por prioridad (Open->Done/Closed).
- Tasa de reopen (% de issues reabiertos por ciclo).
- Aging: número de bugs sin triage > X horas.
- SLA compliance por prioridad.

---

6) Buenas prácticas
- Minimizar estados; evitar ramificaciones innecesarias.
- Toda transición crítica debe automatizar al menos una acción (label/notify/assign).
- Usar labels normalizados (`severity:*`, `area:*`).
- Revisiones semanales del aging y de SLA breaches.

---

7) Errores comunes
- Estados solapados (QA vs Verification sin criterios claros).
- Falta de guardas: transiciones sin `assignee` ni `priority` provocan estancamientos.
- Políticas de reopen/duplicate no documentadas -> ruido operativo.

---

8) Checklist final
- [ ] Estados definidos con entry/exit checks.
- [ ] Transiciones con guards y actions.
- [ ] Prioridades y SLAs documentados.
- [ ] Ownership/routing establecido.
- [ ] Políticas de reopen/duplicate definidas.
- [ ] Notificaciones configuradas.
- [ ] Métricas acordadas y monitoreo activo.

---

9) Referencias cruzadas
- `docs/DOC031-BugIndex.md`
- `schemas/master_blueprint_parts/featureLifecycle.json`
