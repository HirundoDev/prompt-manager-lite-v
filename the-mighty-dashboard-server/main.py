"""
The Mighty Dashboard Server - FastAPI Backend
============================================

API backend para el dashboard servidor con soporte multi-usuario,
autenticación, y gestión centralizada de proyectos mighty-task.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import uvicorn
import os
from pathlib import Path

# Importar módulos locales
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.api import api_router
from app.core.auth import verify_token

# Configurar seguridad
security = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestión del ciclo de vida de la aplicación."""
    # Startup
    print("🚀 Iniciando The Mighty Dashboard Server...")
    
    # Crear tablas de base de datos
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    print("✅ Base de datos inicializada")
    print(f"🌐 Servidor ejecutándose en: http://localhost:{settings.PORT}")
    
    yield
    
    # Shutdown
    print("🛑 Cerrando The Mighty Dashboard Server...")

# Crear aplicación FastAPI
app = FastAPI(
    title="The Mighty Dashboard Server API",
    description="API backend para gestión centralizada de proyectos mighty-task",
    version="1.0.0",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas de la API
app.include_router(api_router, prefix="/api/v1")

# Ruta de salud
@app.get("/health")
async def health_check():
    """Endpoint de verificación de salud."""
    return {
        "status": "healthy",
        "service": "mighty-dashboard-server",
        "version": "1.0.0"
    }

# Ruta raíz
@app.get("/")
async def root():
    """Endpoint raíz con información del servicio."""
    return {
        "service": "The Mighty Dashboard Server",
        "version": "1.0.0",
        "description": "API backend para gestión centralizada de proyectos mighty-task",
        "docs": "/docs" if settings.DEBUG else "Documentación deshabilitada en producción",
        "health": "/health"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
