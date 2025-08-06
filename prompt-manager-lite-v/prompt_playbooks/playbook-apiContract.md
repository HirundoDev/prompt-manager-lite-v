# Playbook: API Contract Discovery (V2 - Deep Static Trace)

**Objective:** To populate the `apiContract` section with a high-fidelity, machine-readable definition of the API by performing a deep static trace of backend routing and controller logic.

**Core Principle:** You will act as a static analysis engine. For each endpoint, you must trace the code execution path from request to response to derive the contract with precision.

---

## Phase 1: Route Enumeration

Your goal is to identify every registered API endpoint in the application.

1.  **Identify Router Files**: Locate the primary API routing files. Use `grep` to search for framework-specific routing patterns:
    -   **Express.js:** `app.get(`, `app.post(`, `router.get(`, `app.use('/api', ...)`
    -   **FastAPI/Flask:** `@app.get(`, `@app.post(`, `@router.get(`
    -   **Laravel:** `Route::get(`, `Route::post(`

2.  **Extract Basic Route Info**: For each route definition found, extract:
    -   **`path`**: The URL path string (e.g., `/users/{id}`).
    -   **`method`**: The HTTP method (`get`, `post`, etc.).
    -   **Handler Reference**: The name or reference to the controller/function that handles the request.

---

## Phase 2: Deep Handler Analysis

For each handler reference from Phase 1, you will perform a deep static trace.

1.  **Parameter Extraction**:
    -   **Path Parameters**: Analyze the route's `path` string for bracketed segments (e.g., `{id}`). For each, create a parameter object with `"in": "path"` and infer its type from its usage in the handler (e.g., if passed to a database function expecting a number, the type is `integer`).
    -   **Query Parameters**: Search the handler's code for access to the request's query object (e.g., `req.query.sortBy`). For each key accessed, create a parameter object with `"in": "query"`.
    -   **Header/Cookie Parameters**: Search for access to headers or cookies (e.g., `req.headers['x-api-key']`). For each, create a parameter object with the corresponding `"in"` value.

2.  **Request Body Schema Inference**:
    -   **Action**: If the handler accesses the request body (e.g., `req.body`), you MUST trace its usage to build a schema.
    -   **Protocol**: Initialize an empty JSON schema object. For every property accessed on the body object (e.g., `const { username, password } = req.body;`), add a corresponding entry to the schema's `properties` field. Infer the `type` from how the variable is used later in the function.

3.  **Response Schema Tracing**:
    -   **Action**: You MUST identify every possible exit point of the handler function to map all potential responses.
    -   **Protocol**:
        1.  Scan the function for all response-sending statements (`res.json(...)`, `res.send(...)`, `res.status(...).json(...)`, `return ...`).
        2.  For each statement, create a separate response definition.
        3.  **Determine Status Code**: If a status is explicitly set (`res.status(404)`), use that. Otherwise, default to `200` for successful data returns, `201` for creations (often after a `POST`), and `204` for successful requests with no body.
        4.  **Analyze Response Body**: Analyze the data structure passed to the response function. Convert this data structure into a JSON schema to define the response `bodySchema`.

---

## Phase 3: Final Assembly

1.  **Create `operationId`**: For each endpoint, create a unique `operationId` by combining the method and a descriptive name (e.g., `get_user_by_id`).
2.  **Assemble the Contract**: Structure all the extracted information—path, method, operationId, parameters, request body, and all possible responses—into a single, valid object conforming to the `apiContract` schema.
3.  **Add to Blueprint**: Add the completed object to the `apiContract.paths` object in the Master Blueprint.