# Schema Playbook — stateManagementPlan

**Propósito:** Template universal para documentar estrategias de gestión de estado en cualquier framework frontend o stack tecnológico. Proporciona estructura adaptable con placeholders para patrones de arquitectura, clasificación de estado, selección de librerías y estrategias de optimización.

**Ubicación:** `schemas/master_blueprint_parts/stateManagementPlan.json`

**Versión:** 3.0 (Template Universal con Placeholders)

---

## 1) Arquitectura del Template (Universal y Adaptable)

### **Filosofía Template-First**
Este schema funciona como template universal que se adapta a cualquier:
- **Framework Frontend:** React, Vue, Angular, Svelte, Vanilla JS, etc.
- **Escala de Aplicación:** Pequeña, mediana, grande, enterprise
- **Arquitectura:** Centralized, distributed, hybrid, atomic, modular
- **Metodología:** Cualquier patrón de gestión de estado

### **Componentes del Template**
- **`metadata`**: Contexto del proyecto y plan con placeholders `[VARIABLE]`
- **`architecture`**: Estrategia arquitectónica adaptable a cualquier enfoque
- **`stateTypes`**: Clasificación universal de tipos de estado
- **`libraries`**: Selección de librerías con criterios adaptables
- **`performance`**: Estrategias de optimización universales
- **`testing`**: Enfoques de testing agnósticos de tecnología
- **`documentation`**: Estrategias de documentación adaptables

### **Principio de Placeholders**
Todos los valores específicos usan placeholders `[VARIABLE]` que se reemplazan según el contexto:
- `[FRONTEND_FRAMEWORK]` → React, Vue, Angular, etc.
- `[ARCHITECTURE_STRATEGY]` → Centralized, Hybrid, Atomic, etc.
- `[LIBRARY_NAME]` → Redux, Zustand, Pinia, NgRx, etc.

---

## 2) Metodología de Uso del Template

### **Fase 1: Análisis del Contexto del Proyecto**
1. **Identificar Framework**: Determinar `[FRONTEND_FRAMEWORK]` y stack tecnológico
2. **Evaluar Escala**: Definir `[APPLICATION_SCALE]` (small, medium, large, enterprise)
3. **Analizar Equipo**: Establecer `[TEAM_SIZE]` y estructura organizacional
4. **Definir Requisitos**: Documentar necesidades específicas de gestión de estado

### **Fase 2: Selección de Estrategia Arquitectónica**
1. **Elegir Estrategia**: Seleccionar `[ARCHITECTURE_STRATEGY]` apropiada
2. **Definir Patrones**: Identificar `[DESIGN_PATTERN]` aplicables
3. **Establecer Flujo**: Determinar `[DATA_FLOW_TYPE]` y comunicación
4. **Planificar Escalabilidad**: Definir `[SCALING_STRATEGY]`

### **Fase 3: Clasificación y Gestión de Estado**
1. **Estado Local**: Definir `[LOCAL_STATE_DEFINITION]` y ejemplos
2. **Estado Global**: Establecer `[GLOBAL_STATE_DEFINITION]` y patrones
3. **Estado Servidor**: Configurar `[SERVER_STATE_DEFINITION]` y caching
4. **Estado Compartido**: Implementar `[SHARED_STATE_DEFINITION]` y sincronización

### **Fase 4: Selección de Herramientas**
1. **Librerías Primarias**: Elegir `[LIBRARY_NAME]` basado en criterios
2. **Utilidades**: Seleccionar `[UTILITY_LIBRARY_NAME]` de apoyo
3. **Criterios**: Documentar `[TECHNICAL_CRITERION]` y `[BUSINESS_CRITERION]`
4. **Justificación**: Explicar `[LIBRARY_JUSTIFICATION]` para cada selección

### **Fase 5: Optimización y Testing**
1. **Performance**: Implementar `[OPTIMIZATION_STRATEGY]` apropiadas
2. **Monitoring**: Configurar `[PERFORMANCE_METRIC]` y herramientas
3. **Testing**: Establecer `[TESTING_APPROACH]` y cobertura
4. **Documentación**: Crear `[DOCUMENTATION_APPROACH]` y recursos

---

## 3) Guía Universal de Selección de Estrategias

### **Árbol de Decisión Universal**

```
¿Cuál es el contexto del proyecto?
├── [SMALL_SCALE] + [SIMPLE_REQUIREMENTS]
│   ├── [UI_FOCUSED] → [BUILT_IN_STATE_MANAGEMENT]
│   ├── [FORM_HEAVY] → [FORM_STATE_LIBRARY]
│   └── [API_HEAVY] → [SERVER_STATE_LIBRARY]
├── [MEDIUM_SCALE] + [MODERATE_COMPLEXITY]
│   ├── [PREDICTABLE_UPDATES] → [CENTRALIZED_STRATEGY]
│   ├── [REACTIVE_PATTERNS] → [REACTIVE_STRATEGY]
│   └── [MODULAR_APPROACH] → [DISTRIBUTED_STRATEGY]
├── [LARGE_SCALE] + [HIGH_COMPLEXITY]
│   ├── [ENTERPRISE_REQUIREMENTS] → [LAYERED_STRATEGY]
│   ├── [PERFORMANCE_CRITICAL] → [ATOMIC_STRATEGY]
│   └── [TEAM_COLLABORATION] → [HYBRID_STRATEGY]
└── [SPECIALIZED_REQUIREMENTS]
    ├── [REAL_TIME] → [EVENT_DRIVEN_STRATEGY]
    ├── [OFFLINE_FIRST] → [PERSISTENCE_STRATEGY]
    └── [COLLABORATIVE] → [SHARED_STATE_STRATEGY]
```

### **Criterios de Selección Universales**

| Criterio | [SMALL_SCALE] | [MEDIUM_SCALE] | [LARGE_SCALE] | [ENTERPRISE_SCALE] |
|----------|---------------|----------------|---------------|-------------------|
| **Complejidad** | [SIMPLE_APPROACH] | [MODERATE_APPROACH] | [COMPLEX_APPROACH] | [ENTERPRISE_APPROACH] |
| **Performance** | [BASIC_OPTIMIZATION] | [MODERATE_OPTIMIZATION] | [ADVANCED_OPTIMIZATION] | [ENTERPRISE_OPTIMIZATION] |
| **Mantenibilidad** | [SIMPLE_MAINTENANCE] | [STRUCTURED_MAINTENANCE] | [SYSTEMATIC_MAINTENANCE] | [ENTERPRISE_MAINTENANCE] |
| **Escalabilidad** | [LIMITED_SCALING] | [MODERATE_SCALING] | [HIGH_SCALING] | [UNLIMITED_SCALING] |
| **Equipo** | [SOLO_DEVELOPER] | [SMALL_TEAM] | [MEDIUM_TEAM] | [LARGE_TEAM] |

---

## 4) Patrones Universales de Optimización

### **Principios de Optimización Agnósticos de Tecnología**

#### **Optimización de Renderizado**
```
Patrón: [RENDER_OPTIMIZATION_PATTERN]
├── [MEMOIZATION_STRATEGY]
│   ├── Selectores: [SELECTOR_OPTIMIZATION]
│   ├── Componentes: [COMPONENT_OPTIMIZATION]
│   └── Valores Computados: [COMPUTED_VALUE_OPTIMIZATION]
├── [STATE_COLOCATION]
│   ├── Principio: Mantener estado cerca de donde se usa
│   ├── Beneficio: Reduce re-renders innecesarios
│   └── Implementación: [COLOCATION_IMPLEMENTATION]
└── [GRANULAR_UPDATES]
    ├── Estrategia: [GRANULAR_UPDATE_STRATEGY]
    ├── Herramientas: [GRANULAR_UPDATE_TOOLS]
    └── Métricas: [GRANULAR_UPDATE_METRICS]
```

#### **Optimización de Datos del Servidor**
```
Patrón: [SERVER_STATE_OPTIMIZATION]
├── [CACHING_STRATEGY]
│   ├── Estrategia: [CACHE_STRATEGY_TYPE]
│   ├── TTL: [CACHE_TTL_CONFIGURATION]
│   └── Invalidación: [CACHE_INVALIDATION_APPROACH]
├── [FETCHING_OPTIMIZATION]
│   ├── Estrategia: [DATA_FETCHING_STRATEGY]
│   ├── Batching: [REQUEST_BATCHING_APPROACH]
│   └── Deduplicación: [REQUEST_DEDUPLICATION]
└── [OPTIMISTIC_UPDATES]
    ├── Implementación: [OPTIMISTIC_UPDATE_IMPLEMENTATION]
    ├── Rollback: [ROLLBACK_STRATEGY]
    └── Conflictos: [CONFLICT_RESOLUTION_APPROACH]
```

#### **Optimización de Memoria**
```
Patrón: [MEMORY_OPTIMIZATION_PATTERN]
├── [STATE_CLEANUP]
│   ├── Estrategia: [CLEANUP_STRATEGY]
│   ├── Triggers: [CLEANUP_TRIGGERS]
│   └── Automatización: [CLEANUP_AUTOMATION]
├── [MEMORY_LEAK_PREVENTION]
│   ├── Detección: [LEAK_DETECTION_APPROACH]
│   ├── Prevención: [LEAK_PREVENTION_STRATEGY]
│   └── Monitoring: [MEMORY_MONITORING_TOOLS]
└── [BUNDLE_OPTIMIZATION]
    ├── Code Splitting: [CODE_SPLITTING_STRATEGY]
    ├── Lazy Loading: [LAZY_LOADING_APPROACH]
    └── Tree Shaking: [TREE_SHAKING_OPTIMIZATION]
```

---

## 5) Patrones Arquitectónicos Universales

### **Arquitectura Híbrida (Recomendada para Múltiples Contextos)**
```
Patrón: [HYBRID_ARCHITECTURE_PATTERN]
├── [LOCAL_STATE_LAYER]
│   ├── Propósito: [LOCAL_STATE_PURPOSE]
│   ├── Implementación: [LOCAL_STATE_IMPLEMENTATION]
│   ├── Herramientas: [LOCAL_STATE_TOOLS]
│   └── Casos de Uso: [LOCAL_STATE_USE_CASES]
├── [GLOBAL_STATE_LAYER]
│   ├── Propósito: [GLOBAL_STATE_PURPOSE]
│   ├── Implementación: [GLOBAL_STATE_IMPLEMENTATION]
│   ├── Herramientas: [GLOBAL_STATE_TOOLS]
│   └── Casos de Uso: [GLOBAL_STATE_USE_CASES]
├── [SERVER_STATE_LAYER]
│   ├── Propósito: [SERVER_STATE_PURPOSE]
│   ├── Implementación: [SERVER_STATE_IMPLEMENTATION]
│   ├── Herramientas: [SERVER_STATE_TOOLS]
│   └── Casos de Uso: [SERVER_STATE_USE_CASES]
└── [INTEGRATION_LAYER]
    ├── Comunicación: [LAYER_COMMUNICATION_APPROACH]
    ├── Sincronización: [LAYER_SYNCHRONIZATION]
    └── Conflictos: [LAYER_CONFLICT_RESOLUTION]
```

### **Arquitectura Atómica (Para Aplicaciones Complejas)**
```
Patrón: [ATOMIC_ARCHITECTURE_PATTERN]
├── [ATOMIC_UNITS]
│   ├── Definición: [ATOMIC_UNIT_DEFINITION]
│   ├── Granularidad: [ATOMIC_GRANULARITY_LEVEL]
│   ├── Composición: [ATOMIC_COMPOSITION_APPROACH]
│   └── Dependencias: [ATOMIC_DEPENDENCY_MANAGEMENT]
├── [DERIVED_STATE]
│   ├── Computación: [DERIVED_STATE_COMPUTATION]
│   ├── Memoización: [DERIVED_STATE_MEMOIZATION]
│   ├── Invalidación: [DERIVED_STATE_INVALIDATION]
│   └── Performance: [DERIVED_STATE_PERFORMANCE]
├── [ASYNC_ATOMS]
│   ├── Gestión: [ASYNC_ATOM_MANAGEMENT]
│   ├── Caching: [ASYNC_ATOM_CACHING]
│   ├── Error Handling: [ASYNC_ATOM_ERROR_HANDLING]
│   └── Loading States: [ASYNC_ATOM_LOADING_STATES]
└── [COMPOSITION_PATTERNS]
    ├── Combinación: [ATOM_COMBINATION_PATTERNS]
    ├── Selección: [ATOM_SELECTION_STRATEGIES]
    └── Optimización: [ATOM_OPTIMIZATION_TECHNIQUES]
```

### **Arquitectura Centralizada (Para Aplicaciones Predecibles)**
```
Patrón: [CENTRALIZED_ARCHITECTURE_PATTERN]
├── [SINGLE_STORE]
│   ├── Estructura: [STORE_STRUCTURE_APPROACH]
│   ├── Normalización: [STATE_NORMALIZATION_STRATEGY]
│   ├── Módulos: [STORE_MODULE_ORGANIZATION]
│   └── Acceso: [STORE_ACCESS_PATTERNS]
├── [ACTION_SYSTEM]
│   ├── Definición: [ACTION_DEFINITION_APPROACH]
│   ├── Dispatch: [ACTION_DISPATCH_MECHANISM]
│   ├── Middleware: [ACTION_MIDDLEWARE_CHAIN]
│   └── Logging: [ACTION_LOGGING_STRATEGY]
├── [REDUCER_PATTERN]
│   ├── Implementación: [REDUCER_IMPLEMENTATION]
│   ├── Composición: [REDUCER_COMPOSITION]
│   ├── Inmutabilidad: [IMMUTABILITY_APPROACH]
│   └── Testing: [REDUCER_TESTING_STRATEGY]
└── [SELECTOR_SYSTEM]
    ├── Definición: [SELECTOR_DEFINITION]
    ├── Memoización: [SELECTOR_MEMOIZATION]
    ├── Composición: [SELECTOR_COMPOSITION]
    └── Performance: [SELECTOR_PERFORMANCE_OPTIMIZATION]
```

---

## 6) Caching Strategies 2025

### **Cache Strategies por Tipo de Datos**

| Tipo de Datos | Strategy | TTL | Background Refetch |
|---------------|----------|-----|-------------------|
| **User Profile** | stale-while-revalidate | 5 min | Yes |
| **Product Catalog** | cache-first | 15 min | Yes |
| **Real-time Data** | network-first | 30 sec | Yes |
| **Static Content** | cache-only | 1 hour | No |
| **Form Data** | network-only | - | No |

### **Cache Invalidation Patterns**
```javascript
// Tag-based invalidation
const useUpdateProduct = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: updateProduct,
    onSuccess: (data) => {
      // Invalidate specific product
      queryClient.invalidateQueries(['product', data.id]);
      // Invalidate product lists
      queryClient.invalidateQueries(['products']);
      // Invalidate related data
      queryClient.invalidateQueries(['categories']);
    },
  });
};
```

---

## 7) Testing Strategies 2025

### **Testing Pyramid para State Management**
```
E2E Tests (10%)
├── User workflows with state changes
├── Real API integration
└── Cross-browser state persistence

Integration Tests (20%)
├── Component + State interactions
├── API + Cache integration
└── State synchronization

Unit Tests (70%)
├── Reducers/Actions (Redux)
├── Store logic (Zustand)
├── Selectors/Computed values
└── State utilities
```

### **Testing Tools por Librería**
```javascript
// Redux Testing
import { configureStore } from '@reduxjs/toolkit';
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';

const renderWithStore = (component, initialState) => {
  const store = configureStore({
    reducer: rootReducer,
    preloadedState: initialState,
  });
  
  return render(
    <Provider store={store}>
      {component}
    </Provider>
  );
};

// Zustand Testing
import { act, renderHook } from '@testing-library/react';

test('should increment count', () => {
  const { result } = renderHook(() => useCountStore());
  
  act(() => {
    result.current.increment();
  });
  
  expect(result.current.count).toBe(1);
});

// TanStack Query Testing
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const createTestQueryClient = () => new QueryClient({
  defaultOptions: {
    queries: { retry: false },
    mutations: { retry: false },
  },
});
```

---

## 8) Migration Strategies

### **Redux → Zustand Migration**
```javascript
// Phase 1: Parallel implementation
const useUserStore = create((set, get) => ({
  // Migrate Redux slice to Zustand
  user: null,
  setUser: (user) => set({ user }),
  clearUser: () => set({ user: null }),
  
  // Keep Redux compatibility during transition
  dispatch: (action) => {
    const state = get();
    // Handle Redux actions in Zustand
    switch (action.type) {
      case 'SET_USER':
        set({ user: action.payload });
        break;
    }
  },
}));

// Phase 2: Component migration
function UserProfile() {
  // Old Redux way (to be removed)
  // const user = useSelector(state => state.user);
  // const dispatch = useDispatch();
  
  // New Zustand way
  const { user, setUser } = useUserStore();
  
  return <div>{user?.name}</div>;
}
```

---

## 9) Ejemplo de Template Completado

### **Ejemplo: Plan de Gestión de Estado para [E-COMMERCE_APPLICATION]**

```json
{
  "metadata": {
    "planName": "[E-COMMERCE_PROJECT] State Management Strategy",
    "version": "[2.1.0]",
    "targetFramework": "[REACT_FRAMEWORK]",
    "lastUpdated": "[2025-01-15T10:30:00Z]",
    "projectContext": {
      "projectType": "[WEB_APPLICATION]",
      "applicationScale": "[MEDIUM_SCALE]",
      "teamSize": "[SMALL_TEAM]",
      "description": "[MODERN_E_COMMERCE_APP_STATE_MANAGEMENT]"
    }
  },
  "architecture": {
    "architecturalStrategy": {
      "strategyType": "[HYBRID_STRATEGY]",
      "rationale": "[COMBINES_LOCAL_GLOBAL_SERVER_STATE_EFFICIENTLY]"
    },
    "designPatterns": [
      {
        "patternName": "[ATOMIC_PATTERN]",
        "applicationContext": "[GRANULAR_STATE_MANAGEMENT]"
      },
      {
        "patternName": "[REACTIVE_PATTERN]",
        "applicationContext": "[AUTOMATIC_UI_UPDATES]"
      }
    ],
    "dataFlowModel": {
      "flowType": "[UNIDIRECTIONAL_FLOW]",
      "communicationModel": "[OBSERVER_COMMUNICATION]"
    }
  },
  "stateTypes": {
    "stateClassification": {
      "localState": {
        "definition": "[COMPONENT_SPECIFIC_UI_STATE]",
        "examples": [
          {
            "stateName": "[SEARCH_FILTERS]",
            "stateType": "[UI_STATE]",
            "scope": "[FEATURE_SCOPE]",
            "persistence": "[SESSION_PERSISTENCE]"
          }
        ],
        "managementApproach": {
          "library": "[BUILT_IN_STATE_HOOKS]",
          "patterns": ["[COMPONENT_STATE_PATTERN]"]
        }
      },
      "globalState": {
        "definition": "[APPLICATION_WIDE_SHARED_STATE]",
        "examples": [
          {
            "stateName": "[USER_SESSION]",
            "stateType": "[AUTHENTICATION]",
            "accessPattern": "[GLOBAL_ACCESS]",
            "persistence": {
              "enabled": true,
              "storage": "[LOCAL_STORAGE]",
              "ttl": "[24_HOURS]"
            }
          }
        ],
        "managementApproach": {
          "library": "[ZUSTAND_LIBRARY]",
          "architecture": "[CENTRALIZED_STORE]"
        }
      },
      "serverState": {
        "definition": "[API_DATA_AND_CACHE_MANAGEMENT]",
        "dataFetching": {
          "strategy": "[QUERY_BASED_FETCHING]",
          "library": "[TANSTACK_QUERY]"
        },
        "caching": {
          "strategy": "[STALE_WHILE_REVALIDATE]",
          "ttl": "[5_MINUTES]"
        }
      }
    }
  },
  "libraries": {
    "primaryLibraries": [
      {
        "name": "[ZUSTAND]",
        "version": "[4.5.0]",
        "purpose": "[GLOBAL_STATE_MANAGEMENT]",
        "justification": "[LIGHTWEIGHT_AND_FLEXIBLE]"
      },
      {
        "name": "[TANSTACK_QUERY]",
        "version": "[5.0.0]",
        "purpose": "[SERVER_STATE_MANAGEMENT]",
        "justification": "[BEST_IN_CLASS_SERVER_STATE]"
      }
    ]
  },
  "performance": {
    "optimizationStrategies": {
      "renderOptimization": {
        "memoization": "[SELECTOR_MEMOIZATION]",
        "componentOptimization": "[REACT_MEMO_USAGE]"
      },
      "bundleOptimization": {
        "codeSplitting": "[FEATURE_BASED_SPLITTING]",
        "lazyLoading": "[ROUTE_BASED_LAZY_LOADING]"
      }
    },
    "monitoring": {
      "metrics": ["[STATE_SIZE]", "[RENDER_COUNT]", "[CACHE_HIT_RATE]"],
      "tools": ["[REACT_DEVTOOLS]", "[QUERY_DEVTOOLS]"]
    }
  }
}
```

### **Cómo Adaptar Este Ejemplo**

1. **Reemplazar Placeholders**: Sustituir todos los `[VARIABLE]` con valores específicos del proyecto
2. **Ajustar Escala**: Modificar estrategias según `[APPLICATION_SCALE]`
3. **Cambiar Framework**: Adaptar librerías según `[FRONTEND_FRAMEWORK]`
4. **Personalizar Contexto**: Ajustar según `[PROJECT_TYPE]` y `[TEAM_SIZE]`

---

## 10) Checklist Universal de Implementación

### **Planificación y Arquitectura**
- [ ] **Análisis de Contexto**: `[PROJECT_CONTEXT]` completamente definido
- [ ] **Selección de Framework**: `[FRONTEND_FRAMEWORK]` y stack tecnológico confirmado
- [ ] **Estrategia Arquitectónica**: `[ARCHITECTURE_STRATEGY]` seleccionada y justificada
- [ ] **Clasificación de Estado**: Tipos de estado `[STATE_TYPES]` identificados y categorizados
- [ ] **Patrones de Diseño**: `[DESIGN_PATTERNS]` aplicables seleccionados
- [ ] **Flujo de Datos**: `[DATA_FLOW_MODEL]` definido y documentado

### **Selección de Herramientas**
- [ ] **Librerías Primarias**: `[PRIMARY_LIBRARIES]` evaluadas y seleccionadas
- [ ] **Criterios de Selección**: `[SELECTION_CRITERIA]` documentados y aplicados
- [ ] **Justificación**: `[LIBRARY_JUSTIFICATION]` para cada herramienta documentada
- [ ] **Compatibilidad**: Integración entre `[LIBRARY_INTEGRATIONS]` verificada
- [ ] **Licencias**: Compatibilidad de licencias `[LICENSE_COMPATIBILITY]` confirmada

### **Implementación**
- [ ] **Estado Local**: `[LOCAL_STATE_IMPLEMENTATION]` configurado según patrones
- [ ] **Estado Global**: `[GLOBAL_STATE_IMPLEMENTATION]` implementado y probado
- [ ] **Estado Servidor**: `[SERVER_STATE_IMPLEMENTATION]` con caching configurado
- [ ] **Estado Compartido**: `[SHARED_STATE_IMPLEMENTATION]` con sincronización
- [ ] **Optimizaciones**: `[OPTIMIZATION_STRATEGIES]` aplicadas y validadas
- [ ] **Manejo de Errores**: `[ERROR_HANDLING_APPROACH]` implementado

### **Testing y Calidad**
- [ ] **Estrategia de Testing**: `[TESTING_STRATEGY]` definida e implementada
- [ ] **Cobertura de Tests**: `[TEST_COVERAGE]` objetivo alcanzado
- [ ] **Tests de Performance**: `[PERFORMANCE_TESTING]` configurados y ejecutados
- [ ] **Herramientas de Testing**: `[TESTING_TOOLS]` configuradas y funcionando
- [ ] **Automatización**: `[TEST_AUTOMATION]` pipeline configurado

### **Monitoring y Performance**
- [ ] **Métricas**: `[PERFORMANCE_METRICS]` definidas y monitoreadas
- [ ] **Herramientas de Monitoring**: `[MONITORING_TOOLS]` configuradas
- [ ] **Alertas**: `[ALERTING_STRATEGY]` implementada y probada
- [ ] **Benchmarks**: `[PERFORMANCE_BENCHMARKS]` establecidos y validados
- [ ] **Optimización Continua**: Proceso de `[CONTINUOUS_OPTIMIZATION]` definido

### **Documentación y Equipo**
- [ ] **Documentación**: `[DOCUMENTATION_STRATEGY]` completada y actualizada
- [ ] **Guías**: `[CODING_STANDARDS]` y `[BEST_PRACTICES]` documentadas
- [ ] **Ejemplos**: `[CODE_EXAMPLES]` creados y validados
- [ ] **Troubleshooting**: `[TROUBLESHOOTING_GUIDE]` preparada
- [ ] **Capacitación**: `[TEAM_TRAINING]` planificada y ejecutada
- [ ] **Mantenimiento**: `[MAINTENANCE_PLAN]` definido y programado

---

## 11) Recursos y Referencias Universales

### **Patrones y Metodologías**
- **State Management Patterns**: Flux, Redux, MobX, Atomic, Reactive patterns
- **Architecture Patterns**: Centralized, Distributed, Hybrid, Layered approaches
- **Performance Patterns**: Memoization, Normalization, Caching strategies
- **Testing Patterns**: Unit, Integration, E2E testing for state management

### **Criterios de Evaluación de Herramientas**
- **Technical Criteria**: `[PERFORMANCE]`, `[BUNDLE_SIZE]`, `[API_DESIGN]`, `[ECOSYSTEM]`
- **Business Criteria**: `[LEARNING_CURVE]`, `[MAINTENANCE_COST]`, `[TEAM_EXPERTISE]`
- **Quality Criteria**: `[DOCUMENTATION]`, `[COMMUNITY_SUPPORT]`, `[STABILITY]`

### **Metodologías de Investigación**
- **Framework Research**: Investigar patrones específicos del `[FRONTEND_FRAMEWORK]`
- **Scale Research**: Buscar soluciones apropiadas para `[APPLICATION_SCALE]`
- **Industry Research**: Analizar casos de uso similares en `[PROJECT_TYPE]`
- **Performance Research**: Estudiar optimizaciones para `[PERFORMANCE_REQUIREMENTS]`

### **Plantillas de Evaluación**
- **Library Comparison Matrix**: Comparar `[LIBRARY_OPTIONS]` según criterios
- **Architecture Decision Records**: Documentar decisiones de `[ARCHITECTURE_CHOICES]`
- **Performance Benchmarks**: Establecer métricas para `[PERFORMANCE_TARGETS]`
- **Migration Plans**: Planificar transiciones entre `[MIGRATION_STRATEGIES]`

### **Recursos de Aprendizaje por Contexto**
- **Small Scale Projects**: Recursos para `[SIMPLE_STATE_MANAGEMENT]`
- **Medium Scale Projects**: Guías para `[MODERATE_COMPLEXITY_STATE]`
- **Large Scale Projects**: Patrones para `[COMPLEX_STATE_ARCHITECTURE]`
- **Enterprise Projects**: Estrategias para `[ENTERPRISE_STATE_MANAGEMENT]`

### **Herramientas de Desarrollo**
- **DevTools**: Herramientas de desarrollo específicas para `[CHOSEN_LIBRARIES]`
- **Testing Tools**: Frameworks de testing compatibles con `[TESTING_STRATEGY]`
- **Performance Tools**: Herramientas de profiling para `[PERFORMANCE_MONITORING]`
- **Documentation Tools**: Generadores de documentación para `[DOCUMENTATION_APPROACH]`

---

**Versión del Template:** 3.0 - Template Universal con Placeholders  
**Última actualización:** Enero 2025 con metodología template-first y patrones universales  
**Compatibilidad:** Cualquier framework frontend, escala de aplicación y stack tecnológico
