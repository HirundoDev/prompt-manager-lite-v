#!/usr/bin/env python3
"""
Mighty Task CLI - Unified Multi-Project Management Interface
==========================================================

CLI unificado para gestión completa de proyectos mighty-task con
soporte para arquitectura dual (local y servidor).
"""

import sys
import argparse
import subprocess
from pathlib import Path

# Agregar el directorio de scripts al path para imports
sys.path.insert(0, str(Path(__file__).parent))

from shared.project_manager import ProjectManager
from shared.colored_output import ColoredOutput

def cmd_project(args):
    """Ejecuta comandos del project manager."""
    cmd = [sys.executable, str(Path(__file__).parent / "project-manager.py")] + args.project_args
    return subprocess.run(cmd).returncode

def cmd_generate(args):
    """Ejecuta el generador de sesiones diarias."""
    cmd = [sys.executable, str(Path(__file__).parent / "generate-daily.py")]
    
    # Agregar argumentos del proyecto si están disponibles
    if hasattr(args, 'project_id') and args.project_id:
        cmd.extend(['--project-id', args.project_id])
    
    # Agregar argumentos específicos
    if hasattr(args, 'theme') and args.theme:
        cmd.extend(['--theme', args.theme])
    if hasattr(args, 'template') and args.template:
        cmd.extend(['--template', args.template])
    if hasattr(args, 'date') and args.date:
        cmd.extend(['--date', args.date])
    if hasattr(args, 'force') and args.force:
        cmd.append('--force')
    if hasattr(args, 'quiet') and args.quiet:
        cmd.append('--quiet')
    
    return subprocess.run(cmd).returncode

def cmd_resume(args):
    """Ejecuta el mission resumer."""
    cmd = [sys.executable, str(Path(__file__).parent / "mission-resumer.py")]
    
    # Agregar argumentos del proyecto si están disponibles
    if hasattr(args, 'project_id') and args.project_id:
        cmd.extend(['--project-id', args.project_id])
    
    # Agregar argumentos específicos
    if hasattr(args, 'output') and args.output:
        cmd.extend(['--output', args.output])
    if hasattr(args, 'theme') and args.theme:
        cmd.extend(['--theme', args.theme])
    if hasattr(args, 'sessions') and args.sessions:
        cmd.extend(['--sessions', args.sessions])
    if hasattr(args, 'force') and args.force:
        cmd.append('--force')
    if hasattr(args, 'quiet') and args.quiet:
        cmd.append('--quiet')
    
    return subprocess.run(cmd).returncode

def cmd_status(args):
    """Ejecuta el status checker."""
    cmd = [sys.executable, str(Path(__file__).parent / "status-checker.py")]
    
    # Agregar argumentos del proyecto si están disponibles
    if hasattr(args, 'project_id') and args.project_id:
        cmd.extend(['--project-id', args.project_id])
    
    return subprocess.run(cmd).returncode

def cmd_consistency(args):
    """Ejecuta el consistency checker."""
    cmd = [sys.executable, str(Path(__file__).parent / "consistency-checker.py")]
    
    # Agregar argumentos del proyecto si están disponibles
    if hasattr(args, 'project_id') and args.project_id:
        cmd.extend(['--project-id', args.project_id])
    
    return subprocess.run(cmd).returncode

def cmd_dashboard(args):
    """Inicia el dashboard web (local o servidor)."""
    if args.mode == 'local':
        ColoredOutput.info("Iniciando Dashboard Local...")
        ColoredOutput.warning("Dashboard Local aún no implementado")
        ColoredOutput.info("Próximamente: Svelte 5 + Tauri")
        return 1
    elif args.mode == 'server':
        ColoredOutput.info("Iniciando Dashboard Servidor...")
        ColoredOutput.warning("Dashboard Servidor aún no implementado")
        ColoredOutput.info("Próximamente: Svelte 5 + FastAPI")
        return 1
    else:
        ColoredOutput.error(f"Modo de dashboard desconocido: {args.mode}")
        return 1

def cmd_info(args):
    """Muestra información del sistema y proyecto actual."""
    pm = ProjectManager()
    
    ColoredOutput.header("The Mighty Task - Sistema Multi-Proyecto")
    ColoredOutput.info("Versión: 5.0.0")
    ColoredOutput.info("Arquitectura: Dual Dashboard (Local + Servidor)")
    ColoredOutput.info("")
    
    # Información del proyecto actual
    current_id = pm.get_current_project()
    if current_id:
        project_info = pm.get_project_info(current_id)
        if project_info:
            metadata = project_info["metadata"]
            project_path = Path(project_info["path"])
            
            ColoredOutput.section("Proyecto Actual")
            ColoredOutput.info(f"Nombre: {metadata['name']}")
            ColoredOutput.info(f"ID: {current_id}")
            ColoredOutput.info(f"Organización: {metadata['organization']}")
            ColoredOutput.info(f"Ruta: {project_path}")
            ColoredOutput.info(f"Estado: {'✅ Existe' if project_path.exists() else '❌ No encontrado'}")
            ColoredOutput.info(f"Creado: {metadata['created_at'][:19]}")
    else:
        ColoredOutput.section("Proyecto Actual")
        ColoredOutput.warning("No hay proyecto activo")
        ColoredOutput.info("Usa 'mighty-task project create' para crear uno nuevo")
        ColoredOutput.info("O 'mighty-task project list' para ver proyectos existentes")
    
    # Estadísticas generales
    projects = pm.list_projects()
    active_projects = [p for p in projects if p["exists"]]
    
    ColoredOutput.section("Estadísticas del Sistema")
    ColoredOutput.info(f"Proyectos registrados: {len(projects)}")
    ColoredOutput.info(f"Proyectos activos: {len(active_projects)}")
    
    # Módulos disponibles
    ColoredOutput.section("Módulos Disponibles")
    modules = [
        ("generate", "Generador de sesiones diarias"),
        ("resume", "Consolidador de sesiones (mission-resumer)"),
        ("status", "Monitor de estado del proyecto"),
        ("consistency", "Verificador de consistencia"),
        ("project", "Gestor de proyectos multi-instancia"),
        ("dashboard", "Interfaz web (local/servidor)")
    ]
    
    for module, description in modules:
        ColoredOutput.info(f"• {module}: {description}")

def main():
    """Función principal del CLI unificado."""
    parser = argparse.ArgumentParser(
        description="The Mighty Task - Sistema Multi-Proyecto v5.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Comandos principales:

  # Gestión de proyectos
  mighty-task project create --name "Mi API" --org "MiEmpresa"
  mighty-task project list
  mighty-task project switch MIEMPRESA-MI-API-20250826194500
  mighty-task project export --output mi-proyecto.mtp
  mighty-task project import proyecto.mtp

  # Trabajo diario
  mighty-task generate --theme "BACKEND-API-SETUP"
  mighty-task resume --output "SPRINT-01-SUMMARY"
  mighty-task status
  mighty-task consistency

  # Dashboard
  mighty-task dashboard --mode local
  mighty-task dashboard --mode server

  # Información
  mighty-task info

Arquitectura Dual:
- Dashboard Local: Gestión directa de archivos locales
- Dashboard Servidor: APIs centralizadas con multi-usuario
        """
    )
    
    # Argumentos globales
    parser.add_argument(
        '--project-id',
        type=str,
        help='ID del proyecto específico (usa proyecto actual si no se especifica)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Modo silencioso'
    )
    
    # Subcomandos
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')
    
    # Comando project (delega al project-manager.py)
    project_parser = subparsers.add_parser('project', help='Gestión de proyectos')
    project_parser.add_argument('project_args', nargs=argparse.REMAINDER, help='Argumentos para project-manager')
    project_parser.set_defaults(func=cmd_project)
    
    # Comando generate
    generate_parser = subparsers.add_parser('generate', help='Generar sesión diaria')
    generate_parser.add_argument('--theme', help='Tema de la sesión')
    generate_parser.add_argument('--template', choices=['development', 'operations', 'research'], 
                                default='development', help='Tipo de template')
    generate_parser.add_argument('--date', help='Fecha (YYYY-MM-DD)')
    generate_parser.add_argument('--force', action='store_true', help='Sobrescribir existente')
    generate_parser.set_defaults(func=cmd_generate)
    
    # Comando resume
    resume_parser = subparsers.add_parser('resume', help='Consolidar sesiones')
    resume_parser.add_argument('--output', help='Nombre del resumen')
    resume_parser.add_argument('--theme', help='Tema específico')
    resume_parser.add_argument('--sessions', help='Sesiones específicas (separadas por coma)')
    resume_parser.add_argument('--force', action='store_true', help='Sobrescribir existente')
    resume_parser.set_defaults(func=cmd_resume)
    
    # Comando status
    status_parser = subparsers.add_parser('status', help='Estado del proyecto')
    status_parser.set_defaults(func=cmd_status)
    
    # Comando consistency
    consistency_parser = subparsers.add_parser('consistency', help='Verificar consistencia')
    consistency_parser.set_defaults(func=cmd_consistency)
    
    # Comando dashboard
    dashboard_parser = subparsers.add_parser('dashboard', help='Iniciar dashboard web')
    dashboard_parser.add_argument('--mode', choices=['local', 'server'], default='local',
                                 help='Modo de dashboard')
    dashboard_parser.set_defaults(func=cmd_dashboard)
    
    # Comando info
    info_parser = subparsers.add_parser('info', help='Información del sistema')
    info_parser.set_defaults(func=cmd_info)
    
    # Parsear argumentos
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        return args.func(args)
    except KeyboardInterrupt:
        ColoredOutput.info("\nOperación cancelada por el usuario")
        return 1
    except Exception as e:
        ColoredOutput.error(f"Error inesperado: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
