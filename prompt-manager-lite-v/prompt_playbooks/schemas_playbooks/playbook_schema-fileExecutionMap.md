# Schema Playbook — fileExecutionMap

Propósito: mapear archivos/rutas a comandos de ejecución o entrypoints para facilitar automatizaciones y auditorías.

Ubicación: `schemas/master_blueprint_parts/fileExecutionMap.json`

---

1) Estructura
- `files[]`: { path, language, purpose, dependencies[], isEntryPoint, command, env[], runtime, entryType(script|service|job) }
- `entries[]`: { path, type(script|service|job), run, env[], deps[] }
- `schedules[]`: { id, cron, targets[] }

---

2) Procedimiento
1. Escanear scripts/servicios y comandos de ejecución.
2. Registrar variables de entorno y dependencias.
3. Definir schedules para jobs.

---

3) Ejemplo
```json
{
  "files": [
    {"path": "scripts/seed.sh", "language": "bash", "purpose": "seed db", "dependencies": ["psql"], "isEntryPoint": false, "command": "bash scripts/seed.sh", "env": ["DB_URL"], "entryType": "script"}
  ],
  "entries": [
    {"path": "scripts/seed.sh", "type": "script", "run": "bash scripts/seed.sh", "env": ["DB_URL"], "deps": ["psql"]}
  ]
}
```

---

4) Checklist
- [ ] Entradas con comando ejecutable.
- [ ] Env/deps documentadas.
- [ ] Schedules (si aplica).
