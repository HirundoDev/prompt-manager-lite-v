#!/usr/bin/env python3
"""
The Mighty Task - Playbook Processor (Refactored)
==================================================

Procesador modular de playbooks que genera marcos de referencia universales.

Uso:
    python scripts/playbook-processor.py --date="2024-01-15" --theme="BACKEND-API-SETUP"
    python scripts/playbook-processor.py --list-playbooks
    python scripts/playbook-processor.py --scan-all

Autor: The Mighty Task System
Fecha: 2025-01-22
Versión: 2.0.0 (Modular)
"""

import argparse
import sys
import os
from pathlib import Path

# Agregar el directorio scripts al path de Python
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

# Importar la nueva estructura modular
try:
    from playbook_processor import PlaybookProcessor, ColoredOutput
    from playbook_processor.utils import PLAYBOOK_FILE_MAPPING
except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("ℹ️  Asegúrate de ejecutar desde el directorio raíz del proyecto")
    print(f"ℹ️  Scripts dir: {scripts_dir}")
    print(f"ℹ️  Current working directory: {os.getcwd()}")
    sys.exit(1)

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Procesador de Playbooks (v2.0 Modular)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Generar marcos de referencia universales para un tema
  python scripts/playbook-processor.py --date="2024-01-15" --theme="BACKEND-API-SETUP"
  
  # Listar todos los playbooks disponibles
  python scripts/playbook-processor.py --list-playbooks
  
  # Escanear y mostrar estado de todos los playbooks
  python scripts/playbook-processor.py --scan-all

Playbooks disponibles: """ + ", ".join(PLAYBOOK_FILE_MAPPING.keys()) + """

Características v2.0:
✅ Marcos de referencia universales (adaptables a cualquier stack)
✅ Templates simplificados y enfocados en decisiones clave
✅ Estructura modular y mantenible
✅ Enlaces a playbooks originales para referencia completa
"""
    )
    
    parser.add_argument('--date', 
                       type=str,
                       help='Fecha de la sesión (formato YYYY-MM-DD)')
    
    parser.add_argument('--theme',
                       type=str, 
                       help='Tema de la sesión (ej: BACKEND-API-SETUP)')
    
    parser.add_argument('--playbook',
                       type=str,
                       help='Código específico de playbook a procesar (ej: DOC006)')
    
    parser.add_argument('--output-dir',
                       type=str,
                       help='Directorio de salida para templates (usado con --playbook)')
    
    parser.add_argument('--list-playbooks',
                       action='store_true',
                       help='Listar todos los playbooks disponibles')
    
    parser.add_argument('--scan-all',
                       action='store_true', 
                       help='Escanear todos los playbooks y mostrar estado')
    
    parser.add_argument('--base-path',
                       type=str,
                       help='Ruta base del proyecto (default: directorio actual)')
    
    args = parser.parse_args()
    
    # Mostrar header de la nueva versión
    ColoredOutput.header("The Mighty Task - Playbook Processor v2.0")
    ColoredOutput.info("✨ Generando marcos de referencia universales...")
    
    # Crear procesador
    try:
        processor = PlaybookProcessor(args.base_path)
    except SystemExit:
        return 1
    
    # Listar playbooks
    if args.list_playbooks or args.scan_all:
        processor.list_available_playbooks()
        return 0
    
    # Procesar playbook específico
    if args.playbook:
        if not args.output_dir:
            ColoredOutput.error("--output-dir es requerido cuando usas --playbook")
            return 1
        
        # TODO: Implementar procesamiento de playbook específico en futuras versiones
        ColoredOutput.warning("Funcionalidad de playbook específico será agregada en v2.1")
        ColoredOutput.info("Por ahora, usa --date y --theme para generar marcos por tema")
        return 0
    
    # Procesar por tema y fecha (funcionalidad principal)
    if args.date and args.theme:
        ColoredOutput.info(f"🎯 Procesando tema: {args.theme}")
        ColoredOutput.info(f"📅 Fecha: {args.date}")
        ColoredOutput.info("🔄 Generando marcos de referencia universales...")
        
        success = processor.process_theme_playbooks(args.theme, args.date)
        
        if success:
            ColoredOutput.success("¡Marcos de referencia generados exitosamente!")
            ColoredOutput.info("")
            ColoredOutput.info("💡 ¿Qué cambió en v2.0?")
            print("   • Los templates ahora son marcos de referencia universales")
            print("   • Enfocados en capturar decisiones técnicas clave")  
            print("   • Adaptables a cualquier tecnología o framework")
            print("   • Simplificados pero con enlaces a documentación completa")
            print("   • Estructura modular para mejor mantenimiento")
            return 0
        else:
            ColoredOutput.error("Errores durante el procesamiento")
            return 1
    
    # Si no hay argumentos válidos
    ColoredOutput.error("Debes especificar --date y --theme, o usar --list-playbooks")
    ColoredOutput.info("Ejemplo: python scripts/playbook-processor.py --date=\"2024-01-22\" --theme=\"BACKEND-API-SETUP\"")
    return 1

if __name__ == '__main__':
    sys.exit(main())
