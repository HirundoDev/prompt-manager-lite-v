# Playbook de Protocolo: `deploymentStrategy`

**Versión 1.0**

---

### 1. Objetivo Filosófico

Esta sección es el **puente entre el código y el usuario final**. Documenta el proceso automatizado (o manual) que lleva el software desde el repositorio de código hasta un entorno operativo donde puede ser utilizado. Comprender esta estrategia es clave para saber cómo se entregan las nuevas características y cómo se gestionan las actualizaciones.

### 2. Misión del Agente: El Ingeniero de DevOps

Tu misión es actuar como un **Ingeniero de DevOps**. Tu principal objetivo es analizar los archivos de configuración de Integración Continua y Despliegue Continuo (CI/CD) para desentrañar el proceso de despliegue. Eres un arqueólogo de pipelines, buscando los scripts, los trabajos y las etapas que definen el camino del código hacia la producción.

### 3. Protocolo de Búsqueda y Extracción

Tu investigación se centrará casi exclusivamente en los archivos de CI/CD.

#### Paso 1: Localizar los Archivos de Configuración de CI/CD

-   **Metodología**: Busca en el directorio raíz y en el directorio `.github/` los siguientes archivos:
    -   **GitHub Actions**: `.github/workflows/*.yml` o `.github/workflows/*.yaml`
    -   **GitLab CI/CD**: `.gitlab-ci.yml`
    -   **CircleCI**: `.circleci/config.yml`
    -   **Jenkins**: `Jenkinsfile`
    -   **Travis CI**: `.travis.yml`

#### Paso 2: Analizar el Contenido de la Pipeline

-   **Metodología**: Una vez que encuentres el archivo de configuración, léelo cuidadosamente para extraer la siguiente información:

    -   **`deploymentEnvironments`**: Busca trabajos (`jobs`) o etapas (`stages`) con nombres que indiquen diferentes entornos. 
        -   **Pistas**: `deploy_staging`, `deploy_prod`, `test`, `build`. Cada uno de estos trabajos o etapas representa un entorno o un paso en el proceso. Lista todos los que encuentres.

    -   **`buildProcess`**: Busca los comandos específicos que compilan, transpilan o empaquetan la aplicación.
        -   **Pistas**: Busca líneas de comando como `npm run build`, `go build -o myapp`, `docker build -t myimage .`, `mvn package`.
        -   **Acción**: Documenta el comando exacto y el entorno en el que se ejecuta.

    -   **`releaseProcess`**: Busca los pasos que indican que se está creando una nueva versión del software.
        -   **Pistas**: Comandos que crean etiquetas de Git (`git tag`), publican en un registro de paquetes (`npm publish`, `poetry publish`), o utilizan herramientas para crear una Release de GitHub (ej. `gh release create`).
        -   **Acción**: Describe qué desencadena una release (ej. un push a `main`, una etiqueta de Git, un disparo manual) y qué acciones se realizan.

    -   **`deploymentInfrastructure`**: Busca los comandos que interactúan con una plataforma en la nube o un proveedor de alojamiento.
        -   **Pistas**: Comandos de CLI como `aws s3 sync`, `gcloud app deploy`, `az webapp up`, o el uso de herramientas de PaaS como `vercel deploy`, `netlify deploy`, `heroku container:push`.
        -   **Acción**: Identifica el proveedor de la nube (AWS, GCP, Azure) o la plataforma (Vercel, Netlify, Heroku) y describe brevemente el servicio utilizado (ej. "Despliega un contenedor de Docker en AWS ECS").

---

### 4. Criterios de Exhaustividad (Reglas Inquebrantables)

-   **Análisis Completo de la Pipeline**: La tarea no se considera completa hasta que hayas analizado **todos** los archivos de flujo de trabajo de CI/CD encontrados en el repositorio. Un proyecto puede tener múltiples flujos de trabajo para diferentes propósitos.
-   **Identificar el Desencadenante (Trigger)**: Para cada proceso de despliegue, debes identificar qué evento lo inicia. ¿Es un `push` a una rama específica? ¿La creación de un `pull request`? ¿Un `schedule` cronometrado? ¿Un evento manual (`workflow_dispatch`)?
-   **Declaración de Ausencia de Automatización**: Si, después de una búsqueda exhaustiva, no encuentras ningún archivo de configuración de CI/CD que maneje el despliegie, **debes declararlo explícitamente**. Tu conclusión debe ser: "No se encontró evidencia de una estrategia de despliegue automatizada en el repositorio. Es probable que el despliegue sea un proceso manual".
-   **Conexión Causa-Efecto**: Documenta la cadena de eventos. Por ejemplo: "Un push al branch `main` desencadena un flujo de trabajo de GitHub Actions que primero construye la aplicación con `npm run build`, y luego despliega los artefactos resultantes en Vercel."