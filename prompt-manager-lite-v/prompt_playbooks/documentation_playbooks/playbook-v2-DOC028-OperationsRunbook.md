# Playbook v2: DOC028 - Runbook de Operaciones

**Objetivo:** Generar un runbook de operaciones completo y accionable, basado en los procedimientos estándar definidos en el blueprint.

**Agente Asignado:** SRE Agent

**Principio Fundamental:** La consistencia en las operaciones reduce el error humano. Tu rol es asegurar que los procedimientos documentados sean un reflejo exacto de las mejores prácticas operativas.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array `operations.runbookProcedures` del `master_blueprint.json`. Cada objeto en este array es un Procedimiento Operativo Estándar (SOP).

---

## Fase 2: Generación de los Procedimientos

Tu misión es construir el cuerpo del runbook iterando sobre los procedimientos.

1.  **Inicializar Bloque de Texto:** Comienza con una cadena vacía para almacenar todos los procedimientos generados.
2.  **Iterar sobre Procedimientos:** Por cada `procedure` en el array `operations.runbookProcedures`:
    -   Copia la estructura de un solo procedimiento de la plantilla.
    -   Reemplaza `[procedure.name]` y `[procedure.objective]`.
    -   **Iterar sobre Pasos:** Construye el bloque de pasos iterando sobre el array `procedure.steps`. Para cada `step`:
        -   Formatea la descripción y el bloque de comando del paso.
        -   Concatena los pasos para formar la secuencia completa del procedimiento.
    -   Añade el bloque del procedimiento completo a tu cadena principal, separado por `---`.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC028-OperationsRunbook.md`.
2.  **Reemplazar Contenido:** Reemplaza la sección de ejemplo del procedimiento con el bloque de texto completo que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC028-OperationsRunbook.md`.