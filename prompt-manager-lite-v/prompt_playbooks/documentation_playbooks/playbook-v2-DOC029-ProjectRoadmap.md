# Playbook v2: DOC029 - Roadmap Estratégico del Producto

**Objetivo:** Generar un roadmap de producto claro y estratégico, basado en las iniciativas y la visión definidas en el blueprint.

**Agente Asignado:** Product Manager Agent

**Principio Fundamental:** Un roadmap es una herramienta de comunicación, no un contrato. Tu rol es traducir la estrategia del producto en una narrativa visual y comprensible sobre el futuro.

---

## Fase 1: Extracción de Datos del Blueprint

Tu misión de extracción de datos es doble:

1.  **Extraer Visión:** Lee y obtén el valor de `productRoadmap.vision` del `master_blueprint.json`.
2.  **Extraer Iniciativas:** Lee y obtén el array `productRoadmap.initiatives`.

---

## Fase 2: Generación del Contenido del Roadmap

Tu misión es organizar las iniciativas en sus respectivos horizontes y temas.

1.  **Agrupar por Horizonte:** Primero, agrupa las iniciativas en tres listas: `now`, `next` y `later`, basándote en el valor de su propiedad `horizon`.
2.  **Generar Bloques de Horizonte:** Para cada una de las tres listas (Now, Next, Later):
    -   Agrupa las iniciativas de esa lista por su `theme`.
    -   Para cada `theme`, genera un bloque de título (`### Tema: [theme.name]`)
    -   Debajo de cada tema, lista las iniciativas correspondientes, formateando cada una como `- **[initiative.title]**: [initiative.description]`.
    -   Concatena estos bloques para formar el contenido completo de cada horizonte.

---

## Fase 3: Ensamblaje Final

1.  **Leer Plantilla:** Carga el contenido de la plantilla `DOC029-ProjectRoadmap.md`.
2.  **Poblar Visión:** Reemplaza `[productRoadmap.vision]` con el valor extraído.
3.  **Reemplazar Contenido:** Reemplaza las secciones de ejemplo de `Ahora`, `Siguiente` y `Después` con los bloques de contenido que generaste en la Fase 2.
4.  **Escribir Archivo:** Escribe el contenido final y poblado en `DOC029-ProjectRoadmap.md`.