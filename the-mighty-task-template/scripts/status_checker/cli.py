#!/usr/bin/env python3
"""
Status Checker CLI - Command Line Interface
==========================================

Interface de línea de comandos para el verificador de estado del sistema.
"""

import argparse
import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from status_checker.status import StatusChecker
from status_checker.display import StatusDisplay
from shared.colored_output import ColoredOutput

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Status Checker v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Estado general del sistema
  python scripts/status-checker.py
  
  # Estado rápido (una línea)
  python scripts/status-checker.py --quick
  
  # Análisis detallado de sesiones
  python scripts/status-checker.py --detailed-sessions
  
  # Exportar reporte de estado
  python scripts/status-checker.py --export-report "status-report.md"
  
  # Solo métricas de calidad
  python scripts/status-checker.py --quality-only
  
  # Modo silencioso con salida JSON
  python scripts/status-checker.py --json --quiet

Características v2.0:
- ✅ Análisis de calidad con TemplateDetector
- ✅ Métricas de productividad y completitud
- ✅ Recomendaciones inteligentes automáticas
- ✅ Dashboard de salud del sistema
- ✅ Integración con PlaybookRegistry
- ✅ Exportación de reportes detallados
        """
    )
    
    # Modos de visualización
    parser.add_argument(
        '--quick',
        action='store_true',
        help='Mostrar estado rápido (una línea)'
    )
    
    parser.add_argument(
        '--detailed-sessions',
        action='store_true',
        help='Mostrar análisis detallado de sesiones'
    )
    
    parser.add_argument(
        '--quality-only',
        action='store_true',
        help='Mostrar solo métricas de calidad'
    )
    
    # Opciones de salida
    parser.add_argument(
        '--export-report',
        type=str,
        help='Exportar reporte completo a archivo'
    )
    
    parser.add_argument(
        '--json',
        action='store_true',
        help='Salida en formato JSON'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (solo salida estructurada)'
    )
    
    parser.add_argument(
        '--base-path',
        type=str,
        help='Ruta base del proyecto (default: directorio actual)'
    )
    
    # Filtros específicos
    parser.add_argument(
        '--theme',
        type=str,
        help='Filtrar análisis por tema específico'
    )
    
    parser.add_argument(
        '--min-quality',
        type=float,
        default=0,
        help='Mostrar solo sesiones con calidad mínima (0-100)'
    )
    
    args = parser.parse_args()
    
    try:
        # Crear checker y display
        checker = StatusChecker(args.base_path)
        display = StatusDisplay()
        
        # Obtener overview del sistema
        if not args.quiet:
            ColoredOutput.progress("Analizando estado del sistema...")
        
        overview = checker.get_system_overview()
        
        # Aplicar filtros si se especifican
        if args.theme:
            # Filtrar sesiones por tema
            sessions_by_theme = overview['sessions']['sessions_by_theme']
            if args.theme not in sessions_by_theme:
                ColoredOutput.warning(f"Tema '{args.theme}' no encontrado")
                return 1
        
        # Procesar según modo solicitado
        if args.json:
            import json
            print(json.dumps(overview, indent=2, ensure_ascii=False))
            
        elif args.quick:
            display.show_quick_status(overview)
            
        elif args.detailed_sessions:
            display.show_detailed_sessions(overview['sessions'])
            
        elif args.quality_only:
            if not args.quiet:
                ColoredOutput.header("Métricas de Calidad del Sistema")
            display._show_health_dashboard(overview['quality_metrics'])
            
        else:
            # Vista general completa (default)
            if not args.quiet:
                display.show_system_overview(overview)
        
        # Exportar reporte si se solicita
        if args.export_report:
            success = display.export_status_report(overview, args.export_report)
            if success and not args.quiet:
                ColoredOutput.success(f"Reporte exportado a: {args.export_report}")
            elif not success:
                return 1
        
        # Determinar código de salida basado en salud del sistema
        health_score = overview['quality_metrics']['overall_health_score']
        high_priority_recs = len([r for r in overview['recommendations'] if r.get('priority') == 'high'])
        
        if high_priority_recs > 0:
            return 2  # Acciones críticas pendientes
        elif health_score < 40:
            return 1  # Sistema necesita atención
        else:
            return 0  # Todo bien
        
    except KeyboardInterrupt:
        ColoredOutput.warning("Análisis cancelado por el usuario")
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