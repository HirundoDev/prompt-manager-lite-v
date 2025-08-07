# Schema Playbook — dataModelDictionary

Propósito: enumerar modelos, atributos y relaciones normalizadas.

Ubicación: `schemas/master_blueprint_parts/dataModelDictionary.json`

Claves:
- `models[]`
  - `modelName`, `description`
  - Opcionales por modelo: `tableName`, `owner`, `tags[]`, `piiLevel(none|low|moderate|high)`, `primaryKey[]`
  - `attributes[]`: { name, dataType, description, isPrimaryKey, isForeignKey, isNullable }
    - Opcionales por atributo: `format`, `length`, `enum[]`, `default`, `example`, `validation`, `classification(pii|sensitive|public|internal)`
  - `relationships[]`: { relatedModel, type(1-1|1-n|n-n), foreignKey }
    - Opcionales por relación: `sourceAttribute`, `targetAttribute`, `onDelete(restrict|cascade|set-null|no-action)`, `onUpdate(...)`, `inverseName`, `description`

Pasos:
1) Listar todos los modelos del dominio.
2) Definir atributos con tipos y flags (PK/FK/nullable).
3) Especificar relaciones y claves foráneas.
4) Mantener sincronía con `dataModel` (nombres y cardinalidades).

Checklist:
- [ ] Todos los modelos documentados.
- [ ] Atributos con tipos y flags completos.
- [ ] Relaciones y FKs definidas.
- [ ] Consistencia con ERD y API.

Ejemplo mínimo:
```json
{
  "models": [
    {
      "modelName": "User",
      "description": "Entidad de usuario",
      "attributes": [
        {"name":"id","dataType":"uuid","isPrimaryKey":true,"isNullable":false},
        {"name":"email","dataType":"string","isNullable":false}
      ],
      "relationships": [
        {"relatedModel":"Order","type":"One-to-Many","foreignKey":"userId"}
      ]
    }
  ]
}
```

Referencias:
- `schemas/master_blueprint_parts/dataModel.json`
- `docs/DOC009-DataModel.md`
