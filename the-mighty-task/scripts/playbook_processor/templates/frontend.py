"""
Templates Frontend
==================

Templates universales para arquitectura frontend, design systems y dependencias.
"""

def create_design_system_template(theme, date_str, filename):
    """Marco de referencia para sistemas de diseño"""
    return f'''# Sistema de Diseño - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Sistema de Diseño  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para sistemas de diseño, adaptable a cualquier tecnología o framework.

### Decisiones Clave a Capturar
- **Filosofía de diseño** adoptada para el proyecto
- **Tokens de diseño** definidos y su justificación
- **Componentes base** y su jerarquía
- **Patrones de interacción** establecidos
- **Herramientas** elegidas y por qué

---

## 🏗️ Fundamentos del Sistema

### Filosofía de Diseño
**Decisión:** [Documentar la filosofía de diseño elegida]  
**Opciones consideradas:**
- Material Design, Human Interface Guidelines, Atomic Design, Custom
- Razones para la elección
- Principios rectores del proyecto

### Tokens de Diseño
**Decisión:** [Definir tokens fundamentales]  

#### Colores
```css
/* Ejemplo - adaptar a tu stack */
--primary: [DEFINIR];
--secondary: [DEFINIR];
--accent: [DEFINIR];
```

#### Tipografía
- **Fuente principal:** [DECIDIR]
- **Escala tipográfica:** [DEFINIR]
- **Pesos utilizados:** [ESPECIFICAR]

#### Espaciado
```css
/* Sistema de espaciado */
--space-xs: [DEFINIR];
--space-sm: [DEFINIR];
--space-md: [DEFINIR];
```

---

## 🧩 Arquitectura de Componentes

### Componentes Atómicos
**Decisión:** [Listar componentes base identificados]
- Botones: [Variantes y estados]
- Inputs: [Tipos y validaciones]
- Typography: [Elementos y jerarquías]

### Componentes Moleculares
**Decisión:** [Componentes compuestos clave]
- Forms: [Patrones de formulario]
- Cards: [Tipos de tarjeta]
- Navigation: [Patrones de navegación]

### Plantillas y Páginas
**Decisión:** [Layouts principales]
- Layout principal: [Estructura]
- Páginas tipo: [Patrones identificados]

---

## 🔧 Implementación Técnica

### Stack Tecnológico
**Decisión:** [Tecnologías elegidas para el design system]

#### Herramientas de Diseño
- **Design tool:** [Figma, Sketch, Adobe XD, etc.]
- **Prototipado:** [Herramienta elegida]
- **Documentación:** [Storybook, Docusaurus, custom]

#### Stack de Desarrollo
- **Framework:** [React, Vue, Angular, Web Components, etc.]
- **Styling:** [CSS-in-JS, Sass, PostCSS, Tailwind, etc.]
- **Bundler:** [Webpack, Vite, Parcel, etc.]

### Arquitectura del Código
```
[DEFINIR estructura de carpetas y organización]
```

---

## 📱 Responsive & Accessibility

### Estrategia Responsive
**Decisión:** [Enfoque responsive elegido]
- **Breakpoints:** [Definir breakpoints]
- **Mobile-first:** [Sí/No y justificación]
- **Componentes adaptativos:** [Estrategia]

### Accesibilidad
**Decisión:** [Estándar de accesibilidad adoptado]
- **WCAG Level:** [AA, AAA]
- **Testing tools:** [Herramientas de testing]
- **Checklist:** [Criterios específicos]

---

## 🚀 Implementación y Mantenimiento

### Flujo de Desarrollo
**Decisión:** [Proceso de contribución al design system]
1. [Paso 1 del proceso]
2. [Paso 2 del proceso]
3. [Paso 3 del proceso]

### Versionado
**Decisión:** [Estrategia de versionado]
- **Semantic versioning:** [Cómo se aplica]
- **Breaking changes:** [Cómo se manejan]
- **Migration guides:** [Proceso]

### Testing
**Decisión:** [Estrategia de testing para componentes]
- **Unit tests:** [Framework y scope]
- **Visual regression:** [Herramientas]
- **Cross-browser:** [Estrategia]

---

## 📊 Métricas y Adopción

### KPIs del Sistema
**Decisión:** [Métricas para medir éxito]
- Adopción por equipos: [Cómo medir]
- Consistencia: [Métricas de consistencia]
- Performance: [Benchmarks]

### Gobernanza
**Decisión:** [Modelo de gobierno del design system]
- **Design System Team:** [Estructura]
- **Contribución:** [Proceso de contribución]
- **Evolución:** [Proceso de evolución]

---

## 🔄 Evolución y Roadmap

### Fases de Implementación
1. **Fase 1:** [Componentes base y tokens]
2. **Fase 2:** [Componentes compuestos]
3. **Fase 3:** [Templates y patrones]
4. **Fase 4:** [Tooling y automatización]

### Próximos Pasos
- [ ] [Tarea inmediata 1]
- [ ] [Tarea inmediata 2]
- [ ] [Tarea inmediata 3]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''

def create_frontend_architecture_template(theme, date_str, filename):
    """Marco de referencia para arquitectura frontend"""
    return f'''# Arquitectura Frontend - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Arquitectura Frontend  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para arquitecturas frontend, adaptable a cualquier framework o tecnología.

### Decisiones Clave a Capturar
- **Framework principal** y justificación
- **Arquitectura de componentes** y patrones
- **Gestión de estado** elegida
- **Routing** y navegación
- **Build system** y herramientas

---

## 🏗️ Framework y Stack Principal

### Framework Elegido
**Decisión:** [Framework frontend principal]
- **Opciones:** React, Vue, Angular, Svelte, Solid, etc.
- **Versión:** [Versión específica]
- **Justificación:** [Por qué se eligió este framework]

### Stack Complementario
**Decisión:** [Herramientas del ecosistema]
- **TypeScript:** [Sí/No y justificación]
- **Bundler:** [Vite, Webpack, Parcel, etc.]
- **Testing:** [Jest, Vitest, Cypress, etc.]

---

## 🧩 Arquitectura de Componentes

### Patrón Arquitectónico
**Decisión:** [Patrón de organización elegido]
- **Container/Presentational** / **Atomic Design** / **Feature-based** / **Custom**
- **Justificación:** [Por qué este enfoque]

### Estructura de Carpetas
```
[DEFINIR estructura del proyecto]
```

### Convenciones de Naming
**Decisión:** [Convenciones establecidas]
- **Componentes:** [PascalCase, kebab-case, etc.]
- **Archivos:** [Naming convention]
- **Props/Events:** [Naming patterns]

---

## 🔄 Gestión de Estado

### Estrategia Principal
**Decisión:** [Solución de state management]
- **Local:** [useState, ref, reactive, etc.]
- **Global:** [Redux, Pinia, Zustand, Context, etc.]
- **Server State:** [React Query, SWR, Apollo, etc.]

### Patrón de Datos
**Decisión:** [Flujo de datos implementado]
- **Unidirectional** / **Bidirectional**
- **Immutable updates:** [Sí/No y herramientas]
- **State normalization:** [Estrategia]

---

## 🛣️ Routing y Navegación

### Sistema de Routing
**Decisión:** [Router elegido]
- **Router:** [React Router, Vue Router, Angular Router, etc.]
- **Tipo:** [Hash, History, Memory]
- **Nested routing:** [Sí/No]

### Estructura de Rutas
```javascript
// [DEFINIR estructura de routing]
```

### Guards y Middleware
**Decisión:** [Protección de rutas]
- **Authentication:** [Estrategia]
- **Authorization:** [Levels]
- **Loading states:** [Cómo se manejan]

---

## 🎨 Styling y UI

### Estrategia de Estilos
**Decisión:** [Enfoque de styling]
- **CSS-in-JS** / **CSS Modules** / **Utility-first** / **Preprocessors**
- **Framework:** [Styled-components, Tailwind, Emotion, etc.]

### Sistema de Temas
**Decisión:** [Theming approach]
- **CSS Custom Properties** / **JS Themes** / **Design Tokens**
- **Dark mode:** [Sí/No y implementación]

### Responsive Design
**Decisión:** [Estrategia responsive]
- **Mobile-first:** [Sí/No]
- **Breakpoints:** [Definidos]
- **Layout system:** [Grid, Flexbox, etc.]

---

## 🔌 Data Fetching

### Estrategia de APIs
**Decisión:** [Approach para consumir APIs]
- **HTTP Client:** [fetch, axios, ky, etc.]
- **GraphQL:** [Apollo, urql, etc.]
- **Real-time:** [WebSockets, SSE, etc.]

### Caching y Optimización
**Decisión:** [Estrategia de cache]
- **Browser cache:** [Headers y estrategia]
- **Memory cache:** [Herramientas]
- **Offline support:** [Service Workers, etc.]

---

## ⚡ Performance

### Optimizaciones Aplicadas
**Decisión:** [Técnicas de optimización]
- **Code splitting:** [Route-based, Component-based]
- **Lazy loading:** [Components, Images, etc.]
- **Bundle optimization:** [Tree shaking, etc.]

### Métricas Objetivo
**Decisión:** [KPIs de performance]
- **Core Web Vitals:** [Targets específicos]
- **Bundle size:** [Límites definidos]
- **Load time:** [Objetivos]

---

## 🧪 Testing Strategy

### Niveles de Testing
**Decisión:** [Tipos de test implementados]

#### Unit Tests
- **Framework:** [Jest, Vitest, etc.]
- **Utilities:** [Testing Library, Enzyme, etc.]
- **Coverage:** [Porcentaje objetivo]

#### Integration Tests
- **Component integration:** [Estrategia]
- **API integration:** [Mocking vs real]

#### E2E Tests
- **Tool:** [Cypress, Playwright, etc.]
- **Critical paths:** [Flows principales]

---

## 📱 Progressive Web App

### PWA Features
**Decisión:** [Características PWA implementadas]
- **Service Worker:** [Sí/No y estrategia]
- **Manifest:** [Configuración]
- **Offline support:** [Nivel de soporte]

### Installation
**Decisión:** [Installability]
- **App-like experience:** [Nivel]
- **Platform integration:** [Notifications, etc.]

---

## 🚀 Build y Deployment

### Build Process
**Decisión:** [Configuración de build]
- **Development:** [Hot reload, etc.]
- **Production:** [Optimizaciones]
- **Preview:** [Staging builds]

### Deployment Strategy
**Decisión:** [Estrategia de deploy]
- **Static hosting:** [Vercel, Netlify, etc.]
- **CDN:** [CloudFront, etc.]
- **Environment configs:** [Manejo]

---

## 🔄 Próximos Pasos

### Setup Inmediato
- [ ] [Configuración inicial del framework]
- [ ] [Setup del bundler y herramientas]
- [ ] [Estructura base del proyecto]

### Desarrollo Core
- [ ] [Componentes base]
- [ ] [Routing setup]
- [ ] [State management]

### Optimización
- [ ] [Performance audit]
- [ ] [SEO optimization]
- [ ] [Accessibility review]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''

def create_frontend_dependencies_template(theme, date_str, filename):
    """Marco de referencia para dependencias frontend"""
    return f'''# Dependencias Frontend - Marco de Referencia

**Sesión:** {theme}  
**Fecha:** {date_str}  
**Marco Universal:** Gestión de Dependencias Frontend  
**Referencia:** [playbooks/documentation_playbooks/{filename}](../../../playbooks/documentation_playbooks/{filename})

---

## 🎯 Propósito del Marco

Este documento sirve como **marco de referencia universal** para la gestión de dependencias en proyectos frontend.

### Decisiones Clave a Capturar
- **Package manager** elegido
- **Dependencias core** y justificación
- **Versionado** y compatibility
- **Bundle size** management
- **Security** y updates

---

## 📦 Package Manager

### Herramienta Elegida
**Decisión:** [Package manager seleccionado]
- **npm** / **yarn** / **pnpm** / **bun**
- **Versión:** [Versión específica]
- **Justificación:** [Razones para la elección]

### Configuración
```json
{{
  "packageManager": "[ESPECIFICAR]",
  "engines": {{
    "node": "[VERSION]",
    "npm": "[VERSION]"
  }}
}}
```

---

## 🏗️ Dependencias Core

### Framework Principal
**Decisión:** [Framework y versión]
```json
{{
  "dependencies": {{
    "[framework]": "[version]"
  }}
}}
```

### Runtime Essentials
**Decisión:** [Dependencias runtime críticas]
- **Router:** [react-router, vue-router, etc.]
- **State Management:** [redux, pinia, zustand, etc.]
- **HTTP Client:** [axios, fetch wrapper, etc.]

### Build Tools
**Decisión:** [Herramientas de build]
- **Bundler:** [vite, webpack, parcel, etc.]
- **Transpiler:** [babel, swc, esbuild, etc.]
- **TypeScript:** [Si aplica y configuración]

---

## 🎨 UI y Styling

### Biblioteca de Componentes
**Decisión:** [UI library elegida]
- **Material-UI** / **Ant Design** / **Chakra UI** / **Custom**
- **Justificación:** [Por qué esta elección]
- **Customization:** [Nivel de personalización]

### Styling Solution
**Decisión:** [Solución de estilos]
- **CSS-in-JS:** [styled-components, emotion, etc.]
- **Utility-first:** [tailwindcss, etc.]
- **Preprocessors:** [sass, less, etc.]

---

## 🔧 Development Tools

### Code Quality
**Decisión:** [Herramientas de calidad]
```json
{{
  "devDependencies": {{
    "eslint": "[version]",
    "prettier": "[version]",
    "husky": "[version]",
    "lint-staged": "[version]"
  }}
}}
```

### Testing Framework
**Decisión:** [Stack de testing]
- **Unit Tests:** [jest, vitest, etc.]
- **Component Tests:** [@testing-library, etc.]
- **E2E Tests:** [cypress, playwright, etc.]

---

## 📊 Bundle Analysis

### Size Optimization
**Decisión:** [Estrategia de optimización]
- **Bundle analyzer:** [webpack-bundle-analyzer, etc.]
- **Tree shaking:** [Configuración]
- **Code splitting:** [Estrategia]

### Performance Budget
**Decisión:** [Límites definidos]
```javascript
// Bundle size limits
const BUNDLE_LIMITS = {{
  maxAssetSize: 250000, // 250kb
  maxEntrypointSize: 250000,
  hints: "warning"
}}
```

---

## 🔒 Security y Updates

### Dependency Security
**Decisión:** [Estrategia de seguridad]
- **Audit frequency:** [Frecuencia de auditoría]
- **Automated updates:** [Dependabot, renovate, etc.]
- **Vulnerability monitoring:** [Herramientas]

### Version Management
**Decisión:** [Estrategia de versionado]
- **Semver policy:** [Cómo se manejan updates]
- **Lock files:** [Política de commit]
- **Major updates:** [Proceso de actualización]

---

## 🏷️ Categorización de Dependencies

### Production Dependencies
```json
{{
  "dependencies": {{
    "// Framework": "",
    "[framework]": "^X.X.X",
    
    "// State Management": "",
    "[state-lib]": "^X.X.X",
    
    "// Routing": "",
    "[router]": "^X.X.X",
    
    "// HTTP Client": "",
    "[http-client]": "^X.X.X",
    
    "// UI Library": "",
    "[ui-lib]": "^X.X.X"
  }}
}}
```

### Development Dependencies
```json
{{
  "devDependencies": {{
    "// Build Tools": "",
    "[bundler]": "^X.X.X",
    
    "// Code Quality": "",
    "eslint": "^X.X.X",
    "prettier": "^X.X.X",
    
    "// Testing": "",
    "[test-framework]": "^X.X.X",
    
    "// Types": "",
    "@types/[library]": "^X.X.X"
  }}
}}
```

---

## 📋 Dependency Checklist

### Evaluación de Nuevas Dependencies
- [ ] **Size impact:** ¿Cómo afecta al bundle size?
- [ ] **Maintenance:** ¿Está activamente mantenida?
- [ ] **Community:** ¿Tiene buena adopción y documentación?
- [ ] **Alternatives:** ¿Se evaluaron alternativas?
- [ ] **Security:** ¿Tiene vulnerabilidades conocidas?
- [ ] **TypeScript:** ¿Tiene soporte TypeScript si es necesario?

### Mantenimiento Regular
- [ ] **Audit mensual:** Revisar vulnerabilities
- [ ] **Update dependencies:** Mantener actualizadas
- [ ] **Bundle analysis:** Monitorear tamaño
- [ ] **Performance impact:** Medir impacto
- [ ] **Remove unused:** Limpiar dependencies no usadas

---

## 🔄 Scripts de Package.json

**Decisión:** [Scripts definidos]
```json
{{
  "scripts": {{
    "dev": "[comando desarrollo]",
    "build": "[comando build]",
    "preview": "[comando preview]",
    "test": "[comando testing]",
    "test:watch": "[comando test watch]",
    "lint": "[comando lint]",
    "lint:fix": "[comando lint fix]",
    "type-check": "[comando type check]",
    "analyze": "[comando bundle analysis]",
    "audit": "[comando security audit]"
  }}
}}
```

---

## 🔄 Próximos Pasos

### Setup Inicial
- [ ] [Configurar package manager]
- [ ] [Instalar dependencies core]
- [ ] [Configurar herramientas de desarrollo]

### Configuración
- [ ] [Setup linting y formatting]
- [ ] [Configurar testing framework]
- [ ] [Setup bundle analysis]

### Mantenimiento
- [ ] [Establecer proceso de updates]
- [ ] [Configurar security scanning]
- [ ] [Documentar dependency decisions]

---

*Marco generado por The Mighty Task System*  
*Consultar playbook original: `playbooks/documentation_playbooks/{filename}`*
'''
