# Plantilla Maestra: Documento de Definición de Producto (PRD)

> **Propósito:** Servir como la única fuente de verdad sobre qué es el producto, para quién es y por qué se está construyendo.
> **Playbook de Referencia:** `playbook-v2-DOC002-ProductDefinition.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Product Manager Agent):
  - Tu misión es poblar esta plantilla usando la información del `master_blueprint.json`.
  - El tono debe ser autoritativo, preciso y claro.
-->

# PRD: [Nombre del Proyecto, desde projectInfo.name]

| Estado | Versión | Autor(es) | Última Actualización |
| --- | --- | --- | --- |
| `[Draft]` | `[v1.0.0]` | `[Nombre del Mantenedor, desde projectInfo.maintainers]` | `[Fecha Actual]` |

---

## 1. Visión General y Estrategia

**Declaración del Problema:** [Resumen del problema que se resuelve, desde productStrategy.problemStatement]

**Visión del Producto:** [Descripción de la solución y propuesta de valor, desde productStrategy.valueProposition]

## 2. Objetivos y Métricas de Éxito (OKRs)

| Objetivo | Resultado Clave (Métrica) | Valor Objetivo |
| --- | --- | --- |
| [Objetivo de negocio/producto] | [Métrica de `qualityGoals.kpis`] | [Valor objetivo de `qualityGoals.kpis`] |

## 3. Audiencia Objetivo y User Personas

[Descripción del público objetivo, desde productStrategy.targetAudience]

## 4. Requisitos Funcionales (Features y User Stories)

[Iterar sobre `featureManifest` para crear una sección para cada feature, con sus user stories y criterios de aceptación.]

### Feature: [Nombre de la feature, desde feature.name]

- **User Story:** Como [rol], quiero [acción] para [beneficio]. (Desde `feature.userStory`)
- **Criterios de Aceptación:**
  - [Criterio 1, desde `feature.acceptanceCriteria`]
  - [Criterio 2, desde `feature.acceptanceCriteria`]

## 5. Requisitos No Funcionales

[Iterar sobre `qualityGoals.nonFunctionalRequirements` para crear una tabla.]

| Categoría | Requisito |
| --- | --- |
| [Categoría, ej. Rendimiento] | [Descripción del requisito] |

## 6. Diseño y Experiencia de Usuario (UX)

La experiencia de usuario se guiará por los principios de simplicidad y eficiencia. Para una especificación visual detallada, consultar el `visualBlueprint`.

[Iterar sobre `visualBlueprint.views` para listar las vistas clave.]

- **Vista:** `[view.name]` - [view.description]

## 7. Fuera de Alcance (Out of Scope)

Las siguientes funcionalidades se consideran explícitamente fuera del alcance para esta versión:

- [Listar elementos de `projectScope.outOfScope`]
