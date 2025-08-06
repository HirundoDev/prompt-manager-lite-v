# Playbook de Protocolo: `deepLogicAnalysis`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Si la sección de `architecture` es el esqueleto del proyecto, `deepLogicAnalysis` es su **alma y su cerebro**. Esta sección no se trata de *qué* tecnologías se usan, sino de *por qué* y *cómo* el código resuelve un problema de negocio específico. El objetivo es decodificar la lógica de negocio implícita en el código y hacerla explícita.

### 2. Misión del Agente: El Analista de Procesos de Negocio

Tu misión es actuar como un **Analista de Procesos de Negocio y un Lector de Código Senior**. Debes trascender la sintaxis y comprender la semántica. Tu trabajo es leer el código para entender el flujo de trabajo que implementa, las reglas que hace cumplir y los algoritmos que utiliza para transformar los datos en valor.

### 3. Protocolo de Búsqueda y Extracción

Esta sección requiere más inferencia que extracción directa. Debes analizar el código en busca de patrones.

#### `coreBusinessLogic`

-   **Puntos de Partida**: Comienza en los puntos de entrada de la aplicación: controladores de API (en web), manejadores de comandos (en CLI), o componentes de UI de nivel superior.
-   **Metodología**: 
    1.  **Identifica las Acciones Clave**: Lista los nombres de las funciones en los controladores o servicios (ej. `createUser`, `processOrder`, `calculateTax`). Estos nombres son la evidencia más clara de la lógica de negocio.
    2.  **Identifica las Entidades Clave**: Analiza los nombres de los modelos de la base de datos o de las estructuras de datos principales (ej. `User`, `Product`, `Invoice`).
    3.  **Sintetiza**: Describe cómo las Acciones operan sobre las Entidades. Por ejemplo: "El sistema permite a un `Admin` (`Action`) crear un `Product` (`Entity`)."

#### `dataFlow`

-   **Metodología**: Elige uno o dos de los procesos de negocio más importantes que identificaste en el paso anterior y traza el flujo de datos de principio a fin.
    -   **Ejemplo (API Web)**: Sigue una solicitud desde el `Controller` (que recibe el DTO), al `Service` (que aplica la lógica de negocio), al `Repository` o `ORM` (que interactúa con la base de datos), y de vuelta.
    -   **Documenta las Transformaciones**: Presta especial atención a cómo cambian los datos en cada paso. ¿Se enriquecen? ¿Se validan? ¿Se agregan?

#### `keyAlgorithmsAndDataStructures`

-   **Metodología**: Escanea el código en busca de lógica que no sea trivial (es decir, que no sea un simple CRUD).
    -   **Pistas a Buscar**: Funciones con alta complejidad ciclomática, cálculos matemáticos complejos, lógica de máquina de estados (state machines), algoritmos de ordenamiento o búsqueda personalizados, o el uso de estructuras de datos no estándar (ej. grafos, árboles).
    -   **Documentación**: Si encuentras un algoritmo clave, describe su propósito, sus entradas y sus salidas en un lenguaje sencillo.

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **`coreBusinessLogic`**: La tarea no se considera completa hasta que hayas mapeado **todos** los puntos de entrada públicos (endpoints de API, comandos de CLI) a un proceso de negocio. Debes poder responder a la pregunta "¿qué hace esta aplicación?" de forma exhaustiva.
-   **`dataFlow`**: Debes haber documentado el flujo de datos de al menos **dos** de los procesos de negocio más críticos. Un solo ejemplo no es suficiente para demostrar que has entendido la dinámica del sistema.
-   **`keyAlgorithmsAndDataStructures`**: Si después de un análisis exhaustivo no encuentras algoritmos complejos, **debes declararlo explícitamente**. Tu conclusión debe ser: "Análisis completado. No se identificaron algoritmos o estructuras de datos personalizadas de alta complejidad. La aplicación se basa principalmente en operaciones estándar de manipulación de datos (CRUD)". Esto confirma que la ausencia de datos es un hallazgo, no una omisión.