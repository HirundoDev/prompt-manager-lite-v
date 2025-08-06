# Plantilla Maestra: Proceso de Lanzamiento

> **Propósito:** Proporcionar una checklist operativa y a prueba de errores para guiar al equipo a través del lanzamiento de una nueva versión del software.
> **Playbook de Referencia:** `playbook-v2-DOC022-ReleaseProcess.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Release Manager Agent):
  - Tu misión es generar este documento utilizando el objeto `releaseManagement` del `master_blueprint.json` para asegurar que el proceso refleje las prácticas actuales.
-->

# Proceso de Lanzamiento: Checklist Operativa

**Estrategia de Versionado:** `[releaseManagement.versioningStrategy]`

## Fase 1: Pre-Lanzamiento

- [ ] **Crear Rama de Lanzamiento:** Crea una rama `release/vX.Y.Z` a partir de la rama `main`.
- [ ] **Finalizar Cambios:** Asegúrate de que todos los PRs para esta versión han sido fusionados en `main`.
- [ ] **Actualizar Dependencias:** Revisa y actualiza las dependencias. ([Ver Panel de Salud de Dependencias](./DOC005-FrontendDependencies.md) y [DOC007-BackendDependencies.md]).
- [ ] **Actualizar Changelog:** Asegúrate de que el `[Unreleased]` en el [Changelog](./DOC013-ChangeLog.md) está completo y es preciso.
- [ ] **Ejecutar Pruebas Finales:** Ejecuta la suite completa de pruebas en la rama de lanzamiento.
    -   Comando de Pruebas: `[qualityAssurance.testExecution.fullSuiteCommand]`

## Fase 2: Lanzamiento

- [ ] **Versionar el Código:**
    -   Actualiza la versión en `package.json` (o archivo correspondiente).
    -   Mueve el contenido de `[Unreleased]` a una nueva sección de versión en el [Changelog](./DOC013-ChangeLog.md).
    -   Crea un commit de versión: `git commit -m "chore(release): vX.Y.Z"`.
- [ ] **Crear Tag de Git:** Crea un tag anotado para la nueva versión.
    -   `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
- [ ] **Publicar Paquetes (si aplica):**
    -   Comando de Publicación: `[releaseManagement.publishCommand]`
- [ ] **Fusionar Rama de Lanzamiento:**
    -   Fusiona la rama `release/vX.Y.Z` de nuevo en `main`.
    -   Fusiona `main` en `develop` (o la rama de desarrollo principal).
- [ ] **Empujar Tags:** `git push --tags`

## Fase 3: Post-Lanzamiento

- [ ] **Crear Release en GitHub/GitLab:** Crea una nueva release en la plataforma, usando las notas del changelog.
- [ ] **Verificar Despliegue:** Confirma que la nueva versión está desplegada y operativa en producción.
- [ ] **Comunicar Lanzamiento:** Anuncia la nueva versión al equipo y a los stakeholders.
- [ ] **Monitorizar:** Vigila los dashboards de monitorización en busca de cualquier anomalía.