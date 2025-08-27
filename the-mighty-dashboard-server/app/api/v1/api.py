"""
API Router principal v1
======================

Router principal que incluye todas las rutas de la API v1.
"""

from fastapi import APIRouter
from .endpoints import auth, projects, sessions, missions, users, dashboard

api_router = APIRouter()

# Incluir routers de endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
api_router.include_router(missions.router, prefix="/missions", tags=["missions"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
