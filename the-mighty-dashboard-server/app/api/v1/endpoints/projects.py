"""
API endpoints para gestión de proyectos
======================================

Endpoints para CRUD de proyectos, export/import, y operaciones multi-proyecto.
"""

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from typing import List, Optional
from pydantic import BaseModel
from app.core.auth import get_current_user, TokenData
import asyncio
import subprocess
from pathlib import Path

router = APIRouter()

class ProjectCreate(BaseModel):
    name: str
    organization: str
    description: Optional[str] = None
    tags: List[str] = []

class ProjectResponse(BaseModel):
    id: str
    name: str
    organization: str
    description: Optional[str]
    tags: List[str]
    path: str
    exists: bool
    created_at: str
    owner_id: str

class ProjectStats(BaseModel):
    total_sessions: int
    completed_missions: int
    last_activity: Optional[str]
    size_mb: float

@router.get("/", response_model=List[ProjectResponse])
async def list_projects(
    current_user: TokenData = Depends(get_current_user)
):
    """Lista todos los proyectos del usuario."""
    # Implementación usando mighty-task CLI
    try:
        result = await asyncio.create_subprocess_exec(
            "python3", "../the-mighty-task-template/scripts/mighty-task.py", "project", "list",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        
        # Parsear salida y filtrar por usuario
        # Por ahora devolvemos mock data
        return [
            ProjectResponse(
                id="TESTORG-DEMOAPIPROJECT-20250826200936",
                name="Demo API Project",
                organization="TestOrg",
                description="Proyecto de demostración",
                tags=["demo", "api"],
                path="/projects/demo-api",
                exists=True,
                created_at="2025-08-26T20:09:36",
                owner_id=current_user.user_id
            )
        ]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error listando proyectos: {str(e)}"
        )

@router.post("/", response_model=ProjectResponse)
async def create_project(
    project: ProjectCreate,
    current_user: TokenData = Depends(get_current_user)
):
    """Crea un nuevo proyecto."""
    try:
        result = await asyncio.create_subprocess_exec(
            "python3", "../the-mighty-task-template/scripts/mighty-task.py", 
            "project", "create",
            "--name", project.name,
            "--org", project.organization,
            "--description", project.description or "",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error creando proyecto: {stderr.decode()}"
            )
        
        # Parsear salida para obtener ID del proyecto
        # Por ahora devolvemos mock data
        return ProjectResponse(
            id="NEWORG-NEWPROJECT-20250826203500",
            name=project.name,
            organization=project.organization,
            description=project.description,
            tags=project.tags,
            path=f"/projects/{project.name.lower().replace(' ', '-')}",
            exists=True,
            created_at="2025-08-26T20:35:00",
            owner_id=current_user.user_id
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creando proyecto: {str(e)}"
        )

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: str,
    current_user: TokenData = Depends(get_current_user)
):
    """Obtiene información de un proyecto específico."""
    # Implementar obtención de proyecto
    return ProjectResponse(
        id=project_id,
        name="Demo Project",
        organization="TestOrg",
        description="Proyecto de demostración",
        tags=["demo"],
        path=f"/projects/{project_id}",
        exists=True,
        created_at="2025-08-26T20:09:36",
        owner_id=current_user.user_id
    )

@router.get("/{project_id}/stats", response_model=ProjectStats)
async def get_project_stats(
    project_id: str,
    current_user: TokenData = Depends(get_current_user)
):
    """Obtiene estadísticas de un proyecto."""
    return ProjectStats(
        total_sessions=5,
        completed_missions=2,
        last_activity="2025-08-26T20:30:00",
        size_mb=15.6
    )

@router.post("/{project_id}/export")
async def export_project(
    project_id: str,
    current_user: TokenData = Depends(get_current_user)
):
    """Exporta un proyecto a formato .mtp."""
    try:
        result = await asyncio.create_subprocess_exec(
            "python3", "../the-mighty-task-template/scripts/mighty-task.py",
            "project", "export",
            "--project-id", project_id,
            "--output", f"/tmp/{project_id}-export.mtp",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error exportando proyecto: {stderr.decode()}"
            )
        
        return {"message": "Proyecto exportado exitosamente", "file": f"{project_id}-export.mtp"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error exportando proyecto: {str(e)}"
        )

@router.post("/import")
async def import_project(
    file: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user)
):
    """Importa un proyecto desde archivo .mtp."""
    if not file.filename.endswith('.mtp'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo debe tener extensión .mtp"
        )
    
    try:
        # Guardar archivo temporalmente
        temp_path = f"/tmp/{file.filename}"
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Importar usando mighty-task CLI
        result = await asyncio.create_subprocess_exec(
            "python3", "../the-mighty-task-template/scripts/mighty-task.py",
            "project", "import", temp_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        
        # Limpiar archivo temporal
        Path(temp_path).unlink(missing_ok=True)
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error importando proyecto: {stderr.decode()}"
            )
        
        return {"message": "Proyecto importado exitosamente"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error importando proyecto: {str(e)}"
        )

@router.delete("/{project_id}")
async def delete_project(
    project_id: str,
    delete_files: bool = False,
    current_user: TokenData = Depends(get_current_user)
):
    """Elimina un proyecto."""
    try:
        args = [
            "python3", "../the-mighty-task-template/scripts/mighty-task.py",
            "project", "delete", project_id, "--force"
        ]
        
        if delete_files:
            args.append("--delete-files")
        
        result = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        
        if result.returncode != 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error eliminando proyecto: {stderr.decode()}"
            )
        
        return {"message": "Proyecto eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error eliminando proyecto: {str(e)}"
        )
