# Playbook: Data Model Dictionary Definition (V2 - Prioritized Source Analysis)

**Objective:** To define the canonical data models and their relationships with high precision by analyzing the most authoritative source of truth available in the codebase.

**Core Principle:** You will execute a prioritized search for data model definitions. You MUST analyze the highest-fidelity source you find and stop. Do not mix sources.

---

## Phase 1: Prioritized Source Identification

You will search for the following sources in this exact order. The first one you find is the **sole source of truth**.

1.  **Priority 1 (Highest Fidelity): Prisma Schema**
    -   **Action:** Search for a `schema.prisma` file in the project root or a `prisma/` directory.
    -   **If Found:** Proceed directly to **Phase 2.A**. This is your source of truth.

2.  **Priority 2 (High Fidelity): Other ORM Models**
    -   **Action:** If no `schema.prisma` is found, search for model directories (e.g., `src/models`, `src/entities`). Look for files defining classes that extend an ORM base class (e.g., `extends Model` for Sequelize/TypeORM).
    -   **If Found:** Proceed to **Phase 2.B**.

3.  **Priority 3 (Lowest Fidelity): TypeScript Types**
    -   **Action:** If no ORM models are found, search for centralized type definition files (e.g., `src/types/index.ts`, `src/interfaces/`).
    -   **If Found:** Proceed to **Phase 2.C**.

---

## Phase 2: Deep Schema Parsing

### Phase 2.A: Parsing `schema.prisma`

For each `model` block in the `schema.prisma` file:
1.  The model name (e.g., `User`) is the `modelId`.
2.  Initialize a new JSON Schema for this model.
3.  For each field in the model (e.g., `id Int @id @default(autoincrement())`):
    -   Extract the `fieldName`, `fieldType` (`Int`, `String`, etc.), and type modifiers (`?` for optional, `[]` for array).
    -   Analyze attributes: `@id` means it's the primary key. `@unique` adds a uniqueness constraint. `@default(...)` specifies the default value.
    -   **Crucially, identify relations**: Look for fields whose type is another model (e.g., `posts Post[]`). This defines a relationship. Note the field name and the related model name.

### Phase 2.B: Parsing Other ORM Models

For each model file:
1.  The class name is the `modelId`.
2.  Analyze class properties, especially those with decorators (`@Column`, `@PrimaryGeneratedColumn`, `@OneToMany`, `@ManyToOne`).
3.  The decorator provides the metadata: `@Column('text')` defines the type. `@OneToMany(() => Post, ...)` defines a one-to-many relationship to the `Post` model.

### Phase 2.C: Parsing TypeScript Types

For each `interface` or `type` alias:
1.  The interface/type name is the `modelId`.
2.  Each property becomes a field in the JSON schema. The TypeScript type is the field type.
3.  **Limitation**: Acknowledge that relationships and database-level constraints are not typically available from this source.

---

## Phase 3: Relationship Mapping

After parsing all models from your chosen source, you will explicitly define the relationships.

1.  Iterate through the relationship metadata you collected in Phase 2.
2.  For each relation found (e.g., from a Prisma `@relation` attribute or a TypeORM `@OneToMany` decorator), create a new object in the `dataModelDictionary.relationships` array.
3.  This object MUST contain the `from` model, the `to` model, and the relationship `type` (e.g., `one-to-one`, `one-to-many`, `many-to-many`).

---

## Phase 4: Final Assembly

Construct the final `dataModelDictionary` object, containing both the `models` (with their JSON schemas) and the `relationships` array. Ensure it is valid against the Master Blueprint schema.