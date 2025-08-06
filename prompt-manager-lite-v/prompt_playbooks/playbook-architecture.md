# Playbook de Protocolo: `architecture`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Esta sección es el **mapa del tesoro** del proyecto. Describe la estructura fundamental del software, cómo sus partes se conectan y las decisiones de ingeniería que le dan forma. Documentar la arquitectura es esencial para la incorporación de nuevos miembros, la planificación de nuevas características y el mantenimiento a largo plazo.

### 2. Misión del Agente: El Cartógrafo de Sistemas

Tu misión es actuar como un **Cartógrafo de Sistemas**. No estás diseñando la arquitectura, la estás descubriendo y trazando su mapa. Debes analizar la estructura de archivos, las dependencias y los puntos de entrada para crear un modelo preciso y detallado del sistema tal y como ha sido construido.

--- 

## PARTE I: El Punto de Bifurcación Crítico

### `applicationType`

Esta es la primera y más importante pieza de información que debes determinar. Define qué camino seguirás para el resto de esta sección.

-   **Archivos a Investigar**: `package.json`, `go.mod`, `requirements.txt`, `pyproject.toml`, `composer.json`, `pom.xml`.
-   **Pistas a Buscar**:
    -   **Para `webApplication`**: Busca dependencias de frameworks web (ej. `react`, `next`, `vue`, `angular`, `django`, `laravel`, `spring-boot`). Busca archivos como `index.html`, `webpack.config.js`, o scripts de `start` que ejecuten un servidor web.
    -   **Para `cliApplication`**: Busca dependencias de frameworks de CLI (ej. `commander`, `yargs`, `click`, `cobra`, `clap`). Busca archivos con un shebang (`#!/usr/bin/env node`) o una función `main` que parsea argumentos de línea de comandos.
-   **Criterio de Exhaustividad**: Debes basar tu decisión en la evidencia más fuerte. La presencia de un framework web de alto nivel (como Next.js o Django) es una señal definitiva de `webApplication`. La presencia de un framework de CLI (como Cobra o Click) es una señal definitiva de `cliApplication`. Documenta la evidencia que usaste para decidir.

--- 

## PARTE II: Protocolos Específicos

Una vez determinado el `applicationType`, sigue **SOLO UNO** de los siguientes protocolos.

### Protocolo para `webApplication`

#### `architecturePattern`
-   **Metodología**: Analiza la estructura de directorios. La presencia de un directorio `packages/` o `services/` con múltiples sub-proyectos sugiere `Monorepo` o `Microservices`. Un único directorio `src/` o `app/` grande sugiere `Monolith`.

#### `frontend`
-   **Metodología**: Busca archivos de configuración (`next.config.js`, `vue.config.js`, `angular.json`) para identificar el `framework`. Analiza `package.json` para el `dependencyManifest`. Revisa los directorios `src/state` o `src/store` para el `stateManagement`.

#### `backend`
-   **Metodología**: Busca archivos de servidor (`server.js`, `app.py`, `main.go`) para identificar el `language` y `framework`. Analiza `package.json`, `go.mod`, etc., para las dependencias.

#### `database`
-   **Metodología**: Busca archivos de configuración de ORM (`prisma/schema.prisma`, `models/`) o variables de entorno con `DATABASE_URL` para identificar el `databaseType`. Analiza los archivos de modelos o migraciones para reconstruir el `databaseSchema`.

#### `infrastructure`
-   **Metodología**: Busca archivos `Dockerfile`, `docker-compose.yml`, `*.tf` (Terraform), o archivos de configuración de CI/CD (ej. `.github/workflows/*.yml`) que contengan comandos de `aws`, `gcloud`, o `az` para describir la `deploymentInfrastructure`.

### Protocolo para `cliApplication`

#### `languageAndTooling`
-   **Metodología**: Determina el `language` a partir de la extensión de los archivos de código fuente y el `framework` a partir de los archivos de manifiesto de dependencias (`go.mod` para Cobra, `requirements.txt` para Click, etc.).

#### `commands`
-   **Metodología (Avanzada)**: Debes analizar el código fuente para encontrar dónde se definen los comandos. 
    -   En Go (Cobra): Busca llamadas a `rootCmd.AddCommand(...)` y `new cobra.Command(...)`.
    -   En Python (Click): Busca funciones decoradas con `@click.command()`.
    -   En JS (Commander): Busca llamadas a `program.command(...)`.
    -   Para cada comando encontrado, extrae su nombre, descripción, y las banderas (`flags`) asociadas, incluyendo su nombre, tipo y descripción.

#### `installCommand`
-   **Metodología**: Infiere el comando de instalación basándote en el lenguaje y el gestor de paquetes. 
    -   Go: `go install [repository_url]`
    -   Python: `pip install -e .` o `pip install [package_name]`
    -   Node.js: `npm install -g` o `npm link`

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **`applicationType`**: No puedes proceder sin tomar una decisión justificada para este campo.
-   **`webApplication`**: Debes intentar rellenar cada sub-campo (`frontend`, `backend`, etc.). Si una parte no existe (ej. un frontend estático sin backend), debes indicarlo explícitamente en la descripción de esa parte.
-   **`cliApplication`**: La sección `commands` no está completa hasta que hayas analizado **todos** los archivos de código fuente y extraído **cada** comando definido. No es suficiente con encontrar el comando raíz; debes encontrar todos los subcomandos.