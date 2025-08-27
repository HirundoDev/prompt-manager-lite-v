# 🆘 **PLAN SISTEMA DE AYUDA CONTEXTUAL - DASHBOARD LOCAL**

**Fecha:** 2025-08-27  
**Objetivo:** Implementar sistema de ayuda contextual con modales y tooltips para mejorar UX  
**Estado:** 📋 **PLANIFICACIÓN**

---

## 🔍 **INVESTIGACIÓN COMPLETA - COMPONENTES MAPEADOS**

### **📊 Estructura del Dashboard Local**
```
src/
├── routes/
│   ├── +layout.svelte          # Layout principal
│   ├── +page.svelte            # Dashboard principal
│   ├── projects/+page.svelte   # Gestión de proyectos
│   ├── sessions/+page.svelte   # Gestión de sesiones
│   ├── missions/+page.svelte   # Gestión de misiones
│   ├── reports/+page.svelte    # Reportes y estadísticas
│   └── settings/+page.svelte   # Configuración
├── lib/components/
│   ├── Header.svelte           # Header con navegación
│   ├── Sidebar.svelte          # Sidebar con menú
│   ├── ProjectCreator.svelte   # Modal crear proyecto
│   ├── SessionCreator.svelte   # Modal crear sesión
│   └── TestRunner.svelte       # Modal ejecutar tests
└── lib/utils/
    └── tauri.js               # Utilidades Tauri
```

---

## 🎯 **COMPONENTES QUE NECESITAN AYUDA CONTEXTUAL**

### **🏠 Dashboard Principal (+page.svelte)**
#### **Elementos identificados:**
1. **Estadísticas Cards (4 cards)**
   - Proyectos Totales
   - Sesiones Recientes  
   - Misiones Completadas
   - Proyecto Activo

2. **Acciones Rápidas (3 botones)**
   - Nueva Sesión
   - Ejecutar Tests
   - Reportes

3. **Actividad Reciente**
   - Lista de actividad
   - Estados de actividad

### **📁 Página de Proyectos (projects/+page.svelte)**
#### **Elementos identificados:**
1. **Header de página**
   - Botón "Importar"
   - Botón "Nuevo Proyecto"

2. **Controles de filtrado**
   - Campo de búsqueda
   - Filtro por estado (all/active/inactive)
   - Ordenamiento (name/created/organization)

3. **Cards de proyecto**
   - Estados del proyecto (Activo/Inactivo/No encontrado)
   - Menú de acciones (Activar/Exportar/Editar/Eliminar)
   - Tags y metadatos

### **🎛️ Header (Header.svelte)**
#### **Elementos identificados:**
1. **Barra de búsqueda**
   - Campo de búsqueda global
   - Funcionalidad de búsqueda

2. **Botones de acción**
   - Refrescar datos
   - Cambiar tema (dark/light)
   - Notificaciones (bell icon)
   - Menú de usuario

### **📋 Sidebar (Sidebar.svelte)**
#### **Elementos identificados:**
1. **Navegación principal (6 items)**
   - Dashboard
   - Proyectos
   - Sesiones
   - Misiones
   - Reportes
   - Configuración

2. **Acciones de proyecto (3 items)**
   - Nueva Sesión
   - Exportar
   - Importar

### **🔧 Modales Existentes**
#### **ProjectCreator.svelte**
- Formulario de creación
- Validaciones
- Campos requeridos

#### **SessionCreator.svelte**
- Tipos de template
- Temas predefinidos
- Validación de formato

#### **TestRunner.svelte**
- Tipos de test (Smoke/Quick/Full)
- Output de resultados
- Estados de ejecución

---

## 🎨 **DISEÑO DEL SISTEMA DE AYUDA**

### **🔧 Componentes a Crear**

#### **1. HelpModal.svelte** (Componente principal)
```svelte
<script>
  export let title = '';
  export let content = '';
  export let examples = [];
  export let relatedLinks = [];
  export let show = false;
</script>
```

#### **2. HelpTooltip.svelte** (Tooltips pequeños)
```svelte
<script>
  export let text = '';
  export let position = 'top'; // top, bottom, left, right
  export let trigger = 'hover'; // hover, click
</script>
```

#### **3. HelpIcon.svelte** (Icono de ayuda reutilizable)
```svelte
<script>
  export let helpKey = '';
  export let size = 'sm'; // sm, md, lg
  export let variant = 'tooltip'; // tooltip, modal
</script>
```

### **📚 Base de Datos de Contenido**

#### **helpContent.js** - Contenido centralizado
```javascript
export const helpContent = {
  // Dashboard Principal
  'dashboard.stats.projects': {
    title: 'Proyectos Totales',
    content: 'Muestra el número total de proyectos registrados...',
    examples: ['Incluye proyectos activos e inactivos'],
    relatedLinks: ['/projects']
  },
  
  // Proyectos
  'projects.import': {
    title: 'Importar Proyecto',
    content: 'Permite importar un proyecto desde archivo .mtp...',
    examples: ['Selecciona archivo .mtp', 'Valida integridad'],
    relatedLinks: []
  },
  
  // ... más contenido
};
```

---

## 🚀 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Componentes Base** 
- [ ] Crear HelpModal.svelte
- [ ] Crear HelpTooltip.svelte  
- [ ] Crear HelpIcon.svelte
- [ ] Crear helpContent.js con contenido inicial

### **Fase 2: Integración Dashboard Principal**
- [ ] Agregar ayuda a estadísticas cards
- [ ] Agregar ayuda a acciones rápidas
- [ ] Agregar ayuda a actividad reciente

### **Fase 3: Integración Header y Sidebar**
- [ ] Agregar ayuda a búsqueda global
- [ ] Agregar ayuda a botones del header
- [ ] Agregar ayuda a navegación del sidebar

### **Fase 4: Integración Páginas**
- [ ] Página de Proyectos
- [ ] Página de Sesiones  
- [ ] Página de Misiones
- [ ] Página de Reportes
- [ ] Página de Configuración

### **Fase 5: Modales Existentes**
- [ ] Mejorar ProjectCreator con ayuda contextual
- [ ] Mejorar SessionCreator con ayuda contextual
- [ ] Mejorar TestRunner con ayuda contextual

### **Fase 6: Funcionalidades Avanzadas**
- [ ] Guías interactivas (tours)
- [ ] Búsqueda en ayuda
- [ ] Ayuda contextual inteligente
- [ ] Shortcuts de teclado para ayuda

---

## 📋 **CONTENIDO DE AYUDA REQUERIDO**

### **🏠 Dashboard Principal**
1. **Estadísticas**
   - `dashboard.stats.projects` - Qué son los proyectos totales
   - `dashboard.stats.sessions` - Qué son las sesiones recientes
   - `dashboard.stats.missions` - Qué son las misiones completadas
   - `dashboard.stats.active-project` - Concepto de proyecto activo

2. **Acciones Rápidas**
   - `dashboard.actions.new-session` - Cómo crear una nueva sesión
   - `dashboard.actions.run-tests` - Para qué sirven los tests
   - `dashboard.actions.reports` - Qué información muestran los reportes

### **📁 Proyectos**
1. **Gestión**
   - `projects.concept` - Qué es un proyecto mighty-task
   - `projects.create` - Cómo crear un nuevo proyecto
   - `projects.import` - Cómo importar desde .mtp
   - `projects.export` - Cómo exportar a .mtp
   - `projects.switch` - Concepto de proyecto activo

2. **Estados**
   - `projects.status.active` - Proyecto actualmente en uso
   - `projects.status.inactive` - Proyectos disponibles
   - `projects.status.missing` - Proyectos con archivos faltantes

### **⚙️ Funcionalidades Generales**
1. **Navegación**
   - `navigation.dashboard` - Qué muestra el dashboard
   - `navigation.projects` - Gestión de proyectos
   - `navigation.sessions` - Gestión de sesiones de trabajo
   - `navigation.missions` - Consolidación de misiones
   - `navigation.reports` - Reportes y estadísticas
   - `navigation.settings` - Configuración del sistema

2. **Herramientas**
   - `tools.search` - Búsqueda global
   - `tools.refresh` - Actualizar datos
   - `tools.theme` - Cambio de tema claro/oscuro
   - `tools.notifications` - Sistema de notificaciones

---

## 🎯 **CRITERIOS DE ÉXITO**

### **✅ Funcionalidad**
- [ ] Todos los elementos tienen ayuda contextual
- [ ] Modales de ayuda se abren correctamente
- [ ] Tooltips aparecen en hover/click
- [ ] Contenido es claro y útil

### **✅ UX/UI**
- [ ] Iconos de ayuda no interfieren con el diseño
- [ ] Modales son responsive
- [ ] Animaciones suaves
- [ ] Accesibilidad (keyboard navigation)

### **✅ Mantenimiento**
- [ ] Contenido centralizado y fácil de editar
- [ ] Componentes reutilizables
- [ ] Estructura escalable
- [ ] Documentación clara

---

## 🔧 **ESPECIFICACIONES TÉCNICAS**

### **Iconos de Ayuda**
- **Icono:** `HelpCircle` de lucide-svelte
- **Tamaño:** 16px (sm), 20px (md), 24px (lg)
- **Color:** `text-gray-400 hover:text-gray-600`
- **Posición:** Junto al elemento que explica

### **Modales de Ayuda**
- **Ancho máximo:** 500px
- **Backdrop:** Semi-transparente
- **Animación:** Fade in/out
- **Cierre:** Click fuera, ESC, botón X

### **Tooltips**
- **Ancho máximo:** 250px
- **Delay:** 500ms
- **Posición:** Automática según espacio
- **Estilo:** Consistente con design system

### **Estructura de Datos**
```javascript
{
  id: 'unique-key',
  title: 'Título corto',
  content: 'Descripción detallada',
  examples: ['Ejemplo 1', 'Ejemplo 2'],
  relatedLinks: ['/ruta1', '/ruta2'],
  type: 'tooltip' | 'modal',
  category: 'dashboard' | 'projects' | 'sessions' | etc
}
```

---

## 📈 **MÉTRICAS Y SEGUIMIENTO**

### **Métricas de Uso**
- Clicks en iconos de ayuda
- Tiempo en modales de ayuda
- Elementos más consultados
- Abandono de ayuda

### **Feedback del Usuario**
- Rating de utilidad (1-5 estrellas)
- Comentarios sobre contenido
- Sugerencias de mejora
- Reportes de errores

---

**🎯 Este plan proporciona una base sólida para implementar un sistema de ayuda contextual completo y escalable en el Dashboard Local de The Mighty Task.**
