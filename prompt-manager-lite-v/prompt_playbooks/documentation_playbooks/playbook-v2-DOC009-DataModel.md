# Playbook v2 — DOC009: Data Model

Guía para documentar el modelo de datos lógico y su ERD.

Relacionado con: `docs/DOC009-DataModel.md`

---

## 1) Propósito

Estandarizar cómo describir entidades, atributos y relaciones, y cómo generar el ERD. Este playbook previene pérdida de formato y asegura trazabilidad con el blueprint.

---

## 2) Estructura obligatoria del documento

1. Diagrama ERD (Mermaid `erDiagram`)
2. Diccionario de Entidades
   - Sección por entidad: nombre, descripción, atributos (tabla), relaciones

Mantener encabezados y tablas según `DOC009-DataModel.md`.

---

## 3) Fuente de datos

- `schemas/master_blueprint_parts/dataModel.json` (o `master_blueprint_combined.json` → `dataModelDictionary`).
- Validar alineación con contratos de API y esquemas de respuesta.

---

## 4) Pasos para completar/actualizar

1. Generar ERD desde `dataModelDictionary.entities` y relaciones.
2. Por cada entidad:
   - Descripción del rol en el sistema.
   - Tabla de atributos: nombre, tipo, descripción, requerido.
   - Relaciones con otras entidades (1:1, 1:N, N:M) con texto claro.
3. Confirmar claves PK/FK cuando aplique y reflejarlas en ERD.
4. Alinear nombres y tipos con APIs y base de datos prevista.

---

## 5) Checklist de validación

- [ ] ERD presente y renderiza (Mermaid válido).
- [ ] Todas las entidades del diccionario tienen sección.
- [ ] Atributos con tipo y requerido completo.
- [ ] Relaciones descritas coherentemente con el ERD.
- [ ] Sin placeholders pendientes.

---

## 6) Ejemplo mínimo de entidad

```markdown
### Entidad: User

- **Descripción:** Representa la cuenta de usuario del sistema.

- **Atributos:**

| Nombre del Atributo | Tipo de Dato | Descripción | ¿Requerido? |
| :--- | :--- | :--- | :--- |
| id | string | Identificador único | Sí |
| email | string | Correo electrónico | Sí |

- **Relaciones:**

User 1 — N Post (User escribe muchos Post)
```

---

## 7) Buenas prácticas

- Usar nombres consistentes y singular para entidades (o decidir convención y mantenerla).
- Tipos de datos claros (string, integer, date-time, etc.).
- Documentar reglas de negocio relevantes como notas adicionales.

---

## 8) Errores comunes a evitar

- ERD que no coincide con el diccionario.
- Atributos sin tipo o sin requerido.
- Relaciones implícitas no documentadas.

---

## 9) Referencias

- Documento: `docs/DOC009-DataModel.md`
- Blueprint: `schemas/master_blueprint_parts/dataModel.json`
- API: `docs/DOC008-APISpecification.md`
- Guía general: `GUIA_COMPLETA_DE_USO.md`

