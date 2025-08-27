"""
Project Manager - Multi-Project Support Module
============================================

Gestión de múltiples proyectos mighty-task con identificadores únicos,
metadatos y capacidades de export/import.
"""

import json
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import hashlib
import shutil
import zipfile
import tempfile
from .colored_output import ColoredOutput

class ProjectManager:
    """Gestor de proyectos múltiples con identificadores únicos."""
    
    def __init__(self, base_path: Optional[Path] = None):
        """
        Inicializa el gestor de proyectos.
        
        Args:
            base_path: Ruta base donde se encuentran los proyectos
        """
        self.base_path = base_path or Path(__file__).parent.parent.parent
        self.projects_registry = self.base_path / '.projects_registry.json'
        self.current_project_file = self.base_path / '.current_project'
        
    def generate_project_id(self, organization: str, project_name: str) -> str:
        """
        Genera un identificador único para el proyecto.
        
        Args:
            organization: Nombre de la organización
            project_name: Nombre del proyecto
            
        Returns:
            ID único en formato ORG-PROJECT-TIMESTAMP
        """
        # Limpiar nombres para usar solo caracteres válidos
        org_clean = ''.join(c.upper() for c in organization if c.isalnum())[:10]
        project_clean = ''.join(c.upper() for c in project_name if c.isalnum() or c in '-_')[:20]
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        
        return f"{org_clean}-{project_clean}-{timestamp}"
    
    def create_project_metadata(self, 
                              project_id: str,
                              name: str,
                              organization: str,
                              description: str = "",
                              tags: List[str] = None,
                              owner: str = "",
                              **kwargs) -> Dict:
        """
        Crea metadatos completos para un proyecto.
        
        Args:
            project_id: ID único del proyecto
            name: Nombre descriptivo del proyecto
            organization: Organización propietaria
            description: Descripción del proyecto
            tags: Lista de etiquetas
            owner: Propietario del proyecto
            **kwargs: Metadatos adicionales
            
        Returns:
            Dict con metadatos completos del proyecto
        """
        now = datetime.now().isoformat()
        
        metadata = {
            "project_id": project_id,
            "name": name,
            "organization": organization,
            "description": description,
            "created_at": now,
            "last_modified": now,
            "version": "1.0.0",
            "tags": tags or [],
            "owner": owner,
            "collaborators": [],
            "settings": {
                "default_template": "development",
                "auto_backup": True,
                "compression_level": 6,
                "export_format": "mtp"
            },
            "statistics": {
                "total_sessions": 0,
                "total_reports": 0,
                "total_mission_resumes": 0,
                "last_activity": now
            },
            "paths": {
                "daily_work": "daily-work",
                "mission_resumes": "mission-resumes", 
                "playbooks": "playbooks",
                "reports": "reports",
                "operational_guides": "operational-guides"
            }
        }
        
        # Agregar metadatos adicionales
        metadata.update(kwargs)
        
        return metadata
    
    def register_project(self, project_path: Path, metadata: Dict) -> bool:
        """
        Registra un nuevo proyecto en el registro global.
        
        Args:
            project_path: Ruta al directorio del proyecto
            metadata: Metadatos del proyecto
            
        Returns:
            True si se registró exitosamente
        """
        try:
            # Cargar registro existente
            registry = self.load_projects_registry()
            
            # Agregar nuevo proyecto
            registry["projects"][metadata["project_id"]] = {
                "metadata": metadata,
                "path": str(project_path.absolute()),
                "registered_at": datetime.now().isoformat(),
                "status": "active"
            }
            
            registry["last_updated"] = datetime.now().isoformat()
            registry["total_projects"] = len(registry["projects"])
            
            # Guardar registro actualizado
            return self.save_projects_registry(registry)
            
        except Exception as e:
            ColoredOutput.error(f"Error registrando proyecto: {e}")
            return False
    
    def load_projects_registry(self) -> Dict:
        """
        Carga el registro de proyectos.
        
        Returns:
            Dict con registro de proyectos
        """
        if not self.projects_registry.exists():
            return {
                "version": "1.0.0",
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "total_projects": 0,
                "projects": {}
            }
        
        try:
            with open(self.projects_registry, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            ColoredOutput.error(f"Error cargando registro de proyectos: {e}")
            return {"projects": {}}
    
    def save_projects_registry(self, registry: Dict) -> bool:
        """
        Guarda el registro de proyectos.
        
        Args:
            registry: Registro de proyectos a guardar
            
        Returns:
            True si se guardó exitosamente
        """
        try:
            with open(self.projects_registry, 'w', encoding='utf-8') as f:
                json.dump(registry, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            ColoredOutput.error(f"Error guardando registro de proyectos: {e}")
            return False
    
    def list_projects(self) -> List[Dict]:
        """
        Lista todos los proyectos registrados.
        
        Returns:
            Lista de proyectos con información básica
        """
        registry = self.load_projects_registry()
        projects = []
        
        for project_id, project_info in registry.get("projects", {}).items():
            metadata = project_info.get("metadata", {})
            project_path = Path(project_info.get("path", ""))
            
            projects.append({
                "project_id": project_id,
                "name": metadata.get("name", "Sin nombre"),
                "organization": metadata.get("organization", ""),
                "description": metadata.get("description", ""),
                "path": str(project_path),
                "exists": project_path.exists(),
                "created_at": metadata.get("created_at", ""),
                "last_modified": metadata.get("last_modified", ""),
                "status": project_info.get("status", "unknown"),
                "tags": metadata.get("tags", [])
            })
        
        return sorted(projects, key=lambda x: x["last_modified"], reverse=True)
    
    def get_current_project(self) -> Optional[str]:
        """
        Obtiene el ID del proyecto actualmente activo.
        
        Returns:
            ID del proyecto activo o None
        """
        try:
            if self.current_project_file.exists():
                return self.current_project_file.read_text(encoding='utf-8').strip()
        except Exception:
            pass
        return None
    
    def set_current_project(self, project_id: str) -> bool:
        """
        Establece el proyecto actualmente activo.
        
        Args:
            project_id: ID del proyecto a activar
            
        Returns:
            True si se estableció exitosamente
        """
        try:
            # Verificar que el proyecto existe
            registry = self.load_projects_registry()
            if project_id not in registry.get("projects", {}):
                ColoredOutput.error(f"Proyecto {project_id} no encontrado")
                return False
            
            # Guardar proyecto actual
            self.current_project_file.write_text(project_id, encoding='utf-8')
            ColoredOutput.success(f"Proyecto activo: {project_id}")
            return True
            
        except Exception as e:
            ColoredOutput.error(f"Error estableciendo proyecto actual: {e}")
            return False
    
    def get_project_info(self, project_id: str) -> Optional[Dict]:
        """
        Obtiene información completa de un proyecto.
        
        Args:
            project_id: ID del proyecto
            
        Returns:
            Dict con información completa del proyecto o None
        """
        registry = self.load_projects_registry()
        return registry.get("projects", {}).get(project_id)
    
    def update_project_metadata(self, project_id: str, updates: Dict) -> bool:
        """
        Actualiza metadatos de un proyecto.
        
        Args:
            project_id: ID del proyecto
            updates: Diccionario con actualizaciones
            
        Returns:
            True si se actualizó exitosamente
        """
        try:
            registry = self.load_projects_registry()
            
            if project_id not in registry.get("projects", {}):
                ColoredOutput.error(f"Proyecto {project_id} no encontrado")
                return False
            
            # Actualizar metadatos
            metadata = registry["projects"][project_id]["metadata"]
            metadata.update(updates)
            metadata["last_modified"] = datetime.now().isoformat()
            
            # Guardar cambios
            return self.save_projects_registry(registry)
            
        except Exception as e:
            ColoredOutput.error(f"Error actualizando proyecto: {e}")
            return False
    
    def delete_project(self, project_id: str, delete_files: bool = False) -> bool:
        """
        Elimina un proyecto del registro.
        
        Args:
            project_id: ID del proyecto
            delete_files: Si eliminar también los archivos del proyecto
            
        Returns:
            True si se eliminó exitosamente
        """
        try:
            registry = self.load_projects_registry()
            
            if project_id not in registry.get("projects", {}):
                ColoredOutput.error(f"Proyecto {project_id} no encontrado")
                return False
            
            project_info = registry["projects"][project_id]
            
            # Eliminar archivos si se solicita
            if delete_files:
                project_path = Path(project_info["path"])
                if project_path.exists():
                    shutil.rmtree(project_path)
                    ColoredOutput.info(f"Archivos del proyecto eliminados: {project_path}")
            
            # Remover del registro
            del registry["projects"][project_id]
            registry["total_projects"] = len(registry["projects"])
            registry["last_updated"] = datetime.now().isoformat()
            
            # Si era el proyecto actual, limpiar
            if self.get_current_project() == project_id:
                self.current_project_file.unlink(missing_ok=True)
            
            return self.save_projects_registry(registry)
            
        except Exception as e:
            ColoredOutput.error(f"Error eliminando proyecto: {e}")
            return False
    
    def validate_project_structure(self, project_path: Path) -> Dict:
        """
        Valida que un directorio tenga la estructura de proyecto mighty-task.
        
        Args:
            project_path: Ruta al directorio del proyecto
            
        Returns:
            Dict con resultado de validación
        """
        validation = {
            "valid": True,
            "issues": [],
            "structure": {},
            "missing_dirs": [],
            "missing_files": []
        }
        
        # Directorios requeridos
        required_dirs = [
            "scripts",
            "playbooks", 
            "daily-work",
            "mission-resumes",
            "reports",
            "guides"
        ]
        
        # Archivos requeridos
        required_files = [
            "template-pendingtask.md",
            "README.md"
        ]
        
        # Verificar directorios
        for dir_name in required_dirs:
            dir_path = project_path / dir_name
            exists = dir_path.exists() and dir_path.is_dir()
            validation["structure"][dir_name] = exists
            
            if not exists:
                validation["valid"] = False
                validation["missing_dirs"].append(dir_name)
        
        # Verificar archivos
        for file_name in required_files:
            file_path = project_path / file_name
            exists = file_path.exists() and file_path.is_file()
            validation["structure"][file_name] = exists
            
            if not exists:
                validation["valid"] = False
                validation["missing_files"].append(file_name)
        
        # Verificar scripts específicos
        scripts_dir = project_path / "scripts"
        if scripts_dir.exists():
            required_scripts = [
                "generate-daily.py",
                "mission-resumer.py",
                "status-checker.py"
            ]
            
            for script in required_scripts:
                script_path = scripts_dir / script
                if not script_path.exists():
                    validation["valid"] = False
                    validation["issues"].append(f"Script faltante: {script}")
        
        return validation
    
    def create_project_structure(self, project_path: Path) -> bool:
        """
        Crea la estructura básica de un proyecto mighty-task.
        
        Args:
            project_path: Ruta donde crear el proyecto
            
        Returns:
            True si se creó exitosamente
        """
        try:
            # Crear directorios
            directories = [
                "scripts/shared",
                "scripts/generate_daily", 
                "scripts/mission_resumer",
                "scripts/status_checker",
                "scripts/consistency_checker",
                "playbooks/documentation_playbooks",
                "daily-work",
                "mission-resumes",
                "reports",
                "guides",
                "operational-guides"
            ]
            
            for dir_path in directories:
                (project_path / dir_path).mkdir(parents=True, exist_ok=True)
            
            # Copiar archivos base desde template
            template_path = self.base_path
            base_files = [
                "template-pendingtask.md",
                "template-operations.md", 
                "template-web-research.md"
            ]
            
            for file_name in base_files:
                src = template_path / file_name
                dst = project_path / file_name
                if src.exists():
                    shutil.copy2(src, dst)
            
            # Copiar scripts
            scripts_src = template_path / "scripts"
            scripts_dst = project_path / "scripts"
            
            if scripts_src.exists():
                shutil.copytree(scripts_src, scripts_dst, dirs_exist_ok=True)
            
            # Crear README básico
            readme_content = f"""# Mighty Task Project

Proyecto creado el {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Estructura del Proyecto

- `daily-work/` - Sesiones de trabajo diarias
- `mission-resumes/` - Consolidaciones de sesiones
- `playbooks/` - Templates universales
- `reports/` - Reportes generados
- `scripts/` - Scripts del sistema

## Comandos Básicos

```bash
# Crear nueva sesión
python3 scripts/generate-daily.py --theme="MI-TEMA"

# Consolidar sesiones
python3 scripts/mission-resumer.py --theme="MI-TEMA"

# Ver estado del sistema
python3 scripts/status-checker.py
```
"""
            
            (project_path / "README.md").write_text(readme_content, encoding='utf-8')
            
            ColoredOutput.success(f"Estructura de proyecto creada en: {project_path}")
            return True
            
        except Exception as e:
            ColoredOutput.error(f"Error creando estructura de proyecto: {e}")
            return False
