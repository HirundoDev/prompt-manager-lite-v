# Plantilla Maestra: Modelo de Datos

> **Propósito:** Documentar el modelo de datos lógico de la aplicación, incluyendo un diagrama de entidad-relación (ERD) y un desglose detallado de cada entidad, sus atributos y sus relaciones.
> **Playbook de Referencia:** `playbook-v2-DOC009-DataModel.md`

<!-- 
  INSTRUCCIONES PARA LA IA (Data Architect Agent):
  - Tu misión es generar este documento a partir del `dataModelDictionary` en el `master_blueprint.json`.
  - Primero, genera el ERD completo con Mermaid.
  - Luego, itera sobre cada entidad para crear su sección de detalle.
-->

## 1. Diagrama de Entidad-Relación (ERD)

```mermaid
erDiagram
    # [Generar el ERD completo aquí, mostrando todas las entidades y sus relaciones]
    # Ejemplo:
    USER {
        string id PK
        string email
    }
    POST {
        string id PK
        string title
        string userId FK
    }
    USER ||--|{ POST : "escribe"
```

---

## 2. Diccionario de Entidades

[Iterar sobre cada entidad en `dataModelDictionary.entities` para generar las siguientes secciones.]

### Entidad: `[Nombre de la Entidad]`

-   **Descripción:** [Propósito y rol de la entidad en el sistema.]

-   **Atributos:**

| Nombre del Atributo | Tipo de Dato | Descripción | ¿Requerido? |
| :--- | :--- | :--- | :--- |
| `[nombre_atributo]` | `[tipo]` | `[descripción]` | `[Sí/No]` |

-   **Relaciones:**

[Describir las relaciones de esta entidad con otras, ej. "Pertenece a un `Usuario`", "Tiene muchos `Comentarios`".]