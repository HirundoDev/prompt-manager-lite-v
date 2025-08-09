---
title: "{Nombre de la Operación/Runbook}"
status: draft|ready|deprecated
owner: "@usuario"
frequency: ad-hoc|daily|weekly|monthly|on-demand
schemaRefs:
  - schemas/master_blueprint_parts/operationalStrategy.json
  - schemas/master_blueprint_parts/deploymentStrategy.json
---

# TASK: {{task_title}}

**ID de Tarea:** {{task_id}}  
**Fecha de Creación:** {{creation_date}}  
**Prioridad:** {{priority}}  
**Estado:** En Progreso  

## Descripción

{{task_description}}

## Objetivos

- [ ] Objetivo principal a completar
- [ ] Objetivo secundario
- [ ] Criterios de aceptación específicos

## Contexto Técnico

**Módulos Afectados:**
- Módulo/componente relevante

**Dependencias:**
- Dependencias técnicas o de otros artefactos

## Plan de Implementación

### Fase 1: Análisis
- Análisis de requisitos
- Revisión de arquitectura existente

### Fase 2: Desarrollo
- Implementación de funcionalidad
- Pruebas unitarias

### Fase 3: Validación
- Pruebas de integración
- Verificación de calidad

## Notas de Implementación

Consideraciones técnicas específicas y notas del desarrollador.

## Enlaces Relacionados

- Enlaces a documentación relevante
- Referencias a otros artefactos del proyecto

---

## Archivos Relacionados / Actualizaciones Requeridas

- Actualiza si corresponde (rutas relativas a `prompt-manager-lite-v/`):
  - `docs/DOC028-OperationsRunbook.md`
  - `docs/DOC010-Deployment.md`
  - `docs/DOC022-ReleaseProcess.md`
  - `docs/DOC025-Observability.md` (si aplica)
- Manifest global: `manifests/documentation_manifest.json` (agregar/ajustar entrada si procede).
- Enlaces cruzados: `features/`, `bugs/` impactados.

## Verificación

```bash
python3 tools/verify_docs_and_schemas.py
python3 tools/verify_integrity.py
```
