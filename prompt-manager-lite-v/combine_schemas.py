#!/usr/bin/env python3
"""
Prompt Manager Lite - Schema Combiner

Este script combina todos los schemas modulares en un master blueprint JSON.
Ejecuta después de completar la documentación de los schemas.
"""

from pathlib import Path
import json
from datetime import datetime

def combine_schemas():
    """Combina todos los schemas en un master blueprint JSON."""
    
    # Rutas
    base_path = Path(__file__).parent
    schemas_path = base_path / 'schemas' / 'master_blueprint_parts'
    master_schema_path = base_path / 'schemas' / 'master_blueprint_schema.json'
    output_path = base_path / 'master_blueprint_combined.json'
    
    print("🔄 Iniciando combinación de schemas...")
    
    # Leer el schema maestro como base
    if master_schema_path.exists():
        with open(master_schema_path, 'r', encoding='utf-8') as f:
            master_schema = json.load(f)
        print(f"✅ Schema maestro cargado: {master_schema_path}")
    else:
        print("⚠️  Schema maestro no encontrado, creando estructura básica")
        master_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Master Blueprint for Software Projects V3",
            "description": "Comprehensive project blueprint",
            "type": "object",
            "properties": {}
        }
    
    # Combinar todas las partes del schema
    combined_properties = {}
    
    if schemas_path.exists():
        for schema_file in schemas_path.glob('*.json'):
            try:
                with open(schema_file, 'r', encoding='utf-8') as f:
                    schema_part = json.load(f)
                
                # Usar el nombre del archivo como clave
                part_name = schema_file.stem
                combined_properties[part_name] = schema_part
                
                print(f"✅ Agregado: {part_name}")
                
            except Exception as e:
                print(f"❌ Error procesando {schema_file}: {e}")
    
    # Actualizar el schema maestro
    master_schema['properties'] = combined_properties
    master_schema['generated_at'] = datetime.now().isoformat()
    master_schema['total_parts'] = len(combined_properties)
    
    # Escribir el resultado
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_schema, f, indent=2, ensure_ascii=False)
    
    print(f"\n🎉 Master blueprint combinado creado exitosamente!")
    print(f"📁 Ubicación: {output_path}")
    print(f"📊 Total de partes combinadas: {len(combined_properties)}")
    
    return output_path

def validate_schemas():
    """Valida que todos los schemas requeridos estén presentes."""
    
    base_path = Path(__file__).parent
    schemas_path = base_path / 'schemas' / 'master_blueprint_parts'
    
    required_schemas = [
        'projectInfo', 'architecture', 'dataModel', 'businessLogic',
        'operationalStrategy', 'designSystem', 'componentLibrary',
        'testingStrategy', 'deploymentStrategy', 'qualityGoals'
    ]
    
    missing = []
    for schema_name in required_schemas:
        schema_file = schemas_path / f"{schema_name}.json"
        if not schema_file.exists():
            missing.append(schema_name)
    
    if missing:
        print(f"⚠️  Schemas faltantes: {', '.join(missing)}")
        return False
    else:
        print("✅ Todos los schemas requeridos están presentes")
        return True

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 PROMPT MANAGER LITE - SCHEMA COMBINER")
    print("=" * 50)
    
    # Validar schemas
    if validate_schemas():
        # Combinar schemas
        output_file = combine_schemas()
        print(f"\n📋 Para usar el blueprint combinado:")
        print(f"   1. Copia el archivo {output_file.name}")
        print(f"   2. Úsalo como fuente de verdad de tu aplicación")
        print(f"   3. Los agentes IA pueden usar este JSON como contexto completo")
    else:
        print("\n❌ Completa todos los schemas antes de combinar")
