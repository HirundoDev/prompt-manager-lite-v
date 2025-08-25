"""
Status Checker - Display Module
===============================

Módulo para mostrar información de estado de forma clara y organizada.
"""

from typing import Dict, List
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.colored_output import ColoredOutput

class StatusDisplay:
    """Clase para mostrar información de estado."""
    
    def show_system_overview(self, overview: Dict):
        """Muestra vista general del sistema."""
        ColoredOutput.header("Estado General del Sistema")
        
        # Métricas principales
        quality = overview['quality_metrics']
        self._show_health_dashboard(quality)
        
        # Resumen de componentes
        self._show_sessions_summary(overview['sessions'])
        self._show_playbooks_summary(overview['playbooks'])
        self._show_resumes_summary(overview['mission_resumes'])
        
        # Recomendaciones
        if overview['recommendations']:
            self._show_recommendations(overview['recommendations'])
    
    def _show_health_dashboard(self, quality: Dict):
        """Muestra dashboard de salud del sistema."""
        ColoredOutput.section("🎯 Dashboard de Salud")
        
        overall_score = quality['overall_health_score']
        
        # Determinar estado general
        if overall_score >= 80:
            ColoredOutput.success(f"Sistema en excelente estado ({overall_score:.1f}%)")
        elif overall_score >= 60:
            ColoredOutput.warning(f"Sistema en buen estado ({overall_score:.1f}%)")
        elif overall_score >= 40:
            ColoredOutput.warning(f"Sistema necesita atención ({overall_score:.1f}%)")
        else:
            ColoredOutput.error(f"Sistema requiere mejoras ({overall_score:.1f}%)")
        
        # Métricas detalladas
        print(f"📊 **Productividad:** {quality['productivity_score']:.1f}%")
        print(f"🔧 **Consistencia:** {quality['consistency_score']:.1f}%")
        print(f"✅ **Completitud:** {quality['completeness_score']:.1f}%")
        print()
    
    def _show_sessions_summary(self, sessions: Dict):
        """Muestra resumen de sesiones."""
        ColoredOutput.section("📝 Sesiones de Trabajo")
        
        total = sessions['total_sessions']
        meaningful = sessions['meaningful_sessions']
        templates = sessions['template_only_sessions']
        high_quality = sessions['high_quality_sessions']
        
        print(f"📊 **Total de sesiones:** {total}")
        
        if total > 0:
            meaningful_pct = (meaningful / total) * 100
            quality_pct = (high_quality / total) * 100
            
            print(f"✅ **Con contenido significativo:** {meaningful} ({meaningful_pct:.1f}%)")
            print(f"⚠️  **Solo templates:** {templates}")
            print(f"🌟 **Alta calidad:** {high_quality} ({quality_pct:.1f}%)")
            print(f"📈 **Completitud promedio:** {sessions['avg_completion']:.1f}%")
        
        # Distribución por tema
        if sessions['sessions_by_theme']:
            print(f"🎯 **Por tema:**")
            for theme, count in sessions['sessions_by_theme'].items():
                print(f"   • {theme}: {count} sesiones")
        
        # Actividad reciente
        if sessions['recent_activity']:
            print(f"🕒 **Actividad reciente:**")
            for activity in sessions['recent_activity'][:3]:
                status = "✅" if activity.get('has_main_file', False) else "⚠️"
                print(f"   {status} {activity['date']} - {activity['theme']}")
        
        print()
    
    def _show_playbooks_summary(self, playbooks: Dict):
        """Muestra resumen de playbooks."""
        ColoredOutput.section("📚 Playbooks y Temas")
        
        print(f"📖 **Total playbooks:** {playbooks['total_playbooks']}")
        print(f"🎯 **Temas disponibles:** {playbooks['available_themes']}")
        
        if playbooks['themes_with_issues'] > 0:
            ColoredOutput.warning(f"⚠️ {playbooks['themes_with_issues']} temas con problemas")
        else:
            ColoredOutput.success("✅ Todos los temas están configurados correctamente")
        
        if playbooks['duplicate_templates'] > 0:
            ColoredOutput.warning(f"🔄 {playbooks['duplicate_templates']} grupos de templates duplicados")
        
        # Estado del registry
        registry_status = playbooks['registry_health']
        if registry_status == 'good':
            ColoredOutput.success("✅ Registry de playbooks saludable")
        else:
            ColoredOutput.warning("⚠️ Registry de playbooks tiene inconsistencias")
        
        print()
    
    def _show_resumes_summary(self, resumes: Dict):
        """Muestra resumen de mission resumes."""
        ColoredOutput.section("📋 Mission Resumes")
        
        total = resumes['total_resumes']
        print(f"📄 **Total resúmenes:** {total}")
        
        if total > 0:
            avg_sessions = resumes['avg_sessions_per_resume']
            print(f"📊 **Sesiones promedio por resumen:** {avg_sessions:.1f}")
            
            # Distribución por tamaño
            sizes = resumes['resumes_by_size']
            print(f"📏 **Por tamaño:** Pequeños: {sizes['small']}, Medianos: {sizes['medium']}, Grandes: {sizes['large']}")
            
            # Resúmenes recientes
            if resumes['recent_resumes']:
                print(f"🕒 **Recientes:**")
                for resume in resumes['recent_resumes'][:2]:
                    sessions_info = f" ({resume['sessions_count']} sesiones)" if 'sessions_count' in resume else ""
                    print(f"   • {resume['name']}{sessions_info}")
        else:
            ColoredOutput.info("No hay mission resumes creados aún")
        
        print()
    
    def _show_recommendations(self, recommendations: List[Dict]):
        """Muestra recomendaciones del sistema."""
        ColoredOutput.section("💡 Recomendaciones")
        
        # Agrupar por prioridad
        high_priority = [r for r in recommendations if r.get('priority') == 'high']
        medium_priority = [r for r in recommendations if r.get('priority') == 'medium']
        low_priority = [r for r in recommendations if r.get('priority') == 'low']
        
        # Mostrar por prioridad
        if high_priority:
            ColoredOutput.error("🚨 Alta Prioridad:")
            for rec in high_priority:
                print(f"   • {rec['message']}")
                if 'command' in rec:
                    print(f"     Comando: `{rec['command']}`")
                print()
        
        if medium_priority:
            ColoredOutput.warning("⚠️ Prioridad Media:")
            for rec in medium_priority:
                print(f"   • {rec['message']}")
                if 'command' in rec:
                    print(f"     Comando: `{rec['command']}`")
                elif 'suggestion' in rec:
                    print(f"     Sugerencia: {rec['suggestion']}")
                print()
        
        if low_priority:
            ColoredOutput.info("💡 Mejoras Sugeridas:")
            for rec in low_priority:
                print(f"   • {rec['message']}")
                if 'command' in rec:
                    print(f"     Comando: `{rec['command']}`")
                elif 'suggestion' in rec:
                    print(f"     Sugerencia: {rec['suggestion']}")
        
        print()
    
    def show_detailed_sessions(self, sessions: Dict):
        """Muestra información detallada de sesiones."""
        ColoredOutput.header("Análisis Detallado de Sesiones")
        
        if sessions['total_sessions'] == 0:
            ColoredOutput.warning("No hay sesiones para analizar")
            return
        
        # Estadísticas generales
        print(f"📊 **Estadísticas Generales:**")
        print(f"   • Total: {sessions['total_sessions']} sesiones")
        print(f"   • Con contenido: {sessions['meaningful_sessions']}")
        print(f"   • Solo templates: {sessions['template_only_sessions']}")
        print(f"   • Incompletas (<30%): {sessions['incomplete_sessions']}")
        print(f"   • Alta calidad (>70%): {sessions['high_quality_sessions']}")
        print(f"   • Completitud promedio: {sessions['avg_completion']:.1f}%")
        print()
        
        # Por tema
        if sessions['sessions_by_theme']:
            ColoredOutput.section("📋 Distribución por Tema")
            for theme, count in sorted(sessions['sessions_by_theme'].items()):
                print(f"   🎯 **{theme}:** {count} sesiones")
            print()
        
        # Actividad reciente detallada
        if sessions['recent_activity']:
            ColoredOutput.section("🕒 Actividad Reciente")
            for activity in sessions['recent_activity']:
                status_icon = "✅" if activity.get('has_main_file', False) else "⚠️"
                assets_info = f" ({activity['assets_count']} assets)" if activity['assets_count'] > 0 else ""
                
                print(f"   {status_icon} **{activity['date']}** - {activity['theme']}{assets_info}")
                print(f"      Directorio: `{activity['directory']}`")
            print()
    
    def show_quick_status(self, overview: Dict):
        """Muestra estado rápido del sistema."""
        sessions = overview['sessions']
        quality = overview['quality_metrics']
        recommendations = overview['recommendations']
        
        # Estado general en una línea
        health_score = quality['overall_health_score']
        if health_score >= 80:
            ColoredOutput.success(f"✅ Sistema saludable ({health_score:.0f}%) | {sessions['meaningful_sessions']}/{sessions['total_sessions']} sesiones activas")
        elif health_score >= 60:
            ColoredOutput.warning(f"⚠️ Sistema funcional ({health_score:.0f}%) | {sessions['meaningful_sessions']}/{sessions['total_sessions']} sesiones activas")
        else:
            ColoredOutput.error(f"❌ Sistema necesita atención ({health_score:.0f}%) | {sessions['meaningful_sessions']}/{sessions['total_sessions']} sesiones activas")
        
        # Alertas críticas
        high_priority_recs = [r for r in recommendations if r.get('priority') == 'high']
        if high_priority_recs:
            ColoredOutput.error(f"🚨 {len(high_priority_recs)} acciones críticas pendientes")
            for rec in high_priority_recs:
                print(f"   • {rec['message']}")
        
        # Próximas acciones sugeridas
        medium_priority_recs = [r for r in recommendations if r.get('priority') == 'medium']
        if medium_priority_recs:
            ColoredOutput.info(f"💡 {len(medium_priority_recs)} mejoras recomendadas disponibles")
    
    def export_status_report(self, overview: Dict, output_file: str) -> bool:
        """Exporta reporte de estado a archivo."""
        try:
            from pathlib import Path
            
            report_lines = []
            
            # Header
            report_lines.append("# Reporte de Estado - The Mighty Task")
            report_lines.append("")
            report_lines.append(f"**Generado:** {overview['timestamp']}")
            report_lines.append("")
            
            # Métricas de salud
            quality = overview['quality_metrics']
            report_lines.append("## 🎯 Métricas de Salud")
            report_lines.append("")
            report_lines.append(f"- **Salud General:** {quality['overall_health_score']:.1f}%")
            report_lines.append(f"- **Productividad:** {quality['productivity_score']:.1f}%")
            report_lines.append(f"- **Consistencia:** {quality['consistency_score']:.1f}%")
            report_lines.append(f"- **Completitud:** {quality['completeness_score']:.1f}%")
            report_lines.append("")
            
            # Sesiones
            sessions = overview['sessions']
            report_lines.append("## 📝 Sesiones de Trabajo")
            report_lines.append("")
            report_lines.append(f"- **Total:** {sessions['total_sessions']}")
            report_lines.append(f"- **Con contenido:** {sessions['meaningful_sessions']}")
            report_lines.append(f"- **Solo templates:** {sessions['template_only_sessions']}")
            report_lines.append(f"- **Alta calidad:** {sessions['high_quality_sessions']}")
            report_lines.append(f"- **Completitud promedio:** {sessions['avg_completion']:.1f}%")
            report_lines.append("")
            
            # Recomendaciones
            if overview['recommendations']:
                report_lines.append("## 💡 Recomendaciones")
                report_lines.append("")
                for rec in overview['recommendations']:
                    priority_icon = {"high": "🚨", "medium": "⚠️", "low": "💡"}.get(rec.get('priority', 'low'), '•')
                    report_lines.append(f"{priority_icon} **{rec['type'].title()}:** {rec['message']}")
                    if 'command' in rec:
                        report_lines.append(f"   - Comando: `{rec['command']}`")
                    elif 'suggestion' in rec:
                        report_lines.append(f"   - Sugerencia: {rec['suggestion']}")
                    report_lines.append("")
            
            # Escribir archivo
            report_content = "\n".join(report_lines)
            Path(output_file).write_text(report_content, encoding='utf-8')
            
            return True
            
        except Exception as e:
            ColoredOutput.error(f"Error exportando reporte: {e}")
            return False