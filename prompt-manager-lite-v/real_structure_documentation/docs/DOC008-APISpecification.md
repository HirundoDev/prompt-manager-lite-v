# API Specification Documentation

> **Purpose:** Comprehensive API specification documentation following 2025 best practices. This document serves as the single source of truth for API contracts, providing clear, interactive, and developer-friendly documentation that enhances developer experience and accelerates API adoption.

**Document Type:** API Specification Documentation  
**Version:** 3.0  
**Last Updated:** 2025-01-15  
**Template Status:** Production Ready - Enhanced with 2025 Best Practices

---

## Document Control

| Field | Value |
|-------|-------|
| **API Name** | [API_NAME] |
| **API Version** | [API_VERSION] |
| **Base URL** | [BASE_URL] |
| **OpenAPI Version** | 3.1.0 |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] |
| **Maintainer** | [MAINTAINER_NAME] |

---

## 📋 Table of Contents

- [🎯 API Overview](#-api-overview)
- [🚀 Getting Started](#-getting-started)
- [🔐 Authentication & Security](#-authentication--security)
- [📊 API Standards & Conventions](#-api-standards--conventions)
- [⚡ Rate Limiting & Quotas](#-rate-limiting--quotas)
- [🔄 Versioning Strategy](#-versioning-strategy)
- [📝 Request & Response Format](#-request--response-format)
- [❌ Error Handling](#-error-handling)
- [🔗 API Endpoints](#-api-endpoints)
- [📡 WebSocket & Real-time APIs](#-websocket--real-time-apis)
- [🧪 Testing & Sandbox](#-testing--sandbox)
- [📈 Monitoring & Analytics](#-monitoring--analytics)
- [🔧 SDKs & Code Examples](#-sdks--code-examples)

---

## 🎯 API Overview

### Executive Summary
The [PROJECT_NAME] API is a modern, RESTful API designed following 2025 best practices. Built with developer experience in mind, it provides comprehensive functionality for [MAIN_PURPOSE] with robust security, excellent performance, and intuitive design patterns.

### API Philosophy
- **Developer-First:** Intuitive design that reduces integration time
- **OpenAPI 3.1 Standard:** Complete specification with interactive documentation
- **Security by Design:** OAuth 2.0, JWT, and comprehensive security measures
- **Performance Optimized:** Sub-100ms response times with intelligent caching
- **AI-Ready:** Publicly accessible documentation for AI code generation tools

### Key Features
- **RESTful Design:** Consistent, predictable API patterns
- **Real-time Support:** WebSocket connections for live data
- **Comprehensive SDKs:** Auto-generated SDKs for major languages
- **Interactive Testing:** Built-in API explorer and sandbox environment
- **Robust Error Handling:** Detailed error responses with actionable guidance

### API Metrics & SLA
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| **Response Time (P95)** | < 100ms | [CURRENT] | [STATUS] |
| **Uptime** | 99.9% | [CURRENT] | [STATUS] |
| **Rate Limit** | 1000 req/min | [CURRENT] | [STATUS] |
| **Error Rate** | < 0.1% | [CURRENT] | [STATUS] |

---

## 🚀 Getting Started

### Quick Start Guide

#### 1. Get Your API Key
```bash
# Register and get your API key
curl -X POST https://api.example.com/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "developer@example.com",
    "name": "Developer Name"
  }'
```

#### 2. Make Your First Request
```bash
# Test your API key
curl -X GET https://api.example.com/v1/users/me \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

#### 3. Expected Response
```json
{
  "id": "user_123",
  "name": "Developer Name",
  "email": "developer@example.com",
  "created_at": "2025-01-15T10:30:00Z",
  "plan": "developer"
}
```

### Base URLs
| Environment | Base URL | Purpose |
|-------------|----------|---------|
| **Production** | `https://api.example.com/v1` | Live production API |
| **Staging** | `https://staging-api.example.com/v1` | Pre-production testing |
| **Sandbox** | `https://sandbox-api.example.com/v1` | Development and testing |

### Supported Content Types
- **Request:** `application/json`, `multipart/form-data`
- **Response:** `application/json`, `application/xml` (on request)
- **Encoding:** UTF-8

---

## 🔐 Authentication & Security

### Authentication Methods

#### OAuth 2.0 (Recommended)
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**OAuth 2.0 Flow:**
1. **Authorization Request:** Redirect user to authorization server
2. **Authorization Grant:** User grants permission
3. **Access Token Request:** Exchange authorization code for access token
4. **API Access:** Use access token for API requests

```javascript
// OAuth 2.0 Authorization URL
const authUrl = `https://api.example.com/oauth/authorize?` +
  `client_id=${CLIENT_ID}&` +
  `redirect_uri=${REDIRECT_URI}&` +
  `response_type=code&` +
  `scope=read write&` +
  `state=${STATE}`;

// Exchange code for token
const tokenResponse = await fetch('https://api.example.com/oauth/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    grant_type: 'authorization_code',
    client_id: CLIENT_ID,
    client_secret: CLIENT_SECRET,
    code: AUTHORIZATION_CODE,
    redirect_uri: REDIRECT_URI
  })
});
```

#### API Key Authentication
```http
Authorization: Bearer api_key_abc123xyz789
```

#### JWT Token Authentication
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Security Features
- **TLS 1.3:** All communications encrypted
- **CORS:** Configurable cross-origin resource sharing
- **Rate Limiting:** Prevents abuse and ensures fair usage
- **Request Signing:** Optional HMAC-SHA256 request signing
- **IP Whitelisting:** Restrict access to specific IP addresses

### Scopes & Permissions
| Scope | Description | Endpoints |
|-------|-------------|-----------|
| **read** | Read access to resources | GET endpoints |
| **write** | Create and update resources | POST, PUT, PATCH endpoints |
| **delete** | Delete resources | DELETE endpoints |
| **admin** | Administrative access | All endpoints + admin functions |

---

## 📊 API Standards & Conventions

### RESTful Design Principles
- **Resource-Based URLs:** `/users/{id}`, `/orders/{id}/items`
- **HTTP Methods:** GET (read), POST (create), PUT (update), DELETE (remove)
- **Stateless:** Each request contains all necessary information
- **Cacheable:** Responses include appropriate cache headers

### URL Structure
```
https://api.example.com/v1/{resource}/{id}/{sub-resource}
```

### URL Structure Examples
- `GET /[API_VERSION]/[RESOURCE_PLURAL]` - List [RESOURCE_NAME] resources
- `GET /[API_VERSION]/[RESOURCE_PLURAL]/[RESOURCE_ID]` - Get specific [RESOURCE_NAME]
- `POST /[API_VERSION]/[RESOURCE_PLURAL]` - Create new [RESOURCE_NAME]
- `PUT /[API_VERSION]/[RESOURCE_PLURAL]/[RESOURCE_ID]` - Update [RESOURCE_NAME]
- `DELETE /[API_VERSION]/[RESOURCE_PLURAL]/[RESOURCE_ID]` - Delete [RESOURCE_NAME]
- `GET /[API_VERSION]/[RESOURCE_PLURAL]/[RESOURCE_ID]/[SUB_RESOURCE]` - Get [RESOURCE_NAME]'s [SUB_RESOURCE]

### HTTP Status Codes
| Code | Meaning | Usage |
|------|---------|-------|
| **200** | OK | Successful GET, PUT, PATCH |
| **201** | Created | Successful POST |
| **204** | No Content | Successful DELETE |
| **400** | Bad Request | Invalid request format |
| **401** | Unauthorized | Authentication required |
| **403** | Forbidden | Insufficient permissions |
| **404** | Not Found | Resource doesn't exist |
| **429** | Too Many Requests | Rate limit exceeded |
| **500** | Internal Server Error | Server error |

### Naming Conventions
- **Resources:** Plural nouns (`[RESOURCE_PLURAL]`, `[SUB_RESOURCE_PLURAL]`)
- **Fields:** [FIELD_NAMING_CONVENTION] (`[FIELD_EXAMPLE_1]`, `[FIELD_EXAMPLE_2]`)
- **Query Parameters:** [QUERY_PARAM_CONVENTION] (`[QUERY_PARAM_1]`, `[QUERY_PARAM_2]`)
- **Headers:** [HEADER_CONVENTION] (`[HEADER_EXAMPLE_1]`, `[HEADER_EXAMPLE_2]`)

---

## ⚡ Rate Limiting & Quotas

### Rate Limits ([YEAR] Standards)
| Plan | Requests/Minute | Requests/Hour | Requests/Day |
|------|-----------------|---------------|--------------|
| **[PLAN_TIER_1]** | [LIMIT_1_MIN] | [LIMIT_1_HOUR] | [LIMIT_1_DAY] |
| **[PLAN_TIER_2]** | [LIMIT_2_MIN] | [LIMIT_2_HOUR] | [LIMIT_2_DAY] |
| **[PLAN_TIER_3]** | [LIMIT_3_MIN] | [LIMIT_3_HOUR] | [LIMIT_3_DAY] |
| **[PLAN_TIER_4]** | [LIMIT_4_MIN] | [LIMIT_4_HOUR] | [LIMIT_4_DAY] |

### Rate Limit Headers
```http
[RATE_LIMIT_HEADER_1]: [LIMIT_VALUE]
[RATE_LIMIT_HEADER_2]: [REMAINING_VALUE]
[RATE_LIMIT_HEADER_3]: [RESET_TIMESTAMP]
[RATE_LIMIT_HEADER_4]: [WINDOW_SECONDS]
```

### Rate Limit Response
```json
{
  "error": {
    "code": "[ERROR_CODE]",
    "message": "[ERROR_MESSAGE]",
    "details": {
      "limit": [LIMIT_VALUE],
      "remaining": [REMAINING_VALUE],
      "reset_at": "[RESET_TIMESTAMP]",
      "retry_after": [RETRY_SECONDS]
    }
  }
}
```

### Best Practices for Rate Limiting
- **Exponential Backoff:** Implement exponential backoff for retries
- **Batch Requests:** Use batch endpoints when available
- **Caching:** Cache responses to reduce API calls
- **Webhooks:** Use webhooks instead of polling for real-time updates

---

## 🔄 Versioning Strategy

### API Versioning Approach
- **URL Versioning:** `/[VERSION_1]/`, `/[VERSION_2]/` in the URL path
- **Semantic Versioning:** [VERSIONING_SCHEME] ([VERSION_FORMAT])
- **Backward Compatibility:** Maintain compatibility within [COMPATIBILITY_SCOPE] versions
- **Deprecation Policy:** [DEPRECATION_PERIOD] notice for breaking changes

### Version Lifecycle
| Version | Status | Support Until | Notes |
|---------|--------|---------------|-------|
| **[VERSION_OLD]** | [STATUS_OLD] | [SUPPORT_DATE_OLD] | [NOTES_OLD] |
| **[VERSION_CURRENT]** | [STATUS_CURRENT] | [SUPPORT_DATE_CURRENT] | [NOTES_CURRENT] |
| **[VERSION_FUTURE]** | [STATUS_FUTURE] | [SUPPORT_DATE_FUTURE] | [NOTES_FUTURE] |

### Migration Guide
```javascript
// [VERSION_OLD] ([STATUS_OLD])
GET /[VERSION_OLD]/[ENDPOINT_OLD]

// [VERSION_CURRENT] ([STATUS_CURRENT])
GET /[VERSION_CURRENT]/[ENDPOINT_CURRENT]

// [VERSION_FUTURE] ([STATUS_FUTURE])
GET /[VERSION_FUTURE]/[ENDPOINT_FUTURE]
```

---

## 📝 Request & Response Format

### Request Format
```json
{
  "data": {
    "type": "[RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": "[VALUE_2]"
    }
  },
  "meta": {
    "request_id": "[REQUEST_ID]"
  }
}
```

### Response Format
```json
{
  "data": {
    "id": "[RESOURCE_ID]",
    "type": "[RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": "[VALUE_2]",
      "[CREATED_FIELD]": "[TIMESTAMP_FORMAT]",
      "[UPDATED_FIELD]": "[TIMESTAMP_FORMAT]"
    }
  },
  "meta": {
    "request_id": "[REQUEST_ID]",
    "response_time": "[RESPONSE_TIME]",
    "version": "[API_VERSION]"
  }
}
```

### Pagination
```json
{
  "data": [...],
  "pagination": {
    "page": [CURRENT_PAGE],
    "per_page": [ITEMS_PER_PAGE],
    "total": [TOTAL_ITEMS],
    "total_pages": [TOTAL_PAGES],
    "has_next": [HAS_NEXT_BOOLEAN],
    "has_prev": [HAS_PREV_BOOLEAN]
  },
  "links": {
    "self": "/[API_VERSION]/[RESOURCE_PLURAL]?page=[CURRENT_PAGE]",
    "next": "/[API_VERSION]/[RESOURCE_PLURAL]?page=[NEXT_PAGE]",
    "prev": [PREV_LINK_OR_NULL],
    "first": "/[API_VERSION]/[RESOURCE_PLURAL]?page=1",
    "last": "/[API_VERSION]/[RESOURCE_PLURAL]?page=[LAST_PAGE]"
  }
}
```

### Filtering & Sorting
```bash
# Filtering
GET /[API_VERSION]/[RESOURCE_PLURAL]?filter[[FILTER_FIELD_1]]=[FILTER_VALUE_1]&filter[[FILTER_FIELD_2]]=[FILTER_VALUE_2]

# Sorting
GET /[API_VERSION]/[RESOURCE_PLURAL]?sort=[SORT_DIRECTION][SORT_FIELD_1],[SORT_FIELD_2]

# Combined
GET /[API_VERSION]/[RESOURCE_PLURAL]?filter[[FILTER_FIELD]]=[FILTER_VALUE]&sort=[SORT_PARAMS]&page=[PAGE_NUM]&per_page=[PAGE_SIZE]
```

---

## ❌ Error Handling

### Error Response Format
```json
{
  "error": {
    "code": "[ERROR_CODE]",
    "message": "[ERROR_MESSAGE]",
    "details": {
      "field": "[FIELD_NAME]",
      "issue": "[ISSUE_DESCRIPTION]",
      "provided": "[PROVIDED_VALUE]",
      "expected": "[EXPECTED_FORMAT]"
    },
    "documentation_url": "[DOCS_URL]/errors/[ERROR_TYPE]",
    "request_id": "[REQUEST_ID]",
    "timestamp": "[TIMESTAMP_FORMAT]"
  }
}
```

### Common Error Codes
| Code | HTTP Status | Description | Action |
|------|-------------|-------------|--------|
| **[ERROR_CODE_1]** | [HTTP_STATUS_1] | [ERROR_DESCRIPTION_1] | [ACTION_1] |
| **[ERROR_CODE_2]** | [HTTP_STATUS_2] | [ERROR_DESCRIPTION_2] | [ACTION_2] |
| **[ERROR_CODE_3]** | [HTTP_STATUS_3] | [ERROR_DESCRIPTION_3] | [ACTION_3] |
| **[ERROR_CODE_4]** | [HTTP_STATUS_4] | [ERROR_DESCRIPTION_4] | [ACTION_4] |
| **[ERROR_CODE_5]** | [HTTP_STATUS_5] | [ERROR_DESCRIPTION_5] | [ACTION_5] |
| **[ERROR_CODE_6]** | [HTTP_STATUS_6] | [ERROR_DESCRIPTION_6] | [ACTION_6] |
| **[ERROR_CODE_7]** | [HTTP_STATUS_7] | [ERROR_DESCRIPTION_7] | [ACTION_7] |

### Validation Errors
```json
{
  "error": {
    "code": "[VALIDATION_ERROR_CODE]",
    "message": "[VALIDATION_ERROR_MESSAGE]",
    "details": {
      "errors": [
        {
          "field": "[FIELD_NAME_1]",
          "code": "[FIELD_ERROR_CODE_1]",
          "message": "[FIELD_ERROR_MESSAGE_1]"
        },
        {
          "field": "[FIELD_NAME_2]",
          "code": "[FIELD_ERROR_CODE_2]",
          "message": "[FIELD_ERROR_MESSAGE_2]"
        }
      ]
    }
  }
}
```

---

## 🔗 API Endpoints

### [RESOURCE_NAME] API

#### Get Current [RESOURCE_NAME]
```http
GET /[API_VERSION]/[RESOURCE_PLURAL]/[CURRENT_ENDPOINT]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
```

**Response:**
```json
{
  "data": {
    "id": "[RESOURCE_ID]",
    "type": "[RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": "[VALUE_2]",
      "[ATTRIBUTE_3]": "[URL_VALUE]",
      "[ATTRIBUTE_4]": "[PLAN_VALUE]",
      "[CREATED_FIELD]": "[TIMESTAMP_FORMAT]",
      "[LAST_ACTION_FIELD]": "[TIMESTAMP_FORMAT]"
    }
  }
}
```

#### List [RESOURCE_PLURAL]
```http
GET /[API_VERSION]/[RESOURCE_PLURAL]?page=[PAGE_NUM]&per_page=[PAGE_SIZE]&sort=[SORT_PARAMS]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
```

**Query Parameters:**
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------||
| `page` | integer | Page number | [DEFAULT_PAGE] |
| `per_page` | integer | Items per page (max [MAX_ITEMS]) | [DEFAULT_PAGE_SIZE] |
| `sort` | string | Sort field ([SORT_ASC_PREFIX]asc, [SORT_DESC_PREFIX]desc) | [DEFAULT_SORT] |
| `filter[[FILTER_FIELD_1]]` | string | Filter by [FILTER_FIELD_1] | [DEFAULT_FILTER_1] |
| `filter[[FILTER_FIELD_2]]` | string | Filter by [FILTER_FIELD_2] | [DEFAULT_FILTER_2] |

#### Create [RESOURCE_NAME]
```http
POST /[API_VERSION]/[RESOURCE_PLURAL]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
Content-Type: [CONTENT_TYPE]
```

**Request Body:**
```json
{
  "data": {
    "type": "[RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": "[VALUE_2]",
      "[ATTRIBUTE_3]": "[VALUE_3]",
      "[ATTRIBUTE_4]": "[VALUE_4]"
    }
  }
}
```

**Response ([HTTP_STATUS_CREATED]):**
```json
{
  "data": {
    "id": "[RESOURCE_ID]",
    "type": "[RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": "[VALUE_2]",
      "[ATTRIBUTE_3]": "[VALUE_3]",
      "[CREATED_FIELD]": "[TIMESTAMP_FORMAT]",
      "[VERIFICATION_FIELD]": [BOOLEAN_VALUE]
    }
  }
}
```

#### Update [RESOURCE_NAME]
```http
PUT /[API_VERSION]/[RESOURCE_PLURAL]/{[RESOURCE_ID_PARAM]}
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
Content-Type: [CONTENT_TYPE]
```

**Request Body:**
```json
{
  "data": {
    "type": "[RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[UPDATED_VALUE_1]",
      "[ATTRIBUTE_2]": "[UPDATED_VALUE_2]"
    }
  }
}
```

#### Delete [RESOURCE_NAME]
```http
DELETE /[API_VERSION]/[RESOURCE_PLURAL]/{[RESOURCE_ID_PARAM]}
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
```

**Response ([HTTP_STATUS_NO_CONTENT])**

### [SECONDARY_RESOURCE_NAME] API

#### List [SECONDARY_RESOURCE_PLURAL]
```http
GET /[API_VERSION]/[SECONDARY_RESOURCE_PLURAL]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
```

#### Create [SECONDARY_RESOURCE_NAME]
```http
POST /[API_VERSION]/[SECONDARY_RESOURCE_PLURAL]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
Content-Type: [CONTENT_TYPE]
```

**Request Body:**
```json
{
  "data": {
    "type": "[SECONDARY_RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": "[VALUE_2]",
      "[ATTRIBUTE_3]": "[VALUE_3]",
      "[ATTRIBUTE_4]": ["[TAG_1]", "[TAG_2]", "[TAG_3]"]
    }
  }
}
```

### [TERTIARY_RESOURCE_NAME] API

#### Upload [TERTIARY_RESOURCE_NAME]
```http
POST /[API_VERSION]/[TERTIARY_RESOURCE_PLURAL]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
Content-Type: [UPLOAD_CONTENT_TYPE]
```

**Form Data:**
- `[UPLOAD_FIELD]`: The [UPLOAD_ITEM] to upload
- `[OPTIONAL_FIELD_1]`: (optional) [OPTIONAL_DESCRIPTION_1]
- `[OPTIONAL_FIELD_2]`: (optional) [OPTIONAL_DESCRIPTION_2]

**Response:**
```json
{
  "data": {
    "id": "[RESOURCE_ID]",
    "type": "[TERTIARY_RESOURCE_TYPE]",
    "attributes": {
      "[ATTRIBUTE_1]": "[VALUE_1]",
      "[ATTRIBUTE_2]": [SIZE_VALUE],
      "[ATTRIBUTE_3]": "[MIME_TYPE]",
      "[ATTRIBUTE_4]": "[URL_VALUE]",
      "[CREATED_FIELD]": "[TIMESTAMP_FORMAT]"
    }
  }
}
```

---

## 📡 WebSocket & Real-time APIs

### WebSocket Connection
```javascript
const ws = new WebSocket('[WEBSOCKET_URL]/[API_VERSION]/[WS_ENDPOINT]');

ws.onopen = function(event) {
  // Send authentication
  ws.send(JSON.stringify({
    type: '[AUTH_MESSAGE_TYPE]',
    token: '[AUTH_TOKEN_PLACEHOLDER]'
  }));
};

ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  console.log('[LOG_MESSAGE]:', data);
};
```

### Real-time Events
```json
{
  "type": "[EVENT_TYPE]",
  "data": {
    "id": "[RESOURCE_ID]",
    "changes": {
      "[CHANGED_FIELD]": "[NEW_VALUE]"
    }
  },
  "timestamp": "[TIMESTAMP_FORMAT]"
}
```

### Server-Sent Events (SSE)
```javascript
const eventSource = new EventSource('[BASE_URL]/[API_VERSION]/[EVENTS_ENDPOINT]');

eventSource.onmessage = function(event) {
  const data = JSON.parse(event.data);
  console.log('[EVENT_LOG_MESSAGE]:', data);
};
```

---

## 🧪 Testing & Sandbox

### Sandbox Environment
- **Base URL:** `[SANDBOX_BASE_URL]/[API_VERSION]`
- **Test Data:** Pre-populated with [TEST_DATA_TYPE]
- **Reset:** Data resets every [RESET_INTERVAL]
- **Rate Limits:** [RATE_LIMIT_POLICY] for testing

### Interactive API Explorer
Access the interactive API explorer at: `[DOCS_BASE_URL]/[API_EXPLORER_PATH]`

Features:
- **Try It Out:** Test endpoints directly from documentation
- **Code Generation:** Auto-generate code snippets
- **Response Validation:** Validate responses against schema
- **Authentication Testing:** Test with different auth methods

### Postman Collection
```bash
# Import Postman collection
curl -o [COLLECTION_FILENAME].json [DOCS_BASE_URL]/[POSTMAN_PATH]/[COLLECTION_FILENAME].json
```

### Test Data
```json
{
  "[TEST_RESOURCE_PLURAL]": [
    {
      "id": "[TEST_RESOURCE_ID]",
      "[ATTRIBUTE_1]": "[TEST_VALUE_1]",
      "[ATTRIBUTE_2]": "[TEST_VALUE_2]"
    }
  ],
  "[TEST_API_KEYS_FIELD]": [
    "[TEST_API_KEY]"
  ]
}
```

---

## 📈 Monitoring & Analytics

### API Health Status
Check API status at: `[STATUS_PAGE_URL]`

### Health Check Endpoint
```http
GET /[API_VERSION]/[HEALTH_ENDPOINT]
```

**Response:**
```json
{
  "status": "[HEALTH_STATUS]",
  "version": "[API_VERSION_NUMBER]",
  "timestamp": "[TIMESTAMP_FORMAT]",
  "services": {
    "[SERVICE_1]": "[SERVICE_1_STATUS]",
    "[SERVICE_2]": "[SERVICE_2_STATUS]",
    "[SERVICE_3]": "[SERVICE_3_STATUS]"
  },
  "response_time": "[RESPONSE_TIME]"
}
```

### Usage Analytics
```http
GET /[API_VERSION]/[ANALYTICS_ENDPOINT]/[USAGE_ENDPOINT]
Authorization: [AUTH_TYPE] {[AUTH_TOKEN]}
```

**Response:**
```json
{
  "data": {
    "[METRIC_1]": [METRIC_1_VALUE],
    "[METRIC_2]": [METRIC_2_VALUE],
    "[TOP_ENDPOINTS_FIELD]": [
      {
        "endpoint": "/[API_VERSION]/[ENDPOINT_PATH]",
        "requests": [REQUEST_COUNT],
        "avg_response_time": "[AVG_RESPONSE_TIME]"
      }
    ]
  }
}
```

---

## 🔧 SDKs & Code Examples

### Official SDKs
| Language | Package | Documentation |
|----------|---------|---------------|
| **[LANGUAGE_1]** | `[PACKAGE_1]` | [[LANGUAGE_1] Docs]([DOCS_BASE_URL]/[LANGUAGE_1_PATH]) |
| **[LANGUAGE_2]** | `[PACKAGE_2]` | [[LANGUAGE_2] Docs]([DOCS_BASE_URL]/[LANGUAGE_2_PATH]) |
| **[LANGUAGE_3]** | `[PACKAGE_3]` | [[LANGUAGE_3] Docs]([DOCS_BASE_URL]/[LANGUAGE_3_PATH]) |
| **[LANGUAGE_4]** | `[PACKAGE_4]` | [[LANGUAGE_4] Docs]([DOCS_BASE_URL]/[LANGUAGE_4_PATH]) |
| **[LANGUAGE_5]** | `[PACKAGE_5]` | [[LANGUAGE_5] Docs]([DOCS_BASE_URL]/[LANGUAGE_5_PATH]) |

### [LANGUAGE_1] SDK Example
```[LANGUAGE_1_CODE]
import { [SDK_CLASS] } from '[PACKAGE_1]';

const client = new [SDK_CLASS]({
  [API_KEY_PARAM]: '[API_KEY_PLACEHOLDER]',
  [BASE_URL_PARAM]: '[BASE_URL]/[API_VERSION]'
});

// Get current [RESOURCE_NAME]
const [RESOURCE_VARIABLE] = await client.[RESOURCE_PLURAL].[METHOD_1]();
console.log([RESOURCE_VARIABLE]);

// Create a new [SECONDARY_RESOURCE_NAME]
const [SECONDARY_RESOURCE_VARIABLE] = await client.[SECONDARY_RESOURCE_PLURAL].[METHOD_2]({
  [ATTRIBUTE_1]: '[VALUE_1]',
  [ATTRIBUTE_2]: '[VALUE_2]'
});
```

### [LANGUAGE_2] SDK Example
```[LANGUAGE_2_CODE]
from [PACKAGE_2] import [SDK_CLASS]

client = [SDK_CLASS]([API_KEY_PARAM]='[API_KEY_PLACEHOLDER]')

# Get current [RESOURCE_NAME]
[RESOURCE_VARIABLE] = client.[RESOURCE_PLURAL].[METHOD_1]()
print([RESOURCE_VARIABLE])

# List [SECONDARY_RESOURCE_PLURAL]
[SECONDARY_RESOURCE_PLURAL] = client.[SECONDARY_RESOURCE_PLURAL].[METHOD_3]([PAGINATION_PARAM_1]=[PAGE_VALUE], [PAGINATION_PARAM_2]=[PER_PAGE_VALUE])
for [SECONDARY_RESOURCE_VARIABLE] in [SECONDARY_RESOURCE_PLURAL]:
    print([SECONDARY_RESOURCE_VARIABLE].[ATTRIBUTE_1])
```

### cURL Examples
```bash
# Get [RESOURCE_NAME]
curl -X GET "[BASE_URL]/[API_VERSION]/[RESOURCE_PLURAL]/[ENDPOINT_SUFFIX]" \
  -H "Authorization: [AUTH_TYPE] [API_KEY_PLACEHOLDER]" \
  -H "Content-Type: [CONTENT_TYPE]"

# Create [SECONDARY_RESOURCE_NAME]
curl -X POST "[BASE_URL]/[API_VERSION]/[SECONDARY_RESOURCE_PLURAL]" \
  -H "Authorization: [AUTH_TYPE] [API_KEY_PLACEHOLDER]" \
  -H "Content-Type: [CONTENT_TYPE]" \
  -d '{
    "data": {
      "type": "[SECONDARY_RESOURCE_TYPE]",
      "attributes": {
        "[ATTRIBUTE_1]": "[VALUE_1]",
        "[ATTRIBUTE_2]": "[VALUE_2]"
      }
    }
  }'
```

---

## OpenAPI 3.1 Specification

### Complete OpenAPI Schema
```yaml
openapi: 3.1.0
info:
  title: [API_TITLE]
  version: [API_VERSION_NUMBER]
  description: [API_DESCRIPTION]
  contact:
    name: [CONTACT_NAME]
    url: [CONTACT_URL]
    email: [CONTACT_EMAIL]
  license:
    name: [LICENSE_NAME]
    url: [LICENSE_URL]

servers:
  - url: [BASE_URL]/[API_VERSION]
    description: [PRODUCTION_SERVER_DESCRIPTION]
  - url: [STAGING_BASE_URL]/[API_VERSION]
    description: [STAGING_SERVER_DESCRIPTION]

security:
  - [SECURITY_SCHEME_NAME]: []

components:
  securitySchemes:
    [SECURITY_SCHEME_NAME]:
      type: [SECURITY_TYPE]
      scheme: [SECURITY_SCHEME]
      bearerFormat: [BEARER_FORMAT]

  schemas:
    [SCHEMA_NAME]:
      type: object
      properties:
        [PROPERTY_1]:
          type: [PROPERTY_1_TYPE]
          example: "[PROPERTY_1_EXAMPLE]"
        [PROPERTY_2]:
          type: [PROPERTY_2_TYPE]
          example: "[PROPERTY_2_EXAMPLE]"
        [PROPERTY_3]:
          type: [PROPERTY_3_TYPE]
          format: [PROPERTY_3_FORMAT]
          example: "[PROPERTY_3_EXAMPLE]"
        [PROPERTY_4]:
          type: [PROPERTY_4_TYPE]
          format: [PROPERTY_4_FORMAT]
          example: "[PROPERTY_4_EXAMPLE]"
      required:
        - [REQUIRED_PROPERTY_1]
        - [REQUIRED_PROPERTY_2]
        - [REQUIRED_PROPERTY_3]

paths:
  /[RESOURCE_PLURAL]/[ENDPOINT_SUFFIX]:
    get:
      summary: [ENDPOINT_SUMMARY]
      operationId: [OPERATION_ID]
      tags:
        - [TAG_NAME]
      responses:
        '[SUCCESS_STATUS_CODE]':
          description: [RESPONSE_DESCRIPTION]
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/[SCHEMA_NAME]'
```

---

## Support & Resources

### Getting Help
- **Documentation:** [[DOCS_BASE_URL]]([DOCS_BASE_URL])
- **API Status:** [[STATUS_PAGE_URL]]([STATUS_PAGE_URL])
- **Support Email:** [SUPPORT_EMAIL]
- **Community Forum:** [[COMMUNITY_URL]]([COMMUNITY_URL])
- **GitHub Issues:** [[GITHUB_ISSUES_URL]]([GITHUB_ISSUES_URL])

### Changelog
- **[VERSION_1]** ([DATE_1]): [CHANGELOG_ENTRY_1]
- **[VERSION_2]** ([DATE_2]): [CHANGELOG_ENTRY_2]
- **[VERSION_3]** ([DATE_3]): [CHANGELOG_ENTRY_3]

### Migration Guides
- [[MIGRATION_GUIDE_1]]([DOCS_BASE_URL]/[MIGRATION_PATH_1])
- [[MIGRATION_GUIDE_2]]([DOCS_BASE_URL]/[MIGRATION_PATH_2])

---

**Document Information:**
- **Template Version:** 3.0 - Enhanced with 2025 Best Practices
- **Last Updated:** 2025-01-15
- **Compatibility:** OpenAPI 3.1, modern API standards, AI-ready documentation
- **Standards:** RESTful design, OAuth 2.0, comprehensive error handling
- **Review Cycle:** Monthly or with API version updates
- **Research Sources:** API documentation best practices 2025, OpenAPI standards, developer experience guidelines