# Schema Playbook — definitions

**Propósito:** Crear sistemas comprehensivos de gestión terminológica siguiendo mejores prácticas de knowledge management 2025, con business glossary management, standardized definitions, cross-references y automated terminology governance con semantic relationships.

**Ubicación:** `schemas/master_blueprint_parts/definitions.json`

---

## **METODOLOGÍA 2025: TERMINOLOGY MANAGEMENT & KNOWLEDGE GOVERNANCE**

### **1. INVESTIGACIÓN PREVIA REQUERIDA**
Antes de crear el glosario, investigar:
- **Terminology Standards:** ISO-1087, ISO-704, ANSI-NISO-Z39.19, Dublin Core, SKOS
- **Knowledge Management:** Business glossary best practices, semantic relationships
- **Governance Frameworks:** Term lifecycle management, approval workflows
- **Integration Patterns:** API documentation, wiki systems, search platforms
- **Automation Tools:** Duplicate detection, consistency checking, link validation

### **2. ESTRUCTURA MODERNA DEL SCHEMA**

#### **A. METADATA SECTION (Requerido)**
```json
{
  "metadata": {
    "name": "E-commerce Platform Glossary",
    "version": "2.1.0",
    "lastUpdated": "2025-01-15T10:30:00Z",
    "description": "Comprehensive terminology for e-commerce platform",
    "domain": "e-commerce|software-development|business-operations",
    "audience": ["developers", "business-users", "stakeholders"],
    "language": "en-US",
    "maintainers": [
      {
        "name": "John Doe",
        "role": "glossary-owner|domain-expert|terminology-manager",
        "email": "john.doe@company.com",
        "department": "Engineering"
      }
    ],
    "standards": ["ISO-1087", "SKOS", "Dublin-Core"]
  }
}
```

#### **B. GLOSSARY SECTION (Core)**
```json
{
  "glossary": {
    "terms": [
      {
        "id": "API_ENDPOINT",
        "term": "API Endpoint",
        "definition": "A specific URL where an API can be accessed by a client application",
        "shortDefinition": "URL for API access",
        "context": {
          "domain": "software-development",
          "subdomain": "web-services",
          "usage": "technical|business|mixed|deprecated",
          "formality": "formal|informal|colloquial|jargon"
        },
        "examples": [
          {
            "example": "https://api.example.com/v1/users",
            "context": "REST API",
            "explanation": "Endpoint for user management operations"
          }
        ],
        "synonyms": ["API URL", "Service Endpoint"],
        "antonyms": ["API Client"],
        "abbreviations": [
          {
            "abbreviation": "API",
            "type": "acronym|initialism|shortening"
          }
        ],
        "relationships": {
          "broaderTerms": ["API"],                    // Hypernyms (more general)
          "narrowerTerms": ["REST Endpoint"],         // Hyponyms (more specific)
          "relatedTerms": ["HTTP Method", "Request"], // Associated terms
          "partOf": ["Web Service"],                  // Terms this is component of
          "hasParts": ["URL Path", "Query Parameters"], // Component terms
          "seeAlso": ["API Documentation"]           // Cross-references
        },
        "translations": [
          {
            "language": "es",
            "term": "Punto de Acceso API",
            "definition": "URL específica donde se puede acceder a una API",
            "verified": true
          }
        ],
        "antiPatterns": [
          {
            "pattern": "Using 'API URL' and 'API Endpoint' interchangeably",
            "reason": "Endpoint implies specific functionality, URL is just location",
            "alternative": "Use 'endpoint' for functional access points"
          }
        ],
        "sources": [
          {
            "type": "specification|documentation|expert|literature",
            "reference": "OpenAPI Specification 3.0",
            "url": "https://spec.openapis.org/oas/v3.0.3",
            "authority": "OpenAPI Initiative",
            "date": "2024-01-15"
          }
        ],
        "lifecycle": {
          "status": "draft|review|approved|deprecated|obsolete",
          "createdAt": "2024-01-15T10:00:00Z",
          "approvedAt": "2024-01-20T14:30:00Z",
          "deprecatedAt": null,
          "replacedBy": null,
          "reviewDate": "2025-01-20"
        },
        "usage": {
          "frequency": "very-common|common|occasional|rare",
          "contexts": ["API documentation", "development", "integration"],
          "searchCount": 1250,
          "lastAccessed": "2025-01-14T16:45:00Z"
        },
        "metadata": {
          "owner": "API Team",
          "steward": "John Doe",
          "reviewer": "Jane Smith",
          "lastModified": "2025-01-10T09:15:00Z",
          "version": "1.2",
          "tags": ["api", "web-services", "integration"],
          "categories": ["technical"],
          "priority": "low|medium|high|critical"
        }
      }
    ],
    "categories": [
      {
        "id": "technical",
        "name": "Technical Terms",
        "description": "Software development and technical concepts",
        "parent": null,
        "children": ["api-terms", "database-terms"],
        "termCount": 150,
        "color": "#007acc",
        "icon": "code"
      }
    ],
    "collections": [
      {
        "id": "api-terms",
        "name": "API & Integration Terms",
        "description": "Terms related to APIs and system integration",
        "terms": ["API_ENDPOINT", "REST_API", "WEBHOOK"],
        "purpose": "Developer onboarding and API documentation",
        "audience": "developers",
        "maintainer": "API Team"
      }
    ]
  }
}
```

#### **C. TYPES SECTION (Reusable Definitions)**
```json
{
  "types": [
    {
      "name": "techStackItem",
      "type": "json-schema|typescript|openapi|graphql|custom",
      "description": "Technology stack component definition",
      "schema": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "category": { 
            "type": "string", 
            "enum": ["Frontend", "Backend", "Database", "DevOps", "Testing", "Mobile", "AI/ML"] 
          },
          "version": { "type": "string" },
          "description": { "type": "string" },
          "status": {
            "type": "string",
            "enum": ["active", "deprecated", "experimental", "legacy"]
          }
        },
        "required": ["name", "category"]
      },
      "examples": [
        {
          "name": "React Framework",
          "value": {
            "name": "React",
            "category": "Frontend",
            "version": "18.2.0",
            "description": "JavaScript library for building user interfaces",
            "status": "active"
          },
          "description": "Modern frontend framework example"
        }
      ],
      "validation": {
        "rules": [
          "Version must follow semantic versioning",
          "Category must be from predefined list"
        ],
        "constraints": {
          "name": { "minLength": 2, "maxLength": 50 },
          "version": { "pattern": "^\\d+\\.\\d+\\.\\d+$" }
        }
      },
      "usage": {
        "contexts": ["architecture documentation", "dependency management"],
        "frequency": "common",
        "dependencies": ["projectInfo", "architecture"]
      },
      "metadata": {
        "version": "2.1.0",
        "deprecated": false,
        "tags": ["technology", "stack", "dependencies"]
      }
    }
  ]
}
```

#### **D. CONVENTIONS SECTION (Style Guidelines)**
```json
{
  "conventions": [
    {
      "id": "CAMEL_CASE_VARS",
      "name": "Camel Case Variables",
      "category": "naming|formatting|structure|documentation|validation",
      "rule": "Variable names should use camelCase notation",
      "pattern": "^[a-z][a-zA-Z0-9]*$",
      "scope": ["variables", "functions", "properties"],
      "examples": [
        {
          "correct": "userName",
          "incorrect": "user_name",
          "explanation": "Use camelCase for better JavaScript/TypeScript readability"
        },
        {
          "correct": "calculateTotalPrice",
          "incorrect": "calculate_total_price",
          "explanation": "Function names should also follow camelCase"
        }
      ],
      "exceptions": [
        {
          "case": "Constants",
          "reason": "Constants use UPPER_SNAKE_CASE by convention",
          "alternative": "MAX_RETRY_COUNT"
        },
        {
          "case": "Database columns",
          "reason": "Database naming conventions may differ",
          "alternative": "user_id (in database), userId (in code)"
        }
      ],
      "enforcement": {
        "automated": true,
        "tools": ["ESLint", "TSLint", "Prettier"],
        "severity": "warning|error|info|critical"
      },
      "rationale": "Consistent naming improves code readability, maintainability, and follows JavaScript/TypeScript community standards",
      "references": [
        "https://google.github.io/styleguide/jsguide.html#naming",
        "https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html"
      ]
    }
  ]
}
```

#### **E. GOVERNANCE SECTION (Management Framework)**
```json
{
  "governance": {
    "workflow": {
      "states": [
        {
          "name": "draft",
          "description": "Term is being created or edited",
          "permissions": ["author", "editor"],
          "transitions": ["review", "approved"]
        },
        {
          "name": "review",
          "description": "Term is under review by domain experts",
          "permissions": ["reviewer", "approver"],
          "transitions": ["draft", "approved", "rejected"]
        },
        {
          "name": "approved",
          "description": "Term is approved and published",
          "permissions": ["approver"],
          "transitions": ["deprecated", "review"]
        }
      ],
      "approvalProcess": {
        "required": true,
        "approvers": ["domain-expert", "glossary-owner"],
        "criteria": [
          "Definition accuracy and clarity",
          "Uniqueness (no duplicates)",
          "Proper categorization",
          "Source attribution"
        ]
      }
    },
    "roles": [
      {
        "name": "glossary-owner",
        "description": "Overall glossary management and governance",
        "responsibilities": [
          "Define glossary strategy and standards",
          "Approve high-level changes",
          "Manage access and permissions"
        ],
        "permissions": ["create", "read", "update", "delete", "approve", "publish"]
      },
      {
        "name": "domain-expert",
        "description": "Subject matter expert for specific domains",
        "responsibilities": [
          "Review and validate domain-specific terms",
          "Provide authoritative definitions",
          "Ensure technical accuracy"
        ],
        "permissions": ["create", "read", "update", "review", "approve"]
      }
    ],
    "qualityControl": {
      "reviewCycle": "quarterly",
      "qualityChecks": [
        "Definition clarity and completeness",
        "Consistency across related terms",
        "Source verification and attribution",
        "Usage frequency analysis"
      ],
      "metrics": [
        "Term approval rate",
        "Review cycle time",
        "User satisfaction scores",
        "Search success rate"
      ],
      "automation": {
        "duplicateDetection": true,
        "consistencyChecks": true,
        "linkValidation": true
      }
    },
    "maintenance": {
      "schedule": "monthly review, quarterly cleanup",
      "tasks": [
        "Review deprecated terms",
        "Update definitions based on usage",
        "Validate external links",
        "Analyze search patterns"
      ],
      "archival": {
        "policy": "Archive obsolete terms after 2 years",
        "retention": "Keep archived terms for historical reference"
      }
    }
  }
}
```

#### **F. INTEGRATIONS SECTION (External Systems)**
```json
{
  "integrations": {
    "systems": [
      {
        "name": "Confluence Wiki",
        "type": "wiki|documentation|cms|api|database|search",
        "url": "https://company.atlassian.net/wiki",
        "syncDirection": "export|import|bidirectional",
        "frequency": "daily",
        "mapping": {
          "term": "page.title",
          "definition": "page.content",
          "categories": "page.labels"
        }
      }
    ],
    "apis": [
      {
        "name": "Glossary API",
        "endpoint": "https://api.company.com/glossary/v1",
        "authentication": "Bearer token",
        "operations": ["search", "create", "update", "delete"]
      }
    ]
  }
}
```

---

## **3. PROCESO DE IMPLEMENTACIÓN**

### **PASO 1: PLANNING & SETUP**
1. **Stakeholder Identification:** Identify glossary owners, domain experts, users
2. **Scope Definition:** Define domains, audience, and coverage boundaries
3. **Standards Selection:** Choose terminology standards and governance framework
4. **Tool Selection:** Select glossary management platform and integration tools

### **PASO 2: CONTENT DEVELOPMENT**
1. **Term Collection:** Gather terms from documentation, code, conversations
2. **Definition Creation:** Write clear, concise, audience-appropriate definitions
3. **Relationship Mapping:** Establish semantic relationships between terms
4. **Categorization:** Organize terms into logical categories and collections

### **PASO 3: QUALITY ASSURANCE**
1. **Review Process:** Implement peer review and expert validation
2. **Consistency Checking:** Ensure consistent terminology usage
3. **Source Verification:** Validate definitions against authoritative sources
4. **User Testing:** Test glossary usability with target audience

### **PASO 4: GOVERNANCE IMPLEMENTATION**
1. **Workflow Setup:** Implement term lifecycle and approval processes
2. **Role Assignment:** Assign owners, stewards, and reviewers
3. **Policy Creation:** Establish maintenance and quality control policies
4. **Training:** Train stakeholders on glossary usage and contribution

### **PASO 5: INTEGRATION & AUTOMATION**
1. **System Integration:** Connect with documentation, wiki, and search systems
2. **API Development:** Create APIs for programmatic access
3. **Automation Setup:** Implement duplicate detection and consistency checking
4. **Analytics:** Set up usage tracking and performance metrics

### **PASO 6: MAINTENANCE & EVOLUTION**
1. **Regular Reviews:** Schedule periodic content reviews and updates
2. **Usage Analysis:** Monitor search patterns and user feedback
3. **Continuous Improvement:** Refine processes based on metrics and feedback
4. **Expansion:** Gradually expand coverage and integrate new domains

---

## **4. CHECKLIST DE COMPLETITUD**

### **📋 CONTENT QUALITY**
- [ ] All critical terms defined with clear, concise definitions
- [ ] Examples provided for complex or ambiguous terms
- [ ] Semantic relationships established between related terms
- [ ] Sources cited for authoritative definitions

### **📋 ORGANIZATION & STRUCTURE**
- [ ] Terms categorized into logical groupings
- [ ] Collections created for specific use cases or audiences
- [ ] Consistent naming conventions applied
- [ ] Cross-references and links properly maintained

### **📋 GOVERNANCE & WORKFLOW**
- [ ] Term lifecycle workflow defined and implemented
- [ ] Roles and responsibilities clearly assigned
- [ ] Approval processes established with clear criteria
- [ ] Quality control measures in place

### **📋 USABILITY & ACCESS**
- [ ] Search functionality optimized for user needs
- [ ] Multiple access methods provided (browse, search, API)
- [ ] User-friendly interface for different audiences
- [ ] Mobile and accessibility considerations addressed

### **📋 INTEGRATION & AUTOMATION**
- [ ] Integration with key systems (wiki, documentation, search)
- [ ] APIs available for programmatic access
- [ ] Automated quality checks implemented
- [ ] Usage analytics and reporting configured

---

## **5. MEJORES PRÁCTICAS 2025**

### **🎯 DEFINITION QUALITY**
- **Clarity:** Use simple, jargon-free language when possible
- **Conciseness:** Keep definitions brief but complete
- **Accuracy:** Ensure technical accuracy and currency
- **Consistency:** Use consistent style and terminology

### **🎯 SEMANTIC RELATIONSHIPS**
- **Hierarchical:** Establish broader/narrower term relationships
- **Associative:** Link related concepts and cross-references
- **Equivalence:** Document synonyms and preferred terms
- **Translation:** Provide multilingual support when needed

### **🎯 GOVERNANCE FRAMEWORK**
- **Ownership:** Clear ownership and stewardship assignments
- **Workflow:** Defined processes for term creation and maintenance
- **Quality Control:** Regular reviews and validation processes
- **Version Control:** Track changes and maintain history

### **🎯 USER EXPERIENCE**
- **Discoverability:** Multiple ways to find relevant terms
- **Context:** Provide usage examples and context
- **Feedback:** Enable user contributions and feedback
- **Integration:** Embed glossary in user workflows

---

## **6. HERRAMIENTAS RECOMENDADAS 2025**

### **📊 GLOSSARY MANAGEMENT**
- **Collibra:** Enterprise data governance and glossary management
- **Alation:** Data catalog with built-in glossary capabilities
- **Apache Atlas:** Open source data governance and metadata management
- **Confluence:** Wiki-based glossary with collaboration features
- **Notion:** Flexible knowledge management with database features

### **📊 TERMINOLOGY STANDARDS**
- **SKOS (Simple Knowledge Organization System):** W3C standard for thesauri
- **Dublin Core:** Metadata element set for resource description
- **ISO 1087:** Terminology work and terminology science vocabulary
- **ISO 704:** Terminology work principles and methods
- **ANSI/NISO Z39.19:** Guidelines for construction of monolingual thesauri

### **📊 INTEGRATION TOOLS**
- **Elasticsearch:** Full-text search and analytics
- **GraphQL:** Flexible API for glossary data access
- **Zapier/Microsoft Power Automate:** Workflow automation
- **Slack/Teams Bots:** Contextual glossary access
- **Browser Extensions:** In-context term definitions

### **📊 QUALITY ASSURANCE**
- **Natural Language Processing:** Automated term extraction and validation
- **Machine Learning:** Duplicate detection and relationship discovery
- **Analytics Platforms:** Usage tracking and performance metrics
- **Feedback Systems:** User rating and comment collection
- **Version Control:** Git-based change tracking for glossary content

---

## **7. EJEMPLO COMPLETO**

```json
{
  "metadata": {
    "name": "E-commerce Platform Glossary",
    "version": "2.1.0",
    "lastUpdated": "2025-01-15T10:30:00Z",
    "domain": "e-commerce",
    "audience": ["developers", "business-users"],
    "standards": ["ISO-1087", "SKOS"]
  },
  "glossary": {
    "terms": [
      {
        "id": "API_ENDPOINT",
        "term": "API Endpoint",
        "definition": "A specific URL where an API can be accessed by a client application",
        "context": {
          "domain": "software-development",
          "usage": "technical"
        },
        "examples": [
          {
            "example": "https://api.example.com/v1/users",
            "context": "REST API",
            "explanation": "Endpoint for user management operations"
          }
        ],
        "synonyms": ["API URL", "Service Endpoint"],
        "relationships": {
          "broaderTerms": ["API"],
          "relatedTerms": ["HTTP Method", "Request", "Response"]
        },
        "lifecycle": {
          "status": "approved",
          "createdAt": "2024-01-15T10:00:00Z"
        },
        "metadata": {
          "owner": "API Team",
          "tags": ["api", "web-services"],
          "priority": "high"
        }
      }
    ],
    "categories": [
      {
        "id": "technical",
        "name": "Technical Terms",
        "description": "Software development and technical concepts"
      }
    ]
  },
  "types": [
    {
      "name": "techStackItem",
      "type": "json-schema",
      "schema": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "category": { "type": "string" },
          "version": { "type": "string" }
        }
      }
    }
  ],
  "conventions": [
    {
      "id": "CAMEL_CASE_VARS",
      "name": "Camel Case Variables",
      "rule": "Variable names should use camelCase",
      "examples": [
        {
          "correct": "userName",
          "incorrect": "user_name"
        }
      ],
      "enforcement": {
        "automated": true,
        "tools": ["ESLint"]
      }
    }
  ],
  "governance": {
    "workflow": {
      "approvalProcess": {
        "required": true,
        "approvers": ["domain-expert", "glossary-owner"]
      }
    }
  }
}
```

---

## **8. REFERENCIAS Y RECURSOS**

### **📚 STANDARDS & FRAMEWORKS**
- **ISO 1087:** Terminology work and terminology science vocabulary
- **ISO 704:** Terminology work principles and methods
- **SKOS:** Simple Knowledge Organization System (W3C)
- **Dublin Core:** Metadata element set for resource description
- **ANSI/NISO Z39.19:** Guidelines for construction of monolingual thesauri

### **📚 TOOLS & PLATFORMS**
- **Collibra Documentation:** https://docs.collibra.com/
- **Apache Atlas:** https://atlas.apache.org/
- **SKOS Specification:** https://www.w3.org/2004/02/skos/
- **Confluence Glossary Templates:** https://www.atlassian.com/software/confluence
- **Elasticsearch Documentation:** https://www.elastic.co/guide/

### **📚 BEST PRACTICES**
- **Business Glossary Management:** Industry best practices and case studies
- **Knowledge Management:** Organizational knowledge capture and sharing
- **Terminology Governance:** Standards and processes for term management
- **User Experience Design:** Making glossaries discoverable and usable
- **Integration Patterns:** Connecting glossaries with existing systems

---

**Última actualización:** 2025-01-15  
**Versión del playbook:** 2.0  
**Compatibilidad:** JSON Schema Draft-07, mejores prácticas 2025
