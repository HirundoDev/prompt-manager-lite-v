# Schema Playbook — definitions

Propósito: glosario canónico de términos, abreviaturas, tipos y convenciones para todo el proyecto.

Ubicación: `schemas/master_blueprint_parts/definitions.json`

---

1) Estructura del schema
- `terms[]`: { term, definition, examples[], synonyms[], antiPatterns[] }
- `types[]`: { name, jsonSchema, description }
- `conventions[]`: { id, rule, examples[] }

---

2) Procedimiento
1. Reunir términos de docs y código (grep/common patterns).
2. Normalizar definiciones y anotar sinónimos/antipatrón.
3. Definir tipos compartidos como JSON Schema reusable.
4. Publicar y enlazar desde otros schemas.

---

3) Ejemplo
```json
{
  "terms": [
    {"term": "tenant", "definition": "Cliente lógico aislado", "examples": ["acme"], "synonyms": ["account"], "antiPatterns": ["org == tenant"]}
  ],
  "types": [
    {"name": "ISODate", "jsonSchema": {"type": "string", "format": "date-time"}, "description": "Fecha en ISO-8601"}
  ],
  "conventions": [
    {"id": "URL-1", "rule": "URLs absolutas en API responses", "examples": ["https://api.example.com/v1/users/1"]}
  ]
}
```

---

4) Checklist
- [ ] Términos críticos definidos y sin ambigüedades.
- [ ] Tipos reusables con JSON Schema.
- [ ] Conexiones a otros schemas (refs).
