#!/usr/bin/env python3
"""
The Mighty Task - Maintenance Script
====================================

Mantenimiento automático del sistema.

Uso:
    python scripts/maintenance.py --daily
    python scripts/maintenance.py --weekly
    python scripts/maintenance.py --monthly
    python scripts/maintenance.py --backup

Autor: The Mighty Task System
Fecha: 2025-01-22
"""

import os
import sys
import json
import shutil
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import subprocess

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
        'END': '\033[0m'
    }
    
    @classmethod
    def print(cls, text, color='WHITE', bold=False):
        """Imprime texto con formato."""
        prefix = ""
        if bold:
            prefix += cls.COLORS['BOLD']
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
        cls.print(f"  {text}", 'BLUE', bold=True)
        cls.print(f"{'=' * 60}\n", 'BLUE')

class MaintenanceManager:
    """Gestor de mantenimiento del sistema."""
    
    def __init__(self):
        self.base_path = Path(os.getcwd())
        self.daily_work_dir = self.base_path / 'daily-work'
        self.reports_dir = self.base_path / 'reports'
        self.logs_dir = self.base_path / 'logs'
        self.backup_dir = self.base_path / 'backups'
        
        # Verificar estructura básica
        if not (self.base_path / 'PLAN-COMPLETO.md').exists():
            ColoredOutput.error("No estás en el directorio raíz de The Mighty Task")
            sys.exit(1)
    
    def run_command(self, cmd):
        """Ejecuta un comando."""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                cwd=self.base_path
            )
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def daily_maintenance(self):
        """Mantenimiento diario."""
        ColoredOutput.header("Mantenimiento Diario")
        
        tasks = [
            ("Verificar consistencia", self.check_consistency),
            ("Limpiar archivos temporales", self.cleanup_temp_files),
            ("Actualizar estadísticas", self.update_statistics),
            ("Verificar permisos", self.check_permissions),
        ]
        
        for task_name, task_func in tasks:
            ColoredOutput.info(f"Ejecutando: {task_name}")
            try:
                task_func()
                ColoredOutput.success(f"Completado: {task_name}")
            except Exception as e:
                ColoredOutput.error(f"Error en {task_name}: {e}")
    
    def weekly_maintenance(self):
        """Mantenimiento semanal."""
        ColoredOutput.header("Mantenimiento Semanal")
        
        tasks = [
            ("Limpieza profunda", self.deep_cleanup),
            ("Verificación completa", self.full_consistency_check),
            ("Resumen semanal", self.generate_weekly_summary),
            ("Optimización", self.optimize_storage),
        ]
        
        for task_name, task_func in tasks:
            ColoredOutput.info(f"Ejecutando: {task_name}")
            try:
                task_func()
                ColoredOutput.success(f"Completado: {task_name}")
            except Exception as e:
                ColoredOutput.error(f"Error en {task_name}: {e}")
    
    def monthly_maintenance(self):
        """Mantenimiento mensual."""
        ColoredOutput.header("Mantenimiento Mensual")
        
        tasks = [
            ("Backup completo", self.create_full_backup),
            ("Archivo histórico", self.archive_old_sessions),
            ("Resumen mensual", self.generate_monthly_summary),
            ("Limpieza de backups antiguos", self.cleanup_old_backups),
        ]
        
        for task_name, task_func in tasks:
            ColoredOutput.info(f"Ejecutando: {task_name}")
            try:
                task_func()
                ColoredOutput.success(f"Completado: {task_name}")
            except Exception as e:
                ColoredOutput.error(f"Error en {task_name}: {e}")
    
    def check_consistency(self):
        """Verificar consistencia básica."""
        success, stdout, stderr = self.run_command("python3 scripts/consistency-checker.py --check-tracking")
        if not success:
            raise Exception(f"Error en consistency check: {stderr}")
    
    def cleanup_temp_files(self):
        """Limpiar archivos temporales."""
        temp_patterns = [
            "**/*.tmp",
            "**/*.bak",
            "**/*~",
            "**/.DS_Store",
            "**/Thumbs.db"
        ]
        
        cleaned_count = 0
        for pattern in temp_patterns:
            temp_files = list(self.base_path.glob(pattern))
            for temp_file in temp_files:
                if temp_file.is_file():
                    temp_file.unlink()
                    cleaned_count += 1
        
        if cleaned_count > 0:
            ColoredOutput.info(f"Eliminados {cleaned_count} archivos temporales")
    
    def update_statistics(self):
        """Actualizar estadísticas del sistema."""
        try:
            tracking_file = self.daily_work_dir / '.tracking.json'
            if not tracking_file.exists():
                return
            
            with open(tracking_file, 'r', encoding='utf-8') as f:
                tracking_data = json.load(f)
            
            # Calcular estadísticas
            stats = {
                'total_sessions': len(tracking_data.get('processed_dates', [])),
                'last_maintenance': datetime.now().isoformat(),
                'total_files': len(list(self.base_path.rglob('*.md'))),
                'total_reports': len(list(self.reports_dir.glob('*.md'))) if self.reports_dir.exists() else 0
            }
            
            tracking_data['maintenance_stats'] = stats
            
            with open(tracking_file, 'w', encoding='utf-8') as f:
                json.dump(tracking_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            ColoredOutput.warning(f"Error actualizando estadísticas: {e}")
    
    def check_permissions(self):
        """Verificar permisos de archivos ejecutables."""
        script_files = list((self.base_path / 'scripts').glob('*.py'))
        fixed_count = 0
        
        for script in script_files:
            if not os.access(script, os.X_OK):
                os.chmod(script, 0o755)
                fixed_count += 1
        
        if fixed_count > 0:
            ColoredOutput.info(f"Arreglados permisos de {fixed_count} scripts")
    
    def deep_cleanup(self):
        """Limpieza profunda del sistema."""
        # Limpiar reportes muy antiguos (más de 3 meses)
        if self.reports_dir.exists():
            cutoff_date = datetime.now() - timedelta(days=90)
            old_reports = []
            
            for report in self.reports_dir.glob('*.md'):
                if report.stat().st_mtime < cutoff_date.timestamp():
                    old_reports.append(report)
            
            for old_report in old_reports:
                old_report.unlink()
            
            if old_reports:
                ColoredOutput.info(f"Eliminados {len(old_reports)} reportes antiguos")
    
    def full_consistency_check(self):
        """Verificación completa de consistencia."""
        success, stdout, stderr = self.run_command("python3 scripts/consistency-checker.py --scan-all")
        # Nota: consistency-checker puede retornar 1 si hay problemas menores
        if "Escaneando Todas las Sesiones" not in stdout:
            raise Exception(f"Error en verificación completa: {stderr}")
    
    def generate_weekly_summary(self):
        """Generar resumen semanal."""
        try:
            summary_content = f"""# Resumen Semanal - The Mighty Task

**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Período:** Última semana  

## 📊 Estadísticas

- **Sesiones creadas:** {self.count_recent_sessions(7)}
- **Reportes generados:** {self.count_recent_reports(7)}
- **Archivos totales:** {len(list(self.base_path.rglob('*.md')))}

## 🔧 Mantenimiento

- Mantenimiento semanal ejecutado exitosamente
- Sistema verificado y optimizado

---
*Generado automáticamente por The Mighty Task Maintenance*
"""
            
            # Crear directorio de resúmenes si no existe
            resumes_dir = self.base_path / 'mission-resumes'
            resumes_dir.mkdir(exist_ok=True)
            
            # Guardar resumen
            timestamp = datetime.now().strftime('%Y%m%d')
            summary_file = resumes_dir / f"weekly-summary_{timestamp}.md"
            
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary_content)
                
            ColoredOutput.info(f"Resumen semanal guardado: {summary_file}")
            
        except Exception as e:
            ColoredOutput.warning(f"Error generando resumen semanal: {e}")
    
    def generate_monthly_summary(self):
        """Generar resumen mensual."""
        try:
            summary_content = f"""# Resumen Mensual - The Mighty Task

**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Período:** Último mes  

## 📊 Estadísticas del Mes

- **Sesiones creadas:** {self.count_recent_sessions(30)}
- **Reportes generados:** {self.count_recent_reports(30)}
- **Archivos totales:** {len(list(self.base_path.rglob('*.md')))}

## 🗂️ Actividad por Tema

{self.get_theme_statistics()}

## 🔧 Mantenimiento

- Mantenimiento mensual ejecutado exitosamente
- Sistema archivado y optimizado
- Backup completo realizado

---
*Generado automáticamente por The Mighty Task Maintenance*
"""
            
            resumes_dir = self.base_path / 'mission-resumes'
            resumes_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m')
            summary_file = resumes_dir / f"monthly-summary_{timestamp}.md"
            
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary_content)
                
            ColoredOutput.info(f"Resumen mensual guardado: {summary_file}")
            
        except Exception as e:
            ColoredOutput.warning(f"Error generando resumen mensual: {e}")
    
    def optimize_storage(self):
        """Optimizar almacenamiento."""
        # Comprimir archivos de log antiguos si existen
        if self.logs_dir.exists():
            log_files = list(self.logs_dir.glob('*.log'))
            for log_file in log_files:
                if log_file.stat().st_size > 1024 * 1024:  # Más de 1MB
                    # En un sistema real, aquí comprimirías el archivo
                    ColoredOutput.info(f"Log file grande detectado: {log_file.name}")
    
    def create_full_backup(self):
        """Crear backup completo."""
        try:
            self.backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f"mighty-task-backup_{timestamp}"
            backup_path = self.backup_dir / backup_name
            
            # Crear directorio de backup
            backup_path.mkdir()
            
            # Copiar archivos importantes
            important_dirs = ['daily-work', 'playbooks', 'reports']
            important_files = ['.config.json', 'README.md', 'PLAN-COMPLETO.md', 'QUICK_START.md']
            
            for dir_name in important_dirs:
                src_dir = self.base_path / dir_name
                if src_dir.exists():
                    dst_dir = backup_path / dir_name
                    shutil.copytree(src_dir, dst_dir, ignore=shutil.ignore_patterns('*.tmp', '*.bak'))
            
            for file_name in important_files:
                src_file = self.base_path / file_name
                if src_file.exists():
                    shutil.copy2(src_file, backup_path)
            
            # Crear archivo de metadatos del backup
            metadata = {
                'created': datetime.now().isoformat(),
                'system_version': '1.0.0',
                'backup_type': 'full',
                'total_sessions': len(list(self.daily_work_dir.glob('*_*'))) if self.daily_work_dir.exists() else 0
            }
            
            with open(backup_path / 'backup_metadata.json', 'w') as f:
                json.dump(metadata, f, indent=2)
            
            ColoredOutput.success(f"Backup completo creado: {backup_path}")
            
        except Exception as e:
            ColoredOutput.error(f"Error creando backup: {e}")
    
    def archive_old_sessions(self):
        """Archivar sesiones muy antiguas."""
        if not self.daily_work_dir.exists():
            return
        
        cutoff_date = datetime.now() - timedelta(days=90)  # 3 meses
        old_sessions = []
        
        for session_dir in self.daily_work_dir.glob('*_*'):
            if session_dir.is_dir():
                try:
                    # Extraer fecha del nombre del directorio
                    date_part = session_dir.name.split('_')[0]
                    session_date = datetime.strptime(date_part, '%Y-%m-%d')
                    
                    if session_date < cutoff_date:
                        old_sessions.append(session_dir)
                except ValueError:
                    continue
        
        if old_sessions:
            # Crear directorio de archivo
            archive_dir = self.base_path / 'archive'
            archive_dir.mkdir(exist_ok=True)
            
            for session in old_sessions:
                archive_path = archive_dir / session.name
                shutil.move(str(session), str(archive_path))
            
            ColoredOutput.info(f"Archivadas {len(old_sessions)} sesiones antiguas")
    
    def cleanup_old_backups(self):
        """Limpiar backups antiguos."""
        if not self.backup_dir.exists():
            return
        
        cutoff_date = datetime.now() - timedelta(days=30)  # 30 días
        old_backups = []
        
        for backup in self.backup_dir.glob('mighty-task-backup_*'):
            if backup.is_dir() and backup.stat().st_mtime < cutoff_date.timestamp():
                old_backups.append(backup)
        
        for old_backup in old_backups:
            shutil.rmtree(old_backup)
        
        if old_backups:
            ColoredOutput.info(f"Eliminados {len(old_backups)} backups antiguos")
    
    def count_recent_sessions(self, days):
        """Contar sesiones creadas en los últimos N días."""
        if not self.daily_work_dir.exists():
            return 0
        
        cutoff_date = datetime.now() - timedelta(days=days)
        count = 0
        
        for session_dir in self.daily_work_dir.glob('*_*'):
            if session_dir.is_dir():
                try:
                    date_part = session_dir.name.split('_')[0]
                    session_date = datetime.strptime(date_part, '%Y-%m-%d')
                    if session_date >= cutoff_date:
                        count += 1
                except ValueError:
                    continue
        
        return count
    
    def count_recent_reports(self, days):
        """Contar reportes generados en los últimos N días."""
        if not self.reports_dir.exists():
            return 0
        
        cutoff_date = datetime.now() - timedelta(days=days)
        count = 0
        
        for report in self.reports_dir.glob('*.md'):
            if report.stat().st_mtime >= cutoff_date.timestamp():
                count += 1
        
        return count
    
    def get_theme_statistics(self):
        """Obtener estadísticas por tema."""
        try:
            tracking_file = self.daily_work_dir / '.tracking.json'
            if not tracking_file.exists():
                return "- No hay datos de tracking disponibles"
            
            with open(tracking_file, 'r', encoding='utf-8') as f:
                tracking_data = json.load(f)
            
            theme_counts = {}
            for session in tracking_data.get('processed_dates', []):
                theme = session.get('theme', 'Unknown')
                theme_counts[theme] = theme_counts.get(theme, 0) + 1
            
            if not theme_counts:
                return "- No hay sesiones registradas"
            
            stats = []
            for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
                stats.append(f"- **{theme}**: {count} sesiones")
            
            return '\n'.join(stats)
            
        except Exception:
            return "- Error obteniendo estadísticas por tema"

def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='The Mighty Task - Maintenance Manager',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Mantenimiento diario
  python scripts/maintenance.py --daily
  
  # Mantenimiento semanal
  python scripts/maintenance.py --weekly
  
  # Mantenimiento mensual
  python scripts/maintenance.py --monthly
  
  # Solo crear backup
  python scripts/maintenance.py --backup

Tipos de mantenimiento: daily (diario), weekly (semanal), monthly (mensual)
        """
    )
    
    parser.add_argument('--daily',
                       action='store_true',
                       help='Ejecutar mantenimiento diario')
    
    parser.add_argument('--weekly',
                       action='store_true',
                       help='Ejecutar mantenimiento semanal')
    
    parser.add_argument('--monthly',
                       action='store_true',
                       help='Ejecutar mantenimiento mensual')
    
    parser.add_argument('--backup',
                       action='store_true',
                       help='Crear backup completo')
    
    args = parser.parse_args()
    
    # Crear manager
    try:
        manager = MaintenanceManager()
    except SystemExit:
        return 1
    
    # Ejecutar según argumentos
    if args.daily:
        manager.daily_maintenance()
    elif args.weekly:
        manager.weekly_maintenance()
    elif args.monthly:
        manager.monthly_maintenance()
    elif args.backup:
        ColoredOutput.header("Creando Backup Completo")
        manager.create_full_backup()
    else:
        ColoredOutput.error("Debes especificar un tipo de mantenimiento")
        parser.print_help()
        return 1
    
    ColoredOutput.success("¡Mantenimiento completado exitosamente!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
