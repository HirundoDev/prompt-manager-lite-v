# Plantilla Maestra: Estrategia de Pruebas

> **Propósito:** Definir el enfoque del proyecto hacia la calidad del software, detallando los tipos de pruebas, herramientas, objetivos de cobertura y procedimientos de ejecución.
> **Playbook de Referencia:** `playbook-v2-DOC011-TestingStrategy.md`

<!-- 
  INSTRUCCIONES PARA LA IA (QA Agent):
  - Tu misión es generar y mantener este documento, asegurando que siempre refleje con precisión la `qualityAssurance` definida en el `master_blueprint.json`.
-->

## 1. Filosofía y Objetivos de Calidad

-   **Filosofía:** `[qualityAssurance.testingStrategy.philosophy]`
-   **Objetivos Clave:**
    -   `[Iterar sobre qualityAssurance.testingStrategy.goals]`

---

## 2. Niveles de Pruebas

[Iterar sobre `qualityAssurance.testingLevels` para generar las siguientes secciones]

### Pruebas de `[level.name]`

-   **Propósito:** `[level.description]`
-   **Herramientas:** `[level.tools]`
-   **Cobertura Objetivo:** `[level.coverageGoal]`

---

## 3. Ejecución de Pruebas

[Iterar sobre `qualityAssurance.testExecution` para generar los siguientes bloques de comandos]

-   **Para ejecutar `[suite.name]`:**
    ```bash
    [suite.command]
    ```

---

## 4. Informes de Pruebas

-   **Informe de Cobertura:** `[qualityAssurance.reporting.coverageReportPath]`
-   **Informe de Resultados:** `[qualityAssurance.reporting.resultsReportPath]`