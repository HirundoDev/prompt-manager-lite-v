"""
Consistency Checker - Report Generator
======================================

Generador de reportes detallados para los resultados de verificación.
"""

from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

class ReportGenerator:
    """Generador de reportes de consistencia."""
    
    def generate_report(self, results: Dict, output_file: Optional[Path] = None) -> str:
        """Genera reporte detallado de la verificación."""
        report_lines = []
        
        # Header
        report_lines.append("# Reporte de Consistencia - The Mighty Task")
        report_lines.append("")
        report_lines.append(f"**Generado:** {results['timestamp']}")
        report_lines.append(f"**Salud General:** {results['overall_health'].upper()}")
        report_lines.append("")
        
        # Resumen ejecutivo
        report_lines.append("## 📊 Resumen Ejecutivo")
        report_lines.append("")
        report_lines.append(f"- **Verificaciones realizadas:** {len(results['checks_performed'])}")
        
        critical_issues = len([i for i in results['issues'] if i.get('severity') == 'critical'])
        major_issues = len([i for i in results['issues'] if i.get('severity') == 'major'])
        
        report_lines.append(f"- **Issues críticos:** {critical_issues}")
        report_lines.append(f"- **Issues mayores:** {major_issues}")
        report_lines.append(f"- **Advertencias:** {len(results['warnings'])}")
        report_lines.append("")
        
        # Estadísticas del sistema
        if results['stats']:
            report_lines.append("## 📈 Estadísticas del Sistema")
            report_lines.append("")
            stats = results['stats']
            report_lines.append(f"- **Sesiones totales:** {stats.get('total_sessions', 0)}")
            report_lines.append(f"- **Sesiones con contenido:** {stats.get('meaningful_sessions', 0)}")
            report_lines.append(f"- **Solo templates:** {stats.get('template_only_sessions', 0)}")
            report_lines.append(f"- **Calidad promedio:** {stats.get('avg_session_quality', 0):.1f}%")
            report_lines.append(f"- **Completitud del sistema:** {stats.get('system_completeness', 0):.1f}%")
            report_lines.append(f"- **Playbooks disponibles:** {stats.get('total_playbooks', 0)}")
            report_lines.append(f"- **Temas configurados:** {stats.get('available_themes', 0)}")
            report_lines.append("")
        
        # Issues críticos
        if critical_issues > 0:
            report_lines.append("## ❌ Issues Críticos")
            report_lines.append("")
            critical_list = [i for i in results['issues'] if i.get('severity') == 'critical']
            for issue in critical_list:
                report_lines.append(f"### {issue['type']}")
                report_lines.append(f"**Mensaje:** {issue['message']}")
                if 'path' in issue:
                    report_lines.append(f"**Ruta:** `{issue['path']}`")
                report_lines.append("")
        
        # Issues mayores
        if major_issues > 0:
            report_lines.append("## ⚠️ Issues Mayores")
            report_lines.append("")
            major_list = [i for i in results['issues'] if i.get('severity') == 'major']
            for issue in major_list:
                report_lines.append(f"### {issue['type']}")
                report_lines.append(f"**Mensaje:** {issue['message']}")
                if 'path' in issue:
                    report_lines.append(f"**Ruta:** `{issue['path']}`")
                report_lines.append("")
        
        # Advertencias
        if results['warnings']:
            report_lines.append("## ⚡ Advertencias")
            report_lines.append("")
            for warning in results['warnings']:
                report_lines.append(f"- **{warning['type']}**: {warning['message']}")
            report_lines.append("")
        
        # Verificaciones realizadas
        report_lines.append("## ✅ Verificaciones Realizadas")
        report_lines.append("")
        for check in results['checks_performed']:
            report_lines.append(f"- {check.replace('_', ' ').title()}")
        report_lines.append("")
        
        # Footer
        report_lines.append("---")
        report_lines.append("")
        report_lines.append("**Generado por:** Consistency Checker v2.0")
        report_lines.append(f"**Timestamp:** {datetime.now().isoformat()}")
        
        report_content = "\n".join(report_lines)
        
        # Guardar archivo si se especifica
        if output_file:
            try:
                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text(report_content, encoding='utf-8')
            except Exception as e:
                print(f"Error guardando reporte: {e}")
        
        return report_content
    
    def show_summary(self, results: Dict):
        """Muestra resumen en consola."""
        from ..shared.colored_output import ColoredOutput
        
        ColoredOutput.header("Resumen de Verificación de Consistencia")
        
        # Salud general
        health = results['overall_health']
        if health == 'good':
            ColoredOutput.success(f"✅ Salud del sistema: {health.upper()}")
        elif health == 'fair':
            ColoredOutput.warning(f"⚠️ Salud del sistema: {health.upper()}")
        else:
            ColoredOutput.error(f"❌ Salud del sistema: {health.upper()}")
        
        # Contadores
        critical_issues = len([i for i in results['issues'] if i.get('severity') == 'critical'])
        major_issues = len([i for i in results['issues'] if i.get('severity') == 'major'])
        
        print(f"📊 **Verificaciones:** {len(results['checks_performed'])}")
        print(f"❌ **Issues críticos:** {critical_issues}")
        print(f"⚠️ **Issues mayores:** {major_issues}")
        print(f"⚡ **Advertencias:** {len(results['warnings'])}")
        
        # Estadísticas clave
        if results['stats']:
            stats = results['stats']
            print(f"📈 **Completitud del sistema:** {stats.get('system_completeness', 0):.1f}%")
            print(f"📝 **Sesiones con contenido:** {stats.get('meaningful_sessions', 0)}/{stats.get('total_sessions', 0)}")
        
        # Recomendaciones
        if critical_issues > 0:
            ColoredOutput.section("🚨 Acción Requerida")
            print("Se encontraron issues críticos que requieren atención inmediata.")
        elif major_issues > 0:
            ColoredOutput.section("⚠️ Recomendaciones")
            print("Se encontraron issues mayores que deberían ser revisados.")
        elif len(results['warnings']) > 5:
            ColoredOutput.section("💡 Sugerencias")
            print("Múltiples advertencias detectadas. Considera revisar para optimizar el sistema.")
        else:
            ColoredOutput.section("✅ Estado")
            print("Sistema en buen estado general. Continúa con el flujo normal de trabajo.")