# Playbook v2: DOC031 - Índice de Bugs

**Objetivo:** Generar un índice de alto nivel, en formato de tabla, que resuma todos los bugs reportados, su severidad y su estado actual.

**Agente Asignado:** Technical Writer Agent

**Principio Fundamental:** Un bug no rastreado es un bug que se repetirá. Tu misión es proporcionar una visibilidad completa y centralizada del estado de la calidad del producto.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array completo `bugLifecycle` del `master_blueprint.json`.

---

## Fase 2: Generación de la Tabla de Bugs

Tu misión es construir el cuerpo de la tabla de bugs.

1.  **Inicializar Bloque de Filas:** Comienza con una cadena vacía para almacenar todas las filas de la tabla.
2.  **Iterar sobre Bugs:** Por cada `bug` en el array `bugLifecycle`:
    -   Crea una nueva fila de tabla en formato markdown, siguiendo la estructura `| [id] | [title] | [sev] | [status] | [Ver Informe]('[path]') |`.
    -   Reemplaza los placeholders con los valores correspondientes de `bug.bugId`, `bug.title`, `bug.severity`, `bug.status` y `bug.reportPath`.
    -   Añade esta nueva fila (con un salto de línea) a tu cadena principal.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC031-BugIndex.md`.
2.  **Reemplazar Contenido:** Reemplaza la fila de ejemplo de la tabla con el bloque de filas completo que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC031-BugIndex.md`.