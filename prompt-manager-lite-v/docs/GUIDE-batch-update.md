# Guía de Usuario: `batch-update`

## DESCRIPCIÓN

El comando `batch-update` permite realizar actualizaciones masivas en múltiples artefactos que coinciden con un conjunto de criterios de filtrado. Es una herramienta poderosa para la gestión de proyectos grandes, permitiendo cambios de estado, asignaciones y otras modificaciones de metadata en lote.

## FLAGS DE FILTRADO (REQUERIDOS AL MENOS UNO)

- **`--filter-query QUERY`**: Busca artefactos cuyo ID o resumen contengan el `QUERY` especificado.
- **`--filter-status STATUS`**: Selecciona artefactos que tengan un `STATUS` específico (ej. `open`, `in-progress`, `completed`).
- **`--filter-type TYPE`**: Filtra artefactos por su `TYPE` (ej. `FEATURE`, `BUG`, `TASK`, `IDEA`).
- **`--filter-tags [TAGS ...]`**: Selecciona artefactos que contengan **todas** las etiquetas especificadas.

## FLAGS DE ACTUALIZACIÓN (REQUERIDOS AL MENOS UNO)

- **`--update-tags [TAGS ...]`**: Añade o reemplaza las etiquetas de los artefactos seleccionados.
- **`--update-priority PRIORITY`**: Cambia la prioridad de los artefactos seleccionados.
- **`--update-assigned-to ASSIGNED_TO`**: Asigna o reasigna los artefactos seleccionados a un miembro del equipo.
- **`--update-estimated-hours ESTIMATED_HOURS`**: Actualiza las horas estimadas de los artefactos seleccionados.
- **`--update-due-date DUE_DATE`**: Establece o cambia la fecha de vencimiento de los artefactos seleccionados.
- **`--update-labels [LABELS ...]`**: Añade o reemplaza las etiquetas de clasificación de los artefactos seleccionados.
- **`--update-description DESCRIPTION`**: Modifica la descripción de los artefactos seleccionados.

## EJEMPLOS DE USO

### Ejemplo 1: Asignar todos los bugs abiertos a un desarrollador

```bash
prompt-engine-cli batch-update --filter-type BUG --filter-status open --update-assigned-to juan.perez
```

Este comando busca todos los artefactos de tipo `BUG` con estado `open` y los asigna a `juan.perez`.

### Ejemplo 2: Marcar todas las tareas de un sprint como completadas

```bash
prompt-engine-cli batch-update --filter-tags "sprint-5" --update-status completed
```

Este comando encuentra todos los artefactos con la etiqueta `sprint-5` y cambia su estado a `completed`.

### Ejemplo 3: Aumentar la prioridad de todos los features críticos

```bash
prompt-engine-cli batch-update --filter-type FEATURE --filter-tags "critical" --update-priority high
```

Este comando busca todos los `FEATURE` con la etiqueta `critical` y les asigna una prioridad `high`.

