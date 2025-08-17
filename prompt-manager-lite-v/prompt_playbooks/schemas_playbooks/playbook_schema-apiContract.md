# Schema Playbook: API Contract Template (Universal Edition)

**Purpose:** Comprehensive guide for using the universal `apiContract.json` template to create API contract specifications that work across any technology stack, API type, or framework. This playbook provides methodology, best practices, and examples for filling placeholders to create adaptable API contracts.

**Schema Location:** `real_structure_documentation/schemas/master_blueprint_parts/apiContract.json`  
**Template Version:** 3.0.0 - Universal Template with Placeholders  
**Last Updated:** 2025-01-15  
**Based on:** OpenAPI 3.1 specification and modern API design patterns for 2025

---

## 📋 Table of Contents
- [🎯 Template Philosophy](#-template-philosophy)
- [🔧 Placeholder System Guide](#-placeholder-system-guide)
- [📊 Template Structure Walkthrough](#-template-structure-walkthrough)
- [💡 API Type Specific Examples](#-api-type-specific-examples)
- [🌍 Technology Stack Examples](#-technology-stack-examples)
- [⚠️ Common Pitfalls to Avoid](#️-common-pitfalls-to-avoid)
- [✅ Quality Checklist](#-quality-checklist)

---

## 🎯 Template Philosophy

### **Universal Template Approach**
The `apiContract.json` schema is designed as a **template with placeholders** that can be adapted to any:

- **API Types:** REST, GraphQL, gRPC, WebSocket, Event-Driven, Custom protocols
- **Technology Stacks:** Any programming language, framework, or platform
- **Industries:** From fintech to healthcare, e-commerce to IoT
- **Scales:** Personal projects to enterprise-grade systems
- **Methodologies:** Agile, Waterfall, DevOps, API-first development

### **Template-First Benefits**
- **Consistency:** Standardized structure across all API contracts
- **Adaptability:** Works with any technology or methodology
- **Maintainability:** Easy to update and version
- **Collaboration:** Clear structure for team communication
- **Automation:** Can be used with code generation tools

### **Placeholder Philosophy**
All values use the format `[PLACEHOLDER_NAME]` to indicate where project-specific information should be filled:
- **Descriptive:** `[API_NAME]` clearly indicates what should go there
- **Contextual:** `[ENDPOINT_PATH]` shows the purpose within the API structure
- **Flexible:** Can accommodate any technology or naming convention

---

## 🔧 Placeholder System Guide

### **Core Placeholder Categories**

#### **1. Identity Placeholders**
- `[API_NAME]` → Your API's name
- `[API_VERSION]` → Semantic version (e.g., "1.0.0")
- `[API_DESCRIPTION]` → Brief API purpose description
- `[API_TYPE]` → REST, GraphQL, gRPC, WebSocket, etc.

#### **2. Infrastructure Placeholders**
- `[BASE_URL]` → API base URL
- `[PROTOCOL]` → HTTP, HTTPS, WebSocket, gRPC
- `[DOMAIN]` → Your domain name
- `[API_PATH]` → Base path for API endpoints

#### **3. Endpoint Placeholders**
- `[ENDPOINT_ID]` → Unique endpoint identifier
- `[ENDPOINT_PATH]` → Endpoint URL path
- `[HTTP_METHOD]` → GET, POST, PUT, DELETE, etc.
- `[ENDPOINT_SUMMARY]` → Brief endpoint description

#### **4. Data Placeholders**
- `[MODEL_NAME]` → Data model/entity name
- `[PROPERTY_NAME]` → Object property name
- `[PROPERTY_TYPE]` → Data type (string, integer, etc.)
- `[PARAMETER_NAME]` → Request parameter name

#### **5. Security Placeholders**
- `[SECURITY_SCHEME_NAME]` → Authentication scheme name
- `[SECURITY_TYPE]` → apiKey, oauth2, http, etc.
- `[AUTH_METHOD_NAME]` → Specific auth method identifier
- `[API_KEY_NAME]` → API key parameter name

### **Placeholder Replacement Strategy**

#### **Step 1: Gather Information**
Before filling placeholders, collect:
- API purpose and scope
- Technology stack details
- Authentication requirements
- Data models and structures
- Endpoint specifications

#### **Step 2: Systematic Replacement**
1. Start with identity placeholders (name, version, type)
2. Fill infrastructure details (URLs, protocols)
3. Define data models and schemas
4. Specify endpoints and operations
5. Configure authentication and security
6. Add documentation and examples

#### **Step 3: Validation**
- Ensure all placeholders are replaced
- Verify consistency across sections
- Validate against your API type requirements
- Test with API documentation tools

---

## 📊 Template Structure Walkthrough

### **1. Contract Information (`contractInfo`)**

**Purpose:** Basic API metadata and identification

**Required Placeholders:**
```json
{
  "apiName": "[API_NAME]",
  "version": "[API_VERSION]",
  "description": "[API_DESCRIPTION]",
  "apiType": "[API_TYPE]"
}
```

**Filling Guide:**
- **`[API_NAME]`:** Use clear, descriptive names
  - ✅ Good: "User Management API", "Payment Gateway", "Analytics Service"
  - ❌ Avoid: "API", "Service", "System"

- **`[API_VERSION]`:** Follow semantic versioning
  - ✅ Good: "1.0.0", "2.1.3", "3.0.0-beta"
  - ❌ Avoid: "v1", "latest", "current"

- **`[API_TYPE]`:** Be specific about API paradigm
  - REST, GraphQL, gRPC, WebSocket, Event-Driven, Hybrid

### **2. API Specification (`apiSpecification`)**

**Purpose:** Technical specification details

**Key Placeholders:**
```json
{
  "specificationFormat": "[SPEC_FORMAT]",
  "contentType": ["[CONTENT_TYPE]"],
  "protocols": ["[PROTOCOL]"]
}
```

**Common Values by API Type:**
- **REST:** OpenAPI 3.1, application/json, HTTPS
- **GraphQL:** GraphQL Schema, application/json, HTTPS
- **gRPC:** Protocol Buffers, application/grpc, HTTP/2
- **WebSocket:** Custom Schema, application/json, WSS

### **3. Endpoints Definition (`endpoints`)**

**Purpose:** API operations and their specifications

**Structure per Endpoint:**
```json
{
  "endpointId": "[ENDPOINT_ID]",
  "path": "[ENDPOINT_PATH]",
  "method": "[HTTP_METHOD]",
  "summary": "[ENDPOINT_SUMMARY]"
}
```

**Best Practices:**
- Use consistent naming for `[ENDPOINT_ID]`
- Follow RESTful conventions for `[ENDPOINT_PATH]`
- Choose appropriate `[HTTP_METHOD]` for operations
- Write clear, concise `[ENDPOINT_SUMMARY]`

### **4. Data Models (`dataModels`)**

**Purpose:** Define data structures and schemas

**Model Structure:**
```json
{
  "modelName": "[MODEL_NAME]",
  "type": "[MODEL_TYPE]",
  "properties": [
    {
      "propertyName": "[PROPERTY_NAME]",
      "type": "[PROPERTY_TYPE]"
    }
  ]
}
```

**Naming Conventions:**
- Use PascalCase for `[MODEL_NAME]`: User, OrderItem, PaymentRequest
- Use camelCase for `[PROPERTY_NAME]`: firstName, createdAt, isActive
- Be specific with `[PROPERTY_TYPE]`: string, integer, boolean, array, object

### **5. Authentication (`authentication`)**

**Purpose:** Security schemes and requirements

**Security Scheme Structure:**
```json
{
  "schemeName": "[SECURITY_SCHEME_NAME]",
  "type": "[SECURITY_TYPE]",
  "description": "[SECURITY_DESCRIPTION]"
}
```

**Common Security Types:**
- **API Key:** `apiKey` with `[API_KEY_LOCATION]` and `[API_KEY_NAME]`
- **Bearer Token:** `http` with `bearer` scheme and `[BEARER_FORMAT]`
- **OAuth2:** `oauth2` with flows and scopes
- **Basic Auth:** `http` with `basic` scheme

---

## 💡 API Type Specific Examples

### **REST API Example**

```json
{
  "contractInfo": {
    "apiName": "E-commerce Product API",
    "version": "2.1.0",
    "description": "RESTful API for managing product catalog and inventory",
    "apiType": "REST",
    "baseUrl": "https://api.example.com/v2"
  },
  "apiSpecification": {
    "specificationFormat": "OpenAPI 3.1",
    "contentType": ["application/json"],
    "protocols": ["HTTPS"]
  }
}
```

### **GraphQL API Example**

```json
{
  "contractInfo": {
    "apiName": "Social Media GraphQL API",
    "version": "1.0.0",
    "description": "GraphQL API for social media platform interactions",
    "apiType": "GraphQL",
    "baseUrl": "https://graphql.example.com/v1"
  },
  "apiSpecification": {
    "specificationFormat": "GraphQL Schema",
    "contentType": ["application/json"],
    "protocols": ["HTTPS"]
  }
}
```

### **gRPC API Example**

```json
{
  "contractInfo": {
    "apiName": "Microservice Communication API",
    "version": "3.0.0",
    "description": "gRPC API for inter-service communication",
    "apiType": "gRPC",
    "baseUrl": "grpc://services.example.com:443"
  },
  "apiSpecification": {
    "specificationFormat": "Protocol Buffers",
    "contentType": ["application/grpc"],
    "protocols": ["HTTP/2"]
  }
}
```

### **WebSocket API Example**

```json
{
  "contractInfo": {
    "apiName": "Real-time Chat API",
    "version": "1.2.0",
    "description": "WebSocket API for real-time messaging",
    "apiType": "WebSocket",
    "baseUrl": "wss://chat.example.com/v1"
  },
  "apiSpecification": {
    "specificationFormat": "Custom WebSocket Schema",
    "contentType": ["application/json"],
    "protocols": ["WSS"]
  }
}
```

---

## 🌍 Technology Stack Examples

### **Node.js + Express + MongoDB**

```json
{
  "contractInfo": {
    "apiName": "Task Management API",
    "apiType": "REST"
  },
  "endpoints": [
    {
      "path": "/tasks",
      "method": "GET",
      "summary": "Retrieve user tasks"
    }
  ],
  "authentication": {
    "securitySchemes": [
      {
        "schemeName": "JWTAuth",
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    ]
  }
}
```

### **Python + FastAPI + PostgreSQL**

```json
{
  "contractInfo": {
    "apiName": "Analytics Data API",
    "apiType": "REST"
  },
  "dataModels": [
    {
      "modelName": "AnalyticsReport",
      "type": "object",
      "properties": [
        {
          "propertyName": "reportId",
          "type": "string",
          "format": "uuid"
        },
        {
          "propertyName": "metrics",
          "type": "array"
        }
      ]
    }
  ]
}
```

### **Java + Spring Boot + MySQL**

```json
{
  "contractInfo": {
    "apiName": "Enterprise User API",
    "apiType": "REST"
  },
  "authentication": {
    "securitySchemes": [
      {
        "schemeName": "OAuth2",
        "type": "oauth2",
        "flows": {
          "authorizationCode": {
            "authorizationUrl": "https://auth.example.com/oauth/authorize",
            "tokenUrl": "https://auth.example.com/oauth/token"
          }
        }
      }
    ]
  }
}
```

---

## ⚠️ Common Pitfalls to Avoid

### **1. Placeholder Mistakes**
- ❌ **Don't leave placeholders unfilled:** `[API_NAME]` should become "User API"
- ❌ **Don't use generic names:** "API" instead of "User Management API"
- ❌ **Don't mix placeholder formats:** Use `[NAME]` not `{NAME}` or `<NAME>`

### **2. Inconsistent Naming**
- ❌ **Mixed case conventions:** "user_id" and "userId" in same API
- ❌ **Inconsistent endpoint patterns:** "/users" and "/user-profile"
- ❌ **Unclear model names:** "Data" instead of "UserProfile"

### **3. Missing Information**
- ❌ **Incomplete security schemes:** Missing required fields for auth type
- ❌ **Vague descriptions:** "Gets data" instead of "Retrieves user profile information"
- ❌ **Missing error responses:** Only documenting success cases

### **4. Technology-Specific Assumptions**
- ❌ **Hardcoding frameworks:** Assuming Express.js when template should be universal
- ❌ **Database-specific types:** Using MongoDB ObjectId when should be generic
- ❌ **Platform assumptions:** Assuming cloud deployment when could be on-premise

---

## ✅ Quality Checklist

### **Template Completion**
- [ ] All `[PLACEHOLDER]` values replaced with actual values
- [ ] API name and description are clear and specific
- [ ] Version follows semantic versioning (x.y.z)
- [ ] API type accurately reflects the implementation

### **Endpoint Documentation**
- [ ] All endpoints have unique IDs
- [ ] Paths follow consistent naming conventions
- [ ] HTTP methods match operation semantics
- [ ] Request/response schemas are defined
- [ ] Error responses are documented

### **Data Model Quality**
- [ ] Model names use consistent case convention
- [ ] Property types are specific and accurate
- [ ] Required fields are clearly marked
- [ ] Validation rules are specified where needed
- [ ] Examples are provided for complex models

### **Security Configuration**
- [ ] Authentication schemes are fully specified
- [ ] Security requirements match endpoint needs
- [ ] OAuth2 flows include all required URLs
- [ ] API key locations and names are specified
- [ ] Scopes and permissions are documented

### **Documentation Standards**
- [ ] Descriptions are clear and concise
- [ ] Examples are realistic and helpful
- [ ] External documentation links are valid
- [ ] Contact information is current
- [ ] License information is accurate

### **Universal Compatibility**
- [ ] No technology-specific assumptions
- [ ] Works with multiple API types
- [ ] Adaptable to different scales
- [ ] Framework-agnostic structure
- [ ] Industry-neutral terminology

---

## 🚀 Next Steps

After completing your API contract template:

1. **Validate Structure:** Use JSON Schema validators to check syntax
2. **Generate Documentation:** Use tools like Swagger UI or Redoc
3. **Code Generation:** Generate client SDKs and server stubs
4. **Team Review:** Have stakeholders review the contract
5. **Version Control:** Track changes and maintain version history
6. **Integration:** Connect with CI/CD pipelines and testing frameworks

---

**Remember:** This template is designed to be universal. Focus on filling placeholders with your specific information while maintaining the flexible structure that allows the contract to work across different technologies and use cases.