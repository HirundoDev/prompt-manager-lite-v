"""
API endpoints para gestión de sesiones
======================================
"""

from fastapi import APIRouter, Depends
from app.core.auth import get_current_user, TokenData

router = APIRouter()

@router.get("/")
async def list_sessions(current_user: TokenData = Depends(get_current_user)):
    """Lista sesiones del usuario."""
    return {"message": "Sessions endpoint - placeholder"}
