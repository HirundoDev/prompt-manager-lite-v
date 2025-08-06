# Plantilla Maestra: Referencia de Comandos de la CLI

> **Propósito:** Proporcionar una referencia completa y clara para todos los comandos de la interfaz de línea de comandos (CLI) disponibles en el proyecto.
> **Playbook de Referencia:** `playbook-v2-DOC019-CLI-Command-Reference.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Technical Scribe Agent):
  - Tu misión es generar este documento iterando sobre el array `cliReference` en el `master_blueprint.json`.
  - Para cada objeto en el array, genera una sección de comando completa como se detalla a continuación.
-->

## Referencia de Comandos CLI

- [Guía de `update-metadata`](./GUIDE-update-metadata.md)
- [Guía de `update-content`](./GUIDE-update-content.md)
- [Guía de `batch-update`](./GUIDE-batch-update.md)

## `[command.name]`

-   **Descripción:** `[command.description]`

-   **Uso:**
    ```bash
    [cli_name] [command.name] [argumentos] [opciones]
    ```

-   **Argumentos:**
    -   `[Iterar sobre command.arguments]`: `[argument.name]` (`[argument.type]`) - `[argument.description]`

-   **Opciones (Flags):**
    -   `[Iterar sobre command.options]`: `[option.flag]`, `[option.longFlag]` (`[option.type]`, por defecto: `[option.default]`) - `[option.description]`

-   **Ejemplo:**
    ```bash
    # [command.example.description]
    [cli_name] [command.example.usage]
    ```

---
