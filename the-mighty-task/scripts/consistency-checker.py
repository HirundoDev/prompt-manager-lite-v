#!/usr/bin/env python3
"""
The Mighty Task - Consistency Checker
=====================================

Verifica consistencia, integridad y detecta duplicados en el sistema.

Uso:
    python scripts/consistency-checker.py --scan-all
    python scripts/consistency-checker.py --check-session --date="2024-01-15" --theme="BACKEND-API-SETUP"
    python scripts/consistency-checker.py --generate-report

Autor: The Mighty Task System
Fecha: 2025-01-22
"""

import os
import sys
import json
import argparse
import hashlib
from datetime import datetime
from pathlib import Path
import re

class ColoredOutput:
    """Clase para output con colores en terminal."""
    COLORS = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'END': '\033[0m'
    }
    
    @classmethod
    def print(cls, text, color='WHITE', bold=False, underline=False):
        """Imprime texto con formato."""
        prefix = ""
        if bold:
            prefix += cls.COLORS['BOLD']
        if underline:
            prefix += cls.COLORS['UNDERLINE']
        if color in cls.COLORS:
            prefix += cls.COLORS[color]
        
        print(f"{prefix}{text}{cls.COLORS['END']}")
    
    @classmethod
    def success(cls, text):
        cls.print(f"✅ {text}", 'GREEN', bold=True)
    
    @classmethod
    def error(cls, text):
        cls.print(f"❌ {text}", 'RED', bold=True)
    
    @classmethod
    def warning(cls, text):
        cls.print(f"⚠️  {text}", 'YELLOW', bold=True)
    
    @classmethod
    def info(cls, text):
        cls.print(f"ℹ️  {text}", 'CYAN')
    
    @classmethod
    def header(cls, text):
        cls.print(f"\n{'=' * 60}", 'BLUE')
        cls.print(f"  {text}", 'BLUE', bold=True, underline=True)
        cls.print(f"{'=' * 60}\n", 'BLUE')

class ConsistencyChecker:
    """Verificador de consistencia del sistema The Mighty Task."""
    
    def __init__(self, base_path=None):
        self.base_path = Path(base_path or os.getcwd())
        self.daily_work_dir = self.base_path / 'daily-work'
        self.playbooks_dir = self.base_path / 'playbooks' / 'documentation_playbooks'
        self.tracking_file = self.daily_work_dir / '.tracking.json'
        self.reports_dir = self.base_path / 'reports'
        
        # Contadores para estadísticas
        self.stats = {
            'total_sessions': 0,
            'valid_sessions': 0,
            'invalid_sessions': 0,
            'missing_files': 0,
            'orphaned_files': 0,
            'duplicate_content': 0,
            'inconsistent_tracking': 0,
            'broken_references': 0,
            'total_files_checked': 0,
            'issues_found': 0
        }
        
        # Lista de problemas encontrados
        self.issues = []
        
        # Verificar estructura base
        if not (self.base_path / 'PLAN-COMPLETO.md').exists():
            ColoredOutput.error("No estás en el directorio raíz de The Mighty Task")
            ColoredOutput.info("Ejecuta este script desde el directorio que contiene PLAN-COMPLETO.md")
            sys.exit(1)
    
    def load_tracking_data(self):
        """Carga los datos de tracking existentes."""
        if not self.tracking_file.exists():
            ColoredOutput.warning("Archivo de tracking no encontrado")
            return {"processed_dates": [], "playbook_usage": {}, "consistency_checks": {}}
        
        try:
            with open(self.tracking_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            ColoredOutput.error(f"Error leyendo tracking: {e}")
            return {"processed_dates": [], "playbook_usage": {}, "consistency_checks": {}}
    
    def save_tracking_data(self, data):
        """Guarda los datos de tracking."""
        try:
            self.tracking_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.tracking_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            ColoredOutput.error(f"Error guardando tracking: {e}")
            return False
    
    def add_issue(self, category, severity, description, file_path=None, suggestion=None):
        """Añade un problema a la lista."""
        issue = {
            'category': category,
            'severity': severity,  # 'high', 'medium', 'low'
            'description': description,
            'file_path': str(file_path) if file_path else None,
            'suggestion': suggestion,
            'timestamp': datetime.now().isoformat()
        }
        
        self.issues.append(issue)
        self.stats['issues_found'] += 1
        
        # Mostrar inmediatamente si es crítico
        if severity == 'high':
            ColoredOutput.error(f"[{category.upper()}] {description}")
        elif severity == 'medium':
            ColoredOutput.warning(f"[{category.upper()}] {description}")
    
    def get_session_directories(self):
        """Obtiene todos los directorios de sesiones."""
        if not self.daily_work_dir.exists():
            return []
        
        session_dirs = []
        for item in self.daily_work_dir.iterdir():
            if item.is_dir() and '_' in item.name and not item.name.startswith('.'):
                # Formato esperado: YYYY-MM-DD_THEME
                if re.match(r'\d{4}-\d{2}-\d{2}_[A-Z-]+', item.name):
                    session_dirs.append(item)
                else:
                    self.add_issue('naming', 'medium', 
                                 f"Directorio con formato incorrecto: {item.name}",
                                 item, "Renombrar a formato YYYY-MM-DD_THEME")
        
        return session_dirs
    
    def check_session_structure(self, session_dir):
        """Verifica la estructura de un directorio de sesión."""
        session_name = session_dir.name
        issues_found = 0
        
        # Extraer fecha y tema del nombre
        try:
            date_part, theme_part = session_name.split('_', 1)
            datetime.strptime(date_part, '%Y-%m-%d')  # Validar formato fecha
        except (ValueError, TypeError):
            self.add_issue('structure', 'high',
                         f"Formato de directorio inválido: {session_name}",
                         session_dir, "Usar formato YYYY-MM-DD_THEME")
            return False
        
        # Verificar estructura de carpetas esperada
        expected_dirs = ['support-docs', 'assets', 'assets/screenshots', 'assets/logs']
        
        for expected_dir in expected_dirs:
            dir_path = session_dir / expected_dir
            if not dir_path.exists():
                self.add_issue('structure', 'medium',
                             f"Directorio faltante: {session_name}/{expected_dir}",
                             dir_path, f"Crear directorio {expected_dir}")
                issues_found += 1
        
        # Verificar archivo principal de tareas
        expected_task_file = f"pending-tasks-{date_part}_{theme_part}.md"
        task_file_path = session_dir / expected_task_file
        
        if not task_file_path.exists():
            self.add_issue('files', 'high',
                         f"Archivo principal de tareas faltante: {expected_task_file}",
                         task_file_path, "Ejecutar generate-daily.py")
            issues_found += 1
        else:
            # Verificar contenido del archivo principal
            self.check_task_file_content(task_file_path, date_part, theme_part)
        
        # Verificar archivos README en subdirectorios
        readme_paths = [
            session_dir / 'support-docs' / 'README.md',
            session_dir / 'assets' / 'README.md'
        ]
        
        for readme_path in readme_paths:
            if readme_path.parent.exists() and not readme_path.exists():
                self.add_issue('files', 'low',
                             f"README faltante en: {readme_path.parent.name}",
                             readme_path, "Regenerar con generate-daily.py")
        
        self.stats['total_files_checked'] += len(list(session_dir.rglob('*')))
        return issues_found == 0
    
    def check_task_file_content(self, task_file_path, date_part, theme_part):
        """Verifica el contenido del archivo principal de tareas."""
        try:
            with open(task_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificaciones de formato
            if f"# Tareas Pendientes - {date_part} - {theme_part}" not in content:
                self.add_issue('content', 'medium',
                             f"Header incorrecto en {task_file_path.name}",
                             task_file_path, "Regenerar archivo con template correcto")
            
            # Verificar presencia de secciones críticas
            required_sections = [
                "## ✅ Tareas Principales",
                "## 📊 Progreso del Día",
                "## 📈 Métricas del Día"
            ]
            
            for section in required_sections:
                if section not in content:
                    self.add_issue('content', 'low',
                                 f"Sección faltante '{section}' en {task_file_path.name}",
                                 task_file_path, "Agregar sección manualmente")
            
            # Verificar que no esté completamente vacío
            if len(content.strip()) < 100:  # Muy pequeño
                self.add_issue('content', 'high',
                             f"Archivo de tareas prácticamente vacío: {task_file_path.name}",
                             task_file_path, "Regenerar con generate-daily.py")
            
        except Exception as e:
            self.add_issue('files', 'high',
                         f"Error leyendo archivo de tareas: {e}",
                         task_file_path, "Verificar permisos y codificación")
    
    def check_tracking_consistency(self):
        """Verifica consistencia del sistema de tracking."""
        ColoredOutput.info("Verificando consistencia del tracking...")
        
        tracking_data = self.load_tracking_data()
        session_dirs = self.get_session_directories()
        
        # Sesiones en tracking vs directorios reales
        tracked_sessions = tracking_data.get('processed_dates', [])
        tracked_session_names = set()
        
        for session in tracked_sessions:
            session_name = f"{session.get('date', '')}_{session.get('theme', '')}" 
            tracked_session_names.add(session_name)
        
        real_session_names = {d.name for d in session_dirs}
        
        # Sesiones en directorio pero no en tracking
        orphaned_dirs = real_session_names - tracked_session_names
        for orphaned in orphaned_dirs:
            self.add_issue('tracking', 'medium',
                         f"Sesión sin tracking: {orphaned}",
                         self.daily_work_dir / orphaned,
                         "Ejecutar scripts para actualizar tracking")
            self.stats['orphaned_files'] += 1
        
        # Sesiones en tracking pero sin directorio
        missing_dirs = tracked_session_names - real_session_names
        for missing in missing_dirs:
            if missing and '_' in missing:  # Validar formato
                self.add_issue('tracking', 'high',
                             f"Sesión en tracking pero directorio faltante: {missing}",
                             self.daily_work_dir / missing,
                             "Regenerar sesión o limpiar tracking")
                self.stats['missing_files'] += 1
        
        # Verificar integridad de archivos listados en tracking
        for session in tracked_sessions:
            files_created = session.get('files_created', [])
            for file_path in files_created:
                if isinstance(file_path, str) and file_path:
                    full_path = self.base_path / file_path.lstrip('./')
                    if not full_path.exists():
                        self.add_issue('tracking', 'medium',
                                     f"Archivo en tracking pero no existe: {file_path}",
                                     full_path, "Actualizar tracking o regenerar archivo")
                        self.stats['broken_references'] += 1
        
        ColoredOutput.success(f"Tracking verificado: {len(orphaned_dirs)} huérfanos, {len(missing_dirs)} faltantes")
    
    def check_duplicate_content(self):
        """Detecta contenido duplicado entre archivos."""
        ColoredOutput.info("Buscando contenido duplicado...")
        
        file_hashes = {}
        session_dirs = self.get_session_directories()
        
        for session_dir in session_dirs:
            # Solo verificar archivos .md en las sesiones
            md_files = list(session_dir.rglob('*.md'))
            
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Hash del contenido (ignorando espacios y fechas)
                    normalized_content = re.sub(r'\d{4}-\d{2}-\d{2}|\d{2}:\d{2}:\d{2}', '', content)
                    normalized_content = re.sub(r'\s+', ' ', normalized_content.lower())
                    
                    content_hash = hashlib.md5(normalized_content.encode()).hexdigest()
                    
                    if content_hash in file_hashes:
                        self.add_issue('duplicates', 'medium',
                                     f"Contenido duplicado detectado: {md_file.name} vs {file_hashes[content_hash].name}",
                                     md_file, "Revisar y eliminar duplicado")
                        self.stats['duplicate_content'] += 1
                    else:
                        file_hashes[content_hash] = md_file
                        
                except Exception as e:
                    ColoredOutput.warning(f"Error leyendo {md_file}: {e}")
        
        ColoredOutput.success(f"Verificación de duplicados completada: {self.stats['duplicate_content']} encontrados")
    
    def scan_all_sessions(self):
        """Escanea todas las sesiones en busca de problemas."""
        ColoredOutput.header("Escaneando Todas las Sesiones")
        
        session_dirs = self.get_session_directories()
        self.stats['total_sessions'] = len(session_dirs)
        
        if not session_dirs:
            ColoredOutput.warning("No se encontraron sesiones para escanear")
            return False
        
        ColoredOutput.info(f"Escaneando {len(session_dirs)} sesiones...")
        
        for session_dir in session_dirs:
            ColoredOutput.info(f"Verificando: {session_dir.name}")
            
            is_valid = self.check_session_structure(session_dir)
            
            if is_valid:
                self.stats['valid_sessions'] += 1
            else:
                self.stats['invalid_sessions'] += 1
        
        # Verificaciones globales
        self.check_tracking_consistency()
        self.check_duplicate_content()
        
        return True
    
    def generate_consistency_report(self):
        """Genera un reporte detallado de consistencia."""
        ColoredOutput.header("Generando Reporte de Consistencia")
        
        # Crear directorio de reportes
        self.reports_dir.mkdir(exist_ok=True)
        
        # Generar contenido del reporte
        report_content = self.build_report_content()
        
        # Guardar reporte en MD
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = self.reports_dir / f"consistency-report_{timestamp}.md"
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            ColoredOutput.success(f"Reporte generado: {report_file}")
            return str(report_file)
        except Exception as e:
            ColoredOutput.error(f"Error generando reporte: {e}")
            return None
    
    def build_report_content(self):
        """Construye el contenido del reporte de consistencia."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        report = f"""# Reporte de Consistencia - The Mighty Task

**Generado:** {timestamp}  
**Sistema:** The Mighty Task Consistency Checker  
**Versión:** 1.0

---

## 📊 Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| **Sesiones Totales** | {self.stats['total_sessions']} |
| **Sesiones Válidas** | {self.stats['valid_sessions']} |
| **Sesiones con Problemas** | {self.stats['invalid_sessions']} |
| **Archivos Verificados** | {self.stats['total_files_checked']} |
| **Problemas Encontrados** | {self.stats['issues_found']} |
| **Archivos Faltantes** | {self.stats['missing_files']} |
| **Archivos Huérfanos** | {self.stats['orphaned_files']} |
| **Contenido Duplicado** | {self.stats['duplicate_content']} |
| **Referencias Rotas** | {self.stats['broken_references']} |

---

## 🎯 Estado General

"""
        
        # Calcular estado general
        if self.stats['issues_found'] == 0:
            report += "✅ **EXCELENTE** - No se encontraron problemas\n\n"
        elif self.stats['issues_found'] <= 5:
            report += "🟡 **BUENO** - Problemas menores encontrados\n\n"
        elif self.stats['issues_found'] <= 15:
            report += "🟠 **NECESITA ATENCIÓN** - Varios problemas detectados\n\n"
        else:
            report += "🔴 **CRÍTICO** - Múltiples problemas graves\n\n"
        
        # Sección de problemas por categoría
        report += "## 🔍 Problemas Detectados\n\n"
        
        if not self.issues:
            report += "✅ No se encontraron problemas en el sistema.\n\n"
        else:
            # Agrupar por categoría
            issues_by_category = {}
            for issue in self.issues:
                category = issue['category']
                if category not in issues_by_category:
                    issues_by_category[category] = []
                issues_by_category[category].append(issue)
            
            for category, issues in issues_by_category.items():
                report += f"### {category.upper()}\n\n"
                
                for issue in issues:
                    severity_icon = {
                        'high': '🔴',
                        'medium': '🟡', 
                        'low': '🟢'
                    }.get(issue['severity'], '⚪')
                    
                    report += f"{severity_icon} **{issue['severity'].upper()}**: {issue['description']}\n"
                    
                    if issue['file_path']:
                        report += f"   - **Archivo:** `{issue['file_path']}`\n"
                    
                    if issue['suggestion']:
                        report += f"   - **Solución:** {issue['suggestion']}\n"
                    
                    report += "\n"
        
        # Sección de recomendaciones
        report += "## 💡 Recomendaciones\n\n"
        
        recommendations = self.generate_recommendations()
        for rec in recommendations:
            report += f"- {rec}\n"
        
        report += "\n---\n\n"
        report += "## 🛠️ Comandos de Reparación\n\n"
        
        repair_commands = self.generate_repair_commands()
        for cmd in repair_commands:
            report += f"```bash\n{cmd}\n```\n\n"
        
        report += "---\n*Reporte generado automáticamente por The Mighty Task System*\n"
        
        return report
    
    def generate_recommendations(self):
        """Genera recomendaciones basadas en los problemas encontrados."""
        recommendations = []
        
        if self.stats['missing_files'] > 0:
            recommendations.append("Ejecutar `python scripts/generate-daily.py` para recrear sesiones faltantes")
        
        if self.stats['orphaned_files'] > 0:
            recommendations.append("Actualizar tracking ejecutando los scripts de generación")
        
        if self.stats['duplicate_content'] > 0:
            recommendations.append("Revisar y eliminar archivos con contenido duplicado")
        
        if self.stats['broken_references'] > 0:
            recommendations.append("Verificar que todos los playbooks referenciados existan")
        
        if self.stats['invalid_sessions'] > 0:
            recommendations.append("Regenerar sesiones con estructura incorrecta")
        
        if not recommendations:
            recommendations.append("Sistema en buen estado - continuar con mantenimiento regular")
        
        return recommendations
    
    def generate_repair_commands(self):
        """Genera comandos específicos para reparar problemas."""
        commands = []
        
        if self.stats['issues_found'] > 0:
            commands.append("# Verificar problemas específicos")
            commands.append("python scripts/consistency-checker.py --scan-all")
        
        if self.stats['missing_files'] > 0 or self.stats['orphaned_files'] > 0:
            commands.append("# Regenerar estructura si es necesario")
            commands.append("# python scripts/generate-daily.py --theme=TEMA --date=FECHA --force")
        
        commands.append("# Generar nuevo reporte después de reparaciones")
        commands.append("python scripts/consistency-checker.py --generate-report")
        
        return commands
    
    def update_consistency_tracking(self):
        """Actualiza el tracking con información de la verificación."""
        tracking_data = self.load_tracking_data()
        
        consistency_info = {
            'last_check': datetime.now().isoformat(),
            'issues_found': self.stats['issues_found'],
            'total_files_checked': self.stats['total_files_checked'],
            'total_sessions': self.stats['total_sessions'],
            'valid_sessions': self.stats['valid_sessions'],
            'invalid_sessions': self.stats['invalid_sessions']
        }
        
        tracking_data['consistency_checks'] = consistency_info
        
        if self.save_tracking_data(tracking_data):
            ColoredOutput.success("Información de consistencia actualizada en tracking")
    
    def show_final_summary(self):
        """Muestra resumen final de la verificación."""
        ColoredOutput.header("Resumen Final de Verificación")
        
        print(f"📊 **Sesiones verificadas:** {self.stats['total_sessions']}")
        print(f"✅ **Sesiones válidas:** {self.stats['valid_sessions']}")
        print(f"❌ **Sesiones con problemas:** {self.stats['invalid_sessions']}")
        print(f"📄 **Archivos verificados:** {self.stats['total_files_checked']}")
        print(f"🔍 **Problemas encontrados:** {self.stats['issues_found']}")
        
        if self.stats['issues_found'] == 0:
            ColoredOutput.success("🎉 ¡Sistema completamente consistente!")
        elif self.stats['issues_found'] <= 5:
            ColoredOutput.info("📋 Sistema en buen estado con problemas menores")
        else:
            ColoredOutput.warning("⚠️  Sistema requiere atención - múltiples problemas detectados")
        
        # Mostrar categorías de problemas
        if self.issues:
            categories = {}
            for issue in self.issues:
                cat = issue['category']
                categories[cat] = categories.get(cat, 0) + 1
            
            ColoredOutput.info("\nProblemas por categoría:")
            for category, count in categories.items():
                print(f"  • {category}: {count}")

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Verificador de Consistencia',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Escanear todo el sistema
  python scripts/consistency-checker.py --scan-all
  
  # Verificar una sesión específica
  python scripts/consistency-checker.py --check-session --date="2024-01-15" --theme="BACKEND-API-SETUP"
  
  # Generar reporte detallado
  python scripts/consistency-checker.py --generate-report
  
  # Solo verificar tracking
  python scripts/consistency-checker.py --check-tracking
  
  # Verificar duplicados
  python scripts/consistency-checker.py --check-duplicates

Tipos de verificación: estructura, tracking, duplicados, referencias
        """
    )
    
    parser.add_argument('--scan-all',
                       action='store_true',
                       help='Escanear todo el sistema en busca de problemas')
    
    parser.add_argument('--check-session',
                       action='store_true',
                       help='Verificar una sesión específica')
    
    parser.add_argument('--date',
                       type=str,
                       help='Fecha de la sesión a verificar (YYYY-MM-DD)')
    
    parser.add_argument('--theme',
                       type=str,
                       help='Tema de la sesión a verificar')
    
    parser.add_argument('--generate-report',
                       action='store_true',
                       help='Generar reporte detallado de consistencia')
    
    parser.add_argument('--check-tracking',
                       action='store_true',
                       help='Solo verificar consistencia del tracking')
    
    parser.add_argument('--check-duplicates',
                       action='store_true',
                       help='Solo verificar contenido duplicado')
    
    parser.add_argument('--base-path',
                       type=str,
                       help='Ruta base del proyecto (default: directorio actual)')
    
    args = parser.parse_args()
    
    # Crear verificador
    try:
        checker = ConsistencyChecker(args.base_path)
    except SystemExit:
        return 1
    
    # Ejecutar verificaciones según argumentos
    if args.scan_all:
        # Escaneo completo
        success = checker.scan_all_sessions()
        
        if success:
            checker.update_consistency_tracking()
            
        checker.show_final_summary()
        
        # Auto-generar reporte si hay problemas
        if checker.stats['issues_found'] > 0:
            report_file = checker.generate_consistency_report()
            if report_file:
                ColoredOutput.info(f"Reporte detallado guardado en: {report_file}")
        
        return 0 if checker.stats['issues_found'] == 0 else 1
    
    elif args.check_session:
        # Verificar sesión específica
        if not args.date or not args.theme:
            ColoredOutput.error("--date y --theme son requeridos para --check-session")
            return 1
        
        session_name = f"{args.date}_{args.theme}"
        session_dir = checker.daily_work_dir / session_name
        
        if not session_dir.exists():
            ColoredOutput.error(f"Sesión no encontrada: {session_name}")
            return 1
        
        ColoredOutput.header(f"Verificando Sesión: {session_name}")
        is_valid = checker.check_session_structure(session_dir)
        
        if is_valid:
            ColoredOutput.success("✅ Sesión válida y consistente")
            return 0
        else:
            ColoredOutput.error("❌ Problemas encontrados en la sesión")
            return 1
    
    elif args.check_tracking:
        # Solo verificar tracking
        checker.check_tracking_consistency()
        return 0 if checker.stats['issues_found'] == 0 else 1
    
    elif args.check_duplicates:
        # Solo verificar duplicados
        checker.check_duplicate_content()
        return 0 if checker.stats['duplicate_content'] == 0 else 1
    
    elif args.generate_report:
        # Solo generar reporte
        report_file = checker.generate_consistency_report()
        return 0 if report_file else 1
    
    else:
        # Sin argumentos, mostrar ayuda
        ColoredOutput.error("Debes especificar una acción a realizar")
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())
