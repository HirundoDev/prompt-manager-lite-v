# Prompt Manager Lite v

## 🎯 Introducción

Prompt Manager Lite es una versión simplificada y portátil del Prompt Manager diseñada para documentar rápidamente proyectos usando un esquema modular flexible. **Plug & Play**: copia la carpeta y comienza a documentar.

## 📁 Estructura de Carpetas

- **docs/**: Plantillas de documentos para la configuración inicial y definición del proyecto
- **schemas/**: Conjunto de schemas JSON modulares para modelar componentes clave del proyecto (incluye `design_system_schema.json` y `master_blueprint_parts/*`)
- **prompt_playbooks/**: Guías y manuales que ayudan en el proceso de planificación y documentación (incluye `documentation_playbooks/` y `schemas_playbooks/`)
- **features/**: Templates y ejemplos para documentar funcionalidades
- **bugs/**: Templates y ejemplos para documentar bugs
- **operations/**: Templates y ejemplos para documentar tareas
- **proposals/**: Templates y ejemplos para documentar ideas
- **guides/**: Guías de conexión y uso (`CONEXION_SCHEMAS_DOCS.md`, `USO_PLAYBOOKS_DOCS.md`)
- **manifests/**: Instancias de manifiestos (`documentation_manifest.json`)

## 🚀 Flujo de Trabajo

### 1. **Establecer Línea Base**
```bash
# Crear snapshot inicial de todos los archivos
python3 tools/verify_integrity.py store
```

### 2. **Completar Documentación**
- Rellena los documentos en `docs/` usando las guías en `prompt_playbooks/`
- Completa los schemas en `schemas/master_blueprint_parts/`
- Usa los templates en `features/`, `bugs/`, `operations/`, `proposals/`

### 3. **Verificar Progreso**
```bash
# Ver qué archivos han sido modificados vs plantillas sin completar
python3 tools/verify_integrity.py
```

### 4. **Verificar consistencia documental**
```bash
# Validar manifest, cobertura de playbooks y cobertura de schemas/guías
python3 tools/verify_docs_and_schemas.py
```

### 5. **Trazabilidad y fuentes**
- Usa `manifests/documentation_manifest.json` como índice de docs (owners, estados, schemaRefs).
- Sigue las guías:
  - `guides/CONEXION_SCHEMAS_DOCS.md` (mapeo Schemas ↔ Docs)
  - `guides/USO_PLAYBOOKS_DOCS.md` (uso de playbooks y frontmatter)

## 🔍 Scripts Disponibles

### **verify_integrity.py**
Verifica qué archivos han sido modificados:
- **Store**: `python3 tools/verify_integrity.py store` - Guarda estado inicial
- **Check**: `python3 tools/verify_integrity.py` - Verifica cambios
- **Detección inteligente**: Cuenta placeholders como `[Nombre del Proyecto]` para determinar completitud

 

### **verify_docs_and_schemas.py**
Valida consistencia documental end-to-end:
- Manifiesto `manifests/documentation_manifest.json` conforme a su schema y archivos DOC existentes.
- Playbooks canónicos por cada `docs/DOC***.md` (sin alias).
- Cobertura de schemas en `guides/CONEXION_SCHEMAS_DOCS.md` y presencia de cada DOC en `guides/USO_PLAYBOOKS_DOCS.md`.
- Cobertura vía `documents[].schemaRefs` (advertencias no bloqueantes para schemas sin referencia; meta-schemas excluidos por configuración).

Ejecutar:
```bash
python3 tools/verify_docs_and_schemas.py
```

## 🧭 Manifest y schemaRefs

- Manifest instancia: `manifests/documentation_manifest.json`
- Schema del manifest: `schemas/master_blueprint_parts/documentationManifest.json`
- Cada entrada `documents[]` acepta `schemaRefs` (opcional) para enlazar DOCs con schemas fuente.
- Recomendado: declarar también `schemaRefs` en el frontmatter de cada DOC (ver `USO_PLAYBOOKS_DOCS.md`).

## 📐 Convención de nombres de playbooks (canónica)

- `prompt_playbooks/documentation_playbooks/playbook-v2-DOC{###}-{Nombre}.md`
- No se usan alias (variantes de capitalización o sin guiones). Se eliminaron alias previos de DOC017, DOC019 y DOC020.

## ⚡ Flujo rápido recomendado

1) Completar schemas en `schemas/master_blueprint_parts/`.
2) Completar DOCs en `docs/` usando `prompt_playbooks/documentation_playbooks/`.
3) Añadir `schemaRefs` en frontmatter y reflejarlos en el manifest.
4) Verificar:
```bash
python3 tools/verify_docs_and_schemas.py
python3 tools/verify_integrity.py
```
5) Mantener actualizados manifest y guías; re-ejecutar verificadores.

## 📊 Estados de Archivos

- ✅ **COMPLETADO**: Sin placeholders, documentación lista
- 🔄 **EN PROGRESO**: Algunos placeholders completados
- 📝 **PLANTILLA**: Sin modificar, necesita completarse
- ⚠️ **MODIFICADO**: Cambios detectados
- 🚫 **FALTANTE**: Archivo eliminado o movido

## 🎯 Ventajas del Sistema

- **Plug & Play**: Copia y comienza a usar inmediatamente
- **Trazabilidad**: Sabe exactamente qué está completo y qué falta
- **Modular**: Cada schema y documento es independiente
- **Portable**: No depende del CLI complejo del Prompt Manager
- **Inteligente**: Detecta automáticamente el progreso de documentación
