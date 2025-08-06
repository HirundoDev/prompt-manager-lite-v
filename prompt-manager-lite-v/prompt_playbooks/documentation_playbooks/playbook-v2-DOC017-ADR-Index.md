# Playbook v2: DOC017 - Índice Automatizado de ADRs

**Objetivo:** Mantener un índice de Registros de Decisiones de Arquitectura (ADR) preciso y actualizado de forma totalmente automática.

**Agente Asignado:** Technical Scribe Agent

**Principio Fundamental:** El sistema de archivos es la única fuente de verdad. El índice de ADRs debe ser un reflejo directo de los archivos de decisión existentes, eliminando la necesidad de mantenimiento manual.

---

## Fase 1: Escaneo y Extracción de Datos

Tu misión es actuar como un indexador de archivos inteligente.

1.  **Escanear Directorio:** Realiza un listado de todos los archivos en el directorio `prompt_docs/adrs/`.
2.  **Filtrar Archivos:** Ignora cualquier archivo que se llame `template-ADR.md` o que no termine en `.md`.
3.  **Procesar cada ADR:** Para cada archivo de ADR encontrado:
    -   **Leer Contenido:** Lee las primeras líneas del archivo para extraer metadatos.
    -   **Extraer Título:** Parsea el título de la primera línea (ej. `# ADR-XXXX: [Título de la Decisión]` -> `[Título de la Decisión]`)
    -   **Extraer Fecha:** Parsea la fecha de la línea que comienza con `- **Fecha:**`.
    -   **Extraer Estado:** Parsea el estado de la línea que comienza con `- **Estado:**`.
    -   **Almacenar Datos:** Guarda el nombre del archivo, el título, la fecha y el estado en una lista estructurada.

---

## Fase 2: Generación de la Tabla del Índice

1.  **Ordenar ADRs:** Ordena la lista de ADRs que recopilaste, preferiblemente por el número en el nombre del archivo.
2.  **Construir Tabla Markdown:** Genera una tabla Markdown con las columnas `ADR`, `Título de la Decisión`, `Fecha` y `Estado`.
3.  **Poblar Filas:** Por cada ADR en tu lista ordenada, añade una nueva fila a la tabla. La columna `ADR` debe contener un enlace Markdown al archivo correspondiente (ej. `[ADR-0001](./adrs/ADR-0001.md)`).

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga la plantilla `DOC017-ADR-Index.md`.
2.  **Reemplazar Contenido:** Reemplaza la tabla de ejemplo en la plantilla con la tabla recién generada.
3.  **Escribir Archivo:** Escribe el contenido final y actualizado de vuelta en `DOC017-ADR-Index.md`.