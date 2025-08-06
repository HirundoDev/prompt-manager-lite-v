# Plantilla Maestra: Manual de Despliegue

> **Propósito:** Proporcionar una guía completa y paso a paso para desplegar la aplicación en todos los entornos (desarrollo, staging, producción).
> **Playbook de Referencia:** `playbook-v2-DOC010-Deployment.md`

<!-- 
  INSTRUCCIONES PARA LA IA (DevOps Agent):
  - Tu misión es generar este manual de operaciones a partir del objeto `operationalManual` en el `master_blueprint.json`.
  - El objetivo es crear una guía tan clara que un nuevo desarrollador pueda desplegar la aplicación sin asistencia.
-->

## 1. Visión General de la Infraestructura

-   **Proveedor de Hosting (Frontend):** `[operationalManual.hosting.frontend.provider]`
-   **Proveedor de Hosting (Backend):** `[operationalManual.hosting.backend.provider]`
-   **Base de Datos:** `[operationalManual.hosting.database.provider]`
-   **Entornos:** `[Lista de entornos, ej. development, staging, production]`

## 2. Prerrequisitos

-   **Herramientas de CLI Requeridas:** `[Ej. Node.js, Docker, AWS CLI, gcloud]`
-   **Acceso Requerido:** `[Ej. Acceso a la cuenta de AWS, permisos en el repositorio de Git]`

## 3. Configuración de Entorno

### Variables de Entorno (Frontend)

| Variable | Descripción | Ejemplo | Entornos |
| :--- | :--- | :--- | :--- |
| `[Iterar sobre operationalManual.environmentVariables.frontend]` | | | |

### Variables de Entorno (Backend)

| Variable | Descripción | Ejemplo | Entornos |
| :--- | :--- | :--- | :--- |
| `[Iterar sobre operationalManual.environmentVariables.backend]` | | | |

## 4. Proceso de Despliegue Paso a Paso

### Despliegue del Backend

1.  **Construir la imagen de Docker:**
    ```bash
    [operationalManual.deploymentSteps.backend.build]
    ```
2.  **Publicar la imagen en el registro:**
    ```bash
    [operationalManual.deploymentSteps.backend.push]
    ```
3.  **Ejecutar migraciones de la base de datos:**
    ```bash
    [operationalManual.deploymentSteps.backend.migrate]
    ```
4.  **Desplegar la nueva versión:**
    ```bash
    [operationalManual.deploymentSteps.backend.deploy]
    ```

### Despliegue del Frontend

1.  **Construir la aplicación:**
    ```bash
    [operationalManual.deploymentSteps.frontend.build]
    ```
2.  **Desplegar en el proveedor de hosting:**
    ```bash
    [operationalManual.deploymentSteps.frontend.deploy]
    ```

## 5. Procedimiento de Rollback

-   **Backend:** `[Descripción del proceso de rollback, ej. redesplegar la versión anterior desde el registro de imágenes]`
-   **Frontend:** `[Descripción del proceso de rollback, ej. revertir al despliegue anterior en Vercel/Netlify]`

## 6. Pipeline de CI/CD

-   **Herramienta de CI/CD:** `[operationalManual.ci_cd.tool, ej. GitHub Actions]`
-   **Triggers:** `[ej. en cada push a main/develop]`
-   **Resumen del Pipeline:** `[Breve descripción de las etapas del pipeline: build, test, deploy]`