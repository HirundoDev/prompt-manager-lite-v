# Checklist de Verificación de Docs y Schemas (manual)

Este archivo centraliza el estado de cobertura y aplicabilidad de los artefactos (DOCs y Schemas) del proyecto.

Cómo usarlo (modo manual):
- Paso 0 del flujo maestro (ver `guides/the_mighty_guide.md`):
  1) Revisa la estructura y tecnologías reales del proyecto (¿frontend?, ¿backend?, ¿CLI?, ¿infra?, etc.).
  2) Marca la columna "Aplica" (si/no/pendiente) por cada fila según corresponda al proyecto.
  3) Cuando modifiques un archivo listado, incrementa "ContadorCambios" y actualiza "UltimaModificacion" (ISO 8601). Puedes usar la fecha actual o la del último commit que tocó el archivo.
- Mantén las rutas relativas a la raíz del repo (`prompt-manager-lite-v/`).
- Si agregas nuevos DOCs o Schemas, añade manualmente una fila a la tabla.

| Tipo | Ruta | Aplica | ContadorCambios | UltimaModificacion | Nota |
|---|---|---|---:|---|---|
| DOC | real_structure_documentation/docs/DOC000-ProjectBrief.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC001-ProjectREADME.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC002-ProductDefinition.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC003-DesignSystem.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC004-FrontendArchitecture.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC005-FrontendDependencies.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC006-BackendArchitecture.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC007-BackendDependencies.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC008-APISpecification.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC009-DataModel.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC010-Deployment.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC011-TestingStrategy.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC012-SecurityCompliance.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC013-ChangeLog.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC014-IssueTemplate.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC015-PullRequestTemplate.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC016-Contributing.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC017-ADR-Index.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC019-CLI-Command-Reference.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC020-CodeOfConduct.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC021-OnboardingGuide.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC022-ReleaseProcess.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC023-BackendManifest.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC024-DatabaseManifest.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC025-FrontendManifest.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC026-ProjectFileManifest.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC027-SharedLibsManifest.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC028-OperationsRunbook.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC029-ProjectRoadmap.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC030-FeatureIndex.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC031-BugIndex.md | pendiente | 0 | - |  |
| DOC | real_structure_documentation/docs/DOC032-FrontendScreenFlow.md | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/cli_schema.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/design_system_schema.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/apiContract.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/architecture.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/bugLifecycle.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/businessLogic.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/componentLibrary.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/dataModel.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/dataModelDictionary.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/deepLogicAnalysis.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/definitions.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/deploymentStrategy.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/designPatterns.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/designSystem.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/featureLifecycle.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/featureManifest.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/fileExecutionMap.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/forensicAudit.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/operationalStrategy.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/projectInfo.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/projectManagement.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/qualityGoals.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/stateManagementPlan.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/testingStrategy.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/visualBlueprint.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_parts/wireframeStates.json | pendiente | 0 | - |  |
| Schema | real_structure_documentation/schemas/master_blueprint_schema.json | pendiente | 0 | - |  |
