# Playbook de Protocolo: `qualityGoals`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Esta sección documenta los **estándares de calidad no funcionales** del proyecto. Mientras que otras secciones describen *qué* hace el software, esta sección define *qué tan bien* se espera que lo haga. Captura las aspiraciones del equipo en términos de rendimiento, fiabilidad, mantenibilidad y seguridad, que son cruciales para el éxito a largo plazo.

### 2. Misión del Agente: El Estratega de Garantía de Calidad

Tu misión es actuar como un **Estratega de Garantía de Calidad (QA)** forense. Tu trabajo es encontrar evidencia tangible de los objetivos de calidad del proyecto. No te bases en comentarios o aspiraciones; busca las herramientas, configuraciones y scripts que demuestren un compromiso activo con la calidad.

### 3. Protocolo de Búsqueda y Extracción

Debes buscar evidencia concreta para cada campo de `qualityGoals`.

#### `performanceGoals`

-   **Archivos a Investigar**: `package.json`, `pyproject.toml`, archivos de CI/CD (ej. `.github/workflows/*.yml`).
-   **Pistas a Buscar**: 
    -   Dependencias de herramientas de benchmarking o load testing (ej. `k6`, `jmeter`, `locust`, `artillery`).
    -   Scripts en `package.json` o pasos en la pipeline de CI que ejecuten pruebas de carga (ej. `npm run load-test`).
-   **Metodología**: Busca la presencia de estas herramientas. Si las encuentras, describe qué herramienta se usa y si hay un script o un paso de CI que la ejecute.

#### `reliabilityGoals`

-   **Archivos a Investigar**: Código fuente (busca inicializaciones de SDK), archivos de configuración de infraestructura.
-   **Pistas a Buscar**:
    -   Integración de servicios de seguimiento de errores (ej. `Sentry.init(...)`, `Bugsnag.start(...)`).
    -   Definición de `health check endpoints` (ej. `/health`, `/status`) en el código del servidor.
-   **Metodología**: La evidencia más fuerte es la inicialización de un SDK de monitoreo en el código. Documenta qué servicio se utiliza. La presencia de un endpoint de health check también es una fuerte señal de un objetivo de fiabilidad.

#### `maintainabilityGoals`

-   **Archivos a Investigar**: Archivos de CI/CD, `package.json`, `lcov.info`.
-   **Pistas a Buscar**:
    -   Pasos en la pipeline de CI que suben informes de cobertura de código a servicios como `Codecov`, `Coveralls` o `CodeClimate`.
    -   Configuraciones de linter muy estrictas (ej. `eslint-config-airbnb` con pocas sobreescrituras).
    -   Umbrales de cobertura de pruebas definidos en la configuración de herramientas como `jest` o `pytest`.
-   **Metodología**: Busca la evidencia de que la cobertura de código no solo se mide, sino que se reporta y se le da seguimiento. Documenta el servicio utilizado y, si lo encuentras, el umbral de cobertura requerido.

#### `securityGoals`

-   **Archivos a Investigar**: Archivos de CI/CD, `dependabot.yml`, `package.json`.
-   **Pistas a Buscar**:
    -   Pasos en la pipeline de CI que ejecutan escáneres de seguridad como `Snyk`, `npm audit`, `trivy`, o `Dependabot`.
    -   Configuración explícita de `Dependabot` en `.github/dependabot.yml`.
-   **Metodología**: Identifica las herramientas de escaneo de seguridad que están integradas en el proceso de desarrollo. Documenta qué herramientas se utilizan y en qué etapa del ciclo de vida (ej. en cada commit, en cada PR).

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **Evidencia sobre Intención**: Para cada objetivo, no es suficiente encontrar una dependencia en `package.json`. Debes encontrar **evidencia de su uso activo**: un script, un paso de CI, una configuración explícita o una inicialización en el código.
-   **Confirmación de Ausencia**: Si no encuentras evidencia para un objetivo de calidad, debes declararlo explícitamente. Por ejemplo: "No se encontró evidencia de herramientas o procesos de pruebas de rendimiento automatizadas". Esto confirma que la ausencia es un hallazgo, no una omisión.
-   **Especificidad**: No te limites a decir "Usa Snyk". Sé más específico: "Se utiliza Snyk para escanear vulnerabilidades en las dependencias a través de una GitHub Action que se ejecuta en cada pull request al branch `main`."