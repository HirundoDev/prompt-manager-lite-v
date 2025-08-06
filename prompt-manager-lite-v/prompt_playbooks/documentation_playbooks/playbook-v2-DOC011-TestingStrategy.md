# Playbook v2: DOC011 - Estrategia de Pruebas

**Objetivo:** Generar un documento completo que detalle el enfoque del proyecto hacia la calidad del software, incluyendo todos los niveles de pruebas, herramientas y procedimientos.

**Agente Asignado:** QA Agent

**Principio Fundamental:** Una estrategia de pruebas clara es la base de un producto de alta calidad. Actuarás como un Líder de QA, traduciendo el plan de pruebas del blueprint en un documento de estrategia formal.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva es leer y extraer el objeto completo `qualityAssurance` del `master_blueprint.json`. Este objeto contiene toda la información necesaria.

---

## Fase 2: Generación del Documento

Poblarás la plantilla `DOC011-TestingStrategy.md` sección por sección.

### 1. Filosofía y Objetivos

-   Puebla la `Filosofía` y los `Objetivos Clave` utilizando el objeto `qualityAssurance.testingStrategy`.

### 2. Niveles de Pruebas

-   Itera sobre el array `qualityAssurance.testingLevels`.
-   Para cada objeto en el array, genera una sección `### Pruebas de [level.name]` y puebla su propósito, herramientas y objetivo de cobertura.

### 3. Ejecución de Pruebas

-   Itera sobre el array `qualityAssurance.testExecution`.
-   Para cada objeto, genera un bloque de código con el comando para ejecutar esa suite de pruebas.

### 4. Informes de Pruebas

-   Puebla las rutas de los informes de cobertura y resultados utilizando el objeto `qualityAssurance.reporting`.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Construye el documento completo.
2.  **Validar:** Asegúrate de que todos los niveles de prueba, comandos y rutas de informes del blueprint están correctamente documentados.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC011-TestingStrategy.md`.