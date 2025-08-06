# Playbook de Protocolo: `projectManagement`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Esta sección documenta el **sistema nervioso** del proyecto: los procesos, rituales y herramientas que el equipo utiliza para colaborar de manera efectiva. Capturar esta información es vital para que cualquier nuevo contribuyente (humano o IA) pueda entender el flujo de trabajo, las normas de calidad y cómo proponer cambios de forma segura y predecible.

### 2. Misión del Agente: El Antropólogo de Desarrollo

Tu misión es actuar como un **Antropólogo de Desarrollo**. Debes observar el comportamiento del equipo a través de los artefactos que dejan en el repositorio. Tu objetivo es deducir y documentar sus prácticas de trabajo, no por lo que dicen, sino por lo que hacen y las herramientas que configuran. La evidencia tangible es tu única fuente de verdad.

### 3. Protocolo de Búsqueda y Extracción

Debes seguir este protocolo para cada campo de `projectManagement`:

#### `workTrackingSystem`

-   **Archivos a Investigar**: `README.md`, `CONTRIBUTING.md`, `docs/**/*.md`.
-   **Patrones de Búsqueda**: Busca menciones explícitas o URLs que contengan palabras clave como `jira`, `trello`, `asana`, `linear`, `youtrack`, o referencias a `GitHub Issues`.
-   **Metodología**: Realiza una búsqueda de texto en todos los archivos de documentación. Si encuentras una URL, extráela. Si encuentras una mención (ej. "Gestionamos las tareas en Jira"), regístrala. Si no encuentras nada, indica que se usan `GitHub Issues` por defecto o que es desconocido.

#### `branchingStrategy`

-   **Fuente Primaria**: El archivo `CONTRIBUTING.md`. Busca secciones tituladas "Branching Model", "Our Workflow", "Cómo Contribuir".
-   **Fuente Secundaria (Inferencial)**: Ejecuta el comando `git branch -r` para listar las ramas remotas. Analiza los nombres de las últimas 20-50 ramas.
-   **Metodología**: Primero, busca la estrategia documentada. Si no existe, debes inferirla. Patrones a buscar en los nombres de las ramas:
    -   `feature/...`, `fix/...`, `release/...`, `hotfix/...` sugiere **GitFlow**.
    -   `[TICKET-123]-feature-name` sugiere una integración con un sistema de tickets.
    -   Nombres de ramas descriptivos sin prefijos sugieren un **Feature Branch Workflow** simple.

#### `codingStandards`

-   **Archivos a Investigar**: Busca la existencia de archivos de configuración de linters y formateadores. Los más comunes son:
    -   JavaScript/TypeScript: `.eslintrc.json`, `.eslintrc.js`, `.prettierrc`, `prettier.config.js`
    -   Python: `pyproject.toml` (buscando secciones de `[tool.ruff]`, `[tool.black]`, `[tool.isort]`), `.flake8`
    -   General: `.editorconfig`
-   **Metodología**: Tu objetivo es identificar las herramientas utilizadas. Extrae los nombres de las herramientas (ESLint, Prettier, Ruff, Black) y, si es posible, el estándar base que extienden (ej. `eslint-config-airbnb`).

#### `pullRequestTemplate`

-   **Archivos a Investigar**: Busca un archivo con el nombre `PULL_REQUEST_TEMPLATE.md` o `pull_request_template.md`.
-   **Directorios a Buscar**: Comprueba en el directorio raíz, en el directorio `.github/`, y en el directorio `docs/`.
-   **Metodología**: Si encuentras el archivo, lee su contenido para entender las secciones que los desarrolladores deben rellenar (ej. "Descripción del Cambio", "Cómo se ha probado", "Checklist"). Resume estas secciones en tu descripción.

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **`workTrackingSystem`**: La tarea no está completa hasta que hayas escaneado todos los archivos `.md` en la raíz, `docs/`, y `.github/` en busca de las palabras clave.
-   **`branchingStrategy`**: Si no encuentras una estrategia documentada, **debes** realizar el análisis inferencial de los nombres de las ramas. No puedes simplemente indicar que es "desconocido" sin haber intentado la inferencia.
-   **`codingStandards`**: No es suficiente encontrar una mención a un estándar. Debes encontrar el **archivo de configuración** real que lo implementa. La ausencia del archivo es la prueba de que no se aplica de forma automatizada.
-   **`pullRequestTemplate`**: Debes verificar las tres ubicaciones canónicas (raíz, `.github/`, `docs/`) antes de concluir que no existe una plantilla de PR.