# Schema Playbook — dataModel (Universal Template Edition)

**Purpose:** Universal template-first methodology for documenting data models that works across any database technology, data storage system, or architectural pattern. This playbook guides you through filling the `dataModel.json` template with placeholders to create comprehensive data models for relational databases, NoSQL systems, data warehouses, or any other data storage paradigm.

**Schema Location:** `schemas/master_blueprint_parts/dataModel.json`  
**Template Version:** 3.0.0 - Universal Template with Placeholders  
**Last Updated:** 2025-01-15  
**Based on:** Universal data modeling patterns, modern database design principles, and data governance best practices

---

## 🎯 Template Philosophy

### **Universal Data Modeling**
This schema is designed as a **template with placeholders** that can be adapted to any:
- **Data Paradigm:** Relational, Document, Graph, Key-Value, Column-Family, Time-Series, Multi-Model
- **Database Technology:** PostgreSQL, MongoDB, Neo4j, Cassandra, Redis, InfluxDB, etc.
- **Use Case:** OLTP, OLAP, Data Lakes, Data Warehouses, Real-time Analytics, IoT Data
- **Scale:** From simple applications to enterprise data platforms

### **Placeholder System**
All values use the format `[PLACEHOLDER_NAME]` to indicate where project-specific information should be filled in:
- `[ENTITY_NAME]` → Your actual entity/table/collection names
- `[DATA_PARADIGM]` → Relational, Document, Graph, etc.
- `[ATTRIBUTE_NAME]` → Your actual field/column/property names
- `[RELATIONSHIP_TYPE]` → Your actual relationship patterns

---

## 📋 Template Structure Guide

### **1. Model Information Section (`modelInfo`)**

**Required Placeholders:**
```json
{
  "modelName": "[MODEL_NAME]",
  "version": "[MODEL_VERSION]",
  "description": "[MODEL_DESCRIPTION]",
  "dataParadigm": "[DATA_PARADIGM]"
}
```

**How to Fill:**
- `[MODEL_NAME]` → Replace with your data model's name (e.g., "E-commerce Data Model", "Customer Analytics Schema", "IoT Sensor Data Model")
- `[MODEL_VERSION]` → Use semantic versioning for model evolution (e.g., "1.0.0", "2.1.0")
- `[MODEL_DESCRIPTION]` → Brief description of what your data model represents
- `[DATA_PARADIGM]` → Primary data paradigm you're using

**Examples for Different Data Paradigms:**

**Relational Database Model:**
```json
{
  "modelName": "E-commerce Platform Data Model",
  "version": "2.0.0",
  "description": "Comprehensive data model for e-commerce platform including customers, products, orders, and analytics",
  "dataParadigm": "Relational",
  "databaseType": "PostgreSQL",
  "domain": "E-commerce",
  "modelingApproach": "Entity-Relationship",
  "compliance": ["GDPR", "PCI-DSS"]
}
```

**Document Database Model:**
```json
{
  "modelName": "Content Management System Data Model",
  "version": "1.5.0",
  "description": "Document-based data model for flexible content management and publishing",
  "dataParadigm": "Document",
  "databaseType": "MongoDB",
  "domain": "Content Management",
  "modelingApproach": "Document-Oriented",
  "compliance": ["GDPR"]
}
```

**Graph Database Model:**
```json
{
  "modelName": "Social Network Data Model",
  "version": "1.0.0",
  "description": "Graph-based data model for social networking platform with users, relationships, and interactions",
  "dataParadigm": "Graph",
  "databaseType": "Neo4j",
  "domain": "Social Media",
  "modelingApproach": "Graph-Based",
  "compliance": ["GDPR", "COPPA"]
}
```

### **2. Entities Section (`entities`)**

**Template Structure:**
```json
[
  {
    "name": "[ENTITY_NAME]",
    "type": "[ENTITY_TYPE]",
    "description": "[ENTITY_DESCRIPTION]",
    "category": "[ENTITY_CATEGORY]",
    "attributes": [
      {
        "name": "[ATTRIBUTE_NAME]",
        "dataType": "[DATA_TYPE]",
        "description": "[ATTRIBUTE_DESCRIPTION]",
        "constraints": {
          "required": "[IS_REQUIRED]",
          "unique": "[IS_UNIQUE]",
          "primaryKey": "[IS_PRIMARY_KEY]"
        }
      }
    ]
  }
]
```

**Examples for Different Database Types:**

**Relational Database Entities:**
```json
[
  {
    "name": "Users",
    "type": "Table",
    "description": "Customer and user account information",
    "category": "Master Data",
    "attributes": [
      {
        "name": "user_id",
        "dataType": "UUID",
        "description": "Unique identifier for user",
        "constraints": {
          "required": true,
          "unique": true,
          "primaryKey": true
        }
      },
      {
        "name": "email",
        "dataType": "String",
        "description": "User email address",
        "constraints": {
          "required": true,
          "unique": true,
          "length": 255,
          "pattern": "^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$"
        },
        "dataClassification": "PII"
      },
      {
        "name": "created_at",
        "dataType": "Timestamp",
        "description": "Account creation timestamp",
        "constraints": {
          "required": true,
          "defaultValue": "CURRENT_TIMESTAMP"
        }
      }
    ],
    "indexes": [
      {
        "name": "idx_users_email",
        "type": "Unique",
        "attributes": ["email"],
        "purpose": "Fast email lookup for authentication"
      }
    ]
  },
  {
    "name": "Products",
    "type": "Table",
    "description": "Product catalog information",
    "category": "Master Data",
    "attributes": [
      {
        "name": "product_id",
        "dataType": "UUID",
        "description": "Unique product identifier",
        "constraints": {
          "required": true,
          "primaryKey": true
        }
      },
      {
        "name": "name",
        "dataType": "String",
        "description": "Product name",
        "constraints": {
          "required": true,
          "length": 200
        }
      },
      {
        "name": "price",
        "dataType": "Decimal",
        "description": "Product price in base currency",
        "constraints": {
          "required": true,
          "minValue": 0,
          "maxValue": 999999.99
        }
      }
    ]
  }
]
```

**Document Database Entities:**
```json
[
  {
    "name": "Articles",
    "type": "Collection",
    "description": "Published articles and blog posts",
    "category": "Content",
    "attributes": [
      {
        "name": "_id",
        "dataType": "ObjectId",
        "description": "MongoDB document identifier",
        "constraints": {
          "required": true,
          "primaryKey": true
        }
      },
      {
        "name": "title",
        "dataType": "String",
        "description": "Article title",
        "constraints": {
          "required": true,
          "length": 200
        }
      },
      {
        "name": "content",
        "dataType": "String",
        "description": "Article content in markdown format",
        "constraints": {
          "required": true
        }
      },
      {
        "name": "tags",
        "dataType": "Array",
        "description": "Article tags for categorization",
        "constraints": {
          "required": false
        }
      },
      {
        "name": "metadata",
        "dataType": "Object",
        "description": "Additional article metadata",
        "attributes": [
          {
            "name": "author",
            "dataType": "String",
            "description": "Article author"
          },
          {
            "name": "publishedAt",
            "dataType": "Date",
            "description": "Publication timestamp"
          }
        ]
      }
    ]
  }
]
```

**Graph Database Entities:**
```json
[
  {
    "name": "Person",
    "type": "Node",
    "description": "Individual users in the social network",
    "category": "Entity",
    "attributes": [
      {
        "name": "id",
        "dataType": "String",
        "description": "Unique person identifier",
        "constraints": {
          "required": true,
          "primaryKey": true
        }
      },
      {
        "name": "name",
        "dataType": "String",
        "description": "Person's display name",
        "constraints": {
          "required": true
        }
      },
      {
        "name": "joinedAt",
        "dataType": "DateTime",
        "description": "When person joined the network",
        "constraints": {
          "required": true
        }
      }
    ]
  },
  {
    "name": "FOLLOWS",
    "type": "Edge",
    "description": "Following relationship between persons",
    "category": "Relationship",
    "attributes": [
      {
        "name": "followedAt",
        "dataType": "DateTime",
        "description": "When the follow relationship was created",
        "constraints": {
          "required": true
        }
      },
      {
        "name": "notificationsEnabled",
        "dataType": "Boolean",
        "description": "Whether notifications are enabled for this follow",
        "constraints": {
          "defaultValue": true
        }
      }
    ]
  }
]
```

### **3. Relationships Section (`relationships`)**

**Template Structure:**
```json
[
  {
    "name": "[RELATIONSHIP_NAME]",
    "type": "[RELATIONSHIP_TYPE]",
    "sourceEntity": "[SOURCE_ENTITY]",
    "targetEntity": "[TARGET_ENTITY]",
    "description": "[RELATIONSHIP_DESCRIPTION]",
    "cardinality": {
      "source": "[SOURCE_CARDINALITY]",
      "target": "[TARGET_CARDINALITY]"
    }
  }
]
```

**Examples for Different Relationship Types:**

**Relational Database Relationships:**
```json
[
  {
    "name": "User-Orders",
    "type": "One-to-Many",
    "sourceEntity": "Users",
    "targetEntity": "Orders",
    "description": "A user can have multiple orders",
    "cardinality": {
      "source": "1",
      "target": "0..*"
    },
    "constraints": [
      "Orders must belong to an existing user",
      "User deletion requires handling of existing orders"
    ],
    "cascadeRules": {
      "onUpdate": "CASCADE",
      "onDelete": "RESTRICT"
    }
  },
  {
    "name": "Order-Products",
    "type": "Many-to-Many",
    "sourceEntity": "Orders",
    "targetEntity": "Products",
    "description": "Orders can contain multiple products, products can be in multiple orders",
    "cardinality": {
      "source": "1..*",
      "target": "1..*"
    },
    "attributes": [
      {
        "name": "quantity",
        "dataType": "Integer",
        "description": "Quantity of product in order"
      },
      {
        "name": "unit_price",
        "dataType": "Decimal",
        "description": "Price of product at time of order"
      }
    ]
  }
]
```

**Document Database Relationships:**
```json
[
  {
    "name": "Article-Comments",
    "type": "One-to-Many",
    "sourceEntity": "Articles",
    "targetEntity": "Comments",
    "description": "Articles can have multiple comments (embedded or referenced)",
    "cardinality": {
      "source": "1",
      "target": "0..*"
    },
    "implementation": "Embedded Array",
    "constraints": [
      "Comments are embedded within article documents",
      "Maximum 1000 comments per article"
    ]
  }
]
```

### **4. Constraints Section (`constraints`)**

**Template Structure:**
```json
{
  "businessRules": [
    {
      "name": "[BUSINESS_RULE_NAME]",
      "description": "[BUSINESS_RULE_DESCRIPTION]",
      "type": "[RULE_TYPE]",
      "scope": ["[AFFECTED_ENTITY]"],
      "implementation": "[RULE_IMPLEMENTATION]"
    }
  ],
  "dataQualityRules": [
    {
      "name": "[QUALITY_RULE_NAME]",
      "description": "[QUALITY_RULE_DESCRIPTION]",
      "dimension": "[QUALITY_DIMENSION]",
      "entities": ["[AFFECTED_ENTITY]"],
      "threshold": "[QUALITY_THRESHOLD]"
    }
  ]
}
```

**Examples:**
```json
{
  "businessRules": [
    {
      "name": "Order Total Calculation",
      "description": "Order total must equal sum of line items plus tax and shipping",
      "type": "Calculation",
      "scope": ["Orders", "OrderItems"],
      "implementation": "Database Trigger",
      "priority": "High"
    },
    {
      "name": "User Age Validation",
      "description": "Users must be at least 13 years old to create an account",
      "type": "Validation",
      "scope": ["Users"],
      "implementation": "Application Logic",
      "priority": "High"
    }
  ],
  "dataQualityRules": [
    {
      "name": "Email Completeness",
      "description": "All active users must have a valid email address",
      "dimension": "Completeness",
      "entities": ["Users"],
      "threshold": "99.5%"
    },
    {
      "name": "Product Price Accuracy",
      "description": "Product prices must be positive and within reasonable ranges",
      "dimension": "Accuracy",
      "entities": ["Products"],
      "threshold": "100%"
    }
  ]
}
```

### **5. Data Governance Section (`dataGovernance`)**

**Template Structure:**
```json
{
  "dataOwnership": [
    {
      "entity": "[OWNED_ENTITY]",
      "owner": "[DATA_OWNER]",
      "steward": "[DATA_STEWARD]",
      "responsibilities": ["[RESPONSIBILITY]"]
    }
  ],
  "privacyControls": [
    {
      "entity": "[PRIVACY_ENTITY]",
      "personalDataType": "[PERSONAL_DATA_TYPE]",
      "legalBasis": "[LEGAL_BASIS]",
      "retentionPeriod": "[RETENTION_PERIOD]"
    }
  ]
}
```

**Examples:**
```json
{
  "dataOwnership": [
    {
      "entity": "Users",
      "owner": "Customer Success Team",
      "steward": "Data Engineering Team",
      "responsibilities": [
        "Ensure data accuracy and completeness",
        "Manage data access permissions",
        "Handle data subject requests"
      ]
    },
    {
      "entity": "Products",
      "owner": "Product Management Team",
      "steward": "Catalog Management Team",
      "responsibilities": [
        "Maintain product information accuracy",
        "Manage product lifecycle data",
        "Ensure pricing data integrity"
      ]
    }
  ],
  "privacyControls": [
    {
      "entity": "Users",
      "personalDataType": "PII",
      "legalBasis": "Consent",
      "retentionPeriod": "7 years after account closure",
      "anonymizationMethod": "Data masking for non-production environments"
    }
  ]
}
```

---

## 🛠️ Implementation Methodology

### **Step 1: Domain Analysis**
1. **Identify Business Domain:** What business area does your data model serve?
2. **Map Business Entities:** What are the key business objects?
3. **Define Relationships:** How do business objects relate to each other?
4. **Identify Constraints:** What business rules must be enforced?

### **Step 2: Technology Selection**
1. **Choose Data Paradigm:** Relational, Document, Graph, Key-Value, etc.
2. **Select Database Technology:** PostgreSQL, MongoDB, Neo4j, etc.
3. **Consider Scale Requirements:** OLTP, OLAP, Real-time, Batch processing
4. **Evaluate Compliance Needs:** GDPR, HIPAA, SOX, etc.

### **Step 3: Fill Template Systematically**
1. **Start with `modelInfo`:** Basic model information and technology choices
2. **Define `entities`:** Core business entities with attributes and constraints
3. **Map `relationships`:** How entities relate to each other
4. **Document `constraints`:** Business rules and data quality requirements
5. **Establish `dataGovernance`:** Ownership, privacy, and compliance controls

### **Step 4: Validate and Iterate**
1. **Review with Business Stakeholders:** Ensure model meets business requirements
2. **Validate Technical Implementation:** Can this be implemented efficiently?
3. **Check Compliance Requirements:** Does model support regulatory needs?
4. **Test Performance Scenarios:** Will model perform under expected load?

---

## 🌍 Universal Examples

### **E-commerce Relational Model**
```json
{
  "modelInfo": {
    "modelName": "E-commerce Platform Data Model",
    "dataParadigm": "Relational",
    "databaseType": "PostgreSQL"
  },
  "entities": [
    {
      "name": "Users",
      "type": "Table",
      "attributes": [
        {
          "name": "user_id",
          "dataType": "UUID",
          "constraints": { "primaryKey": true }
        }
      ]
    }
  ]
}
```

### **IoT Time-Series Model**
```json
{
  "modelInfo": {
    "modelName": "IoT Sensor Data Model",
    "dataParadigm": "Time-Series",
    "databaseType": "InfluxDB"
  },
  "entities": [
    {
      "name": "SensorReadings",
      "type": "Measurement",
      "attributes": [
        {
          "name": "timestamp",
          "dataType": "Timestamp",
          "constraints": { "required": true }
        },
        {
          "name": "sensor_id",
          "dataType": "String",
          "constraints": { "required": true }
        },
        {
          "name": "value",
          "dataType": "Float",
          "constraints": { "required": true }
        }
      ]
    }
  ]
}
```

### **Social Network Graph Model**
```json
{
  "modelInfo": {
    "modelName": "Social Network Data Model",
    "dataParadigm": "Graph",
    "databaseType": "Neo4j"
  },
  "entities": [
    {
      "name": "Person",
      "type": "Node",
      "attributes": [
        {
          "name": "id",
          "dataType": "String",
          "constraints": { "primaryKey": true }
        }
      ]
    },
    {
      "name": "FOLLOWS",
      "type": "Edge",
      "attributes": [
        {
          "name": "followedAt",
          "dataType": "DateTime"
        }
      ]
    }
  ]
}
```

---

## ✅ Validation Checklist

### **Template Completeness**
- [ ] All required placeholders filled with actual values
- [ ] No `[PLACEHOLDER]` format strings remain in final version
- [ ] Data paradigm matches actual database technology
- [ ] All entities have complete attribute definitions

### **Data Model Quality**
- [ ] Entities represent clear business concepts
- [ ] Relationships are properly defined with correct cardinality
- [ ] Business rules are captured as constraints
- [ ] Data types are appropriate for the database technology

### **Governance and Compliance**
- [ ] Data ownership is clearly defined
- [ ] Privacy controls are in place for personal data
- [ ] Compliance requirements are addressed
- [ ] Data quality rules are defined and measurable

### **Performance and Scalability**
- [ ] Indexes are defined for expected query patterns
- [ ] Partitioning strategy is appropriate for data volume
- [ ] Performance targets are realistic and measurable
- [ ] Scalability requirements are addressed

---

## 🔄 Maintenance and Evolution

### **Model Evolution**
- Update `modelInfo.version` when making schema changes
- Document all changes with rationale and impact analysis
- Maintain backward compatibility when possible
- Plan migration strategies for breaking changes

### **Data Governance Updates**
- Regularly review data ownership assignments
- Update privacy controls as regulations change
- Monitor data quality metrics and adjust thresholds
- Review and update business rules as requirements evolve

### **Performance Optimization**
- Monitor query performance and adjust indexes
- Review partitioning strategies as data grows
- Update performance targets based on actual usage
- Consider denormalization or caching for hot data paths

---

**Remember:** This template is designed to be **universal and adaptable**. The key is to replace all placeholders with values specific to your data model while maintaining the structure that makes the documentation useful for development, governance, and maintenance.