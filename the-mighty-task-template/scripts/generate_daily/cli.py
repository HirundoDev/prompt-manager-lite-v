#!/usr/bin/env python3
"""
Generate Daily CLI - Command Line Interface
==========================================

Interface de línea de comandos para el generador de sesiones diarias.
"""

import argparse
import sys
import os
from datetime import date
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generate_daily.generator import DailySessionGenerator
from shared.colored_output import ColoredOutput

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Generador de Sesiones Diarias v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Crear sesión para hoy con tema específico
  python scripts/generate-daily.py --theme "BACKEND-API-SETUP"
  
  # Crear sesión con fecha específica
  python scripts/generate-daily.py --theme "FRONTEND-COMPONENTS" --date "2025-01-22"
  
  # Modo automático (fecha actual + tema default)
  python scripts/generate-daily.py --auto
  
  # Listar temas disponibles
  python scripts/generate-daily.py --list-themes
  
  # Forzar sobrescritura de sesión existente
  python scripts/generate-daily.py --theme "API-DESIGN" --date "2025-01-22" --force
  
  # Modo silencioso
  python scripts/generate-daily.py --theme "DATABASE-SCHEMA" --quiet

Características v2.0:
- ✅ Detección inteligente de templates vs contenido real
- ✅ Validación anti-duplicación avanzada
- ✅ Registro centralizado de playbooks
- ✅ Verificación de consistencia integrada
- ✅ Análisis de calidad de contenido
        """
    )
    
    # Argumentos principales
    parser.add_argument(
        '--theme', 
        type=str,
        help='Tema de la sesión (ej: BACKEND-API-SETUP, FRONTEND-COMPONENTS)'
    )
    
    parser.add_argument(
        '--date',
        type=str,
        default=date.today().strftime('%Y-%m-%d'),
        help='Fecha en formato YYYY-MM-DD (default: hoy)'
    )
    
    # Modos especiales
    parser.add_argument(
        '--auto',
        action='store_true',
        help='Modo automático con valores por defecto'
    )
    
    parser.add_argument(
        '--list-themes',
        action='store_true',
        help='Mostrar todos los temas disponibles'
    )
    
    # Opciones de comportamiento
    parser.add_argument(
        '--force',
        action='store_true',
        help='Sobrescribir sesión existente incluso con contenido'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (menos output)'
    )
    
    parser.add_argument(
        '--base-path',
        type=str,
        help='Ruta base del proyecto (default: directorio actual)'
    )
    
    # Opciones de validación
    parser.add_argument(
        '--skip-validation',
        action='store_true',
        help='Omitir validaciones de duplicación (no recomendado)'
    )
    
    parser.add_argument(
        '--check-duplicates',
        action='store_true',
        help='Solo verificar duplicados sin crear sesión'
    )
    
    args = parser.parse_args()
    
    try:
        # Crear generador
        generator = DailySessionGenerator(args.base_path)
        
        # Procesar argumentos
        if args.list_themes:
            generator.list_available_themes()
            return 0
        
        if args.check_duplicates:
            if not args.theme:
                ColoredOutput.error("--theme es requerido para --check-duplicates")
                return 1
            
            ColoredOutput.header(f"Verificando Duplicados para: {args.theme}")
            duplicates = generator.detect_template_duplicates(args.theme)
            
            if duplicates:
                ColoredOutput.warning(f"Se encontraron {len(duplicates)} posibles duplicados:")
                for dup in duplicates:
                    ColoredOutput.info(f"• {dup['type']}: {dup['file']}")
                    if 'suggestion' in dup:
                        print(f"  Sugerencia: {dup['suggestion']}")
                return 1
            else:
                ColoredOutput.success("No se encontraron duplicados")
                return 0
        
        # Determinar tema
        if args.auto:
            theme = 'BACKEND-API-SETUP'  # Tema por defecto
            if not args.quiet:
                ColoredOutput.info(f"Modo automático: usando tema '{theme}'")
        elif args.theme:
            theme = args.theme
        else:
            ColoredOutput.error("Debes especificar --theme o usar --auto")
            ColoredOutput.info("Usa --list-themes para ver temas disponibles")
            return 1
        
        # Validar parámetros
        if not args.skip_validation:
            is_valid, errors = generator.validate_session_parameters(args.date, theme)
            if not is_valid:
                ColoredOutput.error("Parámetros inválidos:")
                for error in errors:
                    ColoredOutput.error(f"  • {error}")
                return 1
        
        # Verificar duplicados si no se omite validación
        if not args.skip_validation and not args.quiet:
            ColoredOutput.progress("Verificando duplicados...")
            duplicates = generator.detect_template_duplicates(theme)
            if duplicates:
                ColoredOutput.warning(f"Se detectaron {len(duplicates)} posibles duplicados")
                if not args.force:
                    ColoredOutput.info("Usa --force para continuar o revisa duplicados con --check-duplicates")
        
        # Verificar sesión existente
        existing_check = generator.check_existing_session(args.date, theme)
        if existing_check['exists'] and not args.force:
            if existing_check.get('has_meaningful_content', False):
                ColoredOutput.error("Sesión ya existe con contenido significativo")
                ColoredOutput.info("Usa --force para sobrescribir")
                return 1
            elif not args.quiet:
                ColoredOutput.warning("Sesión existe pero solo con templates, sobrescribiendo...")
        
        # Crear sesión
        if not args.quiet:
            ColoredOutput.progress(f"Creando sesión: {args.date}_{theme}")
        
        result = generator.create_session_structure(args.date, theme, args.force)
        
        # Mostrar resultado
        if not args.quiet:
            generator.show_creation_summary(result, args.date, theme)
        
        return 0 if result['success'] else 1
        
    except KeyboardInterrupt:
        ColoredOutput.warning("Operación cancelada por el usuario")
        return 1
    except Exception as e:
        ColoredOutput.error(f"Error inesperado: {e}")
        if not args.quiet:
            import traceback
            ColoredOutput.debug("Traceback completo:")
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())