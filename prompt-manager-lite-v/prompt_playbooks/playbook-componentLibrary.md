# Playbook: UI Component Library Census (V2 - AST Analysis)

**Objective:** To conduct a high-fidelity census of all UI components by performing a deep, AST-based (Abstract Syntax Tree) static analysis of each component file.

**Core Principle:** You will act as a code parser, similar to `react-docgen`. You must analyze the structure of the code, not just its text, to extract a precise definition for each component.

---

## Phase 1: Component Discovery

1.  **Identify Component Directories**: Recursively scan for directories named `components`, `ui`, `views`, or `pages`.
2.  **Filter Component Files**: Within these directories, identify all files with component-like extensions: `.js`, `.jsx`, `.ts`, `.tsx`, `.vue`, `.svelte`.
3.  **Identify Main Export**: For each file, determine the primary exported component name. This will be the `componentName`.

---

## Phase 2: Deep Component Analysis (Simulated AST Traversal)

For each component file, you will perform the following deep analysis:

### 2.1 Props Schema Extraction

1.  **Locate Prop Type Definition**: Find the type definition for the component's props. This is most commonly a TypeScript `interface` or `type` alias (e.g., `interface PrimaryButtonProps`).
2.  **Initialize `propsSchema`**: Start a new JSON Schema object for the component's props.
3.  **Iterate Through Properties**: For each property in the type definition:
    -   **`name`**: The name of the prop.
    -   **`type`**: The TypeScript type (e.g., `string`, `number`, `boolean`, `() => void`). Convert this to a JSON Schema type.
    -   **`description`**: **Crucially**, look for a JSDoc comment block (`/** ... */`) immediately preceding the prop definition. The content of this block is the prop's description.
    -   **`required`**: Determine if the prop is required. In TypeScript, a prop is optional if its name is followed by a `?`. If there is no `?`, it is required.
    -   **`defaultValue`**: Search the component file for a static `defaultProps` object (e.g., `PrimaryButton.defaultProps = { ... };`). If the prop name exists as a key in this object, its value is the `defaultValue`.

### 2.2 Managed State Extraction

1.  **Scan for State Hooks**: Search the component's function body for state declaration hooks (e.g., `useState`, `useReducer` in React) or class properties (`this.state` in class components).
2.  **Document Each State**: For each state variable found, create an entry in the `managedState` array, documenting its `stateName` and inferring its `stateType` from the initial value.

### 2.3 Emitted Events Extraction

1.  **Identify Function Props**: Re-examine the `propsSchema`. Any prop whose type is a function (e.g., `() => void`, `(id: string) => void`) is considered an emitted event.
2.  **Define Event Schema**: For each function prop:
    -   The `eventName` is the prop name (e.g., `onClick`).
    -   Analyze the function's arguments to create a `payloadSchema`. For example, `(user: User) => void` implies the payload is an object conforming to the `User` data model.

---

## Phase 3: Final Assembly

1.  **Assign `componentId`**: Use the `componentName` as the unique `componentId`.
2.  **Gather Usage Examples**: If a corresponding Storybook file exists (`*.stories.tsx`), extract a concise code snippet from it to populate `usageExamples`.
3.  **Construct Final Object**: Assemble all extracted data (`componentId`, `filePath`, `propsSchema`, `managedState`, `emittedEvents`, `usageExamples`) into a single, valid object for the `componentLibrary` array.