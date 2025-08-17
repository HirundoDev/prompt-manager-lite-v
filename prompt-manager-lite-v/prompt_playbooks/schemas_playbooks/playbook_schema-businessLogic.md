# Playbook: Universal Business Logic Schema Template

## Propósito
Este playbook guía el uso del schema `businessLogic.json` como template universal para documentar lógica de negocio y modelos de dominio. El schema utiliza placeholders `[VARIABLE]` que deben ser reemplazados con información específica del proyecto, permitiendo adaptabilidad a cualquier dominio de negocio, arquitectura o patrón de diseño.

## Filosofía Template-First
- **Schema como Receptor**: El schema está diseñado para RECIBIR información, no para definirla
- **Placeholders Universales**: Usar `[VARIABLE]` para todos los valores específicos del proyecto
- **Adaptabilidad Total**: Funciona para cualquier dominio (e-commerce, fintech, healthcare, etc.)
- **Mejores Prácticas Generales**: Incorpora patrones universales de modelado de dominio sin prescribir tecnologías específicas

**Ubicación del schema:** `schemas/master_blueprint_parts/businessLogic.json`

## Metodología de Implementación 2025

### 1. Domain Model - Modelado del Dominio
```json
{
  "domainModel": {
    "boundedContexts": [
      {
        "name": "Order Management",
        "description": "Handles order lifecycle from creation to fulfillment",
        "ubiquitousLanguage": {
          "Order": "A customer request for products or services",
          "OrderLine": "Individual item within an order",
          "Fulfillment": "Process of completing an order"
        },
        "responsibilities": ["Order processing", "Inventory allocation", "Payment handling"]
      }
    ],
    "aggregates": [
      {
        "name": "Order",
        "rootEntity": "Order",
        "invariants": ["Order total must equal sum of line items", "Order cannot be modified after shipping"],
        "consistencyBoundary": "Strong"
      }
    ]
  }
}
```

### 2. Business Rules - Reglas de Negocio Categorizadas
Implementar reglas de negocio organizadas por responsabilidad:
- **Validation Rules:** Syntax, semantic, cross-field validation
- **Business Invariants:** Conditions that must always be true
- **Calculation Rules:** Mathematical and logical computations
- **Decision Rules:** Conditional logic and workflow decisions

```json
{
  "businessRules": {
    "validationRules": [
      {
        "id": "VR-001",
        "name": "Order Date Validation",
        "type": "Syntax",
        "description": "Order date cannot be in the past",
        "validation": {
          "expression": "orderDate >= today()",
          "errorMessage": "Order date must be today or in the future",
          "severity": "Error"
        },
        "scope": "Entity",
        "triggers": ["Create", "Update"]
      }
    ],
    "businessInvariants": [
      {
        "id": "INV-001",
        "name": "Order Total Consistency",
        "description": "Order total must always equal sum of line items plus taxes",
        "invariant": {
          "condition": "order.total == sum(lineItems.amount) + order.taxes",
          "enforcement": "Application-Logic",
          "violationAction": "Reject-Operation"
        },
        "aggregate": "Order",
        "consistencyModel": "Strong"
      }
    ]
  }
}
```

### 3. Domain Events - Eventos del Dominio
Definir eventos que representan cambios significativos en el dominio:
- **Event Design:** Past tense naming, immutable payload
- **Event Sourcing:** Optional event store configuration
- **Event Handlers:** Synchronous and asynchronous processing
- **Event Metadata:** Correlation, causation, timestamps

```json
{
  "domainEvents": {
    "events": [
      {
        "name": "OrderPlaced",
        "description": "Triggered when a customer places a new order",
        "version": "1.0.0",
        "payload": {
          "schema": {
            "orderId": "string",
            "customerId": "string",
            "items": "array",
            "total": "number"
          },
          "required": ["orderId", "customerId", "total"],
          "immutable": true
        },
        "triggers": ["PlaceOrder command"],
        "handlers": [
          {
            "name": "InventoryReservation",
            "type": "Asynchronous",
            "idempotent": true
          }
        ]
      }
    ],
    "eventSourcing": {
      "enabled": true,
      "eventStore": {
        "type": "EventStore",
        "partitioning": "By-Aggregate"
      }
    }
  }
}
```

### 4. Policies - Políticas de Negocio
Implementar políticas que gobiernan el comportamiento del sistema:
- **Policy Types:** Security, compliance, business, technical
- **Enforcement Levels:** Hard, soft, advisory
- **Compliance Mapping:** Link to regulatory frameworks

```json
{
  "policies": [
    {
      "id": "POL-001",
      "name": "Data Retention Policy",
      "type": "Compliance",
      "description": "Customer data must be retained for 7 years for audit purposes",
      "scope": "Global",
      "enforcement": {
        "level": "Hard",
        "mechanism": "Database-Constraint",
        "violationAction": "Block"
      },
      "compliance": ["GDPR", "SOX"],
      "reviewCycle": "Annually"
    }
  ]
}
```

## Proceso de Implementación Paso a Paso

### Fase 1: Domain Discovery (2-3 semanas)
1. **Event Storming:** Identificar domain events y bounded contexts
2. **Ubiquitous Language:** Definir vocabulario común con domain experts
3. **Bounded Context Mapping:** Identificar context boundaries y relationships
4. **Aggregate Design:** Definir aggregates y consistency boundaries
5. **Entity Modeling:** Modelar entities, value objects, y domain services

### Fase 2: Business Rules Analysis (2-3 semanas)
1. **Rule Discovery:** Identificar todas las business rules del dominio
2. **Rule Categorization:** Clasificar rules por tipo y responsabilidad
3. **Validation Design:** Diseñar validation strategies (syntax, semantic)
4. **Invariant Definition:** Definir business invariants y enforcement
5. **Calculation Logic:** Modelar calculation rules y formulas

### Fase 3: Event Design (1-2 semanas)
1. **Event Identification:** Identificar domain events significativos
2. **Event Schema Design:** Diseñar event payloads y versioning
3. **Event Sourcing Setup:** Configurar event store si es necesario
4. **Handler Design:** Diseñar event handlers y processing patterns
5. **Integration Events:** Definir events para integration con otros contexts

### Fase 4: Policy Implementation (1-2 semanas)
1. **Policy Discovery:** Identificar policies de negocio y compliance
2. **Enforcement Design:** Diseñar enforcement mechanisms
3. **Compliance Mapping:** Mapear policies a regulatory requirements
4. **Violation Handling:** Definir actions para policy violations
5. **Review Processes:** Establecer policy review y update cycles

### Fase 5: Rules Engine Setup (2-3 semanas)
1. **Engine Selection:** Elegir rules engine apropiado
2. **Rule Implementation:** Implementar rules en engine format
3. **Testing Strategy:** Crear comprehensive test suites
4. **Performance Optimization:** Optimizar rule execution
5. **Monitoring Setup:** Implementar rule execution monitoring

## Checklist de Validación 2025

### ✅ Domain Model Completeness
- [ ] Bounded contexts claramente definidos con responsibilities
- [ ] Ubiquitous language documentado y compartido
- [ ] Aggregates diseñados con consistency boundaries apropiados
- [ ] Entities y value objects correctamente modelados
- [ ] Domain services identificados para cross-entity logic
- [ ] Integration patterns definidos entre contexts

### ✅ Business Rules Coverage
- [ ] Validation rules cubren syntax y semantic validation
- [ ] Business invariants definidos para cada aggregate
- [ ] Calculation rules implementadas con proper precision
- [ ] Decision rules cubren todos los workflow branches
- [ ] Rule dependencies identificadas y documentadas
- [ ] Error handling y messaging definidos

### ✅ Domain Events Design
- [ ] Events nombrados en past tense con clear semantics
- [ ] Event schemas versionados y backward compatible
- [ ] Event handlers diseñados para idempotency
- [ ] Event sourcing configurado si es requerido
- [ ] Event metadata incluye correlation y causation
- [ ] Integration events definidos para external systems

### ✅ Policy Implementation
- [ ] Policies categorizadas por type y scope
- [ ] Enforcement mechanisms apropiados implementados
- [ ] Compliance requirements mapeados a policies
- [ ] Violation actions definidas y tested
- [ ] Policy owners asignados y review cycles establecidos
- [ ] Policy changes tracked y audited

### ✅ Rules Engine Configuration
- [ ] Engine type seleccionado apropiado para requirements
- [ ] Rule format y execution mode configurados
- [ ] Conflict resolution strategy definida
- [ ] Performance optimization implementada
- [ ] Testing coverage completa para all rules
- [ ] Monitoring y alerting configurados

## Mejores Prácticas 2025

### 🎯 Domain-Driven Design Excellence
- **Bounded Context Clarity:** Definir clear boundaries y responsibilities
- **Ubiquitous Language:** Usar consistent terminology en code y documentation
- **Aggregate Design:** Mantener aggregates small y focused
- **Event-First Thinking:** Diseñar around domain events, no data structures

### 📋 Business Rules Management
- **Rule Categorization:** Separar validation, invariants, calculations, decisions
- **Single Responsibility:** Cada rule debe tener una single, clear responsibility
- **Testability:** Diseñar rules para easy unit y integration testing
- **Traceability:** Link rules a business requirements y compliance needs

### ⚡ Event Sourcing Patterns
- **Event Immutability:** Events nunca deben ser modified después de creation
- **Event Versioning:** Plan for schema evolution desde el beginning
- **Snapshot Strategy:** Implement snapshots para performance optimization
- **Projection Design:** Diseñar projections para specific read models

### 🔧 Rules Engine Optimization
- **Rule Indexing:** Optimize rule matching para performance
- **Fact Caching:** Cache frequently accessed facts
- **Parallel Execution:** Execute independent rules en parallel
- **Monitoring:** Track rule execution performance y accuracy

### 🛡️ Policy Enforcement
- **Defense in Depth:** Implement policies en multiple layers
- **Fail-Safe Defaults:** Default to secure/compliant behavior
- **Audit Trail:** Log all policy decisions y violations
- **Regular Review:** Regularly review y update policies

## Herramientas Recomendadas 2025

### Domain Modeling
- **Event Storming:** Miro, Mural, physical sticky notes
- **Domain Modeling:** PlantUML, Lucidchart, draw.io
- **Documentation:** Confluence, Notion, GitBook

### Business Rules Engines
- **Java:** Drools, Easy Rules, OpenL Tablets
- **.NET:** Microsoft Rules Engine, NRules
- **JavaScript:** JSON Rules Engine, node-rules
- **Cloud:** AWS Rules Engine, Azure Logic Apps

### Event Sourcing
- **Event Stores:** EventStore, Apache Kafka, AWS EventBridge
- **Projections:** Apache Kafka Streams, Azure Stream Analytics
- **CQRS:** Axon Framework, NEventStore, Eventuous

### Testing & Validation
- **Unit Testing:** JUnit, NUnit, Jest, pytest
- **BDD Testing:** Cucumber, SpecFlow, Behave
- **Property Testing:** QuickCheck, FsCheck, Hypothesis

## Patrones de Implementación por Contexto

### E-commerce Platform
```json
{
  "domainModel": {
    "boundedContexts": [
      {
        "name": "Catalog",
        "responsibilities": ["Product management", "Pricing", "Inventory"]
      },
      {
        "name": "Orders",
        "responsibilities": ["Order processing", "Payment", "Fulfillment"]
      }
    ]
  },
  "businessRules": {
    "validationRules": [
      {
        "id": "VR-001",
        "name": "Product Availability",
        "type": "Semantic",
        "description": "Cannot order out-of-stock products"
      }
    ]
  }
}
```

### Financial Services
```json
{
  "policies": [
    {
      "id": "POL-001",
      "name": "KYC Compliance",
      "type": "Compliance",
      "enforcement": {
        "level": "Hard",
        "mechanism": "External-Service"
      },
      "compliance": ["AML", "KYC", "GDPR"]
    }
  ]
}
```

### Healthcare System
```json
{
  "businessRules": {
    "businessInvariants": [
      {
        "id": "INV-001",
        "name": "Patient Privacy",
        "description": "Patient data access must be logged and authorized",
        "enforcement": "Application-Logic",
        "compliance": ["HIPAA"]
      }
    ]
  }
}
```

## Métricas de Éxito

### Domain Model Quality
- **Context Cohesion:** Measure cohesion within bounded contexts
- **Coupling Metrics:** Track coupling between contexts
- **Language Consistency:** Monitor ubiquitous language usage
- **Model Stability:** Track frequency of model changes

### Business Rules Effectiveness
- **Rule Coverage:** Percentage of business requirements covered
- **Rule Accuracy:** Accuracy of rule execution results
- **Rule Performance:** Execution time per rule category
- **Rule Maintenance:** Time to update rules for business changes

### Event Processing
- **Event Throughput:** Events processed per second
- **Processing Latency:** Time from event creation to processing
- **Handler Success Rate:** Percentage of successful event handling
- **Event Store Performance:** Read/write performance metrics

### Policy Compliance
- **Compliance Rate:** Percentage of operations compliant with policies
- **Violation Detection:** Time to detect policy violations
- **Remediation Time:** Time to resolve policy violations
- **Audit Readiness:** Time to generate compliance reports

## Troubleshooting Common Issues

### Domain Model Problems
- **Context Boundaries:** Unclear boundaries leading to tight coupling
- **Solution:** Refactor using context mapping patterns, implement anti-corruption layers

### Business Rules Issues
- **Rule Conflicts:** Multiple rules producing contradictory results
- **Solution:** Implement conflict resolution strategies, prioritize rules

### Event Sourcing Challenges
- **Event Schema Evolution:** Breaking changes in event schemas
- **Solution:** Implement event upcasting, maintain backward compatibility

### Performance Issues
- **Slow Rule Execution:** Rules engine performance degradation
- **Solution:** Implement rule indexing, optimize fact matching, use caching

## Referencias y Recursos

### Domain-Driven Design
- **Eric Evans DDD:** Original Domain-Driven Design book
- **Vaughn Vernon:** Implementing Domain-Driven Design
- **Martin Fowler:** Domain-Driven Design articles
- **DDD Community:** Online resources and patterns

### Business Rules Management
- **Business Rules Group:** BRG standards and best practices
- **SBVR:** Semantics of Business Vocabulary and Rules
- **DMN:** Decision Model and Notation standard

### Event Sourcing & CQRS
- **Greg Young:** Event Sourcing patterns and practices
- **Udi Dahan:** CQRS and event-driven architecture
- **Martin Fowler:** Event Sourcing articles

### Compliance & Governance
- **GDPR:** General Data Protection Regulation
- **SOX:** Sarbanes-Oxley Act requirements
- **HIPAA:** Health Insurance Portability and Accountability Act

---

**Última actualización:** Diciembre 2025  
**Versión del schema:** 3.0.0  
**Compatibilidad:** JSON Schema Draft 2020-12