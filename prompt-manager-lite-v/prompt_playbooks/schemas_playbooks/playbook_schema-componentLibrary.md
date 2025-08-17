# Playbook: Universal Component Library Schema Template

## Propósito
Este playbook guía el uso del schema `componentLibrary.json` como template universal para documentar bibliotecas de componentes UI. El schema utiliza placeholders `[VARIABLE]` que deben ser reemplazados con información específica del proyecto, permitiendo adaptabilidad a cualquier framework UI, tecnología o metodología de design system.

## Filosofía Template-First
- **Schema como Receptor**: El schema está diseñado para RECIBIR información, no para definirla
- **Placeholders Universales**: Usar `[VARIABLE]` para todos los valores específicos del proyecto
- **Adaptabilidad Total**: Funciona para cualquier framework UI (React, Vue, Angular, Web Components, etc.)
- **Mejores Prácticas Generales**: Incorpora patrones universales de component libraries sin prescribir tecnologías específicas

## Mejores Prácticas Investigadas (2025)

### 1. Design Systems Modernos
- **Component-Driven Development**: Desarrollo centrado en componentes reutilizables
- **Design Tokens**: Sistema de tokens para consistencia visual y temática
- **Atomic Design**: Metodología de componentes jerárquicos (Atoms → Molecules → Organisms)
- **Accessibility-First**: WCAG 2.1 AA como estándar mínimo
- **Cross-Platform**: Soporte para web, mobile, desktop

### 2. Design Tokens 2025
- **W3C Design Tokens**: Estándar emergente para tokens
- **Figma Variables**: Integración nativa con herramientas de diseño
- **Style Dictionary**: Transformación automática de tokens a código
- **Semantic Tokens**: Tokens contextuales que se adaptan a temas
- **Token Hierarchies**: Primitive → Semantic → Component tokens

### 3. Herramientas y Frameworks Líderes
#### Documentation Platforms
- **Storybook**: Líder en documentación de componentes, v8+ con mejoras
- **Docusaurus**: Para documentación completa de design systems
- **Custom Platforms**: Soluciones específicas para empresas

#### Development Frameworks
- **React**: Ecosistema maduro, React 19 con mejoras
- **Vue 3**: Composition API, mejor TypeScript support
- **Web Components**: Estándar nativo, framework-agnostic
- **Multi-Framework**: Soporte para múltiples frameworks

#### Testing Tools
- **Chromatic**: Visual regression testing líder
- **Jest/Vitest**: Unit testing moderno
- **axe-core**: Accessibility testing automatizado
- **Playwright**: E2E testing cross-browser

### 4. Accessibility Standards 2025
- **WCAG 2.1 AA**: Estándar mínimo requerido
- **WCAG 2.2**: Nuevos criterios de éxito
- **ARIA Patterns**: Patrones de interacción estándar
- **Keyboard Navigation**: Navegación completa por teclado
- **Screen Reader Support**: Testing con herramientas reales
- **Color Contrast**: Ratios mínimos 4.5:1 (AA) o 7:1 (AAA)

### 5. Performance y Optimización
- **Tree Shaking**: Importación selectiva de componentes
- **Bundle Splitting**: Componentes como módulos separados
- **Lazy Loading**: Carga bajo demanda
- **Performance Budgets**: Límites de tamaño por componente

## Cómo Usar Este Template

### Paso 1: Identificar Información del Proyecto
Antes de llenar el template, recopila la siguiente información:
- **Framework UI**: ¿Qué tecnología usarás? (React, Vue, Angular, Web Components, etc.)
- **Design System**: ¿Tienes un design system existente o crearás uno nuevo?
- **Componentes**: ¿Qué componentes necesitas documentar?
- **Herramientas**: ¿Qué herramientas de documentación, testing, etc. usarás?

### Paso 2: Reemplazar Placeholders
Busca todos los placeholders `[VARIABLE]` en el schema y reemplázalos con valores específicos:

```json
// Template (antes):
{
  "libraryName": "[LIBRARY_NAME]",
  "framework": "[UI_FRAMEWORK]",
  "components": [
    {
      "name": "[COMPONENT_NAME]",
      "category": "[COMPONENT_CATEGORY]"
    }
  ]
}

// Completado (después):
{
  "libraryName": "Acme Design System",
  "framework": "React",
  "components": [
    {
      "name": "Button",
      "category": "Form"
    }
  ]
}
```

### Paso 3: Adaptar Estructura a tu Contexto
El template es flexible. Puedes:
- **Agregar componentes específicos** que necesites para tu proyecto
- **Omitir secciones opcionales** que no apliquen
- **Modificar categorías** para que reflejen tu organización

## Estructura del Schema Template

### Secciones Requeridas

#### 1. **libraryInfo** (Requerido)
Información básica de la biblioteca usando placeholders:
- `libraryName`: `[LIBRARY_NAME]` → Nombre de tu biblioteca
- `version`: `[LIBRARY_VERSION]` → Versión actual
- `framework`: `[UI_FRAMEWORK]` → Tu framework UI
- `description`: `[LIBRARY_DESCRIPTION]` → Descripción del propósito

#### 2. **designSystem** (Requerido)
Sistema de diseño usando placeholders:
- `designTokens.colors`: `[PRIMARY_COLOR]`, `[SECONDARY_COLOR]` → Tus colores
- `designTokens.typography`: `[FONT_FAMILY]`, `[FONT_SIZE]` → Tu tipografía
- `brandGuidelines.brandName`: `[BRAND_NAME]` → Nombre de tu marca

#### 3. **components** (Requerido)
Lista de componentes con placeholders:
- `name`: `[COMPONENT_NAME]` → Nombres de tus componentes
- `category`: `[COMPONENT_CATEGORY]` → Categorías que uses
- `props[].name`: `[PROP_NAME]` → Propiedades específicas

#### 4. **documentation** (Requerido)
Configuración de documentación con placeholders:
- `storybookConfig.tool`: `[DOCUMENTATION_TOOL]` → Tu herramienta de docs
- `storybookConfig.url`: `[DOCUMENTATION_URL]` → URL de tu documentación

### Secciones Opcionales

#### 5. **buildAndDeploy**
Configuración de build con placeholders `[BUILD_TOOL]`, `[PACKAGE_REGISTRY]`

#### 6. **governance**
Governance con placeholders `[VERSIONING_STRATEGY]`, `[RELEASE_SCHEDULE]`

## Ejemplos de Adaptación del Template

### Ejemplo 1: Biblioteca React
**Contexto**: Component library para aplicación React con TypeScript

**Placeholders Reemplazados**:
```json
{
  "libraryInfo": {
    "libraryName": "Acme Design System", // [LIBRARY_NAME]
    "version": "2.1.0", // [LIBRARY_VERSION]
    "framework": "React", // [UI_FRAMEWORK]
    "description": "Component library for Acme's web applications", // [LIBRARY_DESCRIPTION]
    "buildTool": "Vite", // [BUILD_TOOL]
    "packageManager": "npm" // [PACKAGE_MANAGER]
  },
  "designSystem": {
    "designTokens": {
      "colors": {
        "primary": {
          "primary": "#3B82F6", // [PRIMARY_COLOR]
          "secondary": "#10B981" // [SECONDARY_COLOR]
        }
      },
      "typography": {
        "fontFamilies": {
          "primary": "Inter, sans-serif" // [FONT_FAMILY]
        }
      }
    },
    "brandGuidelines": {
      "brandName": "Acme Corporation", // [BRAND_NAME]
      "brandValues": ["Innovation", "Reliability", "User-Centric"] // [BRAND_VALUE]
    }
  },
  "designTokens": {
    "tokenFormat": "Style-Dictionary",
    "categories": {
      "colors": {
        "primitive": [
          {
            "name": "blue-500",
            "value": "#3B82F6",
            "description": "Primary blue color"
          }
        ],
        "semantic": [
          {
            "name": "color-primary",
            "lightValue": "#3B82F6",
            "darkValue": "#60A5FA",
            "contrastRatio": 4.5,
            "usage": "Primary actions and links"
          }
        ]
      },
      "typography": {
        "fontFamilies": [
          {
            "name": "primary",
            "stack": "Inter, -apple-system, BlinkMacSystemFont, sans-serif",
            "weights": [400, 500, 600, 700],
            "webfontUrl": "https://fonts.googleapis.com/css2?family=Inter"
          }
        ],
        "scales": [
          {
            "name": "heading-1",
            "size": "2.25rem",
            "lineHeight": 1.2,
            "letterSpacing": "-0.025em"
          }
        ]
      },
      "spacing": {
        "scale": "Modular",
        "values": [
          {
            "name": "space-1",
            "value": "0.25rem",
            "usage": "Small gaps and padding"
          },
          {
            "name": "space-4",
            "value": "1rem",
            "usage": "Standard spacing unit"
          }
        ]
      }
    },
    "themes": [
      {
        "name": "light",
        "description": "Default light theme",
        "tokens": {
          "color-background": "#FFFFFF",
          "color-text": "#1F2937"
        },
        "default": true
      },
      {
        "name": "dark",
        "description": "Dark theme for low-light environments",
        "tokens": {
          "color-background": "#1F2937",
          "color-text": "#F9FAFB"
        },
        "mediaQuery": "(prefers-color-scheme: dark)"
      }
    ],
    "tooling": {
      "figmaIntegration": {
        "enabled": true,
        "fileId": "abc123def456",
        "tokensPlugin": "Tokens-Studio"
      },
      "styleDictionary": {
        "enabled": true,
        "configPath": "./tokens/config.json",
        "platforms": ["web", "ios", "android"]
      }
    }
  },
  "components": [
    {
      "id": "button",
      "name": "Button",
      "category": "Atoms",
      "status": "Stable",
      "description": "Interactive button component for user actions",
      "purpose": "Use for primary and secondary actions throughout the interface",
      "api": {
        "props": [
          {
            "name": "variant",
            "type": "enum",
            "required": false,
            "default": "primary",
            "description": "Visual style variant",
            "enumValues": ["primary", "secondary", "outline", "ghost"],
            "since": "1.0.0"
          },
          {
            "name": "size",
            "type": "enum",
            "required": false,
            "default": "medium",
            "description": "Button size",
            "enumValues": ["small", "medium", "large"],
            "since": "1.0.0"
          },
          {
            "name": "disabled",
            "type": "boolean",
            "required": false,
            "default": false,
            "description": "Whether the button is disabled",
            "since": "1.0.0"
          },
          {
            "name": "loading",
            "type": "boolean",
            "required": false,
            "default": false,
            "description": "Shows loading state with spinner",
            "since": "1.2.0"
          },
          {
            "name": "onClick",
            "type": "function",
            "required": false,
            "description": "Click event handler"
          }
        ],
        "events": [
          {
            "name": "click",
            "description": "Fired when button is clicked",
            "payloadSchema": {
              "type": "object",
              "properties": {
                "event": {"type": "object"}
              }
            },
            "when": "User clicks the button and it's not disabled"
          }
        ]
      },
      "accessibility": {
        "wcagLevel": "AA",
        "ariaSupport": {
          "roles": ["button"],
          "properties": ["aria-label", "aria-describedby"],
          "states": ["aria-disabled", "aria-pressed"]
        },
        "keyboardNavigation": {
          "supported": true,
          "shortcuts": [
            {
              "key": "Enter",
              "action": "Activate button"
            },
            {
              "key": "Space",
              "action": "Activate button"
            }
          ],
          "focusManagement": "Receives focus and shows focus indicator"
        },
        "screenReader": {
          "tested": true,
          "tools": ["NVDA", "JAWS", "VoiceOver"],
          "announcements": "Announces button text and state"
        },
        "colorContrast": {
          "minimumRatio": 4.5,
          "tested": true,
          "variants": ["primary", "secondary", "outline"]
        },
        "reducedMotion": {
          "supported": true,
          "alternatives": "Disables hover animations when prefers-reduced-motion is set"
        }
      },
      "variants": [
        {
          "name": "primary",
          "description": "Primary action button with brand colors",
          "props": {
            "variant": "primary"
          },
          "tokens": {
            "background": "color-primary",
            "color": "color-on-primary"
          }
        },
        {
          "name": "secondary",
          "description": "Secondary action button with muted colors",
          "props": {
            "variant": "secondary"
          },
          "tokens": {
            "background": "color-secondary",
            "color": "color-on-secondary"
          }
        }
      ],
      "examples": [
        {
          "name": "Basic Usage",
          "description": "Standard button with primary variant",
          "code": "<Button variant=\"primary\">Click me</Button>",
          "interactive": true,
          "responsive": false
        },
        {
          "name": "Loading State",
          "description": "Button showing loading spinner",
          "code": "<Button loading={true}>Processing...</Button>",
          "interactive": true,
          "responsive": false
        }
      ],
      "testing": {
        "unitTests": {
          "coverage": 95,
          "framework": "Jest",
          "testFiles": ["Button.test.tsx", "Button.accessibility.test.tsx"]
        },
        "visualRegression": {
          "enabled": true,
          "tool": "Chromatic",
          "scenarios": ["default", "hover", "focus", "disabled", "loading"]
        },
        "accessibilityTests": {
          "automated": true,
          "tools": ["axe-core", "jest-axe"],
          "manualChecklist": true
        }
      },
      "performance": {
        "bundleSize": "2.3KB gzipped",
        "renderTime": "< 1ms",
        "memoryUsage": "Minimal",
        "optimizations": ["Tree shaking", "CSS-in-JS optimization"]
      },
      "dependencies": {
        "internal": ["Icon", "Spinner"],
        "external": ["react"],
        "peerDependencies": ["react@^18.0.0"]
      },
      "versioning": {
        "version": "2.1.0",
        "changelog": "https://github.com/acme/design-system/blob/main/CHANGELOG.md#button",
        "breaking": false
      },
      "designSpecs": {
        "figmaUrl": "https://figma.com/file/abc123/Button-Component",
        "designTokens": ["color-primary", "space-2", "border-radius-md"],
        "states": ["default", "hover", "focus", "active", "disabled", "loading"]
      },
      "usage": {
        "guidelines": "Use buttons for actions that users can take. Prefer primary buttons for the most important action on a page.",
        "doAndDont": {
          "do": [
            "Use clear, action-oriented labels",
            "Provide adequate spacing between buttons",
            "Use loading states for async actions"
          ],
          "dont": [
            "Use buttons for navigation (use links instead)",
            "Stack too many primary buttons together",
            "Make buttons too small for touch targets"
          ]
        },
        "bestPractices": [
          "Keep button text concise and descriptive",
          "Ensure minimum 44px touch target size",
          "Provide visual feedback for all interactions"
        ],
        "commonMistakes": [
          "Using buttons for navigation",
          "Not providing loading states",
          "Insufficient color contrast"
        ]
      },
      "metadata": {
        "tags": ["interactive", "form", "action"],
        "keywords": ["button", "click", "action", "form"],
        "author": "Design System Team",
        "maintainer": "john.doe@acme.com",
        "created": "2023-01-15T10:00:00Z",
        "lastModified": "2024-12-08T14:30:00Z",
        "reviewers": ["jane.smith@acme.com", "bob.wilson@acme.com"]
      }
    }
  ],
  "documentation": {
    "platform": "Storybook",
    "url": "https://storybook.acme.com",
    "features": {
      "interactiveExamples": true,
      "codePlayground": true,
      "designSpecs": true,
      "accessibilityDocs": true,
      "usageAnalytics": false
    },
    "automation": {
      "autoGeneration": true,
      "propsExtraction": true,
      "exampleGeneration": false,
      "screenshotGeneration": true
    },
    "maintenance": {
      "updateFrequency": "On-Release",
      "reviewProcess": "PR review required for all documentation changes",
      "qualityChecks": ["Accessibility audit", "Content review", "Code examples validation"]
    }
  },
  "tooling": {
    "development": {
      "buildSystem": "Vite",
      "bundling": {
        "strategy": "Per-Component",
        "formats": ["ESM", "CJS"],
        "treeshaking": true
      },
      "typescript": {
        "enabled": true,
        "strict": true,
        "declarationFiles": true
      },
      "linting": {
        "eslint": true,
        "prettier": true,
        "stylelint": false,
        "customRules": ["@acme/design-system-rules"]
      }
    },
    "design": {
      "figmaIntegration": {
        "enabled": true,
        "fileId": "abc123def456",
        "tokenSync": true,
        "componentSync": false
      },
      "designToCode": {
        "enabled": false,
        "tool": "Figma-to-Code",
        "automation": false
      }
    },
    "testing": {
      "unitTesting": {
        "framework": "Jest",
        "coverage": true,
        "threshold": 90
      },
      "visualTesting": {
        "enabled": true,
        "tool": "Chromatic",
        "browsers": ["chrome", "firefox", "safari"]
      },
      "accessibilityTesting": {
        "automated": true,
        "tools": ["axe-core", "jest-axe"],
        "ciIntegration": true
      }
    },
    "cicd": {
      "platform": "GitHub-Actions",
      "automation": {
        "testing": true,
        "building": true,
        "publishing": true,
        "documentation": true
      },
      "qualityGates": ["Tests-Pass", "Coverage-Threshold", "Linting-Pass", "Accessibility-Check"]
    }
  },
  "governance": {
    "contributionProcess": {
      "proposalProcess": "RFC process for new components, GitHub issues for enhancements",
      "reviewCriteria": ["Design consistency", "Accessibility compliance", "Performance impact", "API design"],
      "approvalWorkflow": "Design review → Development review → Accessibility review → Approval",
      "rfcProcess": true
    },
    "maintenance": {
      "team": ["Design System Team", "Frontend Guild"],
      "responsibilities": ["Component development", "Documentation", "Breaking change communication"],
      "updateCadence": "Bi-weekly releases",
      "deprecationPolicy": "6-month deprecation notice with migration guide"
    },
    "adoption": {
      "guidelines": "https://design.acme.com/adoption-guide",
      "training": "Monthly design system workshops",
      "support": "Slack channel #design-system-support",
      "metrics": ["Component usage", "Adoption rate", "Developer satisfaction"]
    }
  }
}
```

## Validaciones Automáticas

### Validaciones de Estructura
- Todas las secciones requeridas están presentes
- IDs de componentes son únicos y siguen kebab-case
- Nombres de componentes siguen PascalCase
- Versiones siguen semantic versioning

### Validaciones de Accesibilidad
- Todos los componentes tienen nivel WCAG definido
- Componentes interactivos tienen keyboard navigation
- Color contrast ratios están definidos
- ARIA support está documentado

### Validaciones de Design Tokens
- Tokens siguen formato especificado
- Valores de color son válidos
- Spacing values siguen unidades consistentes
- Typography scales están bien definidas

## Herramientas Recomendadas

### Documentation
- **Storybook**: Líder en documentación de componentes
- **Docusaurus**: Para documentación completa
- **Zeroheight**: Plataforma especializada en design systems

### Design Tokens
- **Style Dictionary**: Transformación de tokens
- **Tokens Studio**: Plugin de Figma para tokens
- **Figma Variables**: Variables nativas de Figma

### Testing
- **Chromatic**: Visual regression testing
- **Jest/Vitest**: Unit testing
- **axe-core**: Accessibility testing
- **Playwright**: E2E testing

### Development
- **Vite**: Build tool moderno y rápido
- **TypeScript**: Type safety
- **ESLint + Prettier**: Code quality

## Casos de Uso Comunes

### 1. Startup/Producto Simple
- Framework: React o Vue
- Tokens: Básicos (colors, spacing, typography)
- Documentación: Storybook básico
- Testing: Unit tests + accessibility

### 2. Empresa Mediana
- Framework: Multi-framework
- Tokens: Sistema completo con temas
- Documentación: Storybook + custom docs
- Testing: Visual regression + accessibility

### 3. Enterprise
- Framework: Multi-framework + Web Components
- Tokens: Sistema complejo con múltiples marcas
- Documentación: Plataforma custom
- Testing: Suite completa + performance

## Mantenimiento y Evolución

### Versionado
- Semantic versioning para el design system
- Versionado independiente por componente
- Changelog detallado con breaking changes

### Deprecación
- Proceso de deprecación de 6 meses
- Migration guides para breaking changes
- Comunicación proactiva a equipos

### Métricas
- Adoption rate por componente
- Performance metrics
- Developer satisfaction surveys

## Referencias y Recursos

### Estándares
- [W3C Design Tokens](https://design-tokens.github.io/community-group/format/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Atomic Design](https://atomicdesign.bradfrost.com/)

### Herramientas
- [Storybook](https://storybook.js.org/)
- [Style Dictionary](https://amzn.github.io/style-dictionary/)
- [Figma Tokens](https://tokens.studio/)

### Mejores Prácticas
- [Design Systems Handbook](https://www.designbetter.co/design-systems-handbook)
- [Component-Driven Development](https://www.componentdriven.org/)
- [Inclusive Components](https://inclusive-components.design/)