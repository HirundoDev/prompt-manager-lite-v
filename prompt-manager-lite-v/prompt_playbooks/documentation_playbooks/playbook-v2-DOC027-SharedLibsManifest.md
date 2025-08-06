# Playbook v2: DOC027 - Manifiesto de Librerías Compartidas

**Objetivo:** Generar un catálogo preciso de las librerías internas compartidas, basado en la lista definida en el blueprint.

**Agente Asignado:** System Architect Agent

**Principio Fundamental:** La visibilidad de las dependencias internas es clave para la mantenibilidad. Tu rol es hacer que estas dependencias sean explícitas y comprensibles.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array `projectStructure.sharedLibraries` del `master_blueprint.json`. Cada objeto en este array representa una librería o paquete compartido.

---

## Fase 2: Generación de la Tabla de Manifiesto

Tu misión es construir el cuerpo de la tabla del manifiesto.

1.  **Inicializar Filas:** Comienza con una cadena vacía para almacenar las filas de la tabla.
2.  **Iterar sobre Librerías:** Por cada `lib` en el array `projectStructure.sharedLibraries` extraído:
    -   Formatea una nueva fila de la tabla Markdown sustituyendo los placeholders:
        `| [lib.name] | [lib.purpose] | [lib.consumers] | [lib.path] |`
    -   Añade esta nueva fila a tu cadena de filas, asegurándote de incluir un salto de línea.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC027-SharedLibsManifest.md`.
2.  **Reemplazar Contenido:** Reemplaza la fila de ejemplo `| [lib.name]... |` con la cadena completa de filas que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC027-SharedLibsManifest.md`.