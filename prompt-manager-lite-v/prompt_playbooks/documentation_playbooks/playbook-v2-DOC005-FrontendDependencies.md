# Playbook v2: DOC005 - Panel de Control de Dependencias del Frontend

**Objetivo:** Generar un panel de control de salud de dependencias vivo y accionable, ejecutando auditorías de seguridad, licencias y rendimiento.

**Agente Asignado:** Frontend Health Agent

**Principio Fundamental:** La gestión proactiva de dependencias es clave para la seguridad y el rendimiento. Actuarás como un agente de DevSecOps, ejecutando un pipeline de auditoría y presentando los resultados.

---

## Fase 1: Ejecución de Auditorías

Tu primera directiva es ejecutar los siguientes comandos en el directorio del proyecto y capturar sus salidas en formato JSON:

1.  **Leer Manifiesto:** Lee y parsea el archivo `package.json` para obtener las listas de `dependencies` y `devDependencies`.
2.  **Auditoría de Seguridad:**
    ```sh
    npm audit --json
    ```
3.  **Auditoría de Licencias:** (Asumiendo que `license-checker` está instalado)
    ```sh
    npx license-checker --json
    ```
4.  **Análisis de Bundle:** (Asumiendo un script `analyze` en `package.json` que genera un `stats.json`)
    ```sh
    npm run analyze
    ```

---

## Fase 2: Síntesis y Población de Datos

Con los datos de las auditorías, poblarás la plantilla `DOC005-FrontendDependencies.md`.

### 1. Tablas de Dependencias

-   Para cada paquete en `dependencies` y `devDependencies` del `package.json`:
    -   Busca su información de licencia en la salida de `license-checker`.
    -   Busca su información de vulnerabilidades en la salida de `npm audit`.
    -   Busca su tamaño en el bundle en la salida del analizador.
    -   Puebla una fila en la tabla correspondiente.

### 2. Resúmenes de Auditoría

-   **Seguridad:** Analiza la salida de `npm audit` para crear un resumen de las vulnerabilidades encontradas (ej. "Se encontraron 2 vulnerabilidades críticas y 5 altas.").
-   **Licencias:** Analiza la salida de `license-checker` para crear un resumen de los tipos de licencia y señalar cualquier licencia restrictiva (ej. GPL).

### 3. Estado General

-   Determina el "Estado General" del panel de control. Si se encuentran vulnerabilidades críticas/altas o licencias problemáticas, el estado debe ser `⚠️ Requiere Revisión`. De lo contrario, es `✅ Saludable`.

---

## Fase 3: Ensamblaje Final

1.  **Ensamblar:** Combina todas las secciones en un único documento.
2.  **Validar:** Asegúrate de que el estado general refleje con precisión los hallazgos de la auditoría.
3.  **Escribir Archivo:** Escribe el contenido final en `DOC005-FrontendDependencies.md`.