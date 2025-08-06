# Playbook v2: DOC007 - Panel de Control de Dependencias del Backend

**Objetivo:** Generar un panel de control de salud de dependencias vivo y accionable, ejecutando auditorías de seguridad y licencias para la pila del backend.

**Agente Asignado:** Backend Health Agent

**Principio Fundamental:** La gestión proactiva de dependencias es clave para la seguridad y la estabilidad del servidor. Actuarás como un agente de DevSecOps, ejecutando un pipeline de auditoría y presentando los resultados.

---

## Fase 1: Ejecución de Auditorías

Tu primera directiva es identificar el gestor de paquetes del backend (ej. npm, pip, maven) y ejecutar los comandos de auditoría correspondientes, capturando sus salidas en formato JSON:

1.  **Leer Manifiesto:** Lee y parsea el archivo de manifiesto (`package.json`, `requirements.txt`, etc.).
2.  **Auditoría de Seguridad:**
    ```sh
    # Para Node.js
    npm audit --json
    # Para Python
    # pip-audit --format json
    ```
3.  **Auditoría de Licencias:**
    ```sh
    # Para Node.js
    npx license-checker --json
    # Para Python (puede requerir otras herramientas)
    ```

---

## Fase 2: Síntesis y Población de Datos

Con los datos de las auditorías, poblarás la plantilla `DOC007-BackendDependencies.md`.

### 1. Tablas de Dependencias

-   Para cada paquete en el manifiesto:
    -   Busca su información de licencia en la salida de la auditoría de licencias.
    -   Busca su información de vulnerabilidades en la salida de la auditoría de seguridad.
    -   Puebla una fila en la tabla correspondiente (producción o desarrollo).

### 2. Resúmenes de Auditoría

-   **Seguridad:** Analiza la salida de la auditoría para crear un resumen de las vulnerabilidades encontradas.
-   **Licencias:** Analiza la salida de la auditoría para crear un resumen de los tipos de licencia y señalar cualquier licencia restrictiva.

### 3. Estado General

-   Determina el "Estado General". Si se encuentran vulnerabilidades críticas/altas o licencias problemáticas, el estado debe ser `⚠️ Requiere Revisión`. De lo contrario, es `✅ Saludable`.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Combina todas las secciones en un único documento.
2.  **Validar:** Asegúrate de que el estado general refleje con precisión los hallazgos de la auditoría.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC007-BackendDependencies.md`.