# Schema Playbook — dataModelDictionary

**Propósito:** Crear diccionarios de datos comprehensivos siguiendo mejores prácticas de data governance 2025, con metadata management, data lineage, privacy compliance y semantic layer definitions.

**Ubicación:** `schemas/master_blueprint_parts/dataModelDictionary.json`

---

## **METODOLOGÍA 2025: DATA GOVERNANCE & METADATA MANAGEMENT**

### **1. INVESTIGACIÓN PREVIA REQUERIDA**
Antes de crear el diccionario, investigar:
- **Standards Compliance:** ISO-11179, DAMA-DMBOK, W3C-DCAT, FAIR principles
- **Privacy Frameworks:** GDPR, CCPA, data classification standards
- **Data Quality Dimensions:** Completeness, accuracy, consistency, timeliness, validity, uniqueness
- **Metadata Management:** Active metadata, data lineage, automated discovery
- **Semantic Layer:** Business glossary, terminology management, concept mapping

### **2. ESTRUCTURA MODERNA DEL SCHEMA**

#### **A. METADATA SECTION (Requerido)**
```json
{
  "metadata": {
    "name": "Customer Data Dictionary",
    "version": "2.1.0",
    "lastUpdated": "2025-01-15T10:30:00Z",
    "description": "Comprehensive data dictionary purpose",
    "domain": "e-commerce|healthcare|finance|logistics",
    "organization": {
      "name": "CompanyName",
      "dataOwner": "Jane Smith",
      "steward": "John Doe"
    },
    "standards": ["ISO-11179", "GDPR", "DAMA-DMBOK"]
  }
}
```

#### **B. ENTITIES SECTION (Core)**
```json
{
  "entities": [
    {
      "name": "Customer", // PascalCase
      "type": "entity|aggregate|value-object|event|view|dimension|fact",
      "description": "Technical description",
      "businessDefinition": "Business-friendly definition",
      "domain": "customer-management",
      "lifecycle": {
        "status": "active|deprecated|planned|retired",
        "createdAt": "2024-01-01T00:00:00Z"
      },
      "attributes": [
        {
          "name": "customerId", // camelCase
          "dataType": {
            "primitive": "string|integer|decimal|boolean|date|datetime|uuid|json|binary",
            "format": "email|url|phone|currency|percentage",
            "maxLength": 255,
            "pattern": "regex_pattern"
          },
          "description": "Technical description",
          "businessDefinition": "Business-friendly definition",
          "constraints": {
            "required": true,
            "unique": true,
            "primaryKey": true,
            "foreignKey": {
              "entity": "Order",
              "attribute": "customerId",
              "onDelete": "cascade|restrict|set-null",
              "onUpdate": "cascade|restrict|set-null"
            }
          },
          "dataQuality": {
            "completeness": {"required": true, "threshold": 100},
            "accuracy": {"validationRules": ["email_format"]},
            "consistency": {"crossFieldRules": ["email_unique_per_customer"]}
          },
          "privacy": {
            "classification": "public|internal|confidential|restricted|pii|phi",
            "retention": {"period": "7 years", "policy": "customer-data-retention"},
            "consent": {
              "required": true,
              "purpose": "account management",
              "lawfulBasis": "consent|contract|legal-obligation"
            }
          },
          "lineage": {
            "source": {"system": "CRM", "table": "customers", "column": "email"},
            "transformations": [
              {"step": 1, "operation": "normalize", "tool": "ETL Pipeline"}
            ]
          },
          "semantics": {
            "businessTerms": ["Customer Email", "Contact Email"],
            "synonyms": ["Email Address", "Electronic Mail"],
            "businessRules": ["Must be unique per customer"]
          }
        }
      ],
      "relationships": [
        {
          "name": "orders",
          "type": "one-to-one|one-to-many|many-to-one|many-to-many",
          "targetEntity": "Order",
          "description": "Technical relationship description",
          "businessDescription": "Business relationship description",
          "keys": {
            "sourceKey": "customerId",
            "targetKey": "customerId"
          },
          "constraints": {
            "onDelete": "cascade|restrict|set-null",
            "onUpdate": "cascade|restrict|set-null"
          }
        }
      ],
      "indexes": [
        {
          "name": "idx_customer_email",
          "type": "primary|unique|index|composite",
          "columns": ["email"],
          "description": "Performance optimization for email lookups"
        }
      ],
      "storage": {
        "tableName": "customers",
        "schema": "public",
        "database": "ecommerce",
        "encryption": {
          "enabled": true,
          "algorithm": "AES-256",
          "keyManagement": "AWS KMS"
        }
      }
    }
  ]
}
```

#### **C. DATA GOVERNANCE SECTION (Requerido)**
```json
{
  "dataGovernance": {
    "policies": [
      {
        "name": "PII Protection Policy",
        "type": "privacy|retention|access|quality|security",
        "description": "Policy description",
        "scope": ["Customer", "Order"],
        "rules": ["PII must be encrypted", "Access requires permission"],
        "enforcement": "manual|automated|hybrid"
      }
    ],
    "classifications": [
      {
        "level": "pii",
        "description": "Personally Identifiable Information",
        "criteria": ["Contains personal data"],
        "handling": ["Encrypt", "Audit access"]
      }
    ]
  }
}
```

#### **D. BUSINESS GLOSSARY SECTION**
```json
{
  "glossary": [
    {
      "term": "Customer",
      "definition": "Clear, concise business definition",
      "context": "e-commerce domain",
      "synonyms": ["User", "Buyer", "Client"],
      "relatedTerms": ["Account", "Profile"],
      "examples": ["Registered user who made purchase"],
      "owner": "Product Team"
    }
  ]
}
```

#### **E. DATA LINEAGE SECTION**
```json
{
  "dataLineage": {
    "flows": [
      {
        "name": "Customer Data Flow",
        "source": {"system": "CRM", "entity": "Customer"},
        "target": {"system": "Analytics", "entity": "CustomerDim"},
        "transformations": [
          {"step": 1, "operation": "cleanse", "tool": "dbt"}
        ]
      }
    ]
  }
}
```

#### **F. DATA QUALITY SECTION**
```json
{
  "dataQuality": {
    "dimensions": [
      {
        "name": "completeness|accuracy|consistency|timeliness|validity|uniqueness",
        "description": "Quality dimension description",
        "metrics": ["null_percentage", "duplicate_count"],
        "thresholds": {"warning": 95, "critical": 90}
      }
    ],
    "rules": [
      {
        "name": "Email Format Validation",
        "entity": "Customer",
        "attribute": "email",
        "rule": "REGEXP_LIKE(email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$')",
        "severity": "error",
        "automated": true
      }
    ]
  }
}
```

---

## **3. PROCESO DE IMPLEMENTACIÓN**

### **PASO 1: PREPARACIÓN**
1. **Definir Scope:** Determinar entidades, dominios y stakeholders
2. **Establecer Governance:** Definir roles (Data Owner, Steward, Custodian)
3. **Seleccionar Standards:** Elegir frameworks de compliance aplicables
4. **Configurar Tools:** Preparar herramientas de metadata management

### **PASO 2: DISCOVERY & CATALOGING**
1. **Automated Discovery:** Usar herramientas para descubrir datos existentes
2. **Business Interviews:** Recopilar definiciones de negocio
3. **Technical Analysis:** Analizar esquemas, tipos de datos, relaciones
4. **Quality Assessment:** Evaluar calidad actual de los datos

### **PASO 3: MODELING & DOCUMENTATION**
1. **Entity Modeling:** Definir entidades con tipos DDD (entity, aggregate, value-object)
2. **Attribute Definition:** Documentar cada atributo con metadata completo
3. **Relationship Mapping:** Definir relaciones con cardinalidades precisas
4. **Business Glossary:** Crear términos de negocio con definiciones claras

### **PASO 4: GOVERNANCE & COMPLIANCE**
1. **Privacy Classification:** Clasificar datos según sensibilidad (PII, PHI, etc.)
2. **Retention Policies:** Definir políticas de retención por tipo de dato
3. **Access Controls:** Establecer permisos y roles de acceso
4. **Compliance Mapping:** Mapear a frameworks regulatorios

### **PASO 5: QUALITY & LINEAGE**
1. **Quality Rules:** Definir reglas de calidad automatizadas
2. **Lineage Tracking:** Documentar flujos de datos end-to-end
3. **Impact Analysis:** Establecer análisis de impacto upstream/downstream
4. **Monitoring Setup:** Configurar monitoreo continuo de calidad

### **PASO 6: VALIDATION & MAINTENANCE**
1. **Schema Validation:** Validar JSON schema con herramientas
2. **Business Review:** Revisar con stakeholders de negocio
3. **Technical Review:** Validar con equipos técnicos
4. **Maintenance Plan:** Establecer proceso de actualización continua

---

## **4. CHECKLIST DE COMPLETITUD**

### **📋 METADATA & GOVERNANCE**
- [ ] Metadata section completo con versioning
- [ ] Data governance policies definidas
- [ ] Compliance standards identificados
- [ ] Roles y responsabilidades asignados

### **📋 ENTITIES & ATTRIBUTES**
- [ ] Todas las entidades documentadas con tipos DDD
- [ ] Atributos con data types precisos y constraints
- [ ] Business definitions para todos los elementos
- [ ] Privacy classification completa

### **📋 RELATIONSHIPS & CONSTRAINTS**
- [ ] Relaciones con cardinalidades correctas
- [ ] Foreign keys y constraints definidos
- [ ] Referential integrity rules establecidas
- [ ] Indexes de performance documentados

### **📋 QUALITY & LINEAGE**
- [ ] Data quality rules automatizadas
- [ ] Data lineage flows documentados
- [ ] Impact analysis configurado
- [ ] Monitoring y alerting establecido

### **📋 BUSINESS CONTEXT**
- [ ] Business glossary completo
- [ ] Semantic relationships definidas
- [ ] Usage examples incluidos
- [ ] Stakeholder ownership asignado

---

## **5. MEJORES PRÁCTICAS 2025**

### **🎯 NAMING CONVENTIONS**
- **Entities:** PascalCase (Customer, OrderItem)
- **Attributes:** camelCase (customerId, firstName)
- **Relationships:** descriptive names (customerOrders, orderItems)
- **Constraints:** descriptive prefixes (pk_customer_id, fk_order_customer)

### **🎯 DATA CLASSIFICATION**
- **Public:** No restrictions, can be shared openly
- **Internal:** Company internal use only
- **Confidential:** Restricted access, business sensitive
- **Restricted:** Highly restricted, legal/regulatory
- **PII:** Personal data requiring consent/protection
- **PHI:** Health information with special protections

### **🎯 QUALITY DIMENSIONS**
- **Completeness:** Percentage of non-null values
- **Accuracy:** Correctness against reference data
- **Consistency:** Uniformity across systems
- **Timeliness:** Data freshness and update frequency
- **Validity:** Conformance to format/domain rules
- **Uniqueness:** Absence of duplicates

### **🎯 LINEAGE TRACKING**
- **Source Systems:** Original data sources
- **Transformations:** ETL/ELT processing steps
- **Target Systems:** Destination systems/applications
- **Dependencies:** Upstream/downstream relationships
- **Impact Analysis:** Change impact assessment

---

## **6. HERRAMIENTAS RECOMENDADAS 2025**

### **📊 METADATA MANAGEMENT**
- **Apache Atlas:** Open source data governance
- **DataHub:** LinkedIn's metadata platform
- **Amundsen:** Lyft's data discovery platform
- **AWS Glue Data Catalog:** Cloud-native catalog
- **Collibra:** Enterprise data governance platform

### **📊 DATA QUALITY**
- **Great Expectations:** Python data validation
- **dbt:** Data transformation with testing
- **Apache Griffin:** Data quality solution
- **Soda:** Data reliability platform
- **Monte Carlo:** Data observability platform

### **📊 LINEAGE & DISCOVERY**
- **Apache Airflow:** Workflow orchestration with lineage
- **dbt:** Built-in lineage tracking
- **DataHub:** Automated lineage discovery
- **Spline:** Data lineage tracking for Spark
- **OpenLineage:** Open standard for lineage

---

## **7. EJEMPLO COMPLETO**

```json
{
  "metadata": {
    "name": "E-commerce Data Dictionary",
    "version": "2.1.0",
    "lastUpdated": "2025-01-15T10:30:00Z",
    "domain": "e-commerce",
    "standards": ["ISO-11179", "GDPR", "DAMA-DMBOK"]
  },
  "entities": [
    {
      "name": "Customer",
      "type": "entity",
      "businessDefinition": "A person or organization that purchases products",
      "attributes": [
        {
          "name": "customerId",
          "dataType": {"primitive": "uuid"},
          "constraints": {"required": true, "primaryKey": true},
          "privacy": {"classification": "internal"},
          "dataQuality": {"completeness": {"threshold": 100}}
        },
        {
          "name": "email",
          "dataType": {"primitive": "string", "format": "email"},
          "constraints": {"required": true, "unique": true},
          "privacy": {
            "classification": "pii",
            "consent": {"required": true, "lawfulBasis": "consent"}
          },
          "dataQuality": {
            "accuracy": {"validationRules": ["email_format"]}
          }
        }
      ],
      "relationships": [
        {
          "name": "orders",
          "type": "one-to-many",
          "targetEntity": "Order",
          "businessDescription": "All orders placed by this customer"
        }
      ]
    }
  ],
  "dataGovernance": {
    "policies": [
      {
        "name": "PII Protection",
        "type": "privacy",
        "enforcement": "automated"
      }
    ]
  },
  "glossary": [
    {
      "term": "Customer",
      "definition": "A person or organization that purchases products",
      "context": "e-commerce"
    }
  ]
}
```

---

## **8. REFERENCIAS Y RECURSOS**

### **📚 STANDARDS & FRAMEWORKS**
- **ISO/IEC 11179:** Metadata registries standard
- **DAMA-DMBOK:** Data Management Body of Knowledge
- **W3C DCAT:** Data Catalog Vocabulary
- **FAIR Principles:** Findable, Accessible, Interoperable, Reusable
- **GDPR:** General Data Protection Regulation
- **CCPA:** California Consumer Privacy Act

### **📚 TOOLS & PLATFORMS**
- **DataHub Documentation:** https://datahubproject.io/
- **Apache Atlas:** https://atlas.apache.org/
- **Great Expectations:** https://greatexpectations.io/
- **dbt Documentation:** https://docs.getdbt.com/
- **OpenLineage:** https://openlineage.io/

### **📚 BEST PRACTICES**
- **Data Mesh Principles:** Domain-oriented data ownership
- **DataOps:** Agile data management practices
- **Data as a Product:** Treating data with product mindset
- **Semantic Layer:** Business-friendly data abstraction
- **Active Metadata:** Real-time, actionable metadata

---

**Última actualización:** 2025-01-15  
**Versión del playbook:** 2.0  
**Compatibilidad:** JSON Schema Draft-07, mejores prácticas 2025
