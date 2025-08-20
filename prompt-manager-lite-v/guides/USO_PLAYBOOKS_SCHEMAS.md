# 🔧 Guía Completa de Uso de Playbooks de Schemas - Framework 2025

> **📌 REFERENCIA PRINCIPAL:** Para el contexto completo del ecosistema, consulta **[MASTER_GUIDE_2025.md](./MASTER_GUIDE_2025.md)** - La fuente definitiva del sistema Prompt Manager Lite V.

## 🎯 Propósito y Visión 2025

Esta guía establece el framework completo para usar los **playbooks de schemas** con validación avanzada y automatización, proporcionando:
- **Workflow automatizado** para creación y extensión de schemas
- **Validación continua** con herramientas de integridad avanzadas
- **Compatibilidad garantizada** con versionado semántico
- **Trazabilidad completa** entre schemas, playbooks y documentación
- **Mejores prácticas 2025** para desarrollo schema-driven

## 📁 Estructura del Sistema

### **Arquitectura de Schemas y Playbooks:**
```bash
prompt-manager-lite-v/
├── prompt_playbooks/
│   └── schemas_playbooks/                # 🎯 Playbooks de schemas
│       ├── playbook_schema-apiContract.md
│       ├── playbook_schema-dataModel.md
│       ├── playbook_schema-architecture.md
│       └── [28 playbooks totales]
├── real_structure_documentation/
│   └── schemas/                          # 🔧 Schemas JSON
│       ├── master_blueprint_parts/       # Schemas modulares
│       │   ├── apiContract.json
│       │   ├── dataModel.json
│       │   └── [26 schemas core]
│       ├── design_system_schema.json     # Schema canónico
│       └── master_blueprint_schema.json  # Schema maestro
└── tools/
    ├── schema_validator.py               # ✅ Validador avanzado
    ├── schema_generator.py               # 🤖 Generador automático
    ├── compatibility_checker.py         # 🔄 Verificador de compatibilidad
    ├── cross_reference_analyzer.py      # 🔗 Analizador de referencias
    └── schema_merger.py                 # 🔧 Combinador de schemas
```

## 🎯 Principios Fundamentales 2025

### **Compatibilidad y Versionado:**
- **🔄 Retrocompatibilidad:** Añadir solo campos opcionales al extender schemas existentes
- **📌 Versionado Semántico:** Major.Minor.Patch para cambios breaking/features/fixes
- **🔗 Referencias Estables:** Preferir `id`/`slug` para referencias cruzadas
- **📚 Trazabilidad:** Mantener `$comment` enlazando a playbooks correspondientes

### **Arquitectura y Diseño:**
- **🏗️ Separación de Concerns:** Alinear sin mezclar dominios (frontend/backend/infra)
- **📊 Normalización:** Usar `description`, `enum`, `format` para validación robusta
- **🔍 Validación Estricta:** Implementar constraints y patterns apropiados
- **🤖 Automatización:** Maximizar generación y validación automática

## 🚀 Workflow Automatizado 2025

### **Comandos de Automatización:**
```bash
# 1. Validación completa de schemas
python3 tools/schema_validator.py --validate-all --strict

# 2. Verificación de compatibilidad
python3 tools/compatibility_checker.py --check-breaking-changes

# 3. Análisis de referencias cruzadas
python3 tools/cross_reference_analyzer.py --report --fix-broken

# 4. Generación automática desde playbook
python3 tools/schema_generator.py --from-playbook apiContract --validate

# 5. Combinación de schemas
python3 tools/schema_merger.py --output master_blueprint_combined.json

# 6. Pipeline completo
./scripts/schema_validation_pipeline.sh --full-check
```

### **Flujo Detallado por Schema:**
1. **📋 Preparación:** Abrir playbook correspondiente (ej.: `playbook_schema-apiContract.md`)
2. **🔍 Análisis:** Revisar objetivos, campos, ejemplos y checklist del playbook
3. **🔧 Edición:** Modificar schema siguiendo principios de compatibilidad
4. **✅ Validación:** Ejecutar suite completa de validaciones
5. **🔗 Verificación:** Analizar referencias cruzadas y dependencias
6. **📊 Alineación:** Sincronizar con documentos consumidores
7. **🔄 Integración:** Ejecutar pipeline CI/CD para validación continua

## 🔗 Patrones de Referencias Cruzadas

### **Referencias UI/UX:**
```yaml
component_references:
  source: "componentLibrary.components[].{id,slug,name}"
  target: "visualBlueprint.pages[].componentRefs[]"
  strategy: "Preferir id/slug para estabilidad"
  validation: "Verificar que todos los componentRefs resuelvan"
```

### **API ↔ Arquitectura:**
```yaml
api_architecture_sync:
  common_key: "referenceKey"
  endpoints: "apiContract.endpoints[].referenceKey"
  integration: "architecture.integrationPoints[].referenceKey"
  validation: "Sincronización bidireccional obligatoria"
```

### **Modelo de Datos:**
```yaml
data_model_consistency:
  conventions: "dataModel.namingConventions"
  dictionary: "dataModelDictionary.terms[]"
  validation: "Terminología coherente entre ambos"
```

### **Testing ↔ Deployment:**
```yaml
testing_deployment_alignment:
  environments: "testingStrategy.environments[]"
  pipelines: "deploymentStrategy.pipelines[].stages[]"
  gates: "Coherencia en gates y ambientes"
```

### **Design System (Canónico):**
```yaml
design_system_hierarchy:
  canonical: "design_system_schema.json"
  legacy: "master_blueprint_parts/designSystem.json"
  status: "Migrar gradualmente al canónico"
```

## 🔧 Herramientas de Validación Avanzada

### **Validador de Schemas:**
```python
# tools/schema_validator.py
import json
import jsonschema
from pathlib import Path
from typing import Dict, List, Any

class SchemaValidator:
    def __init__(self, schemas_dir: str):
        self.schemas_dir = Path(schemas_dir)
        self.meta_schema = self._load_meta_schema()
    
    def validate_all_schemas(self) -> Dict[str, Any]:
        """Valida todos los schemas contra JSON Schema 2020-12"""
        results = {
            "total": 0,
            "valid": 0,
            "invalid": 0,
            "errors": [],
            "warnings": []
        }
        
        for schema_file in self.schemas_dir.rglob("*.json"):
            try:
                with open(schema_file) as f:
                    schema = json.load(f)
                
                # Validar contra meta-schema
                jsonschema.validate(schema, self.meta_schema)
                
                # Validaciones custom
                self._validate_custom_rules(schema, schema_file.name)
                
                results["valid"] += 1
            except Exception as e:
                results["invalid"] += 1
                results["errors"].append({
                    "file": str(schema_file),
                    "error": str(e)
                })
            
            results["total"] += 1
        
        return results
    
    def _validate_custom_rules(self, schema: Dict, filename: str):
        """Validaciones específicas del framework"""
        # Verificar $comment presente
        if "$comment" not in schema:
            raise ValueError(f"Missing $comment linking to playbook")
        
        # Verificar versionado
        if "version" not in schema.get("properties", {}):
            self.warnings.append(f"{filename}: Consider adding version field")
        
        # Verificar descriptions
        self._check_descriptions(schema, filename)

# Uso
validator = SchemaValidator("real_structure_documentation/schemas/")
results = validator.validate_all_schemas()
print(f"Schemas válidos: {results['valid']}/{results['total']}")
```

### **Verificador de Compatibilidad:**
```python
# tools/compatibility_checker.py
from typing import Dict, List, Tuple
import json
from deepdiff import DeepDiff

class CompatibilityChecker:
    def __init__(self):
        self.breaking_changes = []
        self.safe_changes = []
    
    def check_compatibility(self, old_schema: Dict, new_schema: Dict) -> Dict:
        """Verifica compatibilidad entre versiones de schema"""
        diff = DeepDiff(old_schema, new_schema, ignore_order=True)
        
        breaking_changes = []
        safe_changes = []
        
        # Analizar cambios
        if "dictionary_item_removed" in diff:
            for removed in diff["dictionary_item_removed"]:
                if self._is_required_field(removed, old_schema):
                    breaking_changes.append(f"Removed required field: {removed}")
                else:
                    safe_changes.append(f"Removed optional field: {removed}")
        
        if "dictionary_item_added" in diff:
            for added in diff["dictionary_item_added"]:
                if self._is_required_field(added, new_schema):
                    breaking_changes.append(f"Added required field: {added}")
                else:
                    safe_changes.append(f"Added optional field: {added}")
        
        return {
            "is_compatible": len(breaking_changes) == 0,
            "breaking_changes": breaking_changes,
            "safe_changes": safe_changes,
            "recommended_version_bump": self._suggest_version_bump(breaking_changes, safe_changes)
        }
    
    def _suggest_version_bump(self, breaking: List, safe: List) -> str:
        """Sugiere incremento de versión basado en cambios"""
        if breaking:
            return "major"
        elif safe:
            return "minor"
        else:
            return "patch"
```

### **Analizador de Referencias Cruzadas:**
```python
# tools/cross_reference_analyzer.py
class CrossReferenceAnalyzer:
    def __init__(self, schemas_dir: str):
        self.schemas_dir = Path(schemas_dir)
        self.schemas = self._load_all_schemas()
    
    def analyze_references(self) -> Dict[str, Any]:
        """Analiza todas las referencias cruzadas entre schemas"""
        results = {
            "valid_references": [],
            "broken_references": [],
            "orphaned_entities": [],
            "circular_dependencies": []
        }
        
        # Verificar referencias UI
        self._check_ui_references(results)
        
        # Verificar referencias API-Arquitectura
        self._check_api_architecture_sync(results)
        
        # Verificar modelo de datos
        self._check_data_model_consistency(results)
        
        # Detectar dependencias circulares
        self._detect_circular_dependencies(results)
        
        return results
    
    def _check_ui_references(self, results: Dict):
        """Verifica referencias entre componentLibrary y visualBlueprint"""
        component_lib = self.schemas.get("componentLibrary.json", {})
        visual_blueprint = self.schemas.get("visualBlueprint.json", {})
        
        # Obtener IDs de componentes disponibles
        available_components = set()
        for component in component_lib.get("components", []):
            if "id" in component:
                available_components.add(component["id"])
            if "slug" in component:
                available_components.add(component["slug"])
        
        # Verificar referencias en páginas
        for page in visual_blueprint.get("pages", []):
            for ref in page.get("componentRefs", []):
                if ref not in available_components:
                    results["broken_references"].append({
                        "type": "ui_component",
                        "reference": ref,
                        "location": f"visualBlueprint.pages[].componentRefs"
                    })
                else:
                    results["valid_references"].append({
                        "type": "ui_component",
                        "reference": ref
                    })
```

## 📊 Taxonomía de Campos Recomendada

### **Campos Obligatorios para Extensiones:**
```yaml
compatibilidad:
  nuevos_campos: "SIEMPRE opcionales"
  campos_existentes: "NO modificar si son requeridos"
  
documentacion:
  description: "Obligatorio para todos los campos"
  examples: "Recomendado para campos complejos"
  
validacion:
  enum: "Para valores predefinidos"
  pattern: "Para formatos específicos"
  format: "uri, email, date-time, uuid, etc."
  constraints: "minimum, maximum, minLength, maxLength"
  
versionado:
  version: "Para entidades que afecten contratos"
  deprecated: "Para campos obsoletos"
  
trazabilidad:
  $comment: "Enlace al playbook correspondiente"
  docRefs: "Referencias a documentación relacionada"
```

Recetas de enlaces cruzados
- UI: `visualBlueprint.pages[].componentRefs[]` ↔ `componentLibrary.components[].{id,slug}`.
- API-Arch: `apiContract.endpoints[].referenceKey` ↔ `architecture.integrationPoints[].referenceKey`.
- Datos: `dataModelDictionary.terms[]` ↔ `dataModel.entities[].attributes[]` (alias/sinónimos/constraints).
- DevOps: `deploymentStrategy.pipelines[].gates[]` ↔ `testingStrategy.environments[]`/`types[]`.

Ejemplo de extensión (diff conceptual)
```json
// Antes (fragmento apiContract)
{
  "endpoints": [
    { "method": "GET", "path": "/items", "summary": "List items" }
  ]
}
```
```json
// Después (retrocompatible)
{
  "endpoints": [
    {
      "method": "GET",
      "path": "/items",
      "summary": "List items",
      "referenceKey": "inv_items_list", // para alinear con arquitectura
      "caching": { "strategy": "public", "ttlSeconds": 60 } // opcional
    }
  ],
  "$comment": "Ver prompt_playbooks/schemas_playbooks/playbook_schema-apiContract.md"
}
```

Workflow de PR recomendado
1) Revisa el playbook del schema y justifica la extensión.
2) Aplica cambios manteniendo todos los nuevos campos como opcionales.
3) Actualiza `$comment` con el playbook correspondiente.
4) Ejecuta `python3 tools/verify_integrity.py`.
5) Verifica cruces clave (UI, API-Arch, Datos, DevOps) según esta guía.
6) Anota en la descripción del PR: campos añadidos, motivo, docs afectados.

Schemas principales y sus playbooks
- apiContract → `real_structure_documentation/schemas/master_blueprint_parts/apiContract.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-apiContract.md`
- architecture → `real_structure_documentation/schemas/master_blueprint_parts/architecture.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-architecture.md`
- bugLifecycle → `real_structure_documentation/schemas/master_blueprint_parts/bugLifecycle.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-bugLifecycle.md`
- businessLogic → `real_structure_documentation/schemas/master_blueprint_parts/businessLogic.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-businessLogic.md`
- componentLibrary → `real_structure_documentation/schemas/master_blueprint_parts/componentLibrary.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-componentLibrary.md`
- dataModel → `real_structure_documentation/schemas/master_blueprint_parts/dataModel.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-dataModel.md`
- dataModelDictionary → `real_structure_documentation/schemas/master_blueprint_parts/dataModelDictionary.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-dataModelDictionary.md`
- deepLogicAnalysis → `real_structure_documentation/schemas/master_blueprint_parts/deepLogicAnalysis.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-deepLogicAnalysis.md`
- definitions → `real_structure_documentation/schemas/master_blueprint_parts/definitions.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-definitions.md`
- deploymentStrategy → `real_structure_documentation/schemas/master_blueprint_parts/deploymentStrategy.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-deploymentStrategy.md`
- designPatterns → `real_structure_documentation/schemas/master_blueprint_parts/designPatterns.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-designPatterns.md`
- designSystem (legacy) → `real_structure_documentation/schemas/master_blueprint_parts/designSystem.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-designSystem.md`
- design_system_schema (canónico) → `real_structure_documentation/schemas/design_system_schema.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-design_system_schema.md`
- documentationManifest → `real_structure_documentation/schemas/master_blueprint_parts/documentationManifest.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-documentationManifest.md`
- featureLifecycle → `real_structure_documentation/schemas/master_blueprint_parts/featureLifecycle.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-featureLifecycle.md`
- featureManifest → `real_structure_documentation/schemas/master_blueprint_parts/featureManifest.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-featureManifest.md`
- fileExecutionMap → `real_structure_documentation/schemas/master_blueprint_parts/fileExecutionMap.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-fileExecutionMap.md`
- forensicAudit → `real_structure_documentation/schemas/master_blueprint_parts/forensicAudit.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-forensicAudit.md`
- operationalStrategy → `real_structure_documentation/schemas/master_blueprint_parts/operationalStrategy.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-operationalStrategy.md`
- projectInfo → `real_structure_documentation/schemas/master_blueprint_parts/projectInfo.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-projectInfo.md`
- projectManagement → `real_structure_documentation/schemas/master_blueprint_parts/projectManagement.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-projectManagement.md`
- qualityGoals → `real_structure_documentation/schemas/master_blueprint_parts/qualityGoals.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-qualityGoals.md`
- stateManagementPlan → `real_structure_documentation/schemas/master_blueprint_parts/stateManagementPlan.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-stateManagementPlan.md`
- testingStrategy → `real_structure_documentation/schemas/master_blueprint_parts/testingStrategy.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-testingStrategy.md`
- visualBlueprint → `real_structure_documentation/schemas/master_blueprint_parts/visualBlueprint.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-visualBlueprint.md`
- wireframeStates → `real_structure_documentation/schemas/master_blueprint_parts/wireframeStates.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-wireframeStates.md`
- cli_schema (opcional/placeholder) → `real_structure_documentation/schemas/cli_schema.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-cliSchema.md`
- master_blueprint (meta) → `real_structure_documentation/schemas/master_blueprint_schema.json` | Playbook: `prompt_playbooks/schemas_playbooks/playbook_schema-masterBlueprint.md`

Verificación y calidad
- Comando de validación:
  - `python3 tools/verify_integrity.py`
- Checklist mínimo por PR:
  - [ ] Todos los nuevos campos son opcionales y documentados.
  - [ ] `$comment` actualizado si cambió el playbook.
  - [ ] Cross-referencias coherentes (ids/slug; referenceKey en API/Arquitectura si aplica).
  - [ ] `tools/verify_integrity.py` en verde.

Relación con documentos
- Consulta `guides/CONEXION_SCHEMAS_DOCS.md` para ver qué docs consumen cada schema y qué extractos llenar.
- Recomendación: añadir `schemaRefs` en frontmatter de los docs consumidores, y (opcional) `docRefs` en schemas.

Resolución de gaps
- Si un playbook de schema recomienda campos no presentes y son necesarios para un doc prioritario, añadirlos como opcionales y documentar en el playbook con ejemplo.

Referencias
- Playbooks de schemas: `prompt_playbooks/schemas_playbooks/`
- Guía de conexión: `guides/CONEXION_SCHEMAS_DOCS.md`
- Playbooks de docs: `prompt_playbooks/documentation_playbooks/`
