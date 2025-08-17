# Schema Playbook — designSystem

**Propósito:** Definir un sistema de diseño comprehensivo siguiendo las mejores prácticas 2025 para design tokens, governance de componentes, y consistencia cross-platform.

**Ubicación:** `schemas/master_blueprint_parts/designSystem.json`

**Versión:** 2.0 (Actualizado con mejores prácticas 2025)

---

## 1) Arquitectura del Schema (Mejores Prácticas 2025)

### **Estructura Jerárquica de Tokens**
```
Design Tokens Hierarchy:
├── Primitive Tokens (brand colors, base values)
├── Semantic Tokens (success, error, warning)
└── Component Tokens (button-primary-bg, input-border)
```

### **Componentes Principales**
- **`metadata`**: Información del sistema, versioning, maintainers, plataformas soportadas
- **`tokens`**: Jerarquía completa de design tokens (color, typography, spacing, animation)
- **`foundations`**: Grid system, breakpoints, z-index management
- **`components`**: Catálogo de componentes con status y accessibility specs
- **`governance`**: Workflow de contribución, criterios de aprobación, tooling
- **`accessibility`**: Estándares WCAG, contrast ratios, focus management
- **`themes`**: Soporte multi-theme y multi-brand
- **`documentation`**: Hub de documentación, guidelines, changelog

---

## 2) Metodología de Implementación 2025

### **Fase 1: Auditoría y Catalogación**
1. **Token Audit**: Inventariar todos los tokens existentes en código y diseño
2. **Accessibility Review**: Verificar contrast ratios y WCAG compliance
3. **Platform Analysis**: Identificar diferencias entre web, iOS, Android
4. **Component Mapping**: Catalogar componentes existentes y su estado

### **Fase 2: Estructura de Tokens**
1. **Primitive Tokens**: Definir colores base, tipografías, espaciado fundamental
2. **Semantic Tokens**: Crear tokens semánticos (success, error, warning, info)
3. **Component Tokens**: Tokens específicos por componente y estado
4. **Theme Variants**: Configurar light/dark mode y variantes de marca

### **Fase 3: Governance Setup**
1. **Contribution Workflow**: Definir proceso de propuesta → review → aprobación
2. **Review Criteria**: Establecer criterios de design, accessibility, technical
3. **Tooling Integration**: Configurar Figma, Storybook, Style Dictionary
4. **Automation**: Setup de CI/CD para token sync y validation

### **Fase 4: Documentation & Training**
1. **Documentation Hub**: Crear sitio centralizado con ejemplos y guidelines
2. **Component Catalog**: Documentar cada componente con props y variants
3. **Team Training**: Workshops sobre uso del sistema y contribution workflow
4. **Maintenance Plan**: Establecer schedule de auditorías y updates

---

## 3) Mejores Prácticas de Naming 2025

### **Token Naming Convention**
```
Format: [category]-[concept]-[modifier]-[state]
Examples:
- color-brand-primary (primitive)
- color-semantic-success (semantic)  
- color-button-primary-hover (component)
- space-component-button-padding (spacing)
```

### **Component Naming**
```
Format: [atomic-level]-[component-name]-[variant]
Examples:
- atom-button-primary
- molecule-card-elevated
- organism-header-navigation
```

---

## 4) Tooling Stack Recomendado 2025

### **Design Tools**
- **Figma**: Variables, Team Libraries, Design System plugins
- **Figma Tokens**: Advanced token management y sync
- **Figr Identity**: Automated design system generation

### **Development Tools**
- **Style Dictionary**: Token transformation para múltiples plataformas
- **Storybook**: Component documentation y testing
- **Chromatic**: Visual regression testing
- **Supernova**: Design-to-code handoff

### **Documentation**
- **Zeroheight**: Design system documentation hub
- **Notion/Confluence**: Collaborative guidelines y processes
- **GitBook**: Technical documentation

### **Automation & CI/CD**
- **GitHub Actions**: Automated token sync y validation
- **Semantic Release**: Automated versioning y changelogs
- **axe-core**: Automated accessibility testing

---

## 5) Accessibility Standards 2025

### **WCAG Compliance Requirements**
- **Level AA**: Minimum standard para todos los componentes
- **Color Contrast**: 4.5:1 para texto normal, 3:1 para texto grande
- **Focus Management**: Visible focus indicators, keyboard navigation
- **Screen Reader**: Proper ARIA labels, semantic markup

### **Testing Tools**
- **axe DevTools**: Browser extension para accessibility testing
- **WAVE**: Web accessibility evaluation tool
- **Lighthouse**: Automated accessibility audits
- **Color Oracle**: Color blindness simulator

---

## 6) Governance Framework

### **Contribution Workflow**
1. **Proposal**: RFC (Request for Comments) con rationale y use cases
2. **Design Review**: Visual consistency, brand alignment, accessibility
3. **Technical Review**: Performance, cross-browser compatibility, API design
4. **Documentation**: Component docs, usage examples, migration guides
5. **Approval**: Multi-stakeholder sign-off antes de merge
6. **Release**: Automated versioning, changelog, team notification

### **Review Criteria Checklist**
- [ ] **Design**: Consistent con visual hierarchy y brand guidelines
- [ ] **Accessibility**: WCAG AA compliant, keyboard navigable
- [ ] **Technical**: Cross-platform compatible, performance optimized
- [ ] **Documentation**: Complete usage docs con examples
- [ ] **Testing**: Unit tests, visual regression tests, accessibility tests

---

## 7) Multi-Platform Strategy

### **Token Distribution**
```
Style Dictionary Output:
├── web/
│   ├── css-variables.css
│   ├── scss-variables.scss
│   └── js-tokens.js
├── ios/
│   └── tokens.swift
├── android/
│   └── tokens.xml
└── react-native/
    └── tokens.js
```

### **Platform-Specific Considerations**
- **Web**: CSS custom properties, responsive tokens
- **iOS**: Swift constants, UIKit/SwiftUI compatibility
- **Android**: XML resources, Material Design alignment
- **React Native**: JavaScript constants, platform detection

---

## 8) Ejemplo Completo 2025

```json
{
  "metadata": {
    "name": "Acme Design System",
    "version": "2.1.0",
    "lastUpdated": "2025-01-15T10:30:00Z",
    "platforms": ["web", "ios", "android"],
    "maintainers": [
      {
        "name": "Design System Team",
        "role": "design-lead",
        "email": "design-system@acme.com"
      }
    ]
  },
  "tokens": {
    "color": {
      "primitive": [
        {
          "name": "brand-primary",
          "value": "#3366FF",
          "category": "brand",
          "wcagCompliance": {
            "aa": true,
            "contrastRatio": 4.5
          }
        }
      ],
      "semantic": [
        {
          "name": "color-success",
          "value": "#22C55E",
          "usage": "success",
          "lightMode": "#22C55E",
          "darkMode": "#16A34A"
        }
      ]
    },
    "typography": {
      "textStyles": [
        {
          "name": "heading-large",
          "fontFamily": "Inter",
          "fontSize": "2rem",
          "fontWeight": "700",
          "lineHeight": "1.2"
        }
      ]
    },
    "spacing": {
      "baseUnit": 4,
      "scale": [
        {
          "name": "space-xs",
          "value": "0.25rem",
          "px": 4,
          "usage": ["padding", "margin"]
        }
      ]
    }
  },
  "governance": {
    "contributionWorkflow": {
      "steps": [
        {
          "name": "proposal",
          "description": "Submit RFC with component rationale",
          "automated": false
        },
        {
          "name": "design-review",
          "description": "Visual consistency and accessibility check",
          "automated": true,
          "tools": ["axe-core", "chromatic"]
        }
      ]
    },
    "approvalCriteria": {
      "design": ["Follows visual hierarchy", "Brand consistent"],
      "accessibility": ["WCAG AA compliant", "Keyboard navigable"],
      "technical": ["Cross-browser tested", "Performance optimized"]
    }
  }
}
```

---

## 9) Checklist de Implementación 2025

### **Setup Inicial**
- [ ] **Metadata configurado**: Name, version, maintainers, platforms
- [ ] **Token hierarchy establecida**: Primitive → Semantic → Component
- [ ] **Accessibility standards definidos**: WCAG level, contrast ratios
- [ ] **Governance workflow documentado**: Steps, reviewers, criteria

### **Token Management**
- [ ] **Color tokens auditados**: Primitive, semantic, component levels
- [ ] **Typography system completo**: Font families, sizes, weights, styles
- [ ] **Spacing scale consistente**: Base unit, mathematical scale
- [ ] **Animation tokens definidos**: Durations, easing functions

### **Component Governance**
- [ ] **Component catalog actualizado**: Status, variants, props
- [ ] **Accessibility specs documentadas**: WCAG level, ARIA requirements
- [ ] **Usage guidelines claras**: When to use, examples, anti-patterns
- [ ] **Migration paths definidos**: Deprecation policy, upgrade guides

### **Tooling & Automation**
- [ ] **Style Dictionary configurado**: Multi-platform token output
- [ ] **Storybook setup**: Component documentation y testing
- [ ] **CI/CD pipeline**: Automated testing, versioning, deployment
- [ ] **Documentation hub**: Centralized, searchable, up-to-date

### **Team Adoption**
- [ ] **Training sessions completadas**: Design system usage, contribution
- [ ] **Documentation socializada**: Guidelines accessible y clear
- [ ] **Feedback loops establecidos**: Regular reviews, improvement cycles
- [ ] **Success metrics definidas**: Adoption rate, consistency score

---

## 10) Recursos y Referencias 2025

### **Industry Standards**
- [W3C Design Tokens Specification](https://design-tokens.github.io/community-group/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Material Design 3 Tokens](https://m3.material.io/foundations/design-tokens)

### **Tools & Platforms**
- [Style Dictionary](https://amzn.github.io/style-dictionary/)
- [Figma Variables](https://help.figma.com/hc/en-us/articles/15339657135383)
- [Storybook Design System](https://storybook.js.org/tutorials/design-systems-for-developers/)

### **Best Practice Examples**
- [Atlassian Design System](https://atlassian.design/)
- [Shopify Polaris](https://polaris.shopify.com/)
- [Airbnb Design Language System](https://airbnb.design/building-a-visual-language/)

---

**Última actualización:** Enero 2025 con mejores prácticas de design tokens, governance frameworks, y tooling moderno.
