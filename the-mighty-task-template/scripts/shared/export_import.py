"""
Export/Import System - Mighty Task Package (.mtp) Format
======================================================

Sistema de exportación e importación de proyectos completos mighty-task
usando formato comprimido .mtp (Mighty Task Package).
"""

import json
import zipfile
import hashlib
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from .colored_output import ColoredOutput
from .project_manager import ProjectManager

class ProjectExporter:
    """Exportador de proyectos mighty-task a formato .mtp."""
    
    def __init__(self, project_path: Path):
        """
        Inicializa el exportador.
        
        Args:
            project_path: Ruta al proyecto a exportar
        """
        self.project_path = Path(project_path)
        self.project_manager = ProjectManager()
        
    def export_project(self, output_path: str, compression_level: int = 6) -> bool:
        """
        Exporta el proyecto completo a un archivo .mtp.
        
        Args:
            output_path: Ruta donde guardar el archivo .mtp
            compression_level: Nivel de compresión (0-9)
            
        Returns:
            True si se exportó exitosamente
        """
        try:
            ColoredOutput.info(f"Iniciando exportación de proyecto: {self.project_path}")
            
            # Validar estructura del proyecto
            validation = self.project_manager.validate_project_structure(self.project_path)
            if not validation["valid"]:
                ColoredOutput.warning("Proyecto tiene estructura incompleta, continuando...")
                for issue in validation["issues"]:
                    ColoredOutput.warning(f"  - {issue}")
            
            # Generar manifest del export
            manifest = self.generate_export_manifest()
            
            # Crear archivo .mtp
            output_file = Path(output_path)
            if not output_file.suffix:
                output_file = output_file.with_suffix('.mtp')
            
            with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED, 
                               compresslevel=compression_level) as zf:
                
                # Agregar manifest
                zf.writestr('export-manifest.json', 
                           json.dumps(manifest, indent=2, ensure_ascii=False))
                
                # Agregar metadatos del proyecto si existen
                metadata_file = self.project_path / '.project_metadata.json'
                if metadata_file.exists():
                    zf.write(metadata_file, 'project-metadata.json')
                
                # Exportar directorios principales
                directories_to_export = [
                    'daily-work',
                    'mission-resumes', 
                    'playbooks',
                    'reports',
                    'operational-guides',
                    'guides'
                ]
                
                for dir_name in directories_to_export:
                    dir_path = self.project_path / dir_name
                    if dir_path.exists():
                        self._add_directory_to_zip(zf, dir_path, dir_name)
                
                # Exportar archivos de configuración
                config_files = [
                    'template-pendingtask.md',
                    'template-operations.md',
                    'template-web-research.md',
                    'template-pendingtask-operations-modular.md',
                    'README.md'
                ]
                
                for file_name in config_files:
                    file_path = self.project_path / file_name
                    if file_path.exists():
                        zf.write(file_path, file_name)
                
                # Exportar configuraciones de scripts
                scripts_config_dir = self.project_path / 'scripts' / 'config'
                if scripts_config_dir.exists():
                    self._add_directory_to_zip(zf, scripts_config_dir, 'scripts/config')
                
                # Exportar archivos de tracking
                tracking_files = ['.tracking.json', '.projects_registry.json', '.current_project']
                for file_name in tracking_files:
                    file_path = self.project_path / file_name
                    if file_path.exists():
                        zf.write(file_path, f'tracking/{file_name}')
            
            # Verificar integridad del archivo creado
            if self.verify_export_integrity(output_file, manifest):
                ColoredOutput.success(f"Proyecto exportado exitosamente: {output_file}")
                ColoredOutput.info(f"Tamaño del archivo: {output_file.stat().st_size / 1024 / 1024:.2f} MB")
                return True
            else:
                ColoredOutput.error("Error en la verificación de integridad del export")
                return False
                
        except Exception as e:
            ColoredOutput.error(f"Error exportando proyecto: {e}")
            return False
    
    def generate_export_manifest(self) -> Dict:
        """
        Genera el manifest del export con inventario completo.
        
        Returns:
            Dict con manifest del export
        """
        manifest = {
            "export_date": datetime.now().isoformat(),
            "export_version": "1.0.0",
            "mighty_task_version": "5.0.0",
            "project_path": str(self.project_path),
            "contents": {},
            "statistics": {
                "total_files": 0,
                "total_size_bytes": 0,
                "directories_count": 0
            },
            "compatibility": {
                "min_mighty_task_version": "5.0.0",
                "python_version": "3.8+",
                "required_modules": ["pathlib", "json", "datetime", "hashlib"]
            },
            "checksums": {}
        }
        
        # Analizar contenido de cada directorio
        directories = [
            'daily-work', 'mission-resumes', 'playbooks', 
            'reports', 'operational-guides', 'guides'
        ]
        
        for dir_name in directories:
            dir_path = self.project_path / dir_name
            if dir_path.exists():
                dir_info = self._analyze_directory(dir_path)
                manifest["contents"][dir_name] = dir_info
                manifest["statistics"]["total_files"] += dir_info["files_count"]
                manifest["statistics"]["total_size_bytes"] += dir_info["total_size"]
                manifest["statistics"]["directories_count"] += 1
        
        # Generar checksum del proyecto completo
        manifest["checksums"]["project_hash"] = self._calculate_project_hash()
        
        return manifest
    
    def _analyze_directory(self, dir_path: Path) -> Dict:
        """
        Analiza el contenido de un directorio.
        
        Args:
            dir_path: Ruta al directorio
            
        Returns:
            Dict con información del directorio
        """
        info = {
            "files_count": 0,
            "total_size": 0,
            "file_types": {},
            "last_modified": None,
            "files": []
        }
        
        try:
            for file_path in dir_path.rglob('*'):
                if file_path.is_file():
                    file_stat = file_path.stat()
                    file_size = file_stat.st_size
                    file_ext = file_path.suffix.lower()
                    
                    info["files_count"] += 1
                    info["total_size"] += file_size
                    
                    # Contar tipos de archivo
                    if file_ext in info["file_types"]:
                        info["file_types"][file_ext] += 1
                    else:
                        info["file_types"][file_ext] = 1
                    
                    # Actualizar última modificación
                    file_mtime = datetime.fromtimestamp(file_stat.st_mtime).isoformat()
                    if not info["last_modified"] or file_mtime > info["last_modified"]:
                        info["last_modified"] = file_mtime
                    
                    # Agregar información del archivo
                    relative_path = file_path.relative_to(dir_path)
                    info["files"].append({
                        "path": str(relative_path),
                        "size": file_size,
                        "modified": file_mtime,
                        "type": file_ext
                    })
        
        except Exception as e:
            ColoredOutput.warning(f"Error analizando directorio {dir_path}: {e}")
        
        return info
    
    def _add_directory_to_zip(self, zf: zipfile.ZipFile, dir_path: Path, archive_name: str):
        """
        Agrega un directorio completo al archivo ZIP.
        
        Args:
            zf: Objeto ZipFile
            dir_path: Ruta al directorio
            archive_name: Nombre en el archivo
        """
        for file_path in dir_path.rglob('*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(dir_path)
                archive_path = f"{archive_name}/{relative_path}"
                zf.write(file_path, archive_path)
    
    def _calculate_project_hash(self) -> str:
        """
        Calcula hash SHA256 del proyecto completo.
        
        Returns:
            Hash SHA256 en hexadecimal
        """
        hasher = hashlib.sha256()
        
        # Incluir archivos principales en orden determinístico
        for file_path in sorted(self.project_path.rglob('*')):
            if file_path.is_file() and not file_path.name.startswith('.'):
                try:
                    with open(file_path, 'rb') as f:
                        hasher.update(f.read())
                except Exception:
                    # Ignorar archivos que no se pueden leer
                    pass
        
        return hasher.hexdigest()
    
    def verify_export_integrity(self, export_file: Path, manifest: Dict) -> bool:
        """
        Verifica la integridad del archivo exportado.
        
        Args:
            export_file: Ruta al archivo .mtp
            manifest: Manifest original
            
        Returns:
            True si la integridad es correcta
        """
        try:
            with zipfile.ZipFile(export_file, 'r') as zf:
                # Verificar que el manifest existe
                if 'export-manifest.json' not in zf.namelist():
                    return False
                
                # Leer manifest del archivo
                manifest_content = zf.read('export-manifest.json')
                archived_manifest = json.loads(manifest_content.decode('utf-8'))
                
                # Verificar versiones compatibles
                if archived_manifest.get("export_version") != manifest.get("export_version"):
                    return False
                
                # Verificar que todos los archivos esperados están presentes
                expected_files = set()
                for dir_name, dir_info in manifest["contents"].items():
                    for file_info in dir_info["files"]:
                        expected_files.add(f"{dir_name}/{file_info['path']}")
                
                archived_files = set(zf.namelist())
                missing_files = expected_files - archived_files
                
                if missing_files:
                    ColoredOutput.warning(f"Archivos faltantes en export: {missing_files}")
                    return False
                
                return True
                
        except Exception as e:
            ColoredOutput.error(f"Error verificando integridad: {e}")
            return False


class ProjectImporter:
    """Importador de proyectos desde formato .mtp."""
    
    def __init__(self, target_path: Path):
        """
        Inicializa el importador.
        
        Args:
            target_path: Ruta donde importar el proyecto
        """
        self.target_path = Path(target_path)
        self.project_manager = ProjectManager()
    
    def import_project(self, mtp_file: Path, 
                      merge_mode: str = "skip", 
                      create_backup: bool = True) -> bool:
        """
        Importa un proyecto desde archivo .mtp.
        
        Args:
            mtp_file: Ruta al archivo .mtp
            merge_mode: Modo de fusión ("skip", "overwrite", "merge")
            create_backup: Si crear backup antes de importar
            
        Returns:
            True si se importó exitosamente
        """
        try:
            ColoredOutput.info(f"Iniciando importación desde: {mtp_file}")
            
            # Validar archivo .mtp
            if not self.validate_mtp_file(mtp_file):
                ColoredOutput.error("Archivo .mtp inválido")
                return False
            
            # Crear backup si se solicita
            if create_backup and self.target_path.exists():
                backup_path = self._create_backup()
                ColoredOutput.info(f"Backup creado en: {backup_path}")
            
            # Extraer archivo .mtp
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                
                # Extraer contenido
                with zipfile.ZipFile(mtp_file, 'r') as zf:
                    zf.extractall(temp_path)
                
                # Leer manifest
                manifest_file = temp_path / 'export-manifest.json'
                with open(manifest_file, 'r', encoding='utf-8') as f:
                    manifest = json.load(f)
                
                # Verificar compatibilidad
                if not self.verify_compatibility(manifest):
                    ColoredOutput.error("Proyecto incompatible con esta versión")
                    return False
                
                # Crear estructura de destino
                self.target_path.mkdir(parents=True, exist_ok=True)
                
                # Importar contenido según modo de fusión
                success = self._import_content(temp_path, manifest, merge_mode)
                
                if success:
                    # Importar metadatos del proyecto
                    self._import_project_metadata(temp_path)
                    
                    ColoredOutput.success(f"Proyecto importado exitosamente en: {self.target_path}")
                    return True
                else:
                    ColoredOutput.error("Error durante la importación")
                    return False
                    
        except Exception as e:
            ColoredOutput.error(f"Error importando proyecto: {e}")
            return False
    
    def validate_mtp_file(self, mtp_file: Path) -> bool:
        """
        Valida que el archivo .mtp sea válido.
        
        Args:
            mtp_file: Ruta al archivo .mtp
            
        Returns:
            True si es válido
        """
        try:
            if not mtp_file.exists() or mtp_file.suffix != '.mtp':
                return False
            
            with zipfile.ZipFile(mtp_file, 'r') as zf:
                # Verificar que tiene manifest
                if 'export-manifest.json' not in zf.namelist():
                    return False
                
                # Verificar que el manifest es válido JSON
                manifest_content = zf.read('export-manifest.json')
                manifest = json.loads(manifest_content.decode('utf-8'))
                
                # Verificar campos requeridos
                required_fields = ['export_date', 'export_version', 'contents']
                for field in required_fields:
                    if field not in manifest:
                        return False
                
                return True
                
        except Exception:
            return False
    
    def verify_compatibility(self, manifest: Dict) -> bool:
        """
        Verifica compatibilidad del proyecto a importar.
        
        Args:
            manifest: Manifest del proyecto
            
        Returns:
            True si es compatible
        """
        try:
            # Verificar versión mínima requerida
            min_version = manifest.get("compatibility", {}).get("min_mighty_task_version", "1.0.0")
            current_version = "5.0.0"  # Versión actual del sistema
            
            # Comparación simple de versiones (mejorar si es necesario)
            if min_version > current_version:
                ColoredOutput.error(f"Requiere versión {min_version}, actual: {current_version}")
                return False
            
            return True
            
        except Exception:
            return False
    
    def _import_content(self, source_path: Path, manifest: Dict, merge_mode: str) -> bool:
        """
        Importa el contenido del proyecto.
        
        Args:
            source_path: Ruta temporal con contenido extraído
            manifest: Manifest del proyecto
            merge_mode: Modo de fusión
            
        Returns:
            True si se importó exitosamente
        """
        try:
            # Importar directorios principales
            for dir_name in manifest.get("contents", {}):
                source_dir = source_path / dir_name
                target_dir = self.target_path / dir_name
                
                if source_dir.exists():
                    if merge_mode == "overwrite" and target_dir.exists():
                        shutil.rmtree(target_dir)
                    
                    if not target_dir.exists():
                        shutil.copytree(source_dir, target_dir)
                    elif merge_mode == "merge":
                        self._merge_directories(source_dir, target_dir)
                    # Si es "skip", no hacer nada si ya existe
            
            # Importar archivos de configuración
            config_files = [
                'template-pendingtask.md',
                'template-operations.md',
                'template-web-research.md',
                'README.md'
            ]
            
            for file_name in config_files:
                source_file = source_path / file_name
                target_file = self.target_path / file_name
                
                if source_file.exists():
                    if not target_file.exists() or merge_mode == "overwrite":
                        shutil.copy2(source_file, target_file)
            
            # Importar configuraciones de tracking
            tracking_dir = source_path / 'tracking'
            if tracking_dir.exists():
                for tracking_file in tracking_dir.iterdir():
                    if tracking_file.is_file():
                        target_file = self.target_path / tracking_file.name
                        if merge_mode == "overwrite" or not target_file.exists():
                            shutil.copy2(tracking_file, target_file)
            
            return True
            
        except Exception as e:
            ColoredOutput.error(f"Error importando contenido: {e}")
            return False
    
    def _merge_directories(self, source_dir: Path, target_dir: Path):
        """
        Fusiona dos directorios manteniendo archivos existentes.
        
        Args:
            source_dir: Directorio fuente
            target_dir: Directorio destino
        """
        for item in source_dir.rglob('*'):
            if item.is_file():
                relative_path = item.relative_to(source_dir)
                target_file = target_dir / relative_path
                
                # Crear directorio padre si no existe
                target_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Copiar solo si no existe
                if not target_file.exists():
                    shutil.copy2(item, target_file)
    
    def _import_project_metadata(self, source_path: Path):
        """
        Importa metadatos del proyecto si existen.
        
        Args:
            source_path: Ruta temporal con contenido extraído
        """
        metadata_file = source_path / 'project-metadata.json'
        if metadata_file.exists():
            target_metadata = self.target_path / '.project_metadata.json'
            shutil.copy2(metadata_file, target_metadata)
    
    def _create_backup(self) -> Path:
        """
        Crea backup del proyecto existente.
        
        Returns:
            Ruta al backup creado
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{self.target_path.name}_backup_{timestamp}"
        backup_path = self.target_path.parent / backup_name
        
        shutil.copytree(self.target_path, backup_path)
        return backup_path
