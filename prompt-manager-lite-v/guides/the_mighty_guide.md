# The Mighty Guide

Guía maestra para usar Prompt Manager Lite V: dónde están los archivos, qué guía leer en cada caso y el flujo recomendado para documentar con trazabilidad.

## 🆕 **SISTEMA MODULAR DE ERROR TRACKING IMPLEMENTADO (v3.3)**

**Fecha actualización:** 2025-08-25  
**Estado:** Sistema modular completamente funcional con error tracking integrado

### **Nuevos Archivos Disponibles:**
- ✅ **`playbooks/DOC035-ErrorTracking.md`** - Framework universal para tracking de errores
- ✅ **`playbooks/DOC036-ErrorCodes.md`** - Sistema de códigos únicos de error
- ✅ **`template-web-research.md`** - Template completo para investigaciones web
- ✅ **`template-operations.md`** - Template modular para operaciones/instalaciones
- ✅ **`template-pendingtask.md`** - Actualizado con sección de error tracking

### **Comandos Modulares Disponibles:**
```bash
# Crear sesiones con diferentes templates
python3 scripts/generate-daily.py --theme "BACKEND-API-SETUP" --template development
python3 scripts/generate-daily.py --theme "DEPLOYMENT-CONFIG" --template operations  
python3 scripts/generate-daily.py --theme "TECH-RESEARCH" --template research

# Web-guides con template de investigación
python3 scripts/web-guide-manager.py --create "study-name" --session "session-name" --use-research-template
```

> Regla local (Windsurf/Cascade): este repositorio usa reglas de uso del asistente. Ver `guides/windsurf_cascade_rules.md`. Seguir esta guía al pie de la letra y presentar resultados de verificación en formato simple (✔/✖ por archivo), abriendo `verification_report.md` como checklist visual.

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
- Obligatorio: respetar al pie de la letra el formato de cada plantilla (Schemas JSON, DOCs, PendingTask, Features, Bugs, Operations, Proposals, Manifests) y leer su playbook canónico antes de editar.

0) Análisis inicial del proyecto (tech stack y aplicabilidad)
   - Revisa la estructura y tecnologías reales del proyecto (¿tiene frontend?, ¿backend?, ¿CLI?, ¿infra?, etc.).
   - Actualiza manualmente el checklist `docs_checklist-verificaction.md`: marca "Aplica" (si/no/pendiente) por ruta y registra `ContadorCambios`/`UltimaModificacion` cuando un archivo sea ajustado.

1) Schemas (opcional si ya están completos)
   - Antes de editar cualquier schema, leer y seguir el playbook correspondiente en `prompt_playbooks/schemas_playbooks/` y respetar el schema JSON (tipos, required, estructura, convenciones).
   - Consolidar/completar los schemas en `real_structure_documentation/schemas/master_blueprint_parts/` con información real del proyecto (analizando código/estructura actual) usando los playbooks de `prompt_playbooks/schemas_playbooks/`.
2) Documentación (opcional si ya está completa)
   - Antes de completar cualquier DOC, leer y seguir el playbook canónico en `prompt_playbooks/documentation_playbooks/` y respetar el frontmatter y secciones definidas por la plantilla.
   - Generar/actualizar DOCs en `real_structure_documentation/docs/` a partir de schemas usando los playbooks de `prompt_playbooks/documentation_playbooks/`.
   - Si los DOCs ya están al día, NO regenerar: solo validar consistencia y actualizar referencias.
3) Enlaces y referencias
   - Añadir/validar `schemaRefs` en el frontmatter de cada `real_structure_documentation/docs/DOC***.md` y reflejar los mismos refs en `manifests/documentation_manifest.json`.
4) Artefactos específicos
   - Seguir las guías de `streaming_files/features/`, `streaming_files/bugs/`, `streaming_files/operations/`, `streaming_files/proposals/` según aplique.
5) Verificación (idempotente)
    - `python3 tools/verify_docs_and_schemas.py` (manifest, playbooks canónicos, cobertura de real_structure_documentation/schemas/guías, schemaRefs)
    - `python3 tools/verify_integrity.py` (estado vs plantillas)

## ✅ Lista rápida de verificación (limpia)

- Ejecuta el verificador una sola vez:
  - `python3 tools/verify_docs_and_schemas.py`

- Revisa y corrige en este orden:
  1) Checklist manual (`docs_checklist-verificaction.md`)
     - Cada DOC del manifest debe tener Aplica: "si" o "no" (no "pendiente").
     - Las rutas listadas deben existir y la fecha `UltimaModificacion` ser coherente.
  2) Estructura DOC ↔ Playbook
     - Abre el playbook canónico del DOC y añade las secciones H2/H3 requeridas.
  3) Contenido real (calidad de DOCs y JSON)
     - DOCs: encabezado H1 con el ID (ej. `# DOC010 - …`), sin placeholders (TODO/TBD/PENDIENTE/RELLENAR), longitud mínima razonable.
     - Schemas/JSON: JSON válido, sin placeholders; en schemas incluir metadatos básicos (`title`, `$id`, `$schema`, `type`).
  4) Índices por tipo
     - `DOC031-BugIndex.md` cubre los items en `bugs/`.
     - `DOC030-FeatureIndex.md` cubre los items en `features/`.
     - `DOC028-OperationsRunbook.md` cubre los items en `operations/`.
  5) Schemas y referencias
     - Mantener `schemaRefs` en el frontmatter de los DOCs y en `manifests/documentation_manifest.json`.
     - Asegurar mapeo en `guides/CONEXION_SCHEMAS_DOCS.md`. Evitar schemas JSON "nuevos" no referenciados.
  6) Referencias a scripts
     - Usar rutas correctas con prefijo `tools/` y eliminar referencias obsoletas.

- Errores comunes y cómo resolver:
  - "Heading no incluye ID 'DOCxxx'": cambia el H1 a `# DOCxxx - Título`.
  - "Doc contiene placeholders": reemplaza TODO/TBD/PENDIENTE/RELLENAR por contenido real.
  - "Secciones del playbook ausentes": abre el playbook y añade las secciones H2/H3 exactas.
  - "Schema inválido o sin metadatos": valida el JSON e incluye `title`, `$id`, `$schema`, `type`.
  - "No indexado": añade el enlace o referencia en `DOC028/030/031` según corresponda.

- ¿Cuándo está OK?
  - Cuando el verificador no muestra errores. Las advertencias son aceptables temporalmente, pero deben resolverse.

## ✅ Convenciones Clave
- Playbooks canónicos: `prompt_playbooks/documentation_playbooks/playbook-v2-DOC{###}-{Nombre}.md` (sin alias).
- `schemaRefs` es opcional pero recomendado; mantener consistencia entre frontmatter del DOC y el manifest.
- Mantener actualizado `manifests/documentation_manifest.json` como índice de documentación (owners, estados, schemaRefs, paths).
- Respetar estrictamente las plantillas: no cambiar la estructura, campos o tipos definidos. Para JSON Schemas, validar contra el schema correspondiente; para DOCs, mantener el frontmatter y secciones exactamente como en el playbook/plantilla.
- Leer SIEMPRE el playbook canónico antes de rellenar un artefacto (DOC, schema, pendingtask, feature, bug, operation, proposal, manifest) y seguirlo al pie de la letra.
- PendingTask: usar `template-pendingtask.md` como base; no remover campos obligatorios.

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

