# Playbook v2: DOC001 - Generación del README del Proyecto

**Objetivo:** Generar un archivo `README.md` completo, profesional y amigable para el desarrollador, extrayendo y formateando información del `master_blueprint.json`.

**Agente Asignado:** Technical Writer Agent

**Principio Fundamental:** Un gran README es la puerta de entrada a tu proyecto. Debe ser acogedor, informativo y accionable.

---

## Fase 1: Extracción de Datos del Blueprint

Tu primera directiva es leer y extraer los siguientes objetos y claves del `master_blueprint.json`:

1.  `projectInfo`: (name, slogan, description, logoUrl, license, github.user, github.repo)
2.  `dependencies`: (frontend, backend, database, devops)
3.  `deployment`: (prerequisites, buildSteps.installDependencies, run.development)

---

## Fase 2: Generación del Documento

Construirás el `README.md` sección por sección, utilizando los datos extraídos.

### 1. Cabecera

-   **Logo:** Inserta la URL de `projectInfo.logoUrl`.
-   **Título:** Usa `projectInfo.name`.
-   **Slogan:** Usa `projectInfo.slogan`.
-   **Badges:** Construye las URLs de los badges usando `projectInfo.github.user` y `projectInfo.github.repo`.

### 2. Sobre el Proyecto

-   Pobla esta sección con el contenido de `projectInfo.description`.

### 3. Stack Tecnológico

-   Itera sobre las listas en `dependencies` y crea una lista con viñetas para cada categoría (Frontend, Backend, etc.).

### 4. Primeros Pasos

-   **Prerrequisitos:** Lista los elementos de `deployment.prerequisites`.
-   **Instalación:** Inserta el comando de `deployment.buildSteps.installDependencies` en el bloque de código correspondiente.

### 5. Uso

-   Inserta el comando de `deployment.run.development` en el bloque de código.

### 6. Licencia

-   Inserta el nombre de la licencia desde `projectInfo.license`.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Combina todas las secciones generadas en un único documento.
2.  **Validar:** Asegúrate de que todos los placeholders han sido reemplazados y el formato es limpio y consistente.
3.  **Escribir Archivo:** Escribe el contenido final en el archivo `README.md` en la raíz del proyecto.