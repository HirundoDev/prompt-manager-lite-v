# Schema Playbook — architecture (Universal Template Edition)

**Purpose:** Universal template-first methodology for documenting software architecture that works across any technology stack, architectural pattern, or system type. This playbook guides you through filling the `architecture.json` template with placeholders to create comprehensive architecture documentation for monoliths, microservices, serverless, event-driven, or any other architectural style.

**Schema Location:** `schemas/master_blueprint_parts/architecture.json`  
**Template Version:** 3.0.0 - Universal Template with Placeholders  
**Last Updated:** 2025-01-15  
**Based on:** ARC42, C4 Model, and modern architecture documentation best practices

---

## 🎯 Template Philosophy

### **Universal Architecture Documentation**
This schema is designed as a **template with placeholders** that can be adapted to any:
- **Architectural Style:** Monolith, Microservices, Serverless, Event-Driven, Layered, Hexagonal, Clean Architecture
- **Technology Stack:** Any programming language, framework, database, or infrastructure
- **System Type:** Web applications, mobile backends, data platforms, IoT systems, enterprise software
- **Scale:** From simple applications to complex distributed systems

### **Placeholder System**
All values use the format `[PLACEHOLDER_NAME]` to indicate where project-specific information should be filled in:
- `[SYSTEM_NAME]` → Your actual system name
- `[ARCHITECTURAL_STYLE]` → Monolith, Microservices, etc.
- `[COMPONENT_NAME]` → Your actual component names
- `[TECHNOLOGY_STACK]` → Your chosen technologies

---

## 📋 Template Structure Guide

### **1. System Information Section (`systemInfo`)**

**Required Placeholders:**
```json
{
  "systemName": "[SYSTEM_NAME]",
  "version": "[ARCHITECTURE_VERSION]",
  "description": "[SYSTEM_DESCRIPTION]",
  "architecturalStyle": "[ARCHITECTURAL_STYLE]"
}
```

**How to Fill:**
- `[SYSTEM_NAME]` → Replace with your system's name (e.g., "E-commerce Platform", "Analytics Engine", "User Management System")
- `[ARCHITECTURE_VERSION]` → Use semantic versioning for architecture evolution (e.g., "1.0.0", "2.1.0")
- `[SYSTEM_DESCRIPTION]` → Brief description of what your system does and its main purpose
- `[ARCHITECTURAL_STYLE]` → Primary architectural pattern you're using

**Examples for Different Architectural Styles:**

**Microservices Architecture:**
```json
{
  "systemName": "E-commerce Platform",
  "version": "2.0.0",
  "description": "Distributed e-commerce platform handling product catalog, orders, payments, and user management",
  "architecturalStyle": "Microservices",
  "technologyStack": {
    "programmingLanguages": ["Java", "Node.js", "Python"],
    "frameworks": ["Spring Boot", "Express.js", "FastAPI"],
    "databases": ["PostgreSQL", "MongoDB", "Redis"],
    "infrastructure": ["Kubernetes", "Docker", "AWS"]
  }
}
```

**Monolithic Architecture:**
```json
{
  "systemName": "Content Management System",
  "version": "1.5.0",
  "description": "Integrated content management platform for publishing and editorial workflows",
  "architecturalStyle": "Monolith",
  "technologyStack": {
    "programmingLanguages": ["C#"],
    "frameworks": [".NET Core", "Entity Framework"],
    "databases": ["SQL Server"],
    "infrastructure": ["Azure App Service", "Azure SQL"]
  }
}
```

**Serverless Architecture:**
```json
{
  "systemName": "Image Processing Pipeline",
  "version": "1.0.0",
  "description": "Event-driven image processing and transformation service",
  "architecturalStyle": "Serverless",
  "technologyStack": {
    "programmingLanguages": ["Python", "JavaScript"],
    "frameworks": ["AWS Lambda", "Serverless Framework"],
    "databases": ["DynamoDB", "S3"],
    "infrastructure": ["AWS Lambda", "API Gateway", "CloudWatch"]
  }
}
```

### **2. System Context Section (`systemContext`)**

**Template Structure:**
```json
{
  "businessContext": {
    "stakeholders": [
      {
        "name": "[STAKEHOLDER_NAME]",
        "role": "[STAKEHOLDER_ROLE]",
        "responsibilities": ["[RESPONSIBILITY]"],
        "interactions": ["[INTERACTION_TYPE]"]
      }
    ],
    "externalSystems": [
      {
        "name": "[EXTERNAL_SYSTEM_NAME]",
        "purpose": "[SYSTEM_PURPOSE]",
        "interface": "[INTERFACE_TYPE]",
        "dataExchanged": ["[DATA_TYPE]"]
      }
    ]
  }
}
```

**How to Fill:**
- `[STAKEHOLDER_NAME]` → Actual stakeholder names or types (e.g., "End Users", "Administrators", "Payment Gateway")
- `[EXTERNAL_SYSTEM_NAME]` → Names of external systems you integrate with
- `[INTERFACE_TYPE]` → How you communicate (REST API, GraphQL, Message Queue, etc.)

**Examples for Different System Types:**

**E-commerce System Context:**
```json
{
  "businessContext": {
    "stakeholders": [
      {
        "name": "Customers",
        "role": "End Users",
        "responsibilities": ["Browse products", "Place orders", "Make payments"],
        "interactions": ["Web interface", "Mobile app"]
      },
      {
        "name": "Store Administrators",
        "role": "System Managers",
        "responsibilities": ["Manage inventory", "Process orders", "View analytics"],
        "interactions": ["Admin dashboard", "API access"]
      }
    ],
    "externalSystems": [
      {
        "name": "Payment Gateway",
        "purpose": "Process credit card payments",
        "interface": "REST API",
        "dataExchanged": ["Payment details", "Transaction status"]
      },
      {
        "name": "Shipping Provider",
        "purpose": "Calculate shipping costs and track deliveries",
        "interface": "SOAP API",
        "dataExchanged": ["Shipping rates", "Tracking information"]
      }
    ]
  }
}
```

### **3. Solution Strategy Section (`solutionStrategy`)**

**Template Structure:**
```json
{
  "architecturalPatterns": [
    {
      "pattern": "[ARCHITECTURAL_PATTERN]",
      "rationale": "[PATTERN_RATIONALE]",
      "implementation": "[IMPLEMENTATION_APPROACH]",
      "tradeoffs": ["[TRADEOFF]"]
    }
  ],
  "technologyChoices": [
    {
      "category": "[TECHNOLOGY_CATEGORY]",
      "chosen": "[CHOSEN_TECHNOLOGY]",
      "alternatives": ["[ALTERNATIVE_TECHNOLOGY]"],
      "rationale": "[CHOICE_RATIONALE]"
    }
  ]
}
```

**Examples for Different Patterns:**

**CQRS Pattern Implementation:**
```json
{
  "architecturalPatterns": [
    {
      "pattern": "CQRS (Command Query Responsibility Segregation)",
      "rationale": "Separate read and write operations for better scalability and performance",
      "implementation": "Separate command and query models with event sourcing",
      "tradeoffs": [
        "Increased complexity but better scalability",
        "Eventual consistency vs immediate consistency"
      ]
    }
  ]
}
```

**Repository Pattern Implementation:**
```json
{
  "architecturalPatterns": [
    {
      "pattern": "Repository Pattern",
      "rationale": "Abstract data access layer for better testability and maintainability",
      "implementation": "Interface-based repositories with dependency injection",
      "tradeoffs": [
        "Additional abstraction layer but improved testability",
        "More code but better separation of concerns"
      ]
    }
  ]
}
```

### **4. Building Blocks Section (`buildingBlocks`)**

**Template Structure:**
```json
{
  "components": [
    {
      "name": "[COMPONENT_NAME]",
      "type": "[COMPONENT_TYPE]",
      "description": "[COMPONENT_DESCRIPTION]",
      "responsibilities": ["[RESPONSIBILITY]"],
      "dependencies": ["[DEPENDENCY_NAME]"],
      "interfaces": [
        {
          "name": "[INTERFACE_NAME]",
          "type": "[INTERFACE_TYPE]",
          "description": "[INTERFACE_DESCRIPTION]"
        }
      ]
    }
  ]
}
```

**Examples for Different Component Types:**

**Microservices Components:**
```json
{
  "components": [
    {
      "name": "User Service",
      "type": "Microservice",
      "description": "Manages user accounts, authentication, and profiles",
      "responsibilities": [
        "User registration and authentication",
        "Profile management",
        "User preferences"
      ],
      "dependencies": ["Database", "Authentication Provider", "Email Service"],
      "interfaces": [
        {
          "name": "User REST API",
          "type": "REST",
          "description": "HTTP API for user operations"
        },
        {
          "name": "User Events",
          "type": "Event",
          "description": "Publishes user lifecycle events"
        }
      ]
    },
    {
      "name": "Product Service",
      "type": "Microservice",
      "description": "Manages product catalog and inventory",
      "responsibilities": [
        "Product information management",
        "Inventory tracking",
        "Price management"
      ],
      "dependencies": ["Product Database", "Image Storage"],
      "interfaces": [
        {
          "name": "Product API",
          "type": "GraphQL",
          "description": "GraphQL API for product queries"
        }
      ]
    }
  ]
}
```

**Monolithic Components:**
```json
{
  "components": [
    {
      "name": "Web Controller Layer",
      "type": "Layer",
      "description": "Handles HTTP requests and responses",
      "responsibilities": [
        "Request routing",
        "Input validation",
        "Response formatting"
      ],
      "dependencies": ["Business Logic Layer"],
      "interfaces": [
        {
          "name": "HTTP Endpoints",
          "type": "REST",
          "description": "RESTful API endpoints"
        }
      ]
    },
    {
      "name": "Business Logic Layer",
      "type": "Layer",
      "description": "Contains core business rules and processes",
      "responsibilities": [
        "Business rule enforcement",
        "Data processing",
        "Workflow orchestration"
      ],
      "dependencies": ["Data Access Layer"],
      "interfaces": [
        {
          "name": "Service Interfaces",
          "type": "Internal",
          "description": "Internal service contracts"
        }
      ]
    }
  ]
}
```

### **5. Architectural Decisions Section (`architecturalDecisions`)**

**Template Structure:**
```json
[
  {
    "id": "[ADR_ID]",
    "title": "[ADR_TITLE]",
    "status": "[ADR_STATUS]",
    "date": "[DECISION_DATE]",
    "context": "[DECISION_CONTEXT]",
    "decision": "[DECISION_MADE]",
    "consequences": ["[CONSEQUENCE]"],
    "alternatives": ["[ALTERNATIVE_OPTION]"]
  }
]
```

**Example ADR:**
```json
[
  {
    "id": "ADR-001",
    "title": "Use PostgreSQL as Primary Database",
    "status": "Accepted",
    "date": "2025-01-15",
    "context": "We need a reliable, ACID-compliant database for our e-commerce platform with complex relationships between users, products, and orders.",
    "decision": "We will use PostgreSQL as our primary database for transactional data.",
    "consequences": [
      "Strong consistency and ACID compliance",
      "Excellent support for complex queries and relationships",
      "Need to manage database scaling as we grow"
    ],
    "alternatives": [
      "MongoDB for document-based approach",
      "MySQL for simpler relational needs",
      "DynamoDB for cloud-native scalability"
    ]
  }
]
```

### **6. Runtime View Section (`runtimeView`)**

**Template Structure:**
```json
{
  "scenarios": [
    {
      "name": "[SCENARIO_NAME]",
      "description": "[SCENARIO_DESCRIPTION]",
      "actors": ["[ACTOR_NAME]"],
      "steps": [
        {
          "step": 1,
          "actor": "[STEP_ACTOR]",
          "action": "[ACTION_DESCRIPTION]",
          "result": "[ACTION_RESULT]"
        }
      ]
    }
  ]
}
```

**Example Scenario:**
```json
{
  "scenarios": [
    {
      "name": "User Places Order",
      "description": "Complete flow of a user placing an order in the e-commerce system",
      "actors": ["Customer", "User Service", "Product Service", "Order Service", "Payment Service"],
      "steps": [
        {
          "step": 1,
          "actor": "Customer",
          "action": "Adds products to cart and initiates checkout",
          "result": "Cart data is validated and checkout process begins"
        },
        {
          "step": 2,
          "actor": "User Service",
          "action": "Validates user authentication and shipping address",
          "result": "User credentials confirmed and address validated"
        },
        {
          "step": 3,
          "actor": "Product Service",
          "action": "Checks product availability and reserves inventory",
          "result": "Products reserved for the order"
        },
        {
          "step": 4,
          "actor": "Payment Service",
          "action": "Processes payment with external payment gateway",
          "result": "Payment confirmed and transaction ID generated"
        },
        {
          "step": 5,
          "actor": "Order Service",
          "action": "Creates order record and triggers fulfillment",
          "result": "Order created with confirmation number sent to customer"
        }
      ]
    }
  ]
}
```

---

## 🛠️ Implementation Methodology

### **Step 1: System Analysis**
1. **Identify System Boundaries:** What's inside vs outside your system?
2. **Map Stakeholders:** Who interacts with your system and how?
3. **List External Dependencies:** What systems do you integrate with?
4. **Define Quality Goals:** What are your key quality requirements?

### **Step 2: Architectural Design**
1. **Choose Architectural Style:** Monolith, Microservices, Serverless, etc.
2. **Apply Design Patterns:** Repository, CQRS, Event Sourcing, etc.
3. **Select Technologies:** Programming languages, frameworks, databases
4. **Design Components:** Break down system into logical components

### **Step 3: Fill Template Systematically**
1. **Start with `systemInfo`:** Basic system information and technology stack
2. **Define `systemContext`:** Stakeholders and external systems
3. **Document `solutionStrategy`:** Patterns, principles, and technology choices
4. **Detail `buildingBlocks`:** Components, interfaces, and data flows
5. **Record `architecturalDecisions`:** Key decisions and their rationale

### **Step 4: Validate and Iterate**
1. **Review with Stakeholders:** Ensure architecture meets requirements
2. **Validate Technical Feasibility:** Can this be implemented as designed?
3. **Check Quality Attributes:** Does architecture support quality goals?
4. **Document Runtime Scenarios:** How does the system behave in key scenarios?

---

## 🌍 Universal Examples

### **Microservices E-commerce Platform**
```json
{
  "systemInfo": {
    "systemName": "CloudCommerce Platform",
    "architecturalStyle": "Microservices",
    "technologyStack": {
      "programmingLanguages": ["Java", "Node.js"],
      "frameworks": ["Spring Boot", "Express.js"],
      "infrastructure": ["Kubernetes", "Docker", "AWS"]
    }
  },
  "buildingBlocks": {
    "components": [
      {
        "name": "API Gateway",
        "type": "Gateway",
        "responsibilities": ["Request routing", "Authentication", "Rate limiting"]
      },
      {
        "name": "User Service",
        "type": "Microservice",
        "responsibilities": ["User management", "Authentication"]
      }
    ]
  }
}
```

### **Serverless Data Processing Pipeline**
```json
{
  "systemInfo": {
    "systemName": "Real-time Analytics Pipeline",
    "architecturalStyle": "Serverless",
    "technologyStack": {
      "programmingLanguages": ["Python"],
      "frameworks": ["AWS Lambda"],
      "infrastructure": ["AWS", "Kinesis", "DynamoDB"]
    }
  },
  "buildingBlocks": {
    "components": [
      {
        "name": "Data Ingestion Function",
        "type": "Lambda Function",
        "responsibilities": ["Receive events", "Validate data", "Transform format"]
      }
    ]
  }
}
```

### **Monolithic Web Application**
```json
{
  "systemInfo": {
    "systemName": "Corporate Intranet Portal",
    "architecturalStyle": "Monolith",
    "technologyStack": {
      "programmingLanguages": ["C#"],
      "frameworks": [".NET Core", "Entity Framework"],
      "infrastructure": ["Azure App Service"]
    }
  },
  "buildingBlocks": {
    "components": [
      {
        "name": "Presentation Layer",
        "type": "Layer",
        "responsibilities": ["UI rendering", "User interaction"]
      },
      {
        "name": "Business Logic Layer",
        "type": "Layer",
        "responsibilities": ["Business rules", "Data processing"]
      }
    ]
  }
}
```

---

## ✅ Validation Checklist

### **Template Completeness**
- [ ] All required placeholders filled with actual values
- [ ] No `[PLACEHOLDER]` format strings remain in final version
- [ ] Architectural style matches actual implementation
- [ ] Technology stack is complete and accurate

### **Architecture Quality**
- [ ] System boundaries are clearly defined
- [ ] Components have clear responsibilities
- [ ] Interfaces between components are well-defined
- [ ] Quality goals are addressed by the architecture

### **Documentation Quality**
- [ ] Architectural decisions are documented with rationale
- [ ] Key scenarios are described with step-by-step flows
- [ ] External dependencies are clearly identified
- [ ] Cross-cutting concerns are addressed

### **Stakeholder Value**
- [ ] Architecture supports business requirements
- [ ] Technical constraints are considered
- [ ] Scalability and performance requirements are addressed
- [ ] Security and compliance requirements are met

---

## 🔄 Maintenance and Evolution

### **Architecture Evolution**
- Update `systemInfo.version` when making significant changes
- Document new architectural decisions as ADRs
- Review and update quality goals as requirements change
- Keep technology stack information current

### **Template Updates**
- Regularly review component responsibilities and interfaces
- Update runtime scenarios as system behavior changes
- Maintain accurate deployment and infrastructure information
- Keep stakeholder and external system information current

### **Team Collaboration**
- Use this template as a living document for architecture discussions
- Regularly review with development teams and stakeholders
- Update based on lessons learned during implementation
- Share architectural knowledge across team members

---

**Remember:** This template is designed to be **universal and adaptable**. The key is to replace all placeholders with values specific to your system while maintaining the structure that makes the architecture documentation useful for development, maintenance, and evolution.