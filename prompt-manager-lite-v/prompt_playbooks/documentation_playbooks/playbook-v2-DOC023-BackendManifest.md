# Playbook v2: DOC023 - Manifiesto del Backend

**Objetivo:** Generar un manifiesto arquitectónico preciso del backend, basado en la definición de componentes del blueprint.

**Agente Asignado:** System Architect Agent

**Principio Fundamental:** La documentación debe reflejar la arquitectura diseñada. Tu rol es actuar como un escriba técnico que traduce la visión arquitectónica en un inventario tangible.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array `backendArchitecture.components` del `master_blueprint.json`. Cada objeto en este array representa un componente clave del backend.

---

## Fase 2: Generación de la Tabla de Manifiesto

Tu misión es construir el cuerpo de la tabla del manifiesto.

1.  **Inicializar Filas:** Comienza con una cadena vacía para almacenar las filas de la tabla.
2.  **Iterar sobre Componentes:** Por cada `component` en el array `backendArchitecture.components` extraído:
    -   Formatea una nueva fila de la tabla Markdown sustituyendo los placeholders:
        `| [component.name] | [component.description] | [component.technologies] | [component.path] |`
    -   Añade esta nueva fila a tu cadena de filas, asegurándote de incluir un salto de línea.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC023-BackendManifest.md`.
2.  **Reemplazar Contenido:** Reemplaza la fila de ejemplo `| [component.name]... |` con la cadena completa de filas que generaste en la Fase 2.
3.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC023-BackendManifest.md`.