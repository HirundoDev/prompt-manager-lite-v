# Playbook de Protocolo: `testingStrategy`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Esta sección es el **certificado de confianza** del proyecto. Documenta las estrategias y herramientas que el equipo utiliza para verificar que el código funciona como se espera y para prevenir regresiones. Una estrategia de testing robusta es el indicador más fuerte de un proyecto maduro y mantenible.

### 2. Misión del Agente: El Ingeniero de Automatización de Pruebas

Tu misión es actuar como un **Ingeniero de Automatización de Pruebas (Test Automation Engineer)**. Debes investigar el repositorio para encontrar evidencia de las diferentes capas de la pirámide de pruebas: pruebas unitarias, de integración y de extremo a extremo (E2E). Tu trabajo es identificar las herramientas, las convenciones y los procesos que componen la red de seguridad de calidad del proyecto.

### 3. Protocolo de Búsqueda y Extracción

Debes buscar evidencia para cada capa de la estrategia de testing.

#### `unitTests`

-   **Archivos a Investigar**: Busca archivos de prueba que sigan patrones de nombrado comunes.
    -   **Patrones**: `*.test.js`, `*.spec.ts`, `test_*.py`, `*_test.go`.
    -   **Directorios**: A menudo se encuentran en un directorio `__tests__/` o junto a los archivos de código fuente que prueban.
-   **Pistas a Buscar**:
    -   `framework`: Identifícalo a partir de las dependencias (`jest`, `mocha`, `pytest`, `unittest`, `go test`).
    -   `testRunnerCommand`: Encuentra el script en `package.json` (ej. `"test": "jest"`) o el comando en un archivo de CI (ej. `pytest`).
-   **Metodología**: Cuantifica el número de archivos de prueba encontrados para dar una idea de la cobertura.

#### `integrationTests`

-   **Archivos a Investigar**: Busca directorios de prueba explícitamente nombrados como `tests/integration` o `integration-tests`.
-   **Pistas a Buscar**: Busca archivos de prueba que importen múltiples módulos de la aplicación (ej. un servicio y un modelo) o que configuren una base de datos en memoria o un mock de un servicio externo.
-   **Metodología**: La distinción entre pruebas unitarias y de integración puede ser difusa. Basa tu juicio en la complejidad de la configuración de la prueba (`beforeEach` o `setup`) y el número de componentes internos que se importan. Si no puedes distinguirlas claramente, puedes indicar que las pruebas de integración parecen estar mezcladas con las unitarias.

#### `endToEndTests`

-   **Archivos a Investigar**: Busca directorios específicos de frameworks de E2E como `cypress/`, `playwright/` o `e2e/`.
-   **Pistas a Buscar**:
    -   `framework`: Identifícalo a partir de las dependencias (`cypress`, `playwright`, `selenium`).
    -   `testRunnerCommand`: Busca el script que ejecuta estas pruebas, que a menudo es diferente del comando de pruebas unitarias (ej. `"test:e2e": "cypress run"`).
    -   **Configuración**: Busca archivos de configuración como `cypress.config.js` o `playwright.config.js`.
-   **Metodología**: Las pruebas E2E son un indicador claro de madurez. Su presencia debe ser documentada con alta prioridad.

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **Buscar en Todas las Capas**: La tarea no se considera completa hasta que hayas buscado activamente evidencia de las **tres** capas de pruebas (unitaria, integración, E2E). 
-   **Evidencia de Ejecución**: No es suficiente encontrar archivos de prueba. Debes encontrar el **comando** en `package.json` o en la configuración de CI que los ejecuta. Un conjunto de pruebas que no se ejecuta automáticamente tiene poco valor.
-   **Declaración de Ausencia**: Si no encuentras evidencia para una capa de pruebas, debes declararlo explícitamente. Por ejemplo: "No se encontró evidencia de un framework o directorio dedicado para pruebas de extremo a extremo (E2E)". Esto confirma que la ausencia es un hallazgo, no una omisión.
-   **Distinción Clara**: Debes hacer un esfuerzo razonable por distinguir entre los tipos de pruebas. Si no es posible, documenta la ambigüedad, por ejemplo: "El proyecto tiene una suite de pruebas automatizadas, pero no hay una distinción clara en la estructura de archivos entre pruebas unitarias y de integración."