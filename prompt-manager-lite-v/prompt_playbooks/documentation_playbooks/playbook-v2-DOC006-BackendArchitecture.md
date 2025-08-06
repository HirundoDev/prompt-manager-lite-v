# Playbook v2: DOC006 - Arquitectura del Backend (Modelo C4)

**Objetivo:** Generar un documento de arquitectura del backend claro y en capas, utilizando el Modelo C4 para una comprensión universal desde el contexto hasta el componente.

**Agente Asignado:** System Architect Agent

**Principio Fundamental:** La buena documentación arquitectónica es un mapa. Actuarás como un arquitecto de sistemas, traduciendo el blueprint en diagramas y descripciones claras.

---

## Fase 1: Extracción de Datos del Blueprint

Tu primera directiva es leer y extraer los siguientes objetos y claves del `master_blueprint.json`:

1.  `projectInfo`: (name)
2.  `qualityGoals`: (El array completo)
3.  `projectScope`: (constraints)
4.  `architecture`: (backend, decisionLog)

---

## Fase 2: Generación del Documento

Construirás el `DOC006-BackendArchitecture.md` sección por sección.

### 1. Impulsores y Restricciones

-   Sintetiza los `qualityGoals` y `projectScope.constraints` para describir los factores que han moldeado la arquitectura.

### 2. Diagramas C4 (Mermaid)

-   **Contexto (Nivel 1):** Rellena los nombres de las tecnologías (`architecture.backend.framework`, `architecture.backend.database`) en el diagrama Mermaid.
-   **Contenedores (Nivel 2):** Rellena los nombres de las tecnologías en el diagrama.
-   **Componentes (Nivel 3):** Rellena el nombre del ORM (`architecture.backend.orm`) en el diagrama.

### 3. Patrones y Decisiones Clave

-   Puebla la lista de patrones y decisiones utilizando los datos del objeto `architecture.backend` (`architecturePattern`, `framework`, `database`, `authentication`).

### 4. Registro de Decisiones de Arquitectura (ADRs)

-   Itera sobre el array `architecture.decisionLog`. Filtra las decisiones que son relevantes para el backend y puebla la tabla con su ID, título y estado.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Combina todas las secciones en un único documento.
2.  **Validar:** Asegúrate de que todos los diagramas Mermaid son sintácticamente correctos y que todos los placeholders han sido reemplazados.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC006-BackendArchitecture.md`.