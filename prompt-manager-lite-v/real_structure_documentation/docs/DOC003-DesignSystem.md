# Plantilla Maestra: Sistema de Diseño

> **Propósito:** Servir como la única fuente de verdad para el lenguaje visual y la biblioteca de componentes del proyecto, uniendo diseño e ingeniería.
> **Playbook de Referencia:** `playbook-v2-DOC003-DesignSystem.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Design Technologist Agent):
  - Tu misión es poblar esta plantilla usando las secciones `designSystem` y `componentLibrary` del `master_blueprint.json`.
  - Presenta las decisiones de diseño como "Design Tokens" semánticos (ej. `color.background.primary`).
-->

# Sistema de Diseño: [Nombre del Proyecto]

| Estado | Versión | Propietario(s) | Última Actualización |
| --- | --- | --- | --- |
| `[Live]` | `[v1.0.0]` | `[Equipo de Diseño]` | `[Fecha Actual]` |

---

## 1. Principios de Diseño

[Iterar sobre `designSystem.designPrinciples` para crear una lista con viñetas.]

## 2. Fundamentos (Design Tokens)

### 2.1. Colores

| Token | Valor (HEX) | Uso Semántico |
| --- | --- | --- |
| [Iterar sobre `designSystem.tokens.colors` para poblar la tabla] | | |

### 2.2. Tipografía

| Token | Familia / Peso | Tamaño / Altura | Uso |
| --- | --- | --- | --- |
| [Iterar sobre `designSystem.tokens.typography`] | | | |

### 2.3. Espaciado

| Token | Valor (px/rem) | Uso |
| --- | --- | --- |
| [Iterar sobre `designSystem.tokens.spacing`] | | |

### 2.4. Iconografía

-   **Biblioteca:** [Desde `designSystem.iconography.library`]
-   **Estilo:** [Desde `designSystem.iconography.style`]
-   **Enlace:** [Desde `designSystem.iconography.link`]

## 3. Biblioteca de Componentes

[Iterar sobre cada componente en `componentLibrary` para crear una sección para cada uno.]

### 3.1. [Nombre del Componente, desde `component.name`]

> [Propósito del componente, desde `component.purpose`]

**Guías de Uso:**

-   ✅ **Hacer:** [Mejor práctica, desde `component.guidelines.do`]
-   🚫 **No Hacer:** [Anti-patrón, desde `component.guidelines.dont`]

**API del Componente (Props):**

| Prop | Tipo | Requerido | Default | Descripción |
| --- | --- | --- | --- | --- |
| [Iterar sobre `component.propsSchema`] | | | | |

**Ejemplo de Código:**

```jsx
// Desde `component.codeSnippet`
```

## 4. Accesibilidad (A11y)

[Poblar con una lista de las `designSystem.accessibilityGuidelines`.]