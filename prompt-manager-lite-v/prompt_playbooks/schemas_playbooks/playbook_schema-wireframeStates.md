# Schema Playbook — wireframeStates

**Propósito:** Template universal para documentar wireframes, estados de UI y patrones de flujo de usuario en cualquier herramienta de diseño o plataforma. Proporciona estructura adaptable con placeholders para estados de pantalla, journeys de usuario, interacciones y consideraciones de accesibilidad.

**Ubicación:** `schemas/master_blueprint_parts/wireframeStates.json`

**Versión:** 3.0 (Template Universal con Placeholders)

---

## 1) Arquitectura del Template (Universal y Adaptable)

### **Filosofía Template-First**
Este schema funciona como template universal que se adapta a cualquier:
- **Herramienta de Diseño:** Figma, Sketch, Adobe XD, Axure, Balsamiq, papel, etc.
- **Tipo de Proyecto:** Web, móvil, desktop, responsive, AR/VR, kiosco
- **Nivel de Fidelidad:** Baja, media, alta, mixta
- **Metodología:** Cualquier enfoque de diseño UX/UI

### **Componentes del Template**
- **`metadata`**: Contexto del proyecto y wireframes con placeholders `[VARIABLE]`
- **`designContext`**: Integración con sistemas de diseño adaptable
- **`userFlows`**: Flujos de usuario universales para cualquier journey
- **`screens`**: Definiciones de pantallas con estados adaptables
- **`stateManagement`**: Gestión de estados agnóstica de tecnología
- **`interactions`**: Patrones de interacción universales
- **`accessibility`**: Consideraciones de accesibilidad adaptables
- **`testing`**: Estrategias de validación universales

### **Principio de Placeholders**
Todos los valores específicos usan placeholders `[VARIABLE]` que se reemplazan según el contexto:
- `[DESIGN_TOOL]` → Figma, Sketch, Adobe XD, papel, etc.
- `[PROJECT_TYPE]` → Web app, mobile app, desktop app, etc.
- `[FIDELITY_LEVEL]` → Low, medium, high, mixed
- `[SCREEN_TYPE]` → Landing, form, dashboard, modal, etc.

---

## 2) Metodología de Uso del Template

### **Fase 1: Análisis del Contexto del Proyecto**
1. **Identificar Herramienta**: Determinar `[DESIGN_TOOL]` y capacidades disponibles
2. **Evaluar Tipo de Proyecto**: Definir `[PROJECT_TYPE]` y plataforma objetivo
3. **Establecer Fidelidad**: Seleccionar `[FIDELITY_LEVEL]` apropiado para la fase
4. **Definir Stakeholders**: Identificar `[STAKEHOLDER_ROLE]` y responsabilidades

### **Fase 2: Configuración del Contexto de Diseño**
1. **Sistema de Diseño**: Establecer `[DESIGN_SYSTEM_REFERENCE]` si existe
2. **Componentes**: Definir `[COMPONENT_LIBRARY]` disponible
3. **Tokens**: Configurar `[DESIGN_TOKENS]` para consistencia
4. **Layout**: Seleccionar `[LAYOUT_SYSTEM]` y breakpoints

### **Fase 3: Mapeo de Flujos de Usuario**
1. **Identificar Flujos**: Definir `[USER_FLOW_NAME]` y prioridades
2. **Tipos de Usuario**: Establecer `[USER_TYPE]` y contextos
3. **Pasos del Flujo**: Documentar `[FLOW_STEPS]` y alternativas
4. **Criterios de Éxito**: Definir `[SUCCESS_CRITERIA]` medibles

### **Fase 4: Definición de Pantallas y Estados**
1. **Pantallas**: Crear `[SCREEN_NAME]` y tipos apropiados
2. **Estados**: Definir `[SCREEN_STATES]` para cada pantalla
3. **Contenido**: Especificar `[WIREFRAME_CONTENT]` y estructura
4. **Anotaciones**: Agregar `[ANNOTATION_CONTENT]` explicativo

### **Fase 5: Gestión de Estados e Interacciones**
1. **Transiciones**: Configurar `[STATE_TRANSITIONS]` entre pantallas
2. **Triggers**: Definir `[TRIGGER_TYPE]` y condiciones
3. **Patrones**: Implementar `[INTERACTION_PATTERNS]` consistentes
4. **Feedback**: Establecer `[FEEDBACK_MECHANISMS]` apropiados

### **Fase 6: Accesibilidad y Testing**
1. **Estándares**: Seleccionar `[ACCESSIBILITY_STANDARD]` aplicable
2. **Características**: Implementar `[ACCESSIBILITY_FEATURES]` necesarias
3. **Estrategia de Testing**: Definir `[TESTING_APPROACH]` y métodos
4. **Validación**: Establecer `[VALIDATION_METHODS]` y métricas

---

## 3) Guía Universal de Selección de Herramientas

### **Criterios de Selección Universales**

```
¿Qué herramienta elegir para [DESIGN_TOOL]?
├── [QUICK_SKETCHING] → [LOW_FIDELITY_TOOLS]
├── [TEAM_COLLABORATION] → [COLLABORATIVE_TOOLS]
├── [HIGH_FIDELITY] → [ADVANCED_DESIGN_TOOLS]
├── [COMPLEX_LOGIC] → [PROTOTYPING_TOOLS]
├── [ENTERPRISE_NEEDS] → [ENTERPRISE_TOOLS]
└── [BUDGET_CONSTRAINTS] → [FREE_OR_LOW_COST_TOOLS]
```

### **Matriz de Decisión por Contexto**

| Criterio | [SMALL_PROJECT] | [MEDIUM_PROJECT] | [LARGE_PROJECT] | [ENTERPRISE_PROJECT] |
|----------|-----------------|------------------|-----------------|---------------------|
| **Fidelidad** | [LOW_FIDELITY] | [MEDIUM_FIDELITY] | [HIGH_FIDELITY] | [MIXED_FIDELITY] |
| **Colaboración** | [BASIC_SHARING] | [REAL_TIME_COLLAB] | [ADVANCED_COLLAB] | [ENTERPRISE_COLLAB] |
| **Complejidad** | [SIMPLE_WIREFRAMES] | [INTERACTIVE_PROTOTYPES] | [COMPLEX_INTERACTIONS] | [SYSTEM_INTEGRATION] |
| **Presupuesto** | [FREE_TOOLS] | [AFFORDABLE_TOOLS] | [PROFESSIONAL_TOOLS] | [ENTERPRISE_LICENSES] |
| **Curva de Aprendizaje** | [EASY_TO_LEARN] | [MODERATE_LEARNING] | [ADVANCED_SKILLS] | [SPECIALIZED_TRAINING] |

### **Factores de Selección por Contexto**

#### **Para [PROJECT_TYPE] = [WEB_APPLICATION]**
- **Herramientas Recomendadas**: `[WEB_DESIGN_TOOLS]`
- **Consideraciones**: `[RESPONSIVE_DESIGN_SUPPORT]`
- **Integraciones**: `[WEB_DEV_TOOLS_INTEGRATION]`

#### **Para [PROJECT_TYPE] = [MOBILE_APP]**
- **Herramientas Recomendadas**: `[MOBILE_DESIGN_TOOLS]`
- **Consideraciones**: `[DEVICE_PREVIEW_SUPPORT]`
- **Integraciones**: `[MOBILE_DEV_TOOLS_INTEGRATION]`

#### **Para [FIDELITY_LEVEL] = [LOW_FIDELITY]**
- **Enfoque**: `[RAPID_SKETCHING_APPROACH]`
- **Herramientas**: `[SKETCHING_TOOLS]`
- **Beneficios**: `[QUICK_ITERATION_BENEFITS]`

#### **Para [FIDELITY_LEVEL] = [HIGH_FIDELITY]**
- **Enfoque**: `[DETAILED_DESIGN_APPROACH]`
- **Herramientas**: `[ADVANCED_DESIGN_TOOLS]`
- **Beneficios**: `[REALISTIC_PREVIEW_BENEFITS]`

---

## 4) Patrones Universales de Wireframing

### **Estructura Basada en Componentes**
```
Patrón: [COMPONENT_BASED_WIREFRAMING]
├── [COMPONENT_DEFINITION]
│   ├── Tipo: [COMPONENT_TYPE]
│   ├── Referencia: [DESIGN_SYSTEM_REFERENCE]
│   ├── Variante: [COMPONENT_VARIANT]
│   └── Estado: [COMPONENT_STATE]
├── [ACCESSIBILITY_INTEGRATION]
│   ├── Rol: [ACCESSIBILITY_ROLE]
│   ├── Etiqueta: [ARIA_LABEL]
│   └── Navegación: [KEYBOARD_NAVIGATION]
└── [RESPONSIVE_BEHAVIOR]
    ├── Móvil: [MOBILE_BEHAVIOR]
    ├── Tablet: [TABLET_BEHAVIOR]
    └── Desktop: [DESKTOP_BEHAVIOR]
```

### **Diseño Dirigido por Estados**
```
Patrón: [STATE_DRIVEN_DESIGN]
├── [DEFAULT_STATE]
│   ├── Nombre: [STATE_NAME]
│   ├── Tipo: [STATE_TYPE]
│   ├── Descripción: [STATE_DESCRIPTION]
│   └── Contenido: [STATE_CONTENT]
├── [LOADING_STATE]
│   ├── Indicador: [LOADING_INDICATOR]
│   ├── Skeleton: [SKELETON_PATTERN]
│   └── Mensaje: [LOADING_MESSAGE]
├── [EMPTY_STATE]
│   ├── Ilustración: [EMPTY_ILLUSTRATION]
│   ├── Mensaje: [EMPTY_MESSAGE]
│   └── Acción: [EMPTY_ACTION]
└── [ERROR_STATE]
    ├── Tipo de Error: [ERROR_TYPE]
    ├── Mensaje: [ERROR_MESSAGE]
    └── Recuperación: [ERROR_RECOVERY]
```

### **Patrones de Interacción Universales**
```
Patrón: [INTERACTION_PATTERNS]
├── [CLICK_INTERACTION]
│   ├── Trigger: [CLICK_TRIGGER]
│   ├── Feedback: [CLICK_FEEDBACK]
│   └── Resultado: [CLICK_RESULT]
├── [HOVER_INTERACTION]
│   ├── Trigger: [HOVER_TRIGGER]
│   ├── Feedback: [HOVER_FEEDBACK]
│   └── Duración: [HOVER_DURATION]
├── [SWIPE_INTERACTION]
│   ├── Dirección: [SWIPE_DIRECTION]
│   ├── Distancia: [SWIPE_DISTANCE]
│   └── Acción: [SWIPE_ACTION]
└── [VOICE_INTERACTION]
    ├── Comando: [VOICE_COMMAND]
    ├── Respuesta: [VOICE_RESPONSE]
    └── Fallback: [VOICE_FALLBACK]
```

---

## 5) Mapeo Universal de Flujos de Usuario

### **Estructura Universal de Flujos**
```
Patrón: [USER_FLOW_MAPPING]
├── [FLOW_IDENTIFICATION]
│   ├── Nombre: [USER_FLOW_NAME]
│   ├── Tipo de Usuario: [USER_TYPE]
│   ├── Prioridad: [FLOW_PRIORITY]
│   └── Descripción: [FLOW_DESCRIPTION]
├── [FLOW_STEPS]
│   ├── Paso: [STEP_NUMBER]
│   ├── Pantalla: [SCREEN_REFERENCE]
│   ├── Acción: [USER_ACTION]
│   ├── Resultado: [EXPECTED_OUTCOME]
│   ├── Alternativas: [ALTERNATIVE_PATHS]
│   └── Errores: [ERROR_SCENARIOS]
├── [SUCCESS_METRICS]
│   ├── Criterios: [SUCCESS_CRITERIA]
│   ├── Tiempo: [COMPLETION_TIME]
│   └── Satisfacción: [USER_SATISFACTION]
└── [PAIN_POINTS]
    ├── Identificados: [PAIN_POINT]
    ├── Impacto: [PAIN_POINT_IMPACT]
    └── Soluciones: [PAIN_POINT_SOLUTIONS]
```

### **Mejores Prácticas Universales para Journey Mapping**

#### **1. Enfoque Centrado en Objetivos**
- **Objetivo del Usuario**: `[USER_GOAL]` - ¿Qué quiere lograr?
- **Contexto**: `[USER_CONTEXT]` - ¿Cuándo y dónde ocurre?
- **Motivación**: `[USER_MOTIVATION]` - ¿Por qué es importante?
- **Restricciones**: `[USER_CONSTRAINTS]` - ¿Qué limitaciones existen?

#### **2. Mapeo del Camino Feliz**
- **Flujo Ideal**: `[HAPPY_PATH_FLOW]` - Secuencia sin errores
- **Pasos Mínimos**: `[MINIMUM_STEPS]` - Ruta más eficiente
- **Puntos de Decisión**: `[DECISION_POINTS]` - Donde el usuario elige
- **Confirmaciones**: `[CONFIRMATION_POINTS]` - Validación de progreso

#### **3. Rutas Alternativas**
- **Métodos Alternativos**: `[ALTERNATIVE_METHODS]` - Diferentes formas de completar
- **Atajos**: `[SHORTCUT_PATHS]` - Rutas más rápidas para usuarios expertos
- **Recuperación**: `[RECOVERY_PATHS]` - Cómo volver al flujo principal
- **Salidas**: `[EXIT_POINTS]` - Puntos donde el usuario puede abandonar

#### **4. Gestión de Estados de Error**
- **Tipos de Error**: `[ERROR_TYPES]` - Categorías de problemas posibles
- **Mensajes**: `[ERROR_MESSAGES]` - Comunicación clara del problema
- **Acciones de Recuperación**: `[RECOVERY_ACTIONS]` - Cómo resolver el error
- **Prevención**: `[ERROR_PREVENTION]` - Cómo evitar errores comunes

#### **5. Casos Extremos y Edge Cases**
- **Escenarios Poco Comunes**: `[EDGE_CASE_SCENARIOS]` - Situaciones raras pero importantes
- **Datos Extremos**: `[EXTREME_DATA_CASES]` - Valores muy altos/bajos/vacíos
- **Condiciones de Red**: `[NETWORK_CONDITIONS]` - Conectividad pobre/intermitente
- **Dispositivos**: `[DEVICE_LIMITATIONS]` - Capacidades limitadas del dispositivo

---

## 6) Accessibility-First Wireframing

### **WCAG 2.1 Compliance Checklist**
```javascript
{
  "accessibility": {
    "wcagLevel": "AA",
    "keyboardNavigation": true,
    "screenReaderSupport": true,
    "colorContrast": true,
    "focusManagement": true,
    "ariaLabels": [
      "Main navigation",
      "Search form",
      "User account menu"
    ],
    "landmarks": [
      "header", "nav", "main", "aside", "footer"
    ]
  }
}
```

### **Accessibility Considerations**
- **Keyboard Navigation**: Tab order, focus indicators, skip links
- **Screen Readers**: ARIA labels, semantic markup, alt text
- **Color Contrast**: 4.5:1 for normal text, 3:1 for large text
- **Focus Management**: Logical tab order, visible focus states
- **Responsive Design**: Works on all devices and orientations

---

## 7) Responsive Wireframing Strategy

### **Mobile-First Approach**
```javascript
{
  "responsive": {
    "mobile": {
      "visible": true,
      "layout": {
        "display": "flex",
        "size": { "width": "100%" }
      }
    },
    "tablet": {
      "visible": true,
      "layout": {
        "display": "grid",
        "size": { "width": "50%" }
      }
    },
    "desktop": {
      "visible": true,
      "layout": {
        "display": "grid",
        "size": { "width": "33%" }
      }
    }
  }
}
```

### **Breakpoint Strategy**
- **Mobile**: 320px - 767px (touch-first, vertical scrolling)
- **Tablet**: 768px - 1023px (hybrid interaction, landscape/portrait)
- **Desktop**: 1024px+ (mouse/keyboard, horizontal layouts)

---

## 8) Testing & Validation Framework

### **Usability Testing Plan**
```javascript
{
  "usabilityTests": [
    {
      "name": "Checkout Flow Usability",
      "objective": "Validate checkout process efficiency",
      "targetUsers": ["first-time-buyers", "returning-customers"],
      "tasks": [
        {
          "description": "Complete a purchase as a guest user",
          "successCriteria": "Task completed in <3 minutes",
          "expectedTime": 120
        }
      ],
      "metrics": [
        "task-completion-rate",
        "time-on-task", 
        "error-rate",
        "satisfaction-score"
      ]
    }
  ]
}
```

### **Testing Methods 2025**
- **Moderated Remote Testing**: Video calls con screen sharing
- **Unmoderated Testing**: Automated tasks con recordings
- **A/B Testing**: Comparar diferentes wireframe approaches
- **Accessibility Testing**: Screen readers, keyboard-only navigation
- **Device Testing**: Real devices vs simulators

---

## 9) Ejemplo de Template Completado

### **Ejemplo: Wireframes para [E_COMMERCE_CHECKOUT_PROJECT]**

```json
{
  "metadata": {
    "projectName": "[E_COMMERCE_PROJECT] Checkout Wireframes",
    "version": "[1.2.0]",
    "designTool": "[FIGMA_TOOL]",
    "lastUpdated": "[2025-01-15T10:30:00Z]",
    "projectContext": {
      "projectType": "[WEB_APPLICATION]",
      "fidelityLevel": "[MEDIUM_FIDELITY]",
      "targetPlatform": ["[WEB_PLATFORM]", "[MOBILE_PLATFORM]"],
      "description": "[E_COMMERCE_CHECKOUT_WIREFRAME_PROJECT]"
    }
  },
  "designContext": {
    "designSystemIntegration": {
      "systemReference": "[DESIGN_SYSTEM_URL]",
      "componentLibrary": [
        {
          "componentName": "[BUTTON_COMPONENT]",
          "componentCategory": "[ATOMIC_COMPONENT]",
          "variants": ["[PRIMARY_VARIANT]", "[SECONDARY_VARIANT]", "[GHOST_VARIANT]"],
          "states": ["[DEFAULT_STATE]", "[HOVER_STATE]", "[ACTIVE_STATE]", "[DISABLED_STATE]"]
        }
      ]
    },
    "visualFramework": {
      "layoutSystem": "[RESPONSIVE_LAYOUT]",
      "breakpoints": [
        {
          "name": "[MOBILE_BREAKPOINT]",
          "width": "[320PX_TO_767PX]"
        },
        {
          "name": "[DESKTOP_BREAKPOINT]",
          "width": "[1024PX_PLUS]"
        }
      ]
    }
  },
  "userFlows": [
    {
      "flowName": "[GUEST_CHECKOUT_FLOW]",
      "flowDescription": "[GUEST_USER_CHECKOUT_PROCESS]",
      "userType": "[GUEST_USER]",
      "flowPriority": "[CRITICAL_PRIORITY]",
      "flowSteps": [
        {
          "stepNumber": 1,
          "screenReference": "[CART_REVIEW_SCREEN]",
          "userAction": "[REVIEW_CART_ITEMS]",
          "expectedOutcome": "[USER_CONFIRMS_ITEMS]",
          "alternativePaths": ["[CONTINUE_SHOPPING]", "[SAVE_FOR_LATER]"],
          "errorHandling": ["[ITEM_UNAVAILABLE]", "[PRICE_CHANGE]"]
        }
      ],
      "successCriteria": [
        "[CHECKOUT_COMPLETED_IN_3_MINUTES]",
        "[CLEAR_PROGRESS_INDICATION]",
        "[INTUITIVE_ERROR_RECOVERY]"
      ],
      "painPoints": [
        "[TOO_MANY_FORM_FIELDS]",
        "[UNCLEAR_SHIPPING_OPTIONS]",
        "[HIDDEN_FEES_SURPRISE]"
      ]
    }
  ],
  "screens": [
    {
      "screenId": "[CART_REVIEW_SCREEN_ID]",
      "screenName": "[CART_REVIEW_SCREEN]",
      "screenType": "[LIST_SCREEN]",
      "deviceContext": {
        "targetDevice": "[RESPONSIVE_DEVICE]",
        "viewport": {
          "width": "[RESPONSIVE_WIDTH]",
          "height": "[RESPONSIVE_HEIGHT]"
        }
      },
      "screenStates": [
        {
          "stateName": "[DEFAULT_STATE]",
          "stateType": "[CONTENT_STATE]",
          "stateDescription": "[NORMAL_CART_WITH_ITEMS]",
          "wireframeContent": {
            "layout": "[FLEX_LAYOUT_STRUCTURE]",
            "components": [
              {
                "componentId": "[CART_CONTAINER_ID]",
                "componentType": "[CONTAINER_COMPONENT]",
                "content": "[CART_ITEMS_LIST]",
                "position": "[MAIN_CONTENT_AREA]"
              }
            ],
            "annotations": [
              {
                "annotationId": "[CART_ANNOTATION_1]",
                "content": "[DISPLAY_ITEM_DETAILS_NOTE]",
                "type": "[REQUIREMENT_ANNOTATION]"
              }
            ]
          }
        }
      ]
    }
  ],
  "stateManagement": {
    "stateTransitions": [
      {
        "transitionId": "[CART_TO_CHECKOUT_TRANSITION]",
        "fromState": {
          "screenId": "[CART_REVIEW_SCREEN_ID]",
          "stateName": "[DEFAULT_STATE]"
        },
        "toState": {
          "screenId": "[SHIPPING_INFO_SCREEN_ID]",
          "stateName": "[DEFAULT_STATE]"
        },
        "trigger": {
          "triggerType": "[USER_ACTION_TRIGGER]",
          "condition": "[CHECKOUT_BUTTON_CLICKED]"
        }
      }
    ]
  },
  "interactions": {
    "interactionPatterns": [
      {
        "patternName": "[CHECKOUT_BUTTON_INTERACTION]",
        "patternType": "[CLICK_INTERACTION]",
        "implementation": "[BUTTON_CLICK_HANDLER]",
        "targetElement": "[CHECKOUT_BUTTON]",
        "expectedResponse": "[NAVIGATE_TO_SHIPPING]"
      }
    ]
  },
  "accessibility": {
    "accessibilityStandards": {
      "primaryStandard": "[WCAG_2_1_STANDARD]",
      "complianceLevel": "[LEVEL_AA]"
    },
    "accessibilityFeatures": {
      "keyboardNavigation": {
        "supported": true,
        "tabOrder": "[LOGICAL_TAB_ORDER]",
        "focusManagement": "[CLEAR_FOCUS_INDICATORS]"
      },
      "screenReaderSupport": {
        "supported": true,
        "ariaLabels": ["[SHOPPING_CART_LABEL]", "[CHECKOUT_BUTTON_LABEL]"],
        "landmarks": ["[MAIN_LANDMARK]", "[NAVIGATION_LANDMARK]"]
      }
    }
  },
  "testing": {
    "testingStrategy": {
      "testingApproach": "[USABILITY_TESTING]",
      "testingPhases": ["[WIREFRAME_TESTING]", "[PROTOTYPE_TESTING]"],
      "successMetrics": ["[TASK_COMPLETION_RATE]", "[TIME_ON_TASK]"]
    },
    "validationMethods": [
      {
        "methodName": "[CHECKOUT_FLOW_TEST]",
        "objective": "[VALIDATE_CHECKOUT_EFFICIENCY]",
        "implementation": "[MODERATED_USER_TESTING]",
        "tasks": [
          {
            "taskDescription": "[COMPLETE_GUEST_CHECKOUT]",
            "successCriteria": "[COMPLETED_IN_3_MINUTES]",
            "expectedTime": "[180_SECONDS]"
          }
        ],
        "metrics": ["[TASK_COMPLETION_RATE]", "[TIME_ON_TASK]", "[ERROR_RATE]"]
      }
    ]
  }
}
```

### **Cómo Adaptar Este Ejemplo**

1. **Reemplazar Placeholders**: Sustituir todos los `[VARIABLE]` con valores específicos del proyecto
2. **Ajustar Herramienta**: Modificar según `[DESIGN_TOOL]` seleccionada
3. **Personalizar Flujos**: Adaptar `[USER_FLOWS]` según el tipo de aplicación
4. **Configurar Estados**: Definir `[SCREEN_STATES]` apropiados para el contexto
5. **Establecer Accesibilidad**: Configurar `[ACCESSIBILITY_STANDARDS]` según requisitos

---

## 10) Checklist Universal de Implementación

### **Planificación y Contexto**
- [ ] **Contexto del Proyecto**: `[PROJECT_CONTEXT]` completamente definido
- [ ] **Herramienta Seleccionada**: `[DESIGN_TOOL]` elegida según criterios
- [ ] **Tipo de Proyecto**: `[PROJECT_TYPE]` y plataforma objetivo confirmados
- [ ] **Nivel de Fidelidad**: `[FIDELITY_LEVEL]` apropiado para la fase
- [ ] **Stakeholders**: `[STAKEHOLDER_ROLES]` y responsabilidades definidas

### **Contexto de Diseño**
- [ ] **Sistema de Diseño**: `[DESIGN_SYSTEM_INTEGRATION]` configurada si aplica
- [ ] **Biblioteca de Componentes**: `[COMPONENT_LIBRARY]` disponible documentada
- [ ] **Tokens de Diseño**: `[DESIGN_TOKENS]` establecidos para consistencia
- [ ] **Framework Visual**: `[VISUAL_FRAMEWORK]` y layout system definidos
- [ ] **Breakpoints**: `[RESPONSIVE_BREAKPOINTS]` configurados apropiadamente

### **Flujos de Usuario**
- [ ] **Flujos Identificados**: `[USER_FLOWS]` mapeados y priorizados
- [ ] **Tipos de Usuario**: `[USER_TYPES]` y contextos definidos
- [ ] **Pasos del Flujo**: `[FLOW_STEPS]` documentados con alternativas
- [ ] **Criterios de Éxito**: `[SUCCESS_CRITERIA]` medibles establecidos
- [ ] **Puntos de Dolor**: `[PAIN_POINTS]` identificados y abordados

### **Pantallas y Estados**
- [ ] **Pantallas Definidas**: `[SCREENS]` con nombres y tipos claros
- [ ] **Estados Mapeados**: `[SCREEN_STATES]` completos para cada pantalla
- [ ] **Contenido Wireframe**: `[WIREFRAME_CONTENT]` estructurado apropiadamente
- [ ] **Anotaciones**: `[ANNOTATIONS]` explicativas y claras incluidas
- [ ] **Contexto de Dispositivo**: `[DEVICE_CONTEXT]` y viewport configurados

### **Gestión de Estados e Interacciones**
- [ ] **Transiciones**: `[STATE_TRANSITIONS]` entre pantallas definidas
- [ ] **Triggers**: `[TRIGGER_TYPES]` y condiciones especificadas
- [ ] **Patrones de Interacción**: `[INTERACTION_PATTERNS]` consistentes implementados
- [ ] **Mecanismos de Feedback**: `[FEEDBACK_MECHANISMS]` apropiados establecidos
- [ ] **Lógica de Estados**: `[STATE_LOGIC]` y reglas documentadas

### **Accesibilidad**
- [ ] **Estándares**: `[ACCESSIBILITY_STANDARDS]` seleccionados y aplicados
- [ ] **Nivel de Cumplimiento**: `[COMPLIANCE_LEVEL]` objetivo establecido
- [ ] **Navegación por Teclado**: `[KEYBOARD_NAVIGATION]` implementada
- [ ] **Soporte de Lector de Pantalla**: `[SCREEN_READER_SUPPORT]` configurado
- [ ] **Accesibilidad Visual**: `[VISUAL_ACCESSIBILITY]` consideraciones aplicadas

### **Testing y Validación**
- [ ] **Estrategia de Testing**: `[TESTING_STRATEGY]` definida y planificada
- [ ] **Métodos de Validación**: `[VALIDATION_METHODS]` seleccionados apropiadamente
- [ ] **Usuarios Objetivo**: `[TARGET_USERS]` para testing identificados
- [ ] **Tareas de Testing**: `[TESTING_TASKS]` y criterios de éxito definidos
- [ ] **Métricas**: `[TESTING_METRICS]` para medir efectividad establecidas

### **Documentación y Entrega**
- [ ] **Anotaciones Completas**: `[ANNOTATION_CONTENT]` explicativo incluido
- [ ] **Especificaciones**: `[WIREFRAME_SPECIFICATIONS]` técnicas documentadas
- [ ] **Plan de Iteración**: `[ITERATION_PLAN]` basado en feedback definido
- [ ] **Criterios de Mejora**: `[IMPROVEMENT_CRITERIA]` establecidos
- [ ] **Método de Priorización**: `[PRIORITIZATION_METHOD]` para mejoras definido

---

## 11) Recursos y Referencias Universales

### **Categorías de Herramientas por Contexto**
- **Herramientas de `[LOW_FIDELITY]`**: Para sketching rápido y conceptos iniciales
- **Herramientas de `[MEDIUM_FIDELITY]`**: Para wireframes estructurados con interacciones básicas
- **Herramientas de `[HIGH_FIDELITY]`**: Para prototipos detallados y presentaciones
- **Herramientas de `[COLLABORATIVE_DESIGN]`**: Para trabajo en equipo y feedback

### **Estándares de Accesibilidad por Contexto**
- **`[WCAG_GUIDELINES]`**: Estándares web universales de accesibilidad
- **`[PLATFORM_SPECIFIC_GUIDELINES]`**: Guías específicas por plataforma (iOS, Android, Web)
- **`[INDUSTRY_STANDARDS]`**: Estándares específicos por industria (salud, finanzas, gobierno)
- **`[TESTING_TOOLS]`**: Herramientas para validar accesibilidad

### **Metodologías de Testing por Tipo de Proyecto**
- **`[USABILITY_TESTING_METHODS]`**: Para validar facilidad de uso
- **`[ACCESSIBILITY_TESTING_METHODS]`**: Para validar inclusividad
- **`[PERFORMANCE_TESTING_METHODS]`**: Para validar eficiencia
- **`[CROSS_PLATFORM_TESTING]`**: Para validar consistencia entre dispositivos

### **Patrones de Diseño por Dominio**
- **`[E_COMMERCE_PATTERNS]`**: Patrones específicos para comercio electrónico
- **`[DASHBOARD_PATTERNS]`**: Patrones para interfaces de administración
- **`[MOBILE_PATTERNS]`**: Patrones específicos para aplicaciones móviles
- **`[RESPONSIVE_PATTERNS]`**: Patrones para diseño adaptativo

### **Recursos de Aprendizaje por Nivel**
- **`[BEGINNER_RESOURCES]`**: Para iniciarse en wireframing
- **`[INTERMEDIATE_RESOURCES]`**: Para mejorar técnicas y procesos
- **`[ADVANCED_RESOURCES]`**: Para especialización y liderazgo
- **`[TEAM_RESOURCES]`**: Para coordinación y colaboración en equipo

### **Plantillas y Frameworks**
- **`[WIREFRAME_TEMPLATES]`**: Templates base para diferentes tipos de proyecto
- **`[COMPONENT_LIBRARIES]`**: Bibliotecas de componentes reutilizables
- **`[DESIGN_SYSTEMS]`**: Sistemas de diseño de referencia
- **`[PROCESS_FRAMEWORKS]`**: Marcos de trabajo para procesos de diseño

---

**Versión del Template:** 3.0 - Template Universal con Placeholders  
**Última actualización:** Enero 2025 con metodología template-first y patrones universales  
**Compatibilidad:** Cualquier herramienta de diseño, tipo de proyecto y nivel de fidelidad
