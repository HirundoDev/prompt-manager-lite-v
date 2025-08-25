#!/usr/bin/env python3
"""
Mission Resumer CLI - Command Line Interface
===========================================

Interface de línea de comandos para el consolidador de sesiones.
"""

import argparse
import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mission_resumer.resumer import MissionResumer
from shared.colored_output import ColoredOutput

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Mission Resumer v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Consolidar todas las sesiones disponibles
  python scripts/mission-resumer.py --output "SPRINT-01-SUMMARY"
  
  # Consolidar solo sesiones de un tema específico
  python scripts/mission-resumer.py --theme "BACKEND-API-SETUP" --output "API-DEVELOPMENT"
  
  # Consolidar sesiones específicas por nombre
  python scripts/mission-resumer.py --sessions "2025-01-20_BACKEND-API-SETUP,2025-01-21_FRONTEND-COMPONENTS" --output "WEEK-01"
  
  # Listar sesiones disponibles
  python scripts/mission-resumer.py --list-sessions
  
  # Listar sesiones de un tema específico
  python scripts/mission-resumer.py --list-sessions --theme "DATABASE-SCHEMA"
  
  # Validar sesiones antes de consolidar
  python scripts/mission-resumer.py --validate-only --theme "TESTING-STRATEGY"
  
  # Modo silencioso
  python scripts/mission-resumer.py --output "FINAL-SUMMARY" --quiet

Características v2.0:
- ✅ Detección inteligente de templates vs contenido real
- ✅ Exclusión automática de contenido vacío
- ✅ Consolidación por tema o sesiones específicas
- ✅ Copia inteligente de assets relevantes
- ✅ Logging detallado de consolidación
- ✅ Validación previa de contenido
        """
    )
    
    # Argumentos principales
    parser.add_argument(
        '--output',
        type=str,
        help='Nombre del resumen consolidado a generar'
    )
    
    parser.add_argument(
        '--theme',
        type=str,
        help='Consolidar solo sesiones de un tema específico'
    )
    
    parser.add_argument(
        '--sessions',
        type=str,
        help='Lista de sesiones específicas separadas por coma'
    )
    
    # Modos especiales
    parser.add_argument(
        '--list-sessions',
        action='store_true',
        help='Listar todas las sesiones disponibles'
    )
    
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Solo validar sesiones sin consolidar'
    )
    
    # Opciones de comportamiento
    parser.add_argument(
        '--force',
        action='store_true',
        help='Sobrescribir resumen existente'
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
    
    # Opciones de filtrado
    parser.add_argument(
        '--min-completion',
        type=float,
        default=10.0,
        help='Porcentaje mínimo de completitud para incluir sesión (default: 10%%)'
    )
    
    parser.add_argument(
        '--exclude-templates',
        action='store_true',
        help='Excluir sesiones que solo contengan templates'
    )
    
    args = parser.parse_args()
    
    try:
        # Crear resumer
        resumer = MissionResumer(args.base_path)
        
        # Procesar argumentos
        if args.list_sessions:
            resumer.list_available_sessions(args.theme)
            return 0
        
        # Determinar sesiones a procesar
        if args.sessions:
            # Sesiones específicas
            session_names = [name.strip() for name in args.sessions.split(',')]
            all_sessions = resumer.scan_available_sessions()
            sessions = [s for s in all_sessions if s['name'] in session_names]
            
            # Verificar que se encontraron todas las sesiones
            found_names = set(s['name'] for s in sessions)
            missing_names = set(session_names) - found_names
            if missing_names:
                ColoredOutput.error(f"Sesiones no encontradas: {', '.join(missing_names)}")
                return 1
                
        else:
            # Todas las sesiones o filtradas por tema
            sessions = resumer.scan_available_sessions(args.theme)
        
        if not sessions:
            ColoredOutput.error("No se encontraron sesiones para procesar")
            if args.theme:
                ColoredOutput.info(f"Tema especificado: {args.theme}")
            ColoredOutput.info("Usa --list-sessions para ver sesiones disponibles")
            return 1
        
        # Aplicar filtros adicionales
        if args.exclude_templates:
            sessions = [s for s in sessions if s['has_meaningful_content']]
            if not sessions:
                ColoredOutput.error("No quedan sesiones después de excluir templates")
                return 1
        
        if args.min_completion > 0:
            sessions = [s for s in sessions if s['completion_percentage'] >= args.min_completion]
            if not sessions:
                ColoredOutput.error(f"No quedan sesiones con completitud >= {args.min_completion}%")
                return 1
        
        # Validar sesiones
        if not args.quiet:
            ColoredOutput.progress("Validando sesiones para consolidación...")
        
        validation = resumer.validate_sessions_for_consolidation(sessions)
        
        if not validation['valid']:
            ColoredOutput.error("Validación fallida:")
            for error in validation['errors']:
                ColoredOutput.error(f"  • {error}")
            
            if validation['recommendations']:
                ColoredOutput.section("Recomendaciones")
                for rec in validation['recommendations']:
                    ColoredOutput.info(f"  • {rec}")
            
            return 1
        
        # Mostrar advertencias si las hay
        if validation['warnings'] and not args.quiet:
            ColoredOutput.section("Advertencias")
            for warning in validation['warnings']:
                ColoredOutput.warning(warning)
        
        # Solo validar si se especifica
        if args.validate_only:
            ColoredOutput.success("✅ Validación exitosa")
            ColoredOutput.info(f"Sesiones válidas para consolidación: {len(sessions)}")
            return 0
        
        # Verificar que se especificó output
        if not args.output:
            ColoredOutput.error("--output es requerido para consolidar")
            ColoredOutput.info("Especifica un nombre para el resumen consolidado")
            return 1
        
        # Verificar si ya existe el resumen
        output_dir = resumer.mission_resumes_dir / args.output
        if output_dir.exists() and not args.force:
            ColoredOutput.error(f"Resumen '{args.output}' ya existe")
            ColoredOutput.info("Usa --force para sobrescribir")
            return 1
        
        # Consolidar sesiones
        if not args.quiet:
            ColoredOutput.progress(f"Consolidando {len(sessions)} sesiones...")
        
        result = resumer.create_consolidated_playbook(sessions, args.output)
        
        # Mostrar resultado
        if not args.quiet:
            resumer.show_consolidation_summary(result, sessions, args.output)
        
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