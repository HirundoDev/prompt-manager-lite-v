# Guía de Usuario: `update-metadata`

## DESCRIPCIÓN

El comando `update-metadata` permite a los usuarios modificar la metadata de un artefacto existente en el proyecto. Esta funcionalidad es crucial para mantener la información de los artefactos actualizada, como el estado, la prioridad, el responsable, y más.

## ARGUMENTOS

- **`artefact_id`** (requerido): El ID único del artefacto que se desea actualizar.

## FLAGS (OPCIONALES)

- **`--tags [TAGS ...]`**: Añade o reemplaza las etiquetas del artefacto. Se pueden proporcionar múltiples etiquetas separadas por espacios.
- **`--priority PRIORITY`**: Cambia la prioridad del artefacto (ej. `high`, `medium`, `low`).
- **`--assigned-to ASSIGNED_TO`**: Asigna o reasigna el artefacto a un miembro del equipo.
- **`--estimated-hours ESTIMATED_HOURS`**: Actualiza las horas estimadas para completar el trabajo en el artefacto.
- **`--due-date DUE_DATE`**: Establece o cambia la fecha de vencimiento del artefacto (formato: `YYYY-MM-DD`).
- **`--labels [LABELS ...]`**: Añade o reemplaza las etiquetas de clasificación del artefacto.
- **`--description DESCRIPTION`**: Modifica la descripción o resumen del artefacto.

## EJEMPLOS DE USO

### Ejemplo 1: Cambiar la prioridad y el responsable de un feature

```bash
prompt-engine-cli update-metadata FTR001 --priority high --assigned-to juan.perez
```

Este comando actualiza el artefacto con ID `FTR001`, estableciendo su prioridad como `high` y asignándolo a `juan.perez`.

### Ejemplo 2: Añadir etiquetas y cambiar el estado de un bug

```bash
prompt-engine-cli update-metadata BUG002 --tags "critical ui" --status "in-progress"
```

Este comando añade las etiquetas `critical` y `ui` al artefacto `BUG002`, y actualiza su estado a `in-progress`.

### Ejemplo 3: Actualizar la descripción de una tarea

```bash
prompt-engine-cli update-metadata TASK003 --description "Implementar el nuevo sistema de caché en el backend"
```

Este comando modifica la descripción del artefacto `TASK003` para proporcionar más detalles sobre la tarea.

