# Playbook v2: DOC019 - CLI Command Reference (2025 Enhanced)

**Objetivo:** Crear documentación de CLI universalmente adaptable basada en las mejores prácticas de developer experience 2025, incluyendo interactive documentation, automated testing, y multi-format output generation.

**Agente Asignado:** Developer Experience Specialist

**Principio Fundamental:** Una referencia de CLI efectiva no solo documenta comandos, sino que proporciona una experiencia de aprendizaje interactiva que facilita la adopción, reduce errores, y mejora la productividad del desarrollador a través de ejemplos contextualizados y validación automática.

---

## 🎯 Objetivos del Playbook

### **Objetivo Principal:**
Generar documentación de CLI de clase mundial que permita:
- Referencia completa y navegable de todos los comandos disponibles
- Ejemplos interactivos y casos de uso contextualizados
- Validación automática de sintaxis y parámetros
- Integración con herramientas de desarrollo y CI/CD

### **Estándares de Calidad:**
- **Completitud:** Cobertura completa de comandos, opciones y casos de uso
- **Precisión:** Sincronización automática con implementación actual
- **Usabilidad:** Navegación intuitiva y búsqueda avanzada
- **Interactividad:** Ejemplos ejecutables y validación en tiempo real

---

## 📋 Metodología de Creación (2025 Best Practices)

### **Fase 1: Investigación de CLI Documentation**

#### **1.1 Investigación de Mejores Prácticas**
```yaml
research_areas:
  - CLI design patterns and conventions (POSIX, GNU standards)
  - Developer experience and documentation usability
  - Interactive documentation systems (Swagger, Postman)
  - Automated documentation generation and maintenance
  - Command-line interface testing and validation
  - Multi-format documentation delivery (web, terminal, IDE)
```

#### **1.2 Análisis del CLI Ecosystem**
- Mapear comandos, subcomandos y jerarquías
- Identificar patrones de uso y workflows comunes
- Definir niveles de complejidad y audiencias
- Establecer convenciones de naming y estructura

### **Fase 2: Estructura del Template Universal**

#### **2.1 Componentes Esenciales del CLI Reference**
```yaml
cli_reference_components:
  command_metadata:
    - command_name: "[COMMAND_NAME]"
    - command_category: "[COMMAND_CATEGORY]"
    - command_description: "[COMMAND_DESCRIPTION]"
    - command_version: "[COMMAND_VERSION]"
    - deprecation_status: "[DEPRECATION_STATUS]"
    - last_updated: "[LAST_UPDATED]"
  
  syntax_structure:
    - basic_syntax: "[BASIC_SYNTAX]"
    - argument_patterns: "[ARGUMENT_PATTERNS]"
    - option_flags: "[OPTION_FLAGS]"
    - parameter_types: "[PARAMETER_TYPES]"
    - required_optional: "[REQUIRED_OPTIONAL_INDICATORS]"
  
  usage_examples:
    - basic_examples: "[BASIC_EXAMPLES]"
    - advanced_examples: "[ADVANCED_EXAMPLES]"
    - common_workflows: "[COMMON_WORKFLOWS]"
    - error_scenarios: "[ERROR_SCENARIOS]"
    - integration_examples: "[INTEGRATION_EXAMPLES]"
  
  validation_rules:
    - parameter_validation: "[PARAMETER_VALIDATION_RULES]"
    - dependency_checks: "[DEPENDENCY_CHECKS]"
    - environment_requirements: "[ENVIRONMENT_REQUIREMENTS]"
    - permission_requirements: "[PERMISSION_REQUIREMENTS]"
```

#### **2.2 Placeholders Universales**
- `[CLI_TOOL_NAME]` - Nombre de la herramienta CLI
- `[COMMAND_IDENTIFIER]` - Identificador único del comando
- `[SYNTAX_PATTERN]` - Patrón de sintaxis del comando
- `[PARAMETER_TYPE]` - Tipo de parámetro (string, number, boolean, file)
- `[EXAMPLE_CONTEXT]` - Contexto específico del ejemplo
- `[OUTPUT_FORMAT]` - Formato de salida esperado

### **Fase 3: Command Classification Framework**

#### **3.1 Categorización de Comandos**
```yaml
command_categories:
  core_commands:
    - initialization: "[INITIALIZATION_COMMANDS]"
    - configuration: "[CONFIGURATION_COMMANDS]"
    - execution: "[EXECUTION_COMMANDS]"
    - monitoring: "[MONITORING_COMMANDS]"
  
  data_commands:
    - create_operations: "[CREATE_OPERATIONS]"
    - read_operations: "[READ_OPERATIONS]"
    - update_operations: "[UPDATE_OPERATIONS]"
    - delete_operations: "[DELETE_OPERATIONS]"
  
  utility_commands:
    - debugging: "[DEBUGGING_COMMANDS]"
    - maintenance: "[MAINTENANCE_COMMANDS]"
    - integration: "[INTEGRATION_COMMANDS]"
    - reporting: "[REPORTING_COMMANDS]"
```

#### **3.2 Complexity and Usage Framework**
```yaml
complexity_framework:
  basic_commands:
    - description_style: "[BASIC_DESCRIPTION_STYLE]"
    - example_complexity: "[BASIC_EXAMPLE_COMPLEXITY]"
    - error_handling: "[BASIC_ERROR_HANDLING]"
    - help_text_level: "[BASIC_HELP_TEXT_LEVEL]"
  
  intermediate_commands:
    - description_style: "[INTERMEDIATE_DESCRIPTION_STYLE]"
    - workflow_integration: "[INTERMEDIATE_WORKFLOW_INTEGRATION]"
    - configuration_examples: "[INTERMEDIATE_CONFIG_EXAMPLES]"
    - troubleshooting_guide: "[INTERMEDIATE_TROUBLESHOOTING]"
  
  advanced_commands:
    - description_style: "[ADVANCED_DESCRIPTION_STYLE]"
    - scripting_examples: "[ADVANCED_SCRIPTING_EXAMPLES]"
    - performance_considerations: "[ADVANCED_PERFORMANCE]"
    - extension_points: "[ADVANCED_EXTENSION_POINTS]"
```

### **Fase 4: Interactive Documentation System**

#### **4.1 Command Discovery and Navigation**
```yaml
navigation_system:
  hierarchical_structure:
    - command_tree: "[COMMAND_TREE_STRUCTURE]"
    - category_grouping: "[CATEGORY_GROUPING_LOGIC]"
    - search_indexing: "[SEARCH_INDEX_CONFIGURATION]"
    - cross_references: "[CROSS_REFERENCE_SYSTEM]"
  
  search_capabilities:
    - command_search: "[COMMAND_SEARCH_ALGORITHM]"
    - parameter_search: "[PARAMETER_SEARCH_LOGIC]"
    - example_search: "[EXAMPLE_SEARCH_FUNCTIONALITY]"
    - fuzzy_matching: "[FUZZY_MATCHING_RULES]"
  
  contextual_help:
    - inline_help: "[INLINE_HELP_SYSTEM]"
    - progressive_disclosure: "[PROGRESSIVE_DISCLOSURE]"
    - related_commands: "[RELATED_COMMANDS_SUGGESTIONS]"
    - workflow_guidance: "[WORKFLOW_GUIDANCE_SYSTEM]"
```

#### **4.2 Interactive Examples and Validation**
```yaml
interactive_system:
  example_execution:
    - sandbox_environment: "[SANDBOX_ENVIRONMENT_SETUP]"
    - parameter_substitution: "[PARAMETER_SUBSTITUTION_RULES]"
    - output_visualization: "[OUTPUT_VISUALIZATION_FORMAT]"
    - error_demonstration: "[ERROR_DEMONSTRATION_SYSTEM]"
  
  validation_framework:
    - syntax_checking: "[SYNTAX_CHECKING_RULES]"
    - parameter_validation: "[PARAMETER_VALIDATION_LOGIC]"
    - dependency_verification: "[DEPENDENCY_VERIFICATION]"
    - environment_checks: "[ENVIRONMENT_CHECK_SYSTEM]"
  
  learning_assistance:
    - guided_tutorials: "[GUIDED_TUTORIAL_SYSTEM]"
    - progressive_examples: "[PROGRESSIVE_EXAMPLE_SEQUENCE]"
    - common_mistakes: "[COMMON_MISTAKES_PREVENTION]"
    - best_practices: "[BEST_PRACTICES_INTEGRATION]"
```

### **Fase 5: Automated Generation and Maintenance**

#### **5.1 Source-of-Truth Integration**
```yaml
automation_framework:
  code_analysis:
    - command_discovery: "[COMMAND_DISCOVERY_MECHANISM]"
    - parameter_extraction: "[PARAMETER_EXTRACTION_RULES]"
    - help_text_parsing: "[HELP_TEXT_PARSING_LOGIC]"
    - version_tracking: "[VERSION_TRACKING_SYSTEM]"
  
  documentation_generation:
    - template_population: "[TEMPLATE_POPULATION_LOGIC]"
    - example_generation: "[EXAMPLE_GENERATION_RULES]"
    - cross_reference_linking: "[CROSS_REFERENCE_LINKING]"
    - format_conversion: "[FORMAT_CONVERSION_PIPELINE]"
  
  quality_assurance:
    - completeness_checks: "[COMPLETENESS_CHECK_RULES]"
    - accuracy_validation: "[ACCURACY_VALIDATION_TESTS]"
    - example_testing: "[EXAMPLE_TESTING_FRAMEWORK]"
    - link_validation: "[LINK_VALIDATION_SYSTEM]"
```

#### **5.2 Multi-Format Output Generation**
```yaml
output_formats:
  web_documentation:
    - responsive_design: "[RESPONSIVE_DESIGN_FRAMEWORK]"
    - interactive_elements: "[INTERACTIVE_ELEMENTS_CONFIG]"
    - search_integration: "[SEARCH_INTEGRATION_SETUP]"
    - accessibility_features: "[ACCESSIBILITY_FEATURES]"
  
  terminal_integration:
    - man_page_generation: "[MAN_PAGE_GENERATION_RULES]"
    - help_command_integration: "[HELP_COMMAND_INTEGRATION]"
    - autocomplete_support: "[AUTOCOMPLETE_SUPPORT_GENERATION]"
    - color_coding: "[COLOR_CODING_SCHEME]"
  
  ide_integration:
    - intellisense_support: "[INTELLISENSE_SUPPORT_CONFIG]"
    - snippet_generation: "[SNIPPET_GENERATION_RULES]"
    - hover_documentation: "[HOVER_DOCUMENTATION_FORMAT]"
    - error_integration: "[ERROR_INTEGRATION_SYSTEM]"
```

### **Fase 6: Testing and Validation Framework**

#### **6.1 Documentation Testing**
```yaml
testing_framework:
  example_validation:
    - automated_testing: "[AUTOMATED_TESTING_PIPELINE]"
    - output_verification: "[OUTPUT_VERIFICATION_RULES]"
    - error_case_testing: "[ERROR_CASE_TESTING_FRAMEWORK]"
    - performance_testing: "[PERFORMANCE_TESTING_METRICS]"
  
  usability_testing:
    - user_journey_testing: "[USER_JOURNEY_TESTING_SCENARIOS]"
    - accessibility_testing: "[ACCESSIBILITY_TESTING_CHECKLIST]"
    - mobile_responsiveness: "[MOBILE_RESPONSIVENESS_TESTS]"
    - cross_browser_testing: "[CROSS_BROWSER_TESTING_MATRIX]"
  
  maintenance_validation:
    - sync_verification: "[SYNC_VERIFICATION_CHECKS]"
    - deprecation_tracking: "[DEPRECATION_TRACKING_SYSTEM]"
    - version_compatibility: "[VERSION_COMPATIBILITY_MATRIX]"
    - breaking_change_detection: "[BREAKING_CHANGE_DETECTION]"
```

---

## 🔧 Herramientas y Referencias

### **Herramientas Recomendadas:**
- **Documentation Generation:** Sphinx, GitBook, Docusaurus, VuePress
- **CLI Testing:** Bats, ShellCheck, Expect, Robot Framework
- **Interactive Documentation:** Swagger UI, Postman, Insomnia, Bruno
- **Automation:** GitHub Actions, GitLab CI, Jenkins, Azure DevOps

### **Referencias de Mejores Prácticas:**
- POSIX.1-2017 Command Line Conventions
- GNU Coding Standards for command-line interfaces
- The Art of Command Line (Joshua Levy)
- Command Line Interface Guidelines (Heroku)
- CLI Design Patterns (12 Factor CLI Apps)
- Microsoft Command-Line Style Guide

---

## ✅ Criterios de Éxito

### **CLI Reference Completado Debe Incluir:**
- [ ] Documentación completa de todos los comandos y subcomandos
- [ ] Ejemplos interactivos y casos de uso contextualizados
- [ ] Sistema de navegación y búsqueda avanzada
- [ ] Validación automática de sintaxis y parámetros
- [ ] Integración con herramientas de desarrollo (IDE, terminal)
- [ ] Generación automática desde código fuente
- [ ] Testing automatizado de ejemplos y casos de uso
- [ ] Soporte multi-formato (web, terminal, man pages)
- [ ] Accesibilidad completa y responsive design
- [ ] Analytics de uso y métricas de efectividad

### **Calidad del Template:**
- [ ] 100% de placeholders universales implementados
- [ ] Adaptable a diferentes tipos de CLI tools
- [ ] Sistema de generación completamente automatizado
- [ ] Validación y testing integrados
- [ ] Experiencia de usuario optimizada
- [ ] Validado con diferentes herramientas CLI

---

**Última Actualización:** 2025-08-18  
**Versión:** 2.0 (Enhanced Developer Experience Framework)  
**Próxima Revisión:** Mensual