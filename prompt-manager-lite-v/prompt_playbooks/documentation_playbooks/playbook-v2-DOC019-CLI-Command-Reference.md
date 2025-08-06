# Playbook v2: DOC019 - Referencia de Comandos de la CLI

**Objetivo:** Generar una referencia de comandos de la CLI completa y profesional a partir de los datos estructurados en el blueprint.

**Agente Asignado:** Technical Scribe Agent

**Principio Fundamental:** La documentación de la CLI debe ser un reflejo exacto de su implementación. Actuarás como un generador de documentación técnica, traduciendo la definición de la CLI en una guía para el usuario.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el array `cliReference` del `master_blueprint.json`. Cada objeto en este array representa un comando completo.

---

## Fase 2: Generación del Documento

Tu misión es iterar sobre el array `cliReference` y, para cada objeto `command`, generar una sección completa en el documento `DOC019-CLI-Command-Reference.md`.

1.  **Bucle Principal:** Por cada `command` en `cliReference`:
    -   Copia la estructura de la plantilla para un solo comando.
    -   Rellena el `command.name` y `command.description`.
    -   **Argumentos:** Si `command.arguments` existe, itera sobre él y genera una línea por cada argumento.
    -   **Opciones:** Si `command.options` existe, itera sobre él y genera una línea por cada opción.
    -   **Ejemplo:** Rellena la descripción y el uso del ejemplo desde `command.example`.

---

## Fase 3: Ensamblaje Final

1.  **Concatenar Secciones:** Une todas las secciones de comandos generadas en un solo bloque de texto.
2.  **Leer Plantilla:** Carga la plantilla `DOC019-CLI-Command-Reference.md`.
3.  **Reemplazar Contenido:** Reemplaza la sección de ejemplo de la plantilla con el bloque de texto completo que generaste.
4.  **Escribir Archivo:** Escribe el contenido final y completo en `DOC019-CLI-Command-Reference.md`.