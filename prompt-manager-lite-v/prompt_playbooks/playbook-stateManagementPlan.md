# Playbook: State Management Plan Analysis (V2 - Library-Specific Parsing)

**Objective:** To document the application's global state architecture with high precision by performing a library-specific static analysis of the store's definition.

**Core Principle:** You will act as a specialized parser. You must first identify the state management library being used and then apply the specific protocol for that library. This is not a generic search.

---

## Phase 1: Library Identification

1.  **Action:** Read the `dependencies` and `devDependencies` from the project's `package.json` file.
2.  **Identify Technology**: Based on the packages found, determine the `stateTechnology`.
    -   If `@reduxjs/toolkit` is present, the technology is **Redux Toolkit**.
    -   If `zustand` is present, the technology is **Zustand**.
    -   If `pinia` is present, the technology is **Pinia**.
    -   If `vuex` is present, the technology is **Vuex**.
3.  **Proceed to the corresponding protocol in Phase 2.**

---

## Phase 2: Deep Store Analysis (Library-Specific)

### 2.A Protocol for Redux Toolkit

1.  **Locate Slices**: Search the codebase for files that import `createSlice` from `@reduxjs/toolkit`.
2.  **For each slice file found**:
    -   Parse the `createSlice` call.
    -   The `name` property is the `sliceName`.
    -   The `initialState` object is the source for the `initialStateSchema`. Convert it to a JSON Schema.
    -   The `reducers` object contains the actions. For each key in this object:
        -   The key is the `actionName`.
        -   Analyze the function's arguments (specifically `action.payload`) to define the `payloadSchema`.

### 2.B Protocol for Zustand

1.  **Locate Stores**: Search the codebase for files that import `create` from `zustand`.
2.  **For each store file found**:
    -   The variable the `create` call is assigned to is the `storeName`.
    -   Parse the function passed to `create`. The returned object is the state.
    -   Separate state properties (e.g., `count: 0`) from action properties (e.g., `increment: () => ...`).
    -   The state properties form the `initialStateSchema`.
    -   For each action property, the key is the `actionName`. Analyze its function signature to define the `payloadSchema`.

### 2.C Protocol for Pinia / Vuex

1.  **Locate Stores**: Search the codebase for files that import `defineStore` from `pinia` or `createStore` from `vuex`.
2.  **For each store file found**:
    -   The first argument to `defineStore` is the `storeId` or `sliceName`.
    -   Parse the setup object passed to `defineStore`.
    -   The `state` function's return object is the source for the `initialStateSchema`.
    -   The `actions` object contains the actions. For each key in this object:
        -   The key is the `actionName`.
        -   Analyze the function's signature to define the `payloadSchema`.

---

## Phase 3: Final Assembly

1.  **Consolidate Findings**: Gather all the slices/stores you have analyzed.
2.  **Construct Plan**: Create the final `stateManagementPlan` array, with each object in the array representing a distinct store or slice you documented.
3.  **Validate**: Ensure the final output conforms to the Master Blueprint schema.