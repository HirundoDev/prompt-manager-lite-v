# Playbook v2: DOC016 - Guía de Contribución

**Objetivo:** Generar una guía de contribución (`CONTRIBUTING.md`) acogedora y completa que explique claramente cómo participar en el proyecto.

**Agente Asignado:** Community Manager Agent

**Principio Fundamental:** Las guías de contribución deben reducir la barrera de entrada para nuevos colaboradores, proporcionando instrucciones claras y fomentando la participación.

---

## Fase 1: Extracción de Datos del Blueprint

Tu única directiva de extracción es leer y obtener el objeto `projectManagement.codingStandards` del `master_blueprint.json`.

---

## Fase 2: Generación del Documento

Utilizarás la plantilla `DOC016-Contributing.md` como base. La mayor parte de su contenido es estático y sirve para guiar al contribuyente.

Tu única tarea de poblado dinámico es la sección de **Estándares de Codificación**:

-   Rellena los campos `Estilo de Código`, `Formateo y Linting` y `Comandos` utilizando los valores correspondientes del objeto `codingStandards` que extrajiste.

El resto de la plantilla (Código de Conducta, Proceso de Contribución, etc.) ya contiene los enlaces y la estructura correctos.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Construye el documento completo, combinando la plantilla estática con la sección de estándares de codificación poblada dinámicamente.
2.  **Validar:** Asegúrate de que el documento final sea coherente y que los estándares de codificación del blueprint estén correctamente reflejados.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC016-Contributing.md`.