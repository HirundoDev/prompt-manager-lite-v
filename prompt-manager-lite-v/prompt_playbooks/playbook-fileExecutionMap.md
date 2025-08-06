# Playbook: File Execution Map Indexing (V2 - Content-Driven Analysis)

**Objective:** To create a comprehensive and accurate index of all meaningful files by classifying them based on their content, imports, and exports, not just their location.

**Core Principle:** You will act as a dependency graph analyzer. A file's role is determined by what it does (its code) and how it connects to the rest of the application (its dependencies).

---

## Phase 1: File Inventory

1.  **Action:** Perform a recursive scan of the primary source directory (e.g., `src/`, `app/`).
2.  **Exclude**: Ignore configuration files (`*.config.js`), test files (`*.test.js`, `*.spec.ts`), and non-code assets.
3.  **Output**: A flat list of all relevant file paths to be analyzed.

---

## Phase 2: Content-Based Role Classification

For each file in your inventory, you will assign a `fileRole` by applying the following rules in order. The first rule that matches determines the role.

### High-Confidence Rules (Based on Unique Imports):

1.  **Role: `Component`**
    -   **Condition:** The file imports `React` from `'react'` (or `Vue` from `'vue'`, etc.) AND its body contains JSX syntax (or a Vue `<template>`).

2.  **Role: `Store`**
    -   **Condition:** The file imports `createSlice` or `configureStore` from `'@reduxjs/toolkit'`, `create` from `'zustand'`, or `defineStore` from `'pinia'`.

3.  **Role: `Route`**
    -   **Condition:** The file imports a primary routing component like `BrowserRouter`, `Routes`, or `Route` from `'react-router-dom'` (or equivalent for other frameworks).

### Contextual Rules (Based on Exports and Dependencies):

4.  **Role: `Hook`**
    -   **Condition:** The file's name follows the `use[Name].ts` convention AND it exports one or more functions.

5.  **Role: `Service` / `API Client`**
    -   **Condition:** The file imports a data fetching library like `axios` or `ky` AND exports functions that appear to make network requests.

6.  **Role: `Util`**
    -   **Condition:** The file has few or no internal project imports (imports from other files in `src/`) but exports multiple, typically pure, functions.

7.  **Role: `TypeDefinition`**
    -   **Condition:** The file contains only TypeScript `type` or `interface` definitions and has no runtime code.

8.  **Role: `Other`**
    -   **Condition:** If none of the above rules match, assign the role of `Other`.

---

## Phase 3: Dependency and Export Analysis

For every file, regardless of its assigned role, you MUST perform a final analysis:

1.  **Analyze `exports`**:
    -   Parse the file to identify all exported members.
    -   For each, record its `name` (or `default`) and `type` (Function, Class, Constant, etc.).

2.  **Analyze `dependencies`**:
    -   Parse the file to identify all `import` statements.
    -   Create a list of all relative file paths this file depends on.

---

## Phase 4: Final Assembly

Construct the final `fileExecutionMap` array. Each object in the array represents one file from your inventory and MUST contain its `filePath`, its assigned `fileRole`, and the detailed `exports` and `dependencies` lists.