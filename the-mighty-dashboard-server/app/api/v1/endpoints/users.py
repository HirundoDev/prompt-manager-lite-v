"""
API endpoints para gestión de usuarios
======================================
"""

from fastapi import APIRouter, Depends
from app.core.auth import get_current_user, TokenData

router = APIRouter()

@router.get("/me")
async def get_current_user_info(current_user: TokenData = Depends(get_current_user)):
    """Obtiene información del usuario actual."""
    return {
        "user_id": current_user.user_id,
        "username": current_user.username,
        "email": current_user.email,
        "scopes": current_user.scopes
    }
