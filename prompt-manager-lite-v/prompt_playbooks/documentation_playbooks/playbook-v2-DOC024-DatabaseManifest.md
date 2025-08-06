# Playbook v2: DOC024 - Manifiesto de la Base de Datos

**Objetivo:** Generar un manifiesto preciso de las entidades de datos, basado en la definición del modelo de datos del blueprint.

**Agente Asignado:** Data Architect Agent

**Principio Fundamental:** La documentación debe ser un reflejo del diseño de datos. Tu rol es traducir el modelo de datos conceptual en un inventario claro.

---

## Fase 1: Extracción de Datos del Blueprint

Tu misión de extracción de datos es doble:

1.  **Extraer Entidades:** Lee y obtén el array `dataModel.entities` del `master_blueprint.json`.
2.  **Extraer Tipo de Base de Datos:** Lee y obtén el valor de `dataModel.databaseType`.

---

## Fase 2: Generación de la Tabla de Manifiesto

Tu misión es construir el cuerpo de la tabla del manifiesto.

1.  **Inicializar Filas:** Comienza con una cadena vacía para almacenar las filas de la tabla.
2.  **Iterar sobre Entidades:** Por cada `entity` en el array `dataModel.entities` extraído:
    -   Formatea una nueva fila de la tabla Markdown sustituyendo los placeholders:
        `| [entity.name] | [entity.description] | [dataModel.databaseType] | [entity.schemaPath] |`
    -   Añade esta nueva fila a tu cadena de filas, asegurándote de incluir un salto de línea.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC024-DatabaseManifest.md`.
2.  **Reemplazar Contenido:** Reemplaza la fila de ejemplo `| [entity.name]... |` con la cadena completa de filas que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC024-DatabaseManifest.md`.