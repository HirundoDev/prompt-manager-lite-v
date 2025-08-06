# Playbook de Protocolo: `dependencies`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Esta sección es el **inventario de la cadena de suministro** del proyecto. Documenta todas las bibliotecas y herramientas de terceros sobre las que se construye el software. Una lista precisa y completa es fundamental para la seguridad, la reproducibilidad de los builds, la gestión de licencias y la comprensión del ecosistema tecnológico del proyecto.

### 2. Misión del Agente: El Gerente de la Cadena de Suministro

Tu misión es actuar como un **Gerente de la Cadena de Suministro** meticuloso. Tu única responsabilidad es localizar el manifiesto de dependencias del proyecto y transcribir su contenido con una precisión del 100%. No hay lugar para la inferencia o la interpretación; la exactitud de los nombres y las versiones es primordial.

### 3. Protocolo de Búsqueda y Extracción

#### Paso 1: Identificar el Manifiesto de Dependencias

-   **Metodología**: Primero, determina el lenguaje principal del proyecto para saber qué archivo buscar. Los archivos más comunes son:
    -   **Node.js/JavaScript/TypeScript**: `package.json`
    -   **Python**: `requirements.txt`, `pyproject.toml` (bajo `[project.dependencies]` y `[project.optional-dependencies]`), `Pipfile`
    -   **Go**: `go.mod`
    -   **Java (Maven)**: `pom.xml`
    -   **Java (Gradle)**: `build.gradle`
    -   **PHP**: `composer.json`
    -   **Ruby**: `Gemfile`

#### Paso 2: Extraer y Categorizar las Dependencias

-   **Metodología**: Una vez localizado el archivo, debes analizar su contenido y extraer cada dependencia, asegurándote de capturar la siguiente información:
    -   `name`: El nombre oficial del paquete (ej. `react`, `requests`, `cobra`).
    -   `version`: La cadena de versión exacta especificada en el manifiesto (ej. `^18.2.0`, `~=1.1.1`, `>2.0`).
    -   `type`: La categoría de la dependencia. Esto es crucial.
        -   **`production`**: Dependencias necesarias para que la aplicación se ejecute en producción. En `package.json`, estas se encuentran en la sección `"dependencies"`.
        -   **`development`**: Dependencias utilizadas solo para el desarrollo, como pruebas, linters, o herramientas de build. En `package.json`, estas se encuentran en la sección `"devDependencies"`.
        -   (Otros ecosistemas pueden tener nombres diferentes, como `require-dev` en Composer o grupos de dependencias opcionales en `pyproject.toml`. Debes mapearlos a `production` o `development` según corresponda).

#### Paso 3: Notar la Presencia de un Archivo de Bloqueo (Lock File)

-   **Metodología**: Busca la existencia de un archivo de bloqueo asociado al manifiesto. 
    -   **Ejemplos**: `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `poetry.lock`, `Pipfile.lock`, `composer.lock`.
    -   **Acción**: Si encuentras un archivo de bloqueo, simplemente añade una nota en la descripción general de la sección `dependencies` que diga: `"Se detectó un archivo de bloqueo (ej. package-lock.json), lo que garantiza builds reproducibles."` No necesitas analizar el contenido del archivo de bloqueo.

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **Totalidad Absoluta**: La tarea no se considera completa hasta que hayas extraído **TODAS** las dependencias de **TODAS** las secciones relevantes del manifiesto (ej. `dependencies` Y `devDependencies`). Omitir una sola dependencia es un fallo.
-   **Precisión Literal**: El nombre y la cadena de versión de cada dependencia deben ser transcritos **literalmente** como aparecen en el archivo. No intentes resolver las versiones semánticas (semver) ni normalizar los nombres.
-   **Categorización Obligatoria**: Cada dependencia **debe** ser categorizada como `production` o `development`. Si el manifiesto no hace una distinción, todas las dependencias se considerarán de `production`, pero debes anotar este hecho.