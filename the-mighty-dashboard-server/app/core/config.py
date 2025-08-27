"""
Configuración de la aplicación FastAPI
=====================================

Configuración centralizada usando Pydantic Settings para el dashboard servidor.
"""

from pydantic_settings import BaseSettings
from typing import List, Optional
import os
from pathlib import Path

class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # Configuración básica
    APP_NAME: str = "The Mighty Dashboard Server"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    PORT: int = 8000
    
    # Base de datos
    DATABASE_URL: str = "sqlite+aiosqlite:///./mighty_task.db"
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    
    # Redis (cache y sesiones)
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_EXPIRE_TIME: int = 3600  # 1 hora
    
    # Seguridad
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:1420",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:1420"
    ]
    
    # Rutas del sistema mighty-task
    MIGHTY_TASK_BASE_PATH: str = "../the-mighty-task-template"
    MIGHTY_TASK_SCRIPTS_PATH: str = "../the-mighty-task-template/scripts"
    PROJECTS_BASE_PATH: str = "/tmp/mighty-projects"  # Cambiar en producción
    
    # Límites de archivos
    MAX_UPLOAD_SIZE: int = 100 * 1024 * 1024  # 100MB
    ALLOWED_EXTENSIONS: List[str] = [".mtp", ".md", ".json", ".txt"]
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configuración de workers
    WORKER_TIMEOUT: int = 300  # 5 minutos
    MAX_CONCURRENT_OPERATIONS: int = 10
    
    # Configuración de notificaciones
    ENABLE_NOTIFICATIONS: bool = True
    NOTIFICATION_RETENTION_DAYS: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Instancia global de configuración
settings = Settings()
