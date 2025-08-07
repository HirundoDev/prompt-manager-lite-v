# Schema Playbook — forensicAudit

Propósito: establecer requerimientos de auditoría forense (logs, retención, trails) para incidentes y cumplimiento.

Ubicación: `schemas/master_blueprint_parts/forensicAudit.json`

---

1) Estructura
- `events[]`: { name, description, pii: boolean, retentionDays, storage }
- `trails[]`: { actor, action, object, timestampPolicy }
- `export`: { formats[], accessControls[] }
- `compliance`: { sox|gdpr|hipaa: { requirements[] } }

---

2) Procedimiento
1. Identificar eventos críticos (auth, pagos, cambios de permisos).
2. Definir política de retención y controles de acceso.
3. Alinear con `securityCompliance` y `operations`.

---

3) Ejemplo
```json
{
  "events": [
    {"name": "login", "pii": true, "retentionDays": 90, "storage": "s3://logs/auth"}
  ],
  "export": {"formats": ["parquet"], "accessControls": ["security-team"]}
}
```

---

4) Checklist
- [ ] Eventos críticos cubiertos.
- [ ] Retención y acceso definidos.
- [ ] Export y cumplimiento.
