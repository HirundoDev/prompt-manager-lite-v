# Guía Maestra de Playbooks de Estrategia

## 1. ¿Qué son los Playbooks?

Los playbooks no son prompts de ejecución directa. Son **archivos de conocimiento estratégico** que actúan como el "libro de texto" de un agente. Enseñan a los agentes de planificación (principalmente al **Auditor de Ingeniería Inversa - Agente 3**) a pensar de manera estructurada sobre un dominio específico. 

Por ejemplo, el `playbook-dependencies.md` no le dice al agente "encuentra las dependencias", sino que le enseña un método sistemático para buscarlas, clasificarlas y analizarlas en diferentes ecosistemas (frontend, backend, etc.).

## 2. ¿Cómo se Utilizan?

Los playbooks se activan a través del `agent_registry.json`. Se incluyen en el array `knowledge_sources` de un agente. Cuando el Orquestador invoca a ese agente, carga el contenido de estos playbooks y se lo proporciona como parte de su contexto fundamental, dándole así el conocimiento experto necesario para su misión.

## 3. Catálogo de Playbooks de Análisis Central

Estos playbooks enseñan al agente a realizar la auditoría forense del código fuente.

-   `playbook-apiContract.md`: Estrategia para definir y analizar contratos de API.
-   `playbook-architecture.md`: Guía para analizar y describir la arquitectura de software.
-   `playbook-componentLibrary.md`: Método para identificar y catalogar una biblioteca de componentes.
-   `playbook-dataModelDictionary.md`: Protocolo para crear un diccionario del modelo de datos.
-   `playbook-deepLogicAnalysis.md`: Técnicas para un análisis profundo de la lógica de negocio.
-   `playbook-dependencies.md`: Protocolo para identificar y catalogar dependencias.
-   `playbook-deploymentStrategy.md`: Guía para analizar la estrategia de despliegue.
-   `playbook-designSystem.md`: Método para definir y extraer un sistema de diseño.
-   `playbook-featureManifest.md`: Estrategia para crear un manifiesto de funcionalidades.
-   `playbook-fileExecutionMap.md`: Guía para mapear la ejecución de archivos y flujos de control.
-   `playbook-projectInfo.md`: Protocolo para extraer la información básica de un proyecto.
-   `playbook-projectManagement.md`: Guía para analizar la configuración de gestión del proyecto.
-   `playbook-qualityGoals.md`: Estrategia para definir y medir objetivos de calidad.
-   `playbook-stateManagementPlan.md`: Método para analizar el plan de gestión de estado.
-   `playbook-testingStrategy.md`: Guía para auditar la estrategia de pruebas.

## 4. Catálogo de Playbooks de Documentación

Estos playbooks guían la **planificación** de la documentación técnica. Son utilizados por el Agente 3 para construir el `documentationManifest` dentro del `master_blueprint.json`.

-   `MASTER_DOCUMENTATION_PLAYBOOK.md`: El playbook maestro que orquesta la creación de todos los demás documentos.
-   `playbook-DOC001-ProjectREADME.md`: Estrategia para generar un README de alta calidad.
-   `playbook-DOC002-ProductDefinition.md`: Guía para definir el producto.
-   `playbook-DOC003-DesignSystem.md`: Guía para documentar el sistema de diseño.
-   `playbook-DOC004-FrontendArchitecture.md`: Para documentar la arquitectura del frontend.
-   `playbook-DOC005-FrontendDependencies.md`: Para documentar las dependencias del frontend.
-   `playbook-DOC006-BackendArchitecture.md`: Para documentar la arquitectura del backend.
-   `playbook-DOC007-BackendDependencies.md`: Para documentar las dependencias del backend.
-   `playbook-DOC008-ApiContract.md`: Para documentar el contrato de la API.
-   `playbook-DOC009-DataModelSchema.md`: Para documentar el esquema del modelo de datos.
-   `playbook-DOC010-DeploymentManual.md`: Para crear el manual de despliegue.
-   `playbook-DOC011-TestingStrategy.md`: Para documentar la estrategia de pruebas.
-   `playbook-DOC012-SecurityCompliance.md`: Para documentar la seguridad y el cumplimiento.
-   `playbook-DOC013-ChangeLog.md`: Para mantener el registro de cambios.
-   `playbook-DOC014-IssuePRTemplates.md`: Para crear plantillas de issues y PRs.
-   `playbook-DOC015-License.md`: Para incluir la licencia.
-   `playbook-DOC016-Contributing.md`: Para crear la guía de contribución.
-   `playbook-DOC017-ADR-Index.md`: Para crear un índice de Decisiones de Arquitectura (ADR).
-   `playbook-DOC018-ADR-Template.md`: Para crear una plantilla de ADR.
-   `playbook-DOC019-CLI-Command-Reference.md`: Para documentar los comandos de una CLI.
-   `playbook-DOC020-CodeOfConduct.md`: Para incluir el código de conducta.