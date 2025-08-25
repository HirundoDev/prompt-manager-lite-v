#!/usr/bin/env python3
"""
Consistency Checker CLI - Command Line Interface
===============================================

Interface de línea de comandos para el verificador de consistencia.
"""

import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from consistency_checker.checker import ConsistencyChecker
from shared.colored_output import ColoredOutput

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Consistency Checker v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Verificación completa del sistema
  python scripts/consistency-checker.py --scan-all
  
  # Verificar solo estructura del proyecto
  python scripts/consistency-checker.py --check-structure
  
  # Verificar solo sesiones diarias
  python scripts/consistency-checker.py --check-sessions
  
  # Verificar solo playbooks
  python scripts/consistency-checker.py --check-playbooks
  
  # Generar reporte detallado
  python scripts/consistency-checker.py --scan-all --report-file "consistency-report.md"
  
  # Verificación silenciosa
  python scripts/consistency-checker.py --scan-all --quiet
  
  # Solo mostrar issues críticos
  python scripts/consistency-checker.py --scan-all --critical-only

Características v2.0:
- ✅ Detección inteligente de templates vs contenido real
- ✅ Verificación modular por componentes
- ✅ Análisis de calidad de sesiones
- ✅ Detección de duplicados avanzada
- ✅ Reportes detallados exportables
- ✅ Integración con PlaybookRegistry y TemplateDetector
        """
    )
    
    # Argumentos de verificación
    parser.add_argument(
        '--scan-all',
        action='store_true',
        help='Ejecutar verificación completa del sistema'
    )
    
    parser.add_argument(
        '--check-structure',
        action='store_true',
        help='Verificar solo estructura del proyecto'
    )
    
    parser.add_argument(
        '--check-sessions',
        action='store_true',
        help='Verificar solo sesiones diarias'
    )
    
    parser.add_argument(
        '--check-playbooks',
        action='store_true',
        help='Verificar solo consistencia de playbooks'
    )
    
    parser.add_argument(
        '--check-templates',
        action='store_true',
        help='Verificar solo detección de templates'
    )
    
    parser.add_argument(
        '--check-tracking',
        action='store_true',
        help='Verificar solo sistema de tracking'
    )
    
    parser.add_argument(
        '--check-duplicates',
        action='store_true',
        help='Verificar solo duplicados'
    )
    
    # Opciones de salida
    parser.add_argument(
        '--report-file',
        type=str,
        help='Archivo para guardar reporte detallado'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso (menos output)'
    )
    
    parser.add_argument(
        '--critical-only',
        action='store_true',
        help='Mostrar solo issues críticos'
    )
    
    parser.add_argument(
        '--base-path',
        type=str,
        help='Ruta base del proyecto (default: directorio actual)'
    )
    
    # Opciones de formato
    parser.add_argument(
        '--json-output',
        action='store_true',
        help='Salida en formato JSON'
    )
    
    args = parser.parse_args()
    
    try:
        # Crear checker
        checker = ConsistencyChecker(args.base_path)
        
        # Determinar qué verificaciones ejecutar
        run_full_check = args.scan_all or not any([
            args.check_structure, args.check_sessions, args.check_playbooks,
            args.check_templates, args.check_tracking, args.check_duplicates
        ])
        
        if run_full_check:
            # Verificación completa
            results = checker.run_full_check()
        else:
            # Verificaciones específicas
            results = {
                'timestamp': checker.datetime.now().isoformat(),
                'checks_performed': [],
                'issues': [],
                'warnings': [],
                'stats': {},
                'overall_health': 'unknown'
            }
            
            if args.check_structure:
                if not args.quiet:
                    ColoredOutput.progress("Verificando estructura del proyecto...")
                structure_check = checker.check_project_structure()
                results['checks_performed'].append('project_structure')
                results['issues'].extend(structure_check['issues'])
                results['warnings'].extend(structure_check['warnings'])
            
            if args.check_playbooks:
                if not args.quiet:
                    ColoredOutput.progress("Verificando consistencia de playbooks...")
                playbooks_check = checker.check_playbooks_consistency()
                results['checks_performed'].append('playbooks_consistency')
                results['issues'].extend(playbooks_check['issues'])
                results['warnings'].extend(playbooks_check['warnings'])
            
            if args.check_sessions:
                if not args.quiet:
                    ColoredOutput.progress("Analizando sesiones diarias...")
                sessions_check = checker.check_daily_sessions()
                results['checks_performed'].append('daily_sessions')
                results['issues'].extend(sessions_check['issues'])
                results['warnings'].extend(sessions_check['warnings'])
            
            if args.check_templates:
                if not args.quiet:
                    ColoredOutput.progress("Verificando detección de templates...")
                templates_check = checker.check_template_detection()
                results['checks_performed'].append('template_detection')
                results['issues'].extend(templates_check['issues'])
                results['warnings'].extend(templates_check['warnings'])
            
            if args.check_tracking:
                if not args.quiet:
                    ColoredOutput.progress("Verificando sistema de tracking...")
                tracking_check = checker.check_tracking_consistency()
                results['checks_performed'].append('tracking_consistency')
                results['issues'].extend(tracking_check['issues'])
                results['warnings'].extend(tracking_check['warnings'])
            
            if args.check_duplicates:
                if not args.quiet:
                    ColoredOutput.progress("Detectando duplicados...")
                duplicates_check = checker.check_duplicates()
                results['checks_performed'].append('duplicates_detection')
                results['issues'].extend(duplicates_check['issues'])
                results['warnings'].extend(duplicates_check['warnings'])
            
            # Calcular estadísticas si se ejecutaron verificaciones
            if results['checks_performed']:
                results['stats'] = checker.calculate_system_stats()
            
            # Determinar salud general
            critical_issues = len([i for i in results['issues'] if i.get('severity') == 'critical'])
            major_issues = len([i for i in results['issues'] if i.get('severity') == 'major'])
            
            if critical_issues > 0:
                results['overall_health'] = 'critical'
            elif major_issues > 3:
                results['overall_health'] = 'poor'
            elif major_issues > 0 or len(results['warnings']) > 5:
                results['overall_health'] = 'fair'
            else:
                results['overall_health'] = 'good'
        
        # Filtrar por severidad si se especifica
        if args.critical_only:
            results['issues'] = [i for i in results['issues'] if i.get('severity') == 'critical']
            results['warnings'] = []  # No mostrar advertencias en modo crítico
        
        # Mostrar resultados
        if args.json_output:
            import json
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            # Mostrar resumen simple
            ColoredOutput.success(f"✅ Verificación completada")
            ColoredOutput.info(f"📊 Verificaciones realizadas: {len(results.get('checks_performed', []))}")
            ColoredOutput.info(f"⚠️  Problemas encontrados: {len(results.get('issues', []))}")
            
            if results.get('issues'):
                ColoredOutput.warning("🔍 Problemas detectados:")
                for issue in results['issues'][:5]:  # Mostrar solo los primeros 5
                    severity_icon = "🔴" if issue.get('severity') == 'critical' else "🟡" if issue.get('severity') == 'major' else "🟢"
                    ColoredOutput.info(f"  {severity_icon} {issue.get('message', 'Sin mensaje')}")
                
                if len(results['issues']) > 5:
                    ColoredOutput.info(f"  ... y {len(results['issues']) - 5} problemas más")
            else:
                ColoredOutput.success("🎉 No se encontraron problemas")
            
            # Mostrar estadísticas si están disponibles
            if results.get('stats'):
                stats = results['stats']
                ColoredOutput.info(f"📈 Estadísticas del sistema:")
                ColoredOutput.info(f"  📁 Sesiones totales: {stats.get('total_sessions', 0)}")
                ColoredOutput.info(f"  📚 Playbooks disponibles: {stats.get('total_playbooks', 0)}")
                ColoredOutput.info(f"  🎯 Temas disponibles: {stats.get('available_themes', 0)}")
                ColoredOutput.info(f"  📊 Completitud promedio: {stats.get('system_completeness', 0):.1%}")
            
            # Generar reporte detallado si se especifica
            if args.report_file:
                report_path = Path(args.report_file)
                # Generar reporte simple en JSON
                with open(report_path, 'w', encoding='utf-8') as f:
                    json.dump(results, f, indent=2, ensure_ascii=False)
                if not args.quiet:
                    ColoredOutput.success(f"Reporte guardado en: {report_path}")
        
        # Determinar código de salida
        critical_issues = len([i for i in results['issues'] if i.get('severity') == 'critical'])
        major_issues = len([i for i in results['issues'] if i.get('severity') == 'major'])
        
        if critical_issues > 0:
            return 2  # Issues críticos
        elif major_issues > 0:
            return 1  # Issues mayores
        else:
            return 0  # Todo bien
        
    except KeyboardInterrupt:
        ColoredOutput.warning("Verificación cancelada por el usuario")
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