# Playbook v2: DOC002 - Generación del Documento de Definición de Producto (PRD)

**Objetivo:** Generar un PRD detallado que sirva como la única fuente de verdad para el producto, alineando a todos los stakeholders.

**Agente Asignado:** Product Manager Agent

**Principio Fundamental:** Un PRD previene la ambigüedad. Actuarás como un Product Manager, traduciendo la estrategia y los requisitos del blueprint en un documento formal.

---

## Fase 1: Extracción de Datos del Blueprint

Tu primera directiva es leer y extraer los siguientes objetos del `master_blueprint.json`:

1.  `projectInfo`: (name, maintainers)
2.  `productStrategy`: (problemStatement, valueProposition, targetAudience)
3.  `qualityGoals`: (kpis, nonFunctionalRequirements)
4.  `featureManifest`: (El array completo)
5.  `visualBlueprint`: (El objeto `views`)
6.  `projectScope`: (El array `outOfScope`)

---

## Fase 2: Generación del Documento

Construirás el `DOC002-ProductDefinition.md` sección por sección.

### 1. Cabecera y Metadatos

-   Puebla el título y la tabla de metadatos con `projectInfo.name`, `projectInfo.maintainers`, y la fecha actual.

### 2. Visión General y Estrategia

-   **Declaración del Problema:** Usa `productStrategy.problemStatement`.
-   **Visión del Producto:** Usa `productStrategy.valueProposition`.

### 3. Objetivos y Métricas de Éxito (OKRs)

-   Itera sobre el array `qualityGoals.kpis`. Para cada KPI, crea una fila en la tabla con su `objective`, `metric`, y `targetValue`.

### 4. Audiencia Objetivo

-   Puebla esta sección con `productStrategy.targetAudience`.

### 5. Requisitos Funcionales

-   Itera sobre el array `featureManifest`. Para cada `feature`:
    -   Crea una sección `###` con `feature.name`.
    -   Formatea la `feature.userStory`.
    -   Crea una lista con viñetas para los `feature.acceptanceCriteria`.

### 6. Requisitos No Funcionales

-   Itera sobre `qualityGoals.nonFunctionalRequirements`. Para cada uno, crea una fila en la tabla con su `category` y `requirement`.

### 7. Diseño y UX

-   Itera sobre `visualBlueprint.views`. Para cada `view`, crea una línea con su `name` y `description`.

### 8. Fuera de Alcance

-   Crea una lista con viñetas de los elementos en `projectScope.outOfScope`.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Combina todas las secciones en un único documento.
2.  **Validar:** Asegúrate de que el lenguaje sea claro, conciso y no ambiguo.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC002-ProductDefinition.md`.