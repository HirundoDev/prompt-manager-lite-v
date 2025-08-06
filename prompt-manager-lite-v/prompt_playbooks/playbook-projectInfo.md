# Playbook de Protocolo: `projectInfo`

**Versión 1.0**

--- 

### 1. Objetivo Filosófico

Esta sección es la **cédula de identidad** del proyecto. Contiene la información más fundamental que un humano o una máquina necesita para identificar, referenciar y comprender el propósito esencial del repositorio. La precisión y la obtención de esta información a partir de las fuentes de verdad del código son primordiales.

### 2. Misión del Agente: El Archivista Principal

Tu misión es actuar como el **Archivista Principal** del proyecto. Tu responsabilidad es examinar los metadatos y la documentación de nivel superior del repositorio para extraer con precisión su identidad fundamental. Debes ser metódico y confiar únicamente en la evidencia encontrada en los archivos de configuración y manifiestos del proyecto.

### 3. Protocolo de Búsqueda y Extracción

Debes seguir este protocolo para cada campo de `projectInfo`:

#### `projectName`

-   **Fuentes Primarias**: `package.json` (campo `name`), `pyproject.toml` (campo `name` bajo `[project]`), `pom.xml` (campo `artifactId`).
-   **Fuente Secundaria**: El primer encabezado de nivel 1 (`# `) en `README.md`.
-   **Metodología**: Busca en los archivos de manifiesto del gestor de paquetes primero. Son la fuente de verdad más fiable. Si no existen, recurre al `README.md`.

#### `projectDescription`

-   **Fuentes Primarias**: `package.json` (campo `description`), `pyproject.toml` (campo `description` bajo `[project]`), `pom.xml` (campo `description`).
-   **Fuente Secundaria**: El primer párrafo de texto después del encabezado principal en `README.md`.
-   **Metodología**: Prioriza los archivos de manifiesto. Si la descripción no existe allí, extrae el resumen del `README.md`.

#### `tags` / `keywords`

-   **Fuentes Primarias**: `package.json` (campo `keywords`), `pyproject.toml` (campo `keywords` bajo `[project]`).
-   **Metodología**: Extrae la lista de palabras clave directamente de los archivos de manifiesto. Si no existe, este campo puede dejarse vacío.

#### `repositoryUrl`

-   **Fuente Primaria**: El archivo `.git/config` (busca la URL bajo `[remote "origin"]`).
-   **Fuente Secundaria**: `package.json` (campo `repository.url`), `pyproject.toml` (campo `urls.repository` bajo `[project]`).
-   **Metodología**: El método más fiable es ejecutar el comando `git config --get remote.origin.url`. Si no es posible, analiza los archivos de manifiesto.

#### `version`

-   **Fuentes Primarias**: `package.json` (campo `version`), `pyproject.toml` (campo `version`), `__init__.py` o `__version__.py` (busca una variable `__version__`).
-   **Fuente Secundaria**: Archivos de changelog (`CHANGELOG.md`) o de releases.
-   **Metodología**: La versión casi siempre se define en un archivo de manifiesto o en un archivo de versión dedicado en el código fuente. Búscalo con alta prioridad.

--- 

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **Consistencia entre Fuentes**: La tarea no se considera completa hasta que hayas verificado la información en al menos dos fuentes si es posible (ej. `package.json` y `README.md`).
-   **Resolución de Conflictos**: Si encuentras información contradictoria (ej. un nombre en `package.json` y otro en el `README.md`), debes registrar ambas y seleccionar la del archivo de manifiesto (`package.json`, etc.) como la fuente de verdad, ya que es la que utilizan las herramientas de construcción y publicación. Debes justificar tu elección en el campo `evidence`.
-   **No Asumir**: Si una pieza de información no se puede encontrar en ninguna de las fuentes especificadas, el campo correspondiente debe dejarse vacío o nulo. No debes inventar ni inferir información que no esté explícitamente presente en el repositorio.