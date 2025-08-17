# Playbook: Universal Visual Blueprint Schema Template

## Propósito
Este playbook guía el uso del schema `visualBlueprint.json` como template universal para documentar blueprints visuales, wireframes y especificaciones de diseño UI/UX. El schema utiliza placeholders `[VARIABLE]` que deben ser reemplazados con información específica del proyecto, permitiendo adaptabilidad a cualquier herramienta de diseño, plataforma o metodología de UX.

## Filosofía Template-First
- **Schema como Receptor**: El schema está diseñado para RECIBIR información, no para definirla
- **Placeholders Universales**: Usar `[VARIABLE]` para todos los valores específicos del proyecto
- **Adaptabilidad Total**: Funciona para cualquier herramienta de diseño (Figma, Sketch, Adobe XD, etc.)
- **Mejores Prácticas Generales**: Incorpora patrones universales de wireframing sin prescribir herramientas específicas

## Mejores Prácticas Investigadas (2025)

### 1. Enfoques de Diseño UX Modernos
- **Mobile-First Design**: Diseño que prioriza la experiencia móvil
- **Progressive Enhancement**: Mejora progresiva de funcionalidades
- **Accessibility-First**: Accesibilidad como consideración primaria
- **User-Centered Design**: Diseño centrado en el usuario y sus necesidades
- **Design Systems Integration**: Integración con sistemas de diseño

### 2. Information Architecture 2025
- **Content-First Approach**: Arquitectura basada en contenido
- **Semantic Structure**: Estructura semántica y significativa
- **Progressive Disclosure**: Revelación progresiva de información
- **Cross-Platform Consistency**: Consistencia entre plataformas
- **AI-Powered IA**: Arquitectura de información potenciada por IA

### 3. User Journey Mapping Moderno
- **Omnichannel Journeys**: Experiencias multi-canal
- **Emotional Journey Mapping**: Mapeo de emociones del usuario
- **Real-Time Analytics**: Análisis en tiempo real de comportamiento
- **Personalization**: Personalización basada en datos
- **Micro-Interactions**: Interacciones detalladas y contextuales

### 4. Herramientas de Diseño Líderes 2025
#### Design Tools
- **Figma**: Líder en colaboración y design systems
- **Adobe XD**: Integración con Creative Cloud
- **Sketch**: Maduro en ecosistema Mac
- **Framer**: Prototyping avanzado e interactivo

#### Wireframing Tools
- **Figma**: Wireframing integrado con design system
- **Balsamiq**: Wireframes de baja fidelidad
- **Whimsical**: User flows y wireframes
- **Miro**: Colaboración y mapping

#### Prototyping Tools
- **Figma**: Prototyping nativo
- **Framer**: Prototypes de alta fidelidad
- **Principle**: Animaciones y transiciones
- **ProtoPie**: Prototypes complejos e interactivos

### 5. Responsive Design Patterns 2025
- **Container Queries**: Queries basadas en contenedor
- **Intrinsic Web Design**: Diseño web intrínseco
- **Fluid Typography**: Tipografía fluida y escalable
- **Component-Based Responsive**: Componentes responsivos
- **Performance-First**: Rendimiento como prioridad

### 6. Accessibility Standards 2025
- **WCAG 2.2**: Nuevos criterios de éxito
- **Inclusive Design**: Diseño inclusivo por defecto
- **Cognitive Accessibility**: Accesibilidad cognitiva
- **Voice Interface**: Interfaces de voz accesibles
- **AI-Assisted A11y**: Accesibilidad asistida por IA

## Estructura del Schema

### Secciones Principales

#### 1. **projectInfo** (Requerido)
Metadata del proyecto y enfoque de diseño.

```json
{
  "projectInfo": {
    "name": "E-commerce Mobile App",
    "version": "2.1.0",
    "designApproach": "Mobile-First",
    "targetPlatforms": ["iOS", "Android", "Web"]
  }
}
```

#### 2. **informationArchitecture** (Requerido)
Arquitectura de información y organización de contenido.

**Campos Requeridos:**
- `sitemap`: Estructura y páginas del sitio
- `navigation`: Navegación primaria y patrones

#### 3. **userJourneys** (Requerido)
Mapeo de experiencias y flujos de usuario.

**Campos Requeridos por Journey:**
- `id`: Identificador único
- `name`: Nombre del journey
- `userType`: Tipo de usuario/persona
- `goal`: Objetivo del usuario
- `steps`: Pasos del journey

#### 4. **wireframes** (Requerido)
Wireframes y definiciones de pantallas.

**Campos Requeridos:**
- `fidelity`: Nivel de fidelidad
- `screens`: Pantallas y layouts

#### 5. **responsiveDesign** (Requerido)
Estrategia de diseño responsivo.

**Campos Requeridos:**
- `approach`: Enfoque responsivo
- `breakpoints`: Puntos de quiebre

### Secciones Opcionales

#### 6. **accessibility**
Requisitos y consideraciones de accesibilidad.

#### 7. **prototyping**
Estrategia de prototipado e interactividad.

#### 8. **designAssets**
Assets de diseño y recursos.

#### 9. **designTokens**
Integración con design tokens.

## Ejemplos de Uso

### Ejemplo Básico: E-commerce Mobile App
```json
{
  "projectInfo": {
    "name": "ShopEasy Mobile App",
    "version": "2.1.0",
    "designApproach": "Mobile-First",
    "targetPlatforms": ["iOS", "Android", "Web"],
    "designSystem": {
      "name": "ShopEasy Design System",
      "version": "1.5.0",
      "reference": "https://design.shopeasy.com"
    },
    "stakeholders": [
      {
        "role": "Product-Owner",
        "name": "Sarah Johnson",
        "responsibilities": ["Product vision", "Requirements", "Prioritization"]
      },
      {
        "role": "UX-Designer",
        "name": "Mike Chen",
        "responsibilities": ["User research", "Journey mapping", "Wireframing"]
      }
    ]
  },
  "informationArchitecture": {
    "sitemap": {
      "structure": "Hierarchical",
      "pages": [
        {
          "id": "home",
          "title": "Home",
          "level": 1,
          "route": "/",
          "purpose": "Main landing page showcasing featured products and categories",
          "contentType": "Landing",
          "priority": "Critical",
          "userTypes": ["Guest", "Customer", "Premium"]
        },
        {
          "id": "product-catalog",
          "title": "Product Catalog",
          "level": 2,
          "parent": "home",
          "route": "/products",
          "purpose": "Browse and filter products by category and attributes",
          "contentType": "Category",
          "priority": "Critical",
          "userTypes": ["Guest", "Customer", "Premium"]
        },
        {
          "id": "product-detail",
          "title": "Product Detail",
          "level": 3,
          "parent": "product-catalog",
          "route": "/products/:id",
          "purpose": "Detailed product information, reviews, and purchase options",
          "contentType": "Detail",
          "priority": "Critical",
          "userTypes": ["Guest", "Customer", "Premium"]
        },
        {
          "id": "shopping-cart",
          "title": "Shopping Cart",
          "level": 2,
          "parent": "home",
          "route": "/cart",
          "purpose": "Review selected items before checkout",
          "contentType": "Form",
          "priority": "High",
          "userTypes": ["Customer", "Premium"]
        }
      ]
    },
    "navigation": {
      "primary": {
        "type": "Bottom-Tab",
        "items": [
          {
            "label": "Home",
            "route": "/",
            "icon": "home"
          },
          {
            "label": "Categories",
            "route": "/categories",
            "icon": "grid"
          },
          {
            "label": "Search",
            "route": "/search",
            "icon": "search"
          },
          {
            "label": "Cart",
            "route": "/cart",
            "icon": "shopping-cart"
          },
          {
            "label": "Profile",
            "route": "/profile",
            "icon": "user"
          }
        ],
        "responsive": {
          "mobile": "Bottom-Tab",
          "tablet": "Side-Bar",
          "desktop": "Top-Bar"
        }
      },
      "secondary": [
        {
          "type": "Breadcrumb",
          "context": "Product pages",
          "behavior": "Shows navigation path from home to current product"
        },
        {
          "type": "Filter",
          "context": "Product catalog",
          "behavior": "Allows filtering by price, brand, rating, etc."
        }
      ],
      "patterns": ["Progressive-Disclosure", "Tabbed", "Accordion"]
    },
    "contentStrategy": {
      "contentTypes": [
        {
          "name": "Product",
          "fields": ["title", "description", "price", "images", "specifications"],
          "relationships": ["category", "brand", "reviews"]
        },
        {
          "name": "Category",
          "fields": ["name", "description", "image", "subcategories"],
          "relationships": ["products", "parent-category"]
        }
      ],
      "taxonomy": {
        "categories": ["Electronics", "Clothing", "Home", "Sports"],
        "tags": ["featured", "sale", "new-arrival", "bestseller"],
        "metadata": ["brand", "color", "size", "material"]
      }
    }
  },
  "userJourneys": [
    {
      "id": "first-time-purchase",
      "name": "First Time Purchase Journey",
      "userType": "New Customer",
      "goal": "Successfully complete first purchase on the mobile app",
      "scenario": "User discovers the app through social media ad and wants to buy a specific product",
      "steps": [
        {
          "id": "discover",
          "title": "App Discovery",
          "action": "Downloads app from app store",
          "touchpoint": "App Store",
          "thoughts": "Curious about the app, checking reviews and screenshots",
          "painPoints": ["App store reviews are mixed", "Download size is large"],
          "opportunities": ["Improve app store presence", "Optimize app size"],
          "duration": "2-3 minutes",
          "channels": ["Mobile"]
        },
        {
          "id": "onboarding",
          "title": "First Launch",
          "action": "Opens app and goes through onboarding",
          "touchpoint": "Onboarding Screens",
          "thoughts": "Learning how to use the app, understanding value proposition",
          "painPoints": ["Too many onboarding screens", "Skip option not clear"],
          "opportunities": ["Streamline onboarding", "Progressive onboarding"],
          "duration": "1-2 minutes",
          "channels": ["Mobile"]
        },
        {
          "id": "browse",
          "title": "Product Discovery",
          "action": "Browses categories and searches for specific product",
          "touchpoint": "Home Screen, Category Pages",
          "thoughts": "Looking for specific item, comparing options",
          "painPoints": ["Search results not relevant", "Too many options"],
          "opportunities": ["Improve search algorithm", "Better filtering"],
          "duration": "5-10 minutes",
          "channels": ["Mobile"]
        },
        {
          "id": "product-view",
          "title": "Product Evaluation",
          "action": "Views product details, reads reviews, checks specifications",
          "touchpoint": "Product Detail Page",
          "thoughts": "Evaluating if product meets needs, checking credibility",
          "painPoints": ["Images don't zoom well", "Reviews seem fake"],
          "opportunities": ["Better image gallery", "Verified reviews"],
          "duration": "3-5 minutes",
          "channels": ["Mobile"]
        },
        {
          "id": "add-to-cart",
          "title": "Add to Cart",
          "action": "Selects options and adds product to cart",
          "touchpoint": "Product Detail Page",
          "thoughts": "Ready to purchase, looking for best deal",
          "painPoints": ["Shipping cost not clear", "No size guide"],
          "opportunities": ["Clear shipping info", "Size guide integration"],
          "duration": "1 minute",
          "channels": ["Mobile"]
        },
        {
          "id": "checkout",
          "title": "Checkout Process",
          "action": "Proceeds to checkout, enters shipping and payment info",
          "touchpoint": "Checkout Flow",
          "thoughts": "Wants quick and secure checkout",
          "painPoints": ["Too many form fields", "Payment options limited"],
          "opportunities": ["Guest checkout", "More payment methods"],
          "duration": "3-5 minutes",
          "channels": ["Mobile"]
        },
        {
          "id": "confirmation",
          "title": "Order Confirmation",
          "action": "Receives order confirmation and tracking info",
          "touchpoint": "Confirmation Screen, Email",
          "thoughts": "Relief that order went through, anticipation for delivery",
          "painPoints": ["Delivery date unclear", "No order tracking"],
          "opportunities": ["Clear delivery estimates", "Real-time tracking"],
          "duration": "1 minute",
          "channels": ["Mobile", "Email"]
        }
      ],
      "emotions": {
        "overall": "Mixed",
        "keyMoments": [
          {
            "step": "onboarding",
            "emotion": "Curious",
            "intensity": 3
          },
          {
            "step": "browse",
            "emotion": "Frustrated",
            "intensity": 2
          },
          {
            "step": "checkout",
            "emotion": "Anxious",
            "intensity": 4
          },
          {
            "step": "confirmation",
            "emotion": "Satisfied",
            "intensity": 4
          }
        ]
      },
      "metrics": {
        "successRate": 68,
        "completionTime": "15-25 minutes",
        "dropOffPoints": ["onboarding", "checkout"],
        "satisfactionScore": 7.2
      }
    }
  ],
  "wireframes": {
    "fidelity": "Medium",
    "methodology": "Digital-Wireframes",
    "screens": [
      {
        "id": "home-screen",
        "name": "Home Screen",
        "type": "Page",
        "purpose": "Main landing screen showcasing featured products and easy navigation",
        "userStory": "As a user, I want to quickly see featured products and navigate to different sections",
        "layout": {
          "template": "Single-Column",
          "regions": [
            {
              "name": "Header",
              "purpose": "App branding and search functionality",
              "components": ["Logo", "SearchBar", "NotificationIcon"],
              "priority": "Primary"
            },
            {
              "name": "Main",
              "purpose": "Featured content and category navigation",
              "components": ["HeroBanner", "CategoryGrid", "FeaturedProducts"],
              "priority": "Primary"
            },
            {
              "name": "Navigation",
              "purpose": "Bottom tab navigation",
              "components": ["BottomTabBar"],
              "priority": "Primary"
            }
          ]
        },
        "content": {
          "hierarchy": [
            {
              "level": 1,
              "element": "Heading",
              "content": "Welcome to ShopEasy",
              "importance": "High"
            },
            {
              "level": 2,
              "element": "Subheading",
              "content": "Featured Categories",
              "importance": "Medium"
            },
            {
              "level": 3,
              "element": "Body",
              "content": "Product descriptions and prices",
              "importance": "High"
            }
          ],
          "interactions": [
            {
              "element": "SearchBar",
              "action": "Tap",
              "result": "Navigate to search screen",
              "feedback": "Search screen slides in from right"
            },
            {
              "element": "CategoryCard",
              "action": "Tap",
              "result": "Navigate to category page",
              "feedback": "Card highlights and transitions to category"
            },
            {
              "element": "ProductCard",
              "action": "Tap",
              "result": "Navigate to product detail",
              "feedback": "Product image expands and transitions"
            }
          ]
        },
        "states": [
          {
            "name": "Default",
            "description": "Normal state with all content loaded",
            "wireframeUrl": "https://figma.com/file/abc/home-default",
            "conditions": "User is logged in and content is loaded"
          },
          {
            "name": "Loading",
            "description": "Loading state while fetching featured products",
            "wireframeUrl": "https://figma.com/file/abc/home-loading",
            "conditions": "Initial app load or refresh"
          },
          {
            "name": "Empty",
            "description": "State when no featured products are available",
            "wireframeUrl": "https://figma.com/file/abc/home-empty",
            "conditions": "No featured products configured or network error"
          }
        ],
        "annotations": [
          {
            "target": "HeroBanner",
            "note": "Should auto-rotate every 5 seconds with smooth transition",
            "type": "Behavior",
            "priority": "Medium"
          },
          {
            "target": "CategoryGrid",
            "note": "Icons should be consistent with design system",
            "type": "Design",
            "priority": "High"
          },
          {
            "target": "SearchBar",
            "note": "Must include voice search capability",
            "type": "Technical",
            "priority": "Low"
          }
        ],
        "designFiles": {
          "figmaUrl": "https://figma.com/file/abc123/home-screen",
          "prototypeUrl": "https://figma.com/proto/abc123/home-flow",
          "imageUrl": "https://assets.shopeasy.com/wireframes/home-screen.png"
        }
      }
    ]
  },
  "responsiveDesign": {
    "approach": "Mobile-First",
    "breakpoints": [
      {
        "name": "Mobile",
        "minWidth": 320,
        "maxWidth": 767,
        "description": "Primary mobile experience",
        "targetDevices": ["iPhone", "Android phones"],
        "designConsiderations": ["Touch targets 44px minimum", "Single column layout", "Bottom navigation"]
      },
      {
        "name": "Tablet",
        "minWidth": 768,
        "maxWidth": 1023,
        "description": "Tablet experience with adapted layout",
        "targetDevices": ["iPad", "Android tablets"],
        "designConsiderations": ["Two column layout", "Side navigation", "Larger touch targets"]
      },
      {
        "name": "Desktop",
        "minWidth": 1024,
        "description": "Desktop web experience",
        "targetDevices": ["Desktop browsers", "Laptops"],
        "designConsiderations": ["Multi-column layout", "Top navigation", "Hover states"]
      }
    ],
    "gridSystem": {
      "type": "12-Column",
      "columns": 12,
      "gutters": "16px",
      "margins": "20px",
      "responsive": true
    },
    "adaptiveElements": [
      {
        "element": "Navigation",
        "behavior": "Stack",
        "breakpoint": "Mobile",
        "description": "Bottom tabs on mobile, side navigation on tablet+"
      },
      {
        "element": "ProductGrid",
        "behavior": "Resize",
        "breakpoint": "Tablet",
        "description": "1 column on mobile, 2 on tablet, 3+ on desktop"
      }
    ]
  },
  "accessibility": {
    "wcagLevel": "AA",
    "considerations": [
      {
        "category": "Visual",
        "requirements": [
          "Minimum 4.5:1 contrast ratio for normal text",
          "Minimum 3:1 contrast ratio for large text",
          "Text can be resized up to 200% without loss of functionality"
        ],
        "guidelines": [
          "Use semantic color meanings",
          "Provide alternative text for images",
          "Ensure focus indicators are visible"
        ],
        "testingMethods": ["Color contrast analyzer", "Screen magnifier testing"]
      },
      {
        "category": "Motor",
        "requirements": [
          "Touch targets minimum 44x44px",
          "Adequate spacing between interactive elements",
          "Support for alternative input methods"
        ],
        "guidelines": [
          "Design for one-handed use",
          "Provide large touch targets",
          "Avoid complex gestures"
        ],
        "testingMethods": ["Switch navigation testing", "Voice control testing"]
      },
      {
        "category": "Cognitive",
        "requirements": [
          "Clear and consistent navigation",
          "Simple language and instructions",
          "Error prevention and clear error messages"
        ],
        "guidelines": [
          "Use familiar patterns",
          "Provide clear feedback",
          "Allow users to control timing"
        ],
        "testingMethods": ["Cognitive walkthrough", "User testing with diverse abilities"]
      }
    ],
    "keyboardNavigation": {
      "tabOrder": "Logical top-to-bottom, left-to-right order",
      "focusManagement": "Focus moves predictably and is always visible",
      "shortcuts": [
        {
          "key": "Tab",
          "action": "Move to next focusable element",
          "context": "Global"
        },
        {
          "key": "Shift+Tab",
          "action": "Move to previous focusable element",
          "context": "Global"
        },
        {
          "key": "Enter/Space",
          "action": "Activate focused element",
          "context": "Interactive elements"
        }
      ]
    },
    "colorContrast": {
      "minimumRatio": 4.5,
      "largeTextRatio": 3.0,
      "testingTools": ["WebAIM Contrast Checker", "Colour Contrast Analyser"],
      "colorBlindness": true
    },
    "screenReader": {
      "ariaLabels": true,
      "landmarks": true,
      "headingStructure": true,
      "altText": true
    }
  },
  "prototyping": {
    "fidelity": "High",
    "interactivity": [
      {
        "type": "Click",
        "trigger": "Product card tap",
        "response": "Navigate to product detail with slide transition",
        "duration": "300ms"
      },
      {
        "type": "Swipe",
        "trigger": "Horizontal swipe on product carousel",
        "response": "Show next/previous products",
        "duration": "250ms"
      },
      {
        "type": "Animation",
        "trigger": "Add to cart button press",
        "response": "Button scales and cart icon bounces",
        "duration": "400ms"
      }
    ],
    "userTesting": {
      "planned": true,
      "methods": ["Moderated usability testing", "A/B testing", "First-click testing"],
      "scenarios": ["First-time user onboarding", "Product search and purchase", "Account creation"],
      "metrics": ["Task completion rate", "Time on task", "Error rate", "Satisfaction score"]
    }
  },
  "designAssets": {
    "designFiles": {
      "figma": {
        "fileUrl": "https://figma.com/file/abc123/shopeasy-mobile",
        "prototypeUrl": "https://figma.com/proto/abc123/shopeasy-flow",
        "version": "2.1.0",
        "lastUpdated": "2024-12-08T14:30:00Z"
      }
    },
    "imageAssets": [
      {
        "name": "App Icon",
        "type": "Icon",
        "url": "https://assets.shopeasy.com/icons/app-icon.svg",
        "format": "SVG",
        "usage": "App icon and branding",
        "altText": "ShopEasy shopping bag logo"
      },
      {
        "name": "Hero Banner",
        "type": "Illustration",
        "url": "https://assets.shopeasy.com/images/hero-banner.webp",
        "format": "WebP",
        "usage": "Home screen hero section",
        "altText": "People shopping with mobile devices"
      }
    ],
    "iconLibrary": {
      "source": "Heroicons",
      "style": "Outline",
      "format": "SVG",
      "customIcons": ["shopping-cart-filled", "heart-filled", "star-rating"]
    }
  },
  "designTokens": {
    "integration": true,
    "tokenCategories": ["Colors", "Typography", "Spacing", "Shadows", "Border-Radius"],
    "themingSupport": true,
    "themes": [
      {
        "name": "Light Theme",
        "description": "Default light theme for daytime use",
        "preview": "https://assets.shopeasy.com/themes/light-preview.png"
      },
      {
        "name": "Dark Theme",
        "description": "Dark theme for low-light environments",
        "preview": "https://assets.shopeasy.com/themes/dark-preview.png"
      }
    ]
  }
}
```

## Validaciones Automáticas

### Validaciones de Estructura
- Todas las secciones requeridas están presentes
- IDs siguen formato kebab-case
- Rutas comienzan con "/"
- Versiones siguen semantic versioning

### Validaciones de UX
- User journeys tienen al menos 2 steps
- Wireframes tienen layout definido
- Breakpoints están en orden ascendente
- Navigation patterns son consistentes

### Validaciones de Accesibilidad
- WCAG level está definido
- Color contrast ratios son válidos
- Touch targets cumplen mínimos (44px)
- Keyboard navigation está documentada

## Herramientas Recomendadas

### Design & Wireframing
- **Figma**: Colaboración y design systems
- **Sketch**: Ecosistema Mac maduro
- **Adobe XD**: Integración Creative Cloud
- **Balsamiq**: Wireframes rápidos

### User Journey Mapping
- **Miro**: Colaboración visual
- **Whimsical**: User flows y wireframes
- **Figma**: Journey mapping integrado
- **UserForge**: Personas y journeys

### Prototyping
- **Figma**: Prototyping nativo
- **Framer**: Prototypes avanzados
- **Principle**: Animaciones
- **ProtoPie**: Interacciones complejas

### Accessibility Testing
- **axe DevTools**: Testing automatizado
- **WAVE**: Web accessibility evaluator
- **Color Oracle**: Simulador daltonismo
- **VoiceOver/NVDA**: Screen readers

## Casos de Uso Comunes

### 1. Mobile App
- Approach: Mobile-First
- Navigation: Bottom tabs
- Breakpoints: Mobile, Tablet
- Focus: Touch interactions, gestures

### 2. Web Application
- Approach: Responsive
- Navigation: Top bar + sidebar
- Breakpoints: Mobile, Tablet, Desktop
- Focus: Keyboard navigation, hover states

### 3. Cross-Platform
- Approach: Progressive Enhancement
- Navigation: Adaptive patterns
- Breakpoints: Full spectrum
- Focus: Consistency across platforms

## Mantenimiento y Evolución

### Versionado
- Semantic versioning para designs
- Change logs para updates
- Migration guides para breaking changes

### Testing Continuo
- Regular usability testing
- A/B testing de nuevos patterns
- Accessibility audits periódicos

### Actualización de Assets
- Design files sincronizados
- Asset library actualizada
- Design tokens mantenidos

## Referencias y Recursos

### Estándares
- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)
- [Mobile First Design](https://www.lukew.com/ff/entry.asp?933)
- [Progressive Enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)

### Herramientas
- [Figma](https://figma.com/)
- [Miro](https://miro.com/)
- [axe DevTools](https://www.deque.com/axe/devtools/)

### Mejores Prácticas
- [Nielsen Norman Group](https://www.nngroup.com/)
- [Material Design](https://material.io/design)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)