# Playbook de Protocolo: `designSystem`

**Versión 1.0**

--- 

### 1. Objetivo Filosófico

Esta sección del `master_blueprint` no es una simple lista de estilos; es el **ADN visual y de interacción** del proyecto. Su propósito es realizar una ingeniería inversa del lenguaje de diseño de una aplicación para crear una representación estructurada, explícita y completa. El objetivo final es que esta sección sirva como una fuente de verdad única para desarrolladores, diseñadores y futuros agentes de IA, permitiendo la consistencia, el mantenimiento y la evolución del sistema de diseño.

### 2. Misión del Agente: El Arqueólogo Visual

Tu misión, como agente responsable de rellenar esta sección, es actuar como un **Arqueólogo Visual y un Ingeniero Forense de UI**. No eres un diseñador, eres un detective. Tu trabajo consiste en excavar en la base del código, analizar los artefactos de estilo y de componentes, y reconstruir meticulosamente el sistema de diseño tal y como existe en la realidad. La exhaustividad es tu principal directiva. No debes dejar ninguna piedra sin remover.

### 3. Protocolo de Búsqueda y Extracción

Debes seguir este protocolo para cada sub-sección de `designSystem`:

#### `colorPalette`

-   **Archivos a Investigar**: Busca en todos los archivos con extensiones `.css`, `.scss`, `.sass`, `.less`, `tailwind.config.js`, `.js`, `.ts`, `.jsx`, `.tsx`.
-   **Patrones de Búsqueda (Regex)**:
    -   Códigos Hex: `/#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})/g`
    -   Valores RGB/RGBA: `/rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(,\s*[0-9.]+\s*)?\)/g`
    -   Valores HSL/HSLA: `/hsla?\(\s*\d+\s*,\s*\d+%?\s*,\s*\d+%?\s*(,\s*[0-9.]+\s*)?\)/g`
    -   Variables CSS: `/--[\w-]+:\s*[^;]+/g`
-   **Metodología**: Itera sobre todos los archivos de estilo. Extrae cada definición de color única. Si encuentras variables de color (ej. `--color-primary`), extrae tanto la variable como su valor resuelto. Para el campo `usage`, analiza el selector CSS donde se define el color para inferir su propósito (ej. `.button-primary`, `body`, `.card-header`).

#### `typography`

-   **Archivos a Investigar**: Principalmente archivos de estilo (`.css`, `.scss`, etc.).
-   **Propiedades a Buscar**: `font-family`, `font-size`, `font-weight`, `line-height`, `letter-spacing`.
-   **Metodología**: Identifica todas las reglas CSS que definen tipografía. Agrupa las propiedades que se aplican a selectores comunes (ej. `h1`, `h2`, `p`, `.body-text`) para crear una entrada en el array `typography`. El campo `name` debe ser descriptivo (ej. 'Heading 1'), y el `usage` debe listar los selectores donde se aplica.

#### `spacingScale`

-   **Archivos a Investigar**: Archivos de estilo y archivos de configuración de frameworks (ej. `tailwind.config.js`).
-   **Propiedades a Buscar**: `margin`, `padding`, `gap`, y variables CSS relacionadas con el espaciado (ej. `--spacing-sm`).
-   **Metodología**: Busca todos los valores únicos utilizados para el espaciado en la aplicación. Presta especial atención a las variables CSS o a las escalas de espaciado definidas en archivos de configuración. El objetivo es reconstruir la escala de espaciado del proyecto (ej. 8px, 16px, 24px).

#### `components`

-   **Archivos a Investigar**: Archivos de componentes (`.jsx`, `.tsx`, `.vue`, `.svelte`).
-   **Metodología (Avanzada)**:
    1.  **Análisis de Árbol de Sintaxis Abstracto (AST)**: Este es el método preferido. Utiliza un parser de JavaScript/TypeScript (como Babel o Acorn) para analizar los archivos de componentes.
    2.  **Identificar Exportaciones**: Busca todas las declaraciones `export default` o `export const` que definan un componente de UI (generalmente una función que devuelve JSX/HTML o un objeto de clase).
    3.  **Extraer `componentName`**: El nombre de la función o clase exportada.
    4.  **Extraer `filePath`**: La ruta relativa al archivo del componente.
    5.  **Extraer `props`**: Analiza las `propTypes` o la definición de tipos de TypeScript para la función del componente. Itera sobre cada prop para extraer su `name`, `type`, `isRequired`, y `description` (a menudo disponible en comentarios JSDoc). 
    6.  **Extraer `dependencies`**: Analiza las declaraciones `import` dentro del archivo para identificar otros componentes que este utiliza.

--- 

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

Un agente **NO** debe considerar completa la tarea de rellenar una sub-sección hasta que se cumplan estas condiciones:

-   **`colorPalette`**: Has analizado **TODOS** los archivos de estilo y has extraído **CADA** definición de color única. La tarea solo termina cuando una nueva búsqueda con los patrones no revela nuevos colores.
-   **`typography`**: Has identificado y agrupado **TODAS** las familias tipográficas y combinaciones de tamaño/peso utilizadas en la aplicación. No es suficiente con encontrar una; debes encontrar todas las variaciones.
-   **`spacingScale`**: Has extraído **TODOS** los valores de espaciado recurrentes para reconstruir la escala completa. Si un framework como Tailwind está en uso, debes extraer la escala completa de su configuración.
-   **`components`**: Has analizado **TODOS** los archivos en los directorios de componentes (`/components`, `/src/ui`, etc.) y has creado una entrada para **CADA** componente exportado. La tarea solo finaliza cuando no quedan archivos de componentes por analizar.