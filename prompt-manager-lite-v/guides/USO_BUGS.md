# 🐛 Guía Completa de Gestión de Bugs - 2025

> **📌 REFERENCIA PRINCIPAL:** Para el contexto completo del ecosistema, consulta **[MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)** - La fuente definitiva del sistema Prompt Manager Lite V.

## 🎯 Objetivo
Estandarizar el reporte, tracking, y resolución de bugs con trazabilidad completa, métricas de calidad y mejores prácticas 2025.

## 📁 Estructura de Archivos

### **Ubicaciones Principales:**
```bash
prompt-manager-lite-v/
├── streaming_files/
│   └── bugs/
│       ├── template.md              # Template base para bugs
│       ├── manifest.json            # Manifiesto local de bugs
│       └── B###-{slug}/            # Carpetas individuales de bugs
│           ├── bug_report.md       # Reporte principal
│           ├── pendingtask.md      # Tareas pendientes
│           ├── notes.md            # Notas adicionales
│           └── assets/             # Evidencia (logs, screenshots)
├── real_structure_documentation/
│   ├── docs/
│   │   ├── DOC031-BugIndex.md     # Índice central de bugs
│   │   └── DOC011-TestingStrategy.md # Estrategia de testing
│   └── schemas/
│       └── master_blueprint_parts/
│           └── bugIndex.json       # Schema de bugs
└── tools/
    ├── verify_docs_and_schemas.py # Verificador de integridad
    └── verify_integrity.py        # Verificador estructural
```

## 🧩 Convenciones y Estándares 2025

### **Nomenclatura de Bugs:**
```bash
# Formato: B{###}-{descripcion-corta}
B001-login-failure
B002-data-corruption
B003-performance-degradation
```

### **Frontmatter Completo:**
```yaml
---
title: "[BUG_TITLE]"
bugId: "B###"
status: open|investigating|in-progress|resolved|closed|wontfix
priority: P0-critical|P1-high|P2-medium|P3-low
severity: S1-blocker|S2-major|S3-minor|S4-trivial
owner: "@[ASSIGNEE]"
reporter: "@[REPORTER]"
product: "[PRODUCT_NAME]"
component: "[COMPONENT_NAME]"
version: "[VERSION_AFFECTED]"
environment: "production|staging|development|local"
createdDate: "[YYYY-MM-DD]"
resolvedDate: "[YYYY-MM-DD]"
schemaRefs:
  - real_structure_documentation/schemas/master_blueprint_parts/bugIndex.json
  - real_structure_documentation/schemas/master_blueprint_parts/testingStrategy.json
tags:
  - regression
  - data-loss
  - security
  - performance
  - ui-ux
---
```

## 🔗 Sistema de Trazabilidad Completa

### **1. Enlaces Requeridos:**
- **DOC031-BugIndex.md** - Registro en índice central
- **DOC011-TestingStrategy.md** - Casos de prueba relacionados
- **DOC016-TroubleshootingGuide.md** - Soluciones documentadas
- **DOC020-Changelog.md** - Registro de fixes

### **2. Evidencia Obligatoria:**
```markdown
## 📎 Evidencia
- **Logs:** `assets/console-error-[TIMESTAMP].log`
- **Screenshots:** `assets/bug-screenshot-[TIMESTAMP].png`
- **Stack Traces:** `assets/stacktrace-[TIMESTAMP].txt`
- **Videos:** `assets/bug-reproduction-[TIMESTAMP].mp4`
- **Métricas:** `assets/performance-metrics-[TIMESTAMP].json`
```

### **3. Referencias Cruzadas:**
```yaml
relatedBugs:
  - B### # Bugs relacionados o duplicados
relatedFeatures:
  - F### # Features afectadas
relatedOperations:
  - O### # Operaciones impactadas
relatedProposals:
  - P### # Propuestas de solución
```

## 📝 Template Completo de Bug Report

```markdown
# Bug Report: [BUG_TITLE]

## 🔴 Resumen Ejecutivo
**Impacto:** [CRITICAL|HIGH|MEDIUM|LOW]
**Usuarios Afectados:** [NUMBER] ([PERCENTAGE]%)
**Pérdida Estimada:** $[AMOUNT] por [TIME_UNIT]
**Tiempo de Resolución Objetivo:** [HOURS] horas

## 🐛 Descripción del Bug
[DESCRIPCIÓN_DETALLADA]

## 📋 Pasos para Reproducir
1. [PASO_1]
2. [PASO_2]
3. [PASO_3]
4. [OBSERVAR_ERROR]

## ✅ Comportamiento Esperado
[QUÉ_DEBERÍA_PASAR]

## ❌ Comportamiento Actual
[QUÉ_ESTÁ_PASANDO]

## 🔍 Análisis de Causa Raíz
### Investigación Inicial
- [ ] Logs revisados
- [ ] Métricas analizadas
- [ ] Código inspeccionado
- [ ] Tests ejecutados

### Causa Identificada
[CAUSA_RAÍZ_DETALLADA]

## 🛠️ Solución Propuesta
### Opción 1: [SOLUCIÓN_RÁPIDA]
- **Pros:** [VENTAJAS]
- **Contras:** [DESVENTAJAS]
- **Tiempo:** [HORAS]

### Opción 2: [SOLUCIÓN_COMPLETA]
- **Pros:** [VENTAJAS]
- **Contras:** [DESVENTAJAS]
- **Tiempo:** [DÍAS]

## 📊 Métricas de Calidad
- **MTTR (Mean Time To Resolve):** [HOURS]
- **Recurrencia:** [YES/NO]
- **Regresión:** [YES/NO]
- **Test Coverage Pre-Fix:** [PERCENTAGE]%
- **Test Coverage Post-Fix:** [PERCENTAGE]%

## 🔄 Plan de Acción
1. **Inmediato:** [MITIGACIÓN]
2. **Corto Plazo:** [FIX_TEMPORAL]
3. **Largo Plazo:** [SOLUCIÓN_PERMANENTE]

## ✔️ Criterios de Aceptación
- [ ] Bug no reproducible en [ENVIRONMENT]
- [ ] Tests automatizados agregados
- [ ] Documentación actualizada
- [ ] Code review aprobado
- [ ] QA validación completa
```

## 🔄 Workflow Completo de Gestión de Bugs

### **FASE 1: Detección y Reporte**
```bash
# 1. Crear carpeta del bug
mkdir -p streaming_files/bugs/B###-{descripcion}/

# 2. Copiar template
cp streaming_files/bugs/template.md streaming_files/bugs/B###-{descripcion}/bug_report.md

# 3. Llenar información del bug
# Editar bug_report.md con todos los detalles

# 4. Agregar evidencia
cp /path/to/logs streaming_files/bugs/B###-{descripcion}/assets/
cp /path/to/screenshots streaming_files/bugs/B###-{descripcion}/assets/
```

### **FASE 2: Investigación**
```bash
# 1. Actualizar status
status: "investigating"

# 2. Documentar análisis
# Agregar findings en notes.md

# 3. Identificar causa raíz
# Actualizar sección de RCA en bug_report.md
```

### **FASE 3: Resolución**
```bash
# 1. Implementar fix
# Código + tests

# 2. Actualizar documentación
# DOC031-BugIndex.md
# DOC016-TroubleshootingGuide.md

# 3. Cerrar bug
status: "resolved"
resolvedDate: "[YYYY-MM-DD]"
```

### **FASE 4: Verificación Post-Fix**
```bash
# 1. Ejecutar verificadores
python3 tools/verify_docs_and_schemas.py
python3 tools/verify_integrity.py

# 2. Validar en producción
# Monitorear métricas por 24-48 horas

# 3. Cerrar definitivamente
status: "closed"
```

## 📊 Métricas y KPIs de Bugs

### **Métricas Clave:**
```yaml
# SLA por Severidad
P0_Critical:
  detection_to_acknowledgment: 15min
  acknowledgment_to_mitigation: 1h
  mitigation_to_resolution: 4h
  
P1_High:
  detection_to_acknowledgment: 1h
  acknowledgment_to_mitigation: 4h
  mitigation_to_resolution: 24h
  
P2_Medium:
  detection_to_acknowledgment: 4h
  acknowledgment_to_mitigation: 24h
  mitigation_to_resolution: 72h
  
P3_Low:
  detection_to_acknowledgment: 24h
  acknowledgment_to_mitigation: 72h
  mitigation_to_resolution: 1week
```

### **Dashboard de Bugs:**
```markdown
## 📈 Bug Metrics Dashboard

### Current Status
- **Open Bugs:** [TOTAL]
  - P0: [COUNT]
  - P1: [COUNT]
  - P2: [COUNT]
  - P3: [COUNT]

### Trends (Last 30 days)
- **New Bugs:** [COUNT]
- **Resolved:** [COUNT]
- **Reopened:** [COUNT]
- **MTTR:** [HOURS]

### Quality Metrics
- **Escape Rate:** [PERCENTAGE]%
- **Regression Rate:** [PERCENTAGE]%
- **First-Time Fix Rate:** [PERCENTAGE]%
```

## ✅ Checklist Completo de Validación

### **Pre-Reporte:**
- [ ] Bug reproducible consistentemente
- [ ] Búsqueda de duplicados realizada
- [ ] Severidad correctamente asignada
- [ ] Componente afectado identificado

### **Reporte:**
- [ ] Título descriptivo y único
- [ ] Pasos de reproducción claros
- [ ] Resultado esperado vs actual documentado
- [ ] Evidencia adjunta (logs, screenshots)
- [ ] Impacto en usuarios cuantificado
- [ ] SchemaRefs agregados correctamente

### **Investigación:**
- [ ] Logs del sistema analizados
- [ ] Código fuente revisado
- [ ] Tests de regresión ejecutados
- [ ] Causa raíz identificada
- [ ] Solución propuesta documentada

### **Resolución:**
- [ ] Fix implementado y testeado
- [ ] Code review completado
- [ ] Tests automatizados agregados
- [ ] Documentación actualizada
- [ ] DOC031-BugIndex.md actualizado

### **Post-Fix:**
- [ ] Validación en staging
- [ ] Deployment a producción
- [ ] Monitoreo post-deployment (24h)
- [ ] Retrospectiva documentada
- [ ] Lecciones aprendidas capturadas

## 🧪 Verificación y Validación

### **Comandos de Verificación:**
```bash
# 1. Verificar integridad de documentación
python3 tools/verify_docs_and_schemas.py

# 2. Verificar estructura
python3 tools/verify_integrity.py

# 3. Validar bug específico
python3 tools/validate_bug.py B###

# 4. Generar reporte de bugs
python3 tools/generate_bug_report.py --last-30-days
```

### **Automatización con CI/CD:**
```yaml
# .github/workflows/bug-validation.yml
name: Bug Validation
on:
  push:
    paths:
      - 'streaming_files/bugs/**'
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate Bug Reports
        run: |
          python3 tools/verify_docs_and_schemas.py
          python3 tools/verify_integrity.py
```

## 🎯 Mejores Prácticas 2025

### **DO's:**
- ✅ Usar IDs secuenciales (B001, B002, ...)
- ✅ Incluir evidencia visual siempre que sea posible
- ✅ Documentar workarounds mientras se resuelve
- ✅ Hacer post-mortems para bugs P0/P1
- ✅ Mantener trazabilidad completa

### **DON'Ts:**
- ❌ Cerrar bugs sin validación en producción
- ❌ Omitir tests de regresión
- ❌ Ignorar bugs de baja prioridad indefinidamente
- ❌ Duplicar bugs sin verificar el índice
- ❌ Resolver sin actualizar documentación

## 📚 Referencias
- **Master Guide:** [MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)
- **Bug Index:** `real_structure_documentation/docs/DOC031-BugIndex.md`
- **Testing Strategy:** `real_structure_documentation/docs/DOC011-TestingStrategy.md`
- **Troubleshooting:** `real_structure_documentation/docs/DOC016-TroubleshootingGuide.md`

---

**Última Actualización:** 2025-01-18
**Versión:** 2.0 (Enhanced para 2025)
**Próxima Revisión:** Mensual
