# The Mighty Guide

Guía maestra para usar Prompt Manager Lite V: dónde están los archivos, qué guía leer en cada caso y el flujo recomendado para documentar con trazabilidad.

## 🧭 Mapa Rápido
- Base del repositorio: `prompt-manager-lite-v/` (todas las rutas a continuación se asumen relativas a esta carpeta)
- Docs base: `prompt-manager-lite-v/real_structure_documentation/docs/`
- Schemas: `prompt-manager-lite-v/real_structure_documentation/schemas/master_blueprint_parts/`
- Playbooks: `prompt-manager-lite-v/prompt_playbooks/documentation_playbooks/` (nombres canónicos, sin alias)
- Playbooks de Schemas: `prompt-manager-lite-v/prompt_playbooks/schemas_playbooks/`
- Manifiestos: `prompt-manager-lite-v/manifests/`
- Features: `prompt-manager-lite-v/streaming_files/features/`
- Bugs: `prompt-manager-lite-v/streaming_files/bugs/`
- Operations: `prompt-manager-lite-v/streaming_files/operations/`
- Proposals: `prompt-manager-lite-v/streaming_files/proposals/`
- Guías: `prompt-manager-lite-v/guides/`

## 📚 Guías Clave
- Conexión Schemas ↔ Docs: `guides/CONEXION_SCHEMAS_DOCS.md`
- Uso de Playbooks + Frontmatter: `guides/USO_PLAYBOOKS_DOCS.md`
- Uso de Features: `guides/USO_FEATURES.md`
- Uso de Bugs: `guides/USO_BUGS.md`
- Uso de Operations: `guides/USO_OPERATIONS.md`
- Uso de Proposals: `guides/USO_PROPOSALS.md`
- Uso de Manifests: `guides/USO_MANIFESTS.md`
- Uso de Pending Task Template: `guides/USO_PENDINGTASK.md`

## 🚀 Flujo Maestro (de 0 a OK)
Notas importantes antes de empezar:
- Fuente de verdad: los Schemas. Los DOCs derivan de ellos.
- Pasos 1 y 2 son OPCIONALES según el estado del proyecto. Nunca sobrescribas documentación establecida; si ya está completa, solo valida y alinea `schemaRefs`/manifest.

0) Análisis inicial del proyecto (tech stack y aplicabilidad)
   - Revisa la estructura y tecnologías reales del proyecto (¿tiene frontend?, ¿backend?, ¿CLI?, ¿infra?, etc.).
   - Actualiza manualmente el checklist `docs_checklist-verificaction.md`: marca "Aplica" (si/no/pendiente) por ruta y registra `ContadorCambios`/`UltimaModificacion` cuando un archivo sea ajustado.

1) Schemas (opcional si ya están completos)
   - Consolidar/completar los schemas en `real_structure_documentation/schemas/master_blueprint_parts/` con información real del proyecto (analizando código/estructura actual) usando los playbooks de `prompt_playbooks/schemas_playbooks/`.
2) Documentación (opcional si ya está completa)
   - Generar/actualizar DOCs en `real_structure_documentation/docs/` a partir de schemas usando los playbooks de `prompt_playbooks/documentation_playbooks/`.
   - Si los DOCs ya están al día, NO regenerar: solo validar consistencia y actualizar referencias.
3) Enlaces y referencias
   - Añadir/validar `schemaRefs` en el frontmatter de cada `real_structure_documentation/docs/DOC***.md` y reflejar los mismos refs en `manifests/documentation_manifest.json`.
4) Artefactos específicos
   - Seguir las guías de `streaming_files/features/`, `streaming_files/bugs/`, `streaming_files/operations/`, `streaming_files/proposals/` según aplique.
5) Verificación (idempotente)
   - `python3 tools/verify_docs_and_schemas.py` (manifest, playbooks canónicos, cobertura de real_structure_documentation/schemas/guías, schemaRefs)
   - `python3 tools/verify_integrity.py` (estado vs plantillas)

## ✅ Convenciones Clave
- Playbooks canónicos: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC{###}-{Nombre}.md` (sin alias).
- `schemaRefs` es opcional pero recomendado; mantener consistencia entre frontmatter del DOC y el manifest.
- Mantener actualizado `manifests/documentation_manifest.json` como índice de documentación (owners, estados, schemaRefs, paths).

## 📎 Enlaces útiles
- Manifest (instancia): `manifests/documentation_manifest.json`
- Manifest (schema): `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json`
- Lista de DOCs ↔ Playbooks canónicos: ver `guides/USO_PLAYBOOKS_DOCS.md`
- Mapeo Schemas ↔ DOCs: ver `guides/CONEXION_SCHEMAS_DOCS.md`

## 🧩 Qué se actualiza por artefacto (consistencia)
- Features (`streaming_files/features/*.md`):
  - DOCs afectados (API, DataModel, Frontend/Backend Architecture, CLI, Operaciones).
  - `manifests/documentation_manifest.json` (si la feature se indexa o afecta DOCs).
  - Enlaces cruzados a `streaming_files/proposals/`, `streaming_files/bugs/`, `streaming_files/operations/` relacionados.
- Bugs (`streaming_files/bugs/*.md`):
  - DOCs de pruebas/estrategia y changelog.
  - `manifests/documentation_manifest.json` si procede.
  - Criterios de verificación y evidencia.
- Operations (`streaming_files/operations/*.md`):
  - Runbooks y despliegue, riesgos/rollback.
  - `manifests/documentation_manifest.json` si procede.
- Proposals (`streaming_files/proposals/*.md`):
  - Roadmap/ADR si se aprueba; crear feature enlazada.
  - `manifests/documentation_manifest.json` si procede.
- PendingTask (`/template-pendingtask.md` → copia a carpeta correspondiente):
  - Si impacta DOC oficial, actualizar manifest y ejecutar verificadores.
- Manifests:
  - Mantener `schemaRefs` alineados con el frontmatter de cada DOC/guía.

## 🗂️ Estructura por artefacto y creación (recomendada)

Para permitir archivos opcionales (assets, notas, adjuntos), cada artefacto vive en su propia carpeta, con un archivo principal y opcionales. Al crear un nuevo artefacto, copiar también `template-pendingtask.md` dentro de la carpeta del artefacto para registrar tareas puntuales relacionadas.

- Features
  - Carpeta: `streaming_files/features/F###-{slug}/`
  - Principal: `feature.md` (basado en `streaming_files/features/template.md`)
  - Opcionales: `assets/`, `notes.md`, `pendingtask.md` (copiado de `template-pendingtask.md`)

- Bugs
  - Carpeta: `streaming_files/bugs/B###-{slug}/`
  - Principal: `bug_report.md` (basado en `streaming_files/bugs/template.md`)
  - Opcionales: `assets/`, `notes.md`, `pendingtask.md`

- Operations
  - Carpeta: `streaming_files/operations/OP###-{slug}/`
  - Principal: `runbook.md` (basado en `streaming_files/operations/template.md`)
  - Opcionales: `assets/`, `notes.md`, `pendingtask.md`

- Proposals
  - Carpeta: `streaming_files/proposals/P###-{slug}/`
  - Principal: `proposal.md` (basado en `streaming_files/proposals/template.md`)
  - Opcionales: `assets/`, `notes.md`, `pendingtask.md`

Notas:
- Los IDs (`F###`, `B###`, `OP###`, `P###`) se incrementan secuencialmente y forman parte del nombre de carpeta para mantener orden.
- `pendingtask.md` es una copia de `template-pendingtask.md` y se usa para tareas pequeñas locales al artefacto.
- Si prefieres archivo suelto sin carpeta, puedes hacerlo; sin embargo, la carpeta por artefacto es recomendada para escalabilidad.

## 🔢 Reglas de IDs y nombres (manual, sin herramientas)

Para mantener orden sin scripts:

1) Identificar el próximo ID
   - Revisar la carpeta del artefacto (`streaming_files/features/`, `streaming_files/bugs/`, `streaming_files/operations/`, `streaming_files/proposals/`).
   - Tomar el ID más alto del patrón existente y sumar 1.
   - Formato con 3 dígitos: `001`, `002`, ...

2) Patrones de carpeta y archivo principal
   - Feature: carpeta `streaming_files/features/F###-{slug}/` y archivo principal `feature.md`.
   - Bug: carpeta `streaming_files/bugs/B###-{slug}/` y archivo principal `bug_report.md`.
   - Operation: carpeta `streaming_files/operations/OP###-{slug}/` y archivo principal `runbook.md`.
   - Proposal: carpeta `streaming_files/proposals/P###-{slug}/` y archivo principal `proposal.md`.

3) Archivos opcionales dentro de la carpeta
   - `pendingtask.md` (copiado de `template-pendingtask.md`).
   - `notes.md` para notas rápidas.
   - `assets/` para imágenes u otros adjuntos.

4) Índice local por tipo
   - En cada carpeta raíz de tipo (`streaming_files/features/`, `streaming_files/bugs/`, `streaming_files/operations/`, `streaming_files/proposals/`) mantener un `000-README.md` que explique estas reglas y liste ejemplos.

