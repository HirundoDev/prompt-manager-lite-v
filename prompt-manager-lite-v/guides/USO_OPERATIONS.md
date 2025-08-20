# Guía de Uso: Operations

## 🎯 Objetivo
Estandarizar tareas operativas y runbooks.

## 📁 Ubicación
- Base del repositorio: `prompt-manager-lite-v/`
- Carpeta: `prompt-manager-lite-v/streaming_files/operations/`
- Templates existentes: `prompt-manager-lite-v/streaming_files/operations/template.md`
- Manifiesto local (si aplica): `prompt-manager-lite-v/streaming_files/operations/manifest.json`

## 🧩 Convenciones
- Nombre de archivo sugerido: `op-{slug}.md` o `runbook-{slug}.md`
- Frontmatter recomendado:
```
---
title: "{Nombre de la Tarea}"
status: draft|ready|deprecated
owner: "@usuario"
frequency: ad-hoc|daily|weekly|monthly|on-demand
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/operationalStrategy.json
  - real_structure_documentation/schemas/master_blueprint_parts/deploymentStrategy.json
---
```

## 🔗 Trazabilidad
- Enlaza `DOC028-OperationsRunbook.md` y otros DOCs técnicos.
- Si la operación impacta releases, enlaza `DOC022-ReleaseProcess.md`.

## 🧷 Archivos relacionados obligatorios (consistencia)
- Actualiza si corresponde:
  - Runbook general: `prompt-manager-lite-v/real_structure_documentation/docs/DOC028-OperationsRunbook.md`
  - Proceso de despliegue: `prompt-manager-lite-v/real_structure_documentation/docs/DOC010-Deployment.md`
  - Política de releases: `prompt-manager-lite-v/real_structure_documentation/docs/DOC022-ReleaseProcess.md`
  - Monitoreo/alertas (si aplica): `prompt-manager-lite-v/real_structure_documentation/docs/DOC025-Observability.md`
- Manifest global: `prompt-manager-lite-v/manifests/documentation_manifest.json`.
- Enlaces cruzados con `streaming_files/features/` y `streaming_files/bugs/` impactados por la operación.

## 📎 Rutas ejemplo
- Runbook nuevo: `prompt-manager-lite-v/streaming_files/operations/runbook-cache-warmup.md`
- DOCs relacionados: `prompt-manager-lite-v/real_structure_documentation/docs/DOC028-OperationsRunbook.md`
- Manifest: `prompt-manager-lite-v/manifests/documentation_manifest.json`

## 🤖 Automatización y Orquestación

### **Infrastructure as Code:**
```yaml
# automation.yaml
name: "[OPERATION_NAME]"
version: "1.0.0"
description: "[OPERATION_DESCRIPTION]"

triggers:
  - type: schedule
    cron: "0 2 * * *"  # Daily at 2 AM
  - type: event
    source: monitoring
    condition: "alert.severity == 'critical'"

steps:
  - name: "Pre-flight checks"
    type: health_check
    targets:
      - service: "[SERVICE_NAME]"
        endpoint: "/health"
        expected_status: 200
    
  - name: "Execute operation"
    type: script
    script: |
      #!/bin/bash
      [OPERATION_COMMANDS]
    timeout: 3600
    
  - name: "Validation"
    type: validation
    checks:
      - metric: "error_rate"
        operator: "<"
        value: 0.01
      - metric: "response_time_p95"
        operator: "<"
        value: 500

rollback:
  automatic: true
  conditions:
    - "step.status == 'failed'"
    - "validation.failed == true"
  script: |
    [ROLLBACK_COMMANDS]

notifications:
  - channel: slack
    webhook: "[WEBHOOK_URL]"
    events: [start, success, failure]
  - channel: pagerduty
    integration_key: "[KEY]"
    events: [failure]
```

### **Ansible Playbook Example:**
```yaml
---
- name: "[OPERATION_NAME] Playbook"
  hosts: [TARGET_HOSTS]
  become: yes
  
  vars:
    operation_id: "OP###"
    environment: "{{ env | default('staging') }}"
    
  pre_tasks:
    - name: "Create backup"
      include_role:
        name: backup
      when: environment == 'production'
      
  tasks:
    - name: "[TASK_1_NAME]"
      [MODULE_NAME]:
        [PARAMETERS]
      register: result
      
    - name: "Verify task completion"
      assert:
        that:
          - result.rc == 0
        fail_msg: "Task failed: {{ result.stderr }}"
        
  post_tasks:
    - name: "Send notification"
      uri:
        url: "{{ slack_webhook }}"
        method: POST
        body_format: json
        body:
          text: "Operation {{ operation_id }} completed"
```

## ✅ Checklist Completo de Operations

### **Pre-Operations:**
- [ ] Change request aprobado
- [ ] Maintenance window scheduled
- [ ] Stakeholders notificados
- [ ] Backup verificado
- [ ] Rollback plan documentado
- [ ] Access permissions validados

### **Durante la Operación:**
- [ ] Pre-flight checks passed
- [ ] Monitoring activo
- [ ] Communication channel abierto
- [ ] Progress tracking actualizado
- [ ] Anomalies documentadas

### **Post-Operations:**
- [ ] Validation checks completed
- [ ] Performance metrics normales
- [ ] Error rates aceptables
- [ ] User impact evaluado
- [ ] Documentation actualizada
- [ ] Post-mortem scheduled (si aplica)

### **Continuous Improvement:**
- [ ] Runbook actualizado con learnings
- [ ] Automation opportunities identificadas
- [ ] Metrics baselines actualizados
- [ ] Training needs evaluados
- [ ] Tool improvements propuestos

## 🧪 Testing y Validación

### **Testing de Runbooks:**
```bash
# 1. Dry run del runbook
./tools/runbook-executor.py dry-run OP### --verbose

# 2. Test en staging environment
./tools/runbook-executor.py test OP### \
  --env staging \
  --rollback-enabled

# 3. Chaos engineering test
./tools/chaos-runner.py test OP### \
  --scenario network-partition \
  --duration 5m

# 4. Load testing durante operación
./tools/load-tester.py run \
  --during-operation OP### \
  --rps 1000
```

### **Comandos de Validación:**
```bash
# Verificar runbook syntax
python3 tools/validate_runbook.py OP###

# Health check completo
python3 tools/health-checker.py full --verbose

# Verificar automation scripts
python3 tools/automation-validator.py OP###/automation.yaml

# Generate operation report
python3 tools/operation-reporter.py OP### --format html
```

## 🎯 Mejores Prácticas 2025

### **DO's:**
- ✅ Automatizar todo lo repetitivo
- ✅ Implementar observability desde el inicio
- ✅ Documentar cada decisión y cambio
- ✅ Practicar chaos engineering regularmente
- ✅ Mantener runbooks versionados y actualizados
- ✅ Implementar progressive rollouts
- ✅ Usar feature flags para cambios riesgosos

### **DON'Ts:**
- ❌ Ejecutar en producción sin test en staging
- ❌ Ignorar alertas o métricas anómalas
- ❌ Hacer cambios sin rollback plan
- ❌ Saltarse el change management process
- ❌ Ejecutar operaciones sin monitoring activo
- ❌ Depender de conocimiento no documentado

## 💡 Casos de Uso Comunes

### **1. Database Maintenance:**
```bash
OP001-database-backup       # Backup periódico
OP002-index-optimization    # Optimización de índices
OP003-partition-cleanup     # Limpieza de particiones
OP004-replication-setup     # Configuración de replicación
```

### **2. Infrastructure Scaling:**
```bash
OP010-horizontal-scaling    # Auto-scaling de servicios
OP011-capacity-planning     # Planificación de capacidad
OP012-resource-optimization # Optimización de recursos
```

### **3. Security Operations:**
```bash
OP020-certificate-rotation  # Rotación de certificados
OP021-secret-rotation       # Rotación de secrets
OP022-security-patching     # Aplicación de parches
```

### **4. Disaster Recovery:**
```bash
OP030-disaster-recovery     # DR drill completo
OP031-backup-restoration    # Restauración desde backup
OP032-failover-test         # Test de failover
```

## 📚 Referencias
- **Master Guide:** [MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)
- **Operations Runbook:** `real_structure_documentation/docs/DOC028-OperationsRunbook.md`
- **Deployment Guide:** `real_structure_documentation/docs/DOC010-Deployment.md`
- **Release Process:** `real_structure_documentation/docs/DOC022-ReleaseProcess.md`
- **Observability:** `real_structure_documentation/docs/DOC025-FrontendManifest.md`

---

**Última Actualización:** 2025-01-18
**Versión:** 2.0 (Enhanced para 2025 con SRE best practices)
**Próxima Revisión:** Mensual
