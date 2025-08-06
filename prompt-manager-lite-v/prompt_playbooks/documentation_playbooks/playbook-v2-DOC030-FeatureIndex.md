# Playbook v2: DOC030 - Índice de Features

**Objetivo:** Generar un índice de alto nivel, en formato de tabla, que resuma todas las funcionalidades del proyecto y su estado actual.

**Agente Asignado:** Technical Writer Agent

**Principio Fundamental:** La visibilidad del trabajo en curso es clave para la alineación del equipo. Tu misión es proporcionar una vista clara y centralizada del pipeline de desarrollo de features.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array completo `featureLifecycle` del `master_blueprint.json`.

---

## Fase 2: Generación de la Tabla de Features

Tu misión es construir el cuerpo de la tabla de features.

1.  **Inicializar Bloque de Filas:** Comienza con una cadena vacía para almacenar todas las filas de la tabla.
2.  **Iterar sobre Features:** Por cada `feature` en el array `featureLifecycle`:
    -   Crea una nueva fila de tabla en formato markdown, siguiendo la estructura `| [id] | [title] | [status] | [Ver Spec]('[specPath]') |`.
    -   Reemplaza los placeholders con los valores correspondientes de `feature.featureId`, `feature.title`, `feature.status` y `feature.specPath`.
    -   Añade esta nueva fila (con un salto de línea) a tu cadena principal.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC030-FeatureIndex.md`.
2.  **Reemplazar Contenido:** Reemplaza la fila de ejemplo de la tabla con el bloque de filas completo que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC030-FeatureIndex.md`.