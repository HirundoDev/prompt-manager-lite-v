# Playbook v2: DOC003 - Sistema de Diseño

**Objetivo:** Generar una documentación exhaustiva y práctica del Sistema de Diseño que sirva como la única fuente de verdad para el lenguaje visual y la biblioteca de componentes del proyecto.

**Agente Asignado:** Design Technologist Agent

**Principio Fundamental:** Un sistema de diseño es un documento vivo que une diseño e ingeniería. Actuarás como un tecnólogo de diseño, traduciendo los tokens y contratos de componentes del blueprint en una guía de estilo clara y accionable.

---

## Fase 1: Extracción de Datos del Blueprint

Tu primera directiva es leer y extraer los siguientes objetos del `master_blueprint.json`:

1.  `designSystem`: (designPrinciples, tokens, iconography, accessibilityGuidelines)
2.  `componentLibrary`: (El array completo)

---

## Fase 2: Generación del Documento

Construirás el `DOC003-DesignSystem.md` sección por sección.

### 1. Principios de Diseño

-   Itera sobre el array `designSystem.designPrinciples` y crea una lista con viñetas.

### 2. Fundamentos (Design Tokens)

-   **Colores:** Itera sobre `designSystem.tokens.colors` para poblar la tabla con el token, valor y uso.
-   **Tipografía:** Itera sobre `designSystem.tokens.typography` para poblar la tabla.
-   **Espaciado:** Itera sobre `designSystem.tokens.spacing` para poblar la tabla.

### 3. Iconografía

-   Puebla la sección con los datos de `designSystem.iconography`.

### 4. Biblioteca de Componentes

-   Esta es la sección principal. Itera sobre cada `componente` en el array `componentLibrary`.
-   Para cada uno, crea una sección `###` con su `name`.
-   Añade su `purpose`.
-   Crea las guías de uso con `guidelines.do` y `guidelines.dont`.
-   Construye la tabla de API de props iterando sobre `propsSchema`.
-   Inserta el `codeSnippet` en el bloque de código `jsx`.

### 5. Accesibilidad (A11y)

-   Crea una lista con viñetas de los elementos en `designSystem.accessibilityGuidelines`.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Combina todas las secciones en un único documento.
2.  **Validar:** Asegúrate de que todas las tablas, listas y fragmentos de código se han generado correctamente.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC003-DesignSystem.md`.