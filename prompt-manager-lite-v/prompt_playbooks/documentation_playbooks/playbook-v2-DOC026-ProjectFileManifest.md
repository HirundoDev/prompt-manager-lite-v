# Playbook v2: DOC026 - Manifiesto de Archivos y Directorios Críticos

**Objetivo:** Generar un mapa curado de los archivos y directorios más importantes del proyecto, basado en la lista definida en el blueprint.

**Agente Asignado:** System Architect Agent

**Principio Fundamental:** La documentación estructural debe guiar la atención a lo que es importante. Tu rol es filtrar el ruido y presentar un mapa claro del repositorio.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array `projectStructure.keyPaths` del `master_blueprint.json`. Cada objeto en este array representa un archivo o directorio crítico.

---

## Fase 2: Generación de la Tabla de Manifiesto

Tu misión es construir el cuerpo de la tabla del manifiesto.

1.  **Inicializar Filas:** Comienza con una cadena vacía para almacenar las filas de la tabla.
2.  **Iterar sobre Rutas:** Por cada `path` en el array `projectStructure.keyPaths` extraído:
    -   Formatea una nueva fila de la tabla Markdown sustituyendo los placeholders:
        `| [path.location] | [path.type] | [path.purpose] |`
    -   Añade esta nueva fila a tu cadena de filas, asegurándote de incluir un salto de línea.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC026-ProjectFileManifest.md`.
2.  **Reemplazar Contenido:** Reemplaza la fila de ejemplo `| [path.location]... |` con la cadena completa de filas que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC026-ProjectFileManifest.md`.