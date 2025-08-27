#!/usr/bin/env python3
"""
Project Manager CLI - Multi-Project Management Tool
==================================================

Herramienta CLI para gestionar múltiples proyectos mighty-task con
identificadores únicos, export/import y switching entre proyectos.
"""

import sys
import argparse
from pathlib import Path

# Agregar el directorio scripts al path para imports
sys.path.insert(0, str(Path(__file__).parent))

from shared.project_manager import ProjectManager
from shared.colored_output import ColoredOutput
from shared.export_import import ProjectExporter, ProjectImporter

def create_project(args):
    """Crea un nuevo proyecto mighty-task."""
    pm = ProjectManager()
    
    # Generar ID único
    project_id = pm.generate_project_id(args.organization, args.name)
    
    # Crear metadatos
    metadata = pm.create_project_metadata(
        project_id=project_id,
        name=args.name,
        organization=args.organization,
        description=args.description or "",
        tags=args.tags.split(',') if args.tags else [],
        owner=args.owner or ""
    )
    
    # Determinar ruta del proyecto
    if args.path:
        project_path = Path(args.path).resolve()
    else:
        project_path = Path.cwd() / f"mighty-task-{args.name.lower().replace(' ', '-')}"
    
    # Crear estructura del proyecto
    if pm.create_project_structure(project_path):
        # Guardar metadatos en el proyecto
        metadata_file = project_path / '.project_metadata.json'
        import json
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        # Registrar proyecto
        if pm.register_project(project_path, metadata):
            # Establecer como proyecto actual
            pm.set_current_project(project_id)
            
            ColoredOutput.success(f"Proyecto creado exitosamente:")
            ColoredOutput.info(f"  ID: {project_id}")
            ColoredOutput.info(f"  Nombre: {args.name}")
            ColoredOutput.info(f"  Ruta: {project_path}")
            ColoredOutput.info(f"  Organización: {args.organization}")
        else:
            ColoredOutput.error("Error registrando el proyecto")
    else:
        ColoredOutput.error("Error creando la estructura del proyecto")

def list_projects(args):
    """Lista todos los proyectos registrados."""
    pm = ProjectManager()
    projects = pm.list_projects()
    current_project = pm.get_current_project()
    
    if not projects:
        ColoredOutput.info("No hay proyectos registrados")
        return
    
    ColoredOutput.info(f"Proyectos registrados ({len(projects)}):")
    ColoredOutput.info("=" * 60)
    
    for project in projects:
        status_icon = "✅" if project["exists"] else "❌"
        current_icon = "👉" if project["project_id"] == current_project else "  "
        
        ColoredOutput.info(f"{current_icon} {status_icon} {project['name']}")
        ColoredOutput.info(f"     ID: {project['project_id']}")
        ColoredOutput.info(f"     Org: {project['organization']}")
        ColoredOutput.info(f"     Ruta: {project['path']}")
        
        if project["description"]:
            ColoredOutput.info(f"     Desc: {project['description']}")
        
        if project["tags"]:
            ColoredOutput.info(f"     Tags: {', '.join(project['tags'])}")
        
        ColoredOutput.info(f"     Creado: {project['created_at'][:19]}")
        ColoredOutput.info("")

def switch_project(args):
    """Cambia al proyecto especificado."""
    pm = ProjectManager()
    
    if pm.set_current_project(args.project_id):
        project_info = pm.get_project_info(args.project_id)
        if project_info:
            metadata = project_info["metadata"]
            ColoredOutput.success(f"Proyecto activo cambiado a: {metadata['name']}")
            ColoredOutput.info(f"Ruta: {project_info['path']}")
    else:
        ColoredOutput.error(f"No se pudo cambiar al proyecto: {args.project_id}")

def show_current(args):
    """Muestra información del proyecto actual."""
    pm = ProjectManager()
    current_id = pm.get_current_project()
    
    if not current_id:
        ColoredOutput.info("No hay proyecto activo")
        return
    
    project_info = pm.get_project_info(current_id)
    if not project_info:
        ColoredOutput.error(f"Proyecto actual {current_id} no encontrado")
        return
    
    metadata = project_info["metadata"]
    project_path = Path(project_info["path"])
    
    ColoredOutput.success("Proyecto Actual:")
    ColoredOutput.info(f"  ID: {current_id}")
    ColoredOutput.info(f"  Nombre: {metadata['name']}")
    ColoredOutput.info(f"  Organización: {metadata['organization']}")
    ColoredOutput.info(f"  Ruta: {project_path}")
    ColoredOutput.info(f"  Existe: {'✅' if project_path.exists() else '❌'}")
    ColoredOutput.info(f"  Creado: {metadata['created_at'][:19]}")
    ColoredOutput.info(f"  Modificado: {metadata['last_modified'][:19]}")
    
    if metadata.get("description"):
        ColoredOutput.info(f"  Descripción: {metadata['description']}")
    
    if metadata.get("tags"):
        ColoredOutput.info(f"  Tags: {', '.join(metadata['tags'])}")

def export_project(args):
    """Exporta un proyecto a formato .mtp."""
    pm = ProjectManager()
    
    # Determinar proyecto a exportar
    if args.project_id:
        project_info = pm.get_project_info(args.project_id)
        if not project_info:
            ColoredOutput.error(f"Proyecto {args.project_id} no encontrado")
            return
        project_path = Path(project_info["path"])
    else:
        # Usar proyecto actual
        current_id = pm.get_current_project()
        if not current_id:
            ColoredOutput.error("No hay proyecto activo. Especifica --project-id")
            return
        project_info = pm.get_project_info(current_id)
        project_path = Path(project_info["path"])
    
    if not project_path.exists():
        ColoredOutput.error(f"Ruta del proyecto no existe: {project_path}")
        return
    
    # Determinar archivo de salida
    if args.output:
        output_path = args.output
    else:
        project_name = project_info["metadata"]["name"].lower().replace(' ', '-')
        output_path = f"{project_name}-export.mtp"
    
    # Exportar proyecto
    exporter = ProjectExporter(project_path)
    if exporter.export_project(output_path, args.compression):
        ColoredOutput.success(f"Proyecto exportado: {output_path}")
    else:
        ColoredOutput.error("Error durante la exportación")

def import_project(args):
    """Importa un proyecto desde formato .mtp."""
    mtp_file = Path(args.mtp_file)
    
    if not mtp_file.exists():
        ColoredOutput.error(f"Archivo .mtp no encontrado: {mtp_file}")
        return
    
    # Determinar directorio de destino
    if args.target_path:
        target_path = Path(args.target_path)
    else:
        # Usar nombre base del archivo
        project_name = mtp_file.stem.replace('-export', '')
        target_path = Path.cwd() / f"imported-{project_name}"
    
    # Importar proyecto
    importer = ProjectImporter(target_path)
    if importer.import_project(mtp_file, args.merge_mode, args.backup):
        ColoredOutput.success(f"Proyecto importado en: {target_path}")
        
        # Registrar proyecto importado si tiene metadatos
        metadata_file = target_path / '.project_metadata.json'
        if metadata_file.exists():
            import json
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            pm = ProjectManager()
            if pm.register_project(target_path, metadata):
                ColoredOutput.info(f"Proyecto registrado con ID: {metadata['project_id']}")
    else:
        ColoredOutput.error("Error durante la importación")

def delete_project(args):
    """Elimina un proyecto del registro."""
    pm = ProjectManager()
    
    project_info = pm.get_project_info(args.project_id)
    if not project_info:
        ColoredOutput.error(f"Proyecto {args.project_id} no encontrado")
        return
    
    project_name = project_info["metadata"]["name"]
    
    # Confirmación
    if not args.force:
        response = input(f"¿Eliminar proyecto '{project_name}' ({args.project_id})? [y/N]: ")
        if response.lower() != 'y':
            ColoredOutput.info("Operación cancelada")
            return
    
    if pm.delete_project(args.project_id, args.delete_files):
        ColoredOutput.success(f"Proyecto eliminado: {project_name}")
        if args.delete_files:
            ColoredOutput.info("Archivos del proyecto también eliminados")
    else:
        ColoredOutput.error("Error eliminando el proyecto")

def main():
    """Función principal del CLI."""
    parser = argparse.ArgumentParser(
        description="Gestor de proyectos mighty-task multi-proyecto",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Crear nuevo proyecto
  python3 project-manager.py create --name "Mi API Backend" --org "MiEmpresa"
  
  # Listar proyectos
  python3 project-manager.py list
  
  # Cambiar proyecto activo
  python3 project-manager.py switch MIEMPRESA-MI-API-BACKEND-20250826194500
  
  # Exportar proyecto actual
  python3 project-manager.py export --output mi-proyecto.mtp
  
  # Importar proyecto
  python3 project-manager.py import proyecto-backup.mtp --target-path ./nuevo-proyecto
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comandos disponibles')
    
    # Comando create
    create_parser = subparsers.add_parser('create', help='Crear nuevo proyecto')
    create_parser.add_argument('--name', required=True, help='Nombre del proyecto')
    create_parser.add_argument('--org', '--organization', required=True, dest='organization', help='Organización')
    create_parser.add_argument('--description', help='Descripción del proyecto')
    create_parser.add_argument('--tags', help='Tags separados por comas')
    create_parser.add_argument('--owner', help='Propietario del proyecto')
    create_parser.add_argument('--path', help='Ruta donde crear el proyecto')
    create_parser.set_defaults(func=create_project)
    
    # Comando list
    list_parser = subparsers.add_parser('list', help='Listar proyectos registrados')
    list_parser.set_defaults(func=list_projects)
    
    # Comando switch
    switch_parser = subparsers.add_parser('switch', help='Cambiar proyecto activo')
    switch_parser.add_argument('project_id', help='ID del proyecto')
    switch_parser.set_defaults(func=switch_project)
    
    # Comando current
    current_parser = subparsers.add_parser('current', help='Mostrar proyecto actual')
    current_parser.set_defaults(func=show_current)
    
    # Comando export
    export_parser = subparsers.add_parser('export', help='Exportar proyecto a .mtp')
    export_parser.add_argument('--project-id', help='ID del proyecto (usa actual si no se especifica)')
    export_parser.add_argument('--output', help='Archivo de salida .mtp')
    export_parser.add_argument('--compression', type=int, default=6, choices=range(0, 10), 
                              help='Nivel de compresión (0-9)')
    export_parser.set_defaults(func=export_project)
    
    # Comando import
    import_parser = subparsers.add_parser('import', help='Importar proyecto desde .mtp')
    import_parser.add_argument('mtp_file', help='Archivo .mtp a importar')
    import_parser.add_argument('--target-path', help='Directorio de destino')
    import_parser.add_argument('--merge-mode', choices=['skip', 'overwrite', 'merge'], 
                              default='skip', help='Modo de fusión')
    import_parser.add_argument('--no-backup', dest='backup', action='store_false', 
                              help='No crear backup antes de importar')
    import_parser.set_defaults(func=import_project)
    
    # Comando delete
    delete_parser = subparsers.add_parser('delete', help='Eliminar proyecto')
    delete_parser.add_argument('project_id', help='ID del proyecto')
    delete_parser.add_argument('--delete-files', action='store_true', 
                              help='Eliminar también archivos del proyecto')
    delete_parser.add_argument('--force', action='store_true', 
                              help='No pedir confirmación')
    delete_parser.set_defaults(func=delete_project)
    
    # Parsear argumentos
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        args.func(args)
    except KeyboardInterrupt:
        ColoredOutput.info("\nOperación cancelada por el usuario")
    except Exception as e:
        ColoredOutput.error(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
