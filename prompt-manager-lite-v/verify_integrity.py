#!/usr/bin/env python3
"""
Prompt Manager Lite - File Integrity Checker

Este script analiza qué documentos han sido modificados vs cuáles siguen siendo plantillas.
Usa múltiples métodos para detectar modificaciones de forma precisa.
"""

import hashlib
import json
import re
from pathlib import Path
from datetime import datetime

# Configuración
BASE_PATH = Path(__file__).parent
DOCS_PATH = BASE_PATH / 'docs'
FEATURES_PATH = BASE_PATH / 'features'
BUGS_PATH = BASE_PATH / 'bugs'
OPERATIONS_PATH = BASE_PATH / 'operations'
PROPOSALS_PATH = BASE_PATH / 'proposals'
SCHEMAS_PATH = BASE_PATH / 'schemas' / 'master_blueprint_parts'
HASH_FILE = BASE_PATH / 'file_integrity.json'

# Patrones de placeholders comunes
PLACEHOLDER_PATTERNS = [
    r'\[.*?\]',  # [Nombre del Proyecto], [placeholder], etc.
    r'\{\{.*?\}\}',  # {{variable}}
    r'\[ID\]',  # [ID]
    r'\[.*?del.*?\]',  # [Nombre del Proyecto]
    r'`\[.*?\]`',  # `[placeholder]`
]

def generate_file_hash(file_path):
    """Genera hash SHA-256 de un archivo."""
    h = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        print(f"❌ Error generando hash para {file_path}: {e}")
        return None

def count_placeholders(file_path):
    """Cuenta placeholders en un archivo de texto."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        total_placeholders = 0
        found_patterns = []
        
        for pattern in PLACEHOLDER_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                total_placeholders += len(matches)
                found_patterns.extend(matches)
        
        return total_placeholders, list(set(found_patterns))
    except Exception as e:
        print(f"❌ Error analizando placeholders en {file_path}: {e}")
        return 0, []

def get_file_stats(file_path):
    """Obtiene estadísticas completas de un archivo."""
    try:
        stat = file_path.stat()
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'size': stat.st_size,
            'modified': stat.st_mtime,
            'lines': len(content.splitlines()),
            'chars': len(content),
            'words': len(content.split())
        }
    except Exception as e:
        print(f"❌ Error obteniendo estadísticas de {file_path}: {e}")
        return None

def analyze_file(file_path):
    """Análisis completo de un archivo."""
    hash_val = generate_file_hash(file_path)
    placeholder_count, placeholders = count_placeholders(file_path)
    stats = get_file_stats(file_path)
    
    return {
        'path': str(file_path),
        'hash': hash_val,
        'placeholder_count': placeholder_count,
        'placeholders': placeholders,
        'stats': stats,
        'analyzed_at': datetime.now().isoformat()
    }

def store_initial_state():
    """Almacena el estado inicial de todos los archivos."""
    print("🔍 Analizando estado inicial de archivos...")
    
    initial_state = {
        'created_at': datetime.now().isoformat(),
        'files': {}
    }
    
    # Analizar todas las carpetas
    paths_to_analyze = [
        (DOCS_PATH, '*.md'),
        (FEATURES_PATH, '*.md'),
        (BUGS_PATH, '*.md'),
        (OPERATIONS_PATH, '*.md'),
        (PROPOSALS_PATH, '*.md'),
        (SCHEMAS_PATH, '*.json')
    ]
    
    total_files = 0
    for base_path, pattern in paths_to_analyze:
        if base_path.exists():
            for file_path in base_path.rglob(pattern):
                if file_path.is_file():
                    analysis = analyze_file(file_path)
                    if analysis['hash']:
                        initial_state['files'][str(file_path)] = analysis
                        total_files += 1
                        print(f"✅ Analizado: {file_path.name}")
    
    # Guardar estado inicial
    with open(HASH_FILE, 'w', encoding='utf-8') as f:
        json.dump(initial_state, f, indent=2, ensure_ascii=False)
    
    print(f"\n📊 Estado inicial guardado:")
    print(f"   📁 Archivos analizados: {total_files}")
    print(f"   💾 Guardado en: {HASH_FILE}")

def verify_file_integrity():
    """Verifica integridad y cambios en archivos."""
    if not HASH_FILE.exists():
        print(f"❌ {HASH_FILE} no existe.")
        print("   Ejecuta: python verify_integrity.py store")
        return
    
    # Cargar estado inicial
    with open(HASH_FILE, 'r', encoding='utf-8') as f:
        initial_state = json.load(f)
    
    print("🔍 Verificando integridad de archivos...")
    print(f"📅 Estado inicial creado: {initial_state['created_at']}")
    print("=" * 60)
    
    modified_files = []
    unchanged_files = []
    missing_files = []
    template_files = []  # Archivos que siguen siendo plantillas
    completed_files = []  # Archivos que han sido completados
    
    for file_path_str, initial_data in initial_state['files'].items():
        file_path = Path(file_path_str)
        
        if not file_path.exists():
            missing_files.append(file_path_str)
            print(f"🚫 FALTANTE: {file_path.name}")
            continue
        
        # Análisis actual
        current_analysis = analyze_file(file_path)
        
        # Comparar hashes
        if current_analysis['hash'] != initial_data['hash']:
            modified_files.append({
                'path': file_path_str,
                'initial_placeholders': initial_data['placeholder_count'],
                'current_placeholders': current_analysis['placeholder_count'],
                'status': 'modified'
            })
            
            # Determinar si fue completado o parcialmente modificado
            if current_analysis['placeholder_count'] == 0:
                completed_files.append(file_path_str)
                print(f"✅ COMPLETADO: {file_path.name} (0 placeholders restantes)")
            elif current_analysis['placeholder_count'] < initial_data['placeholder_count']:
                print(f"🔄 EN PROGRESO: {file_path.name} ({current_analysis['placeholder_count']}/{initial_data['placeholder_count']} placeholders restantes)")
            else:
                print(f"⚠️  MODIFICADO: {file_path.name} (cambios detectados)")
                
        else:
            unchanged_files.append(file_path_str)
            if initial_data['placeholder_count'] > 0:
                template_files.append(file_path_str)
                print(f"📝 PLANTILLA: {file_path.name} ({initial_data['placeholder_count']} placeholders)")
            else:
                print(f"✨ SIN CAMBIOS: {file_path.name}")
    
    # Resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE ESTADO:")
    print(f"   ✅ Completados: {len(completed_files)}")
    print(f"   🔄 En progreso: {len(modified_files) - len(completed_files)}")
    print(f"   📝 Plantillas sin modificar: {len(template_files)}")
    print(f"   ✨ Sin cambios: {len(unchanged_files) - len(template_files)}")
    print(f"   🚫 Archivos faltantes: {len(missing_files)}")
    
    if template_files:
        print(f"\n📝 ARCHIVOS QUE NECESITAN COMPLETARSE:")
        for template in template_files:
            print(f"   - {Path(template).name}")
    
    return {
        'completed': completed_files,
        'templates': template_files,
        'modified': modified_files,
        'missing': missing_files
    }

if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("🔍 PROMPT MANAGER LITE - VERIFICADOR DE INTEGRIDAD")
    print("=" * 60)
    
    if len(sys.argv) > 1 and sys.argv[1] == 'store':
        store_initial_state()
    else:
        verify_file_integrity()
