"""
API endpoints para gestión de misiones
======================================
"""

from fastapi import APIRouter, Depends
from app.core.auth import get_current_user, TokenData

router = APIRouter()

@router.get("/")
async def list_missions(current_user: TokenData = Depends(get_current_user)):
    """Lista misiones del usuario."""
    return {"message": "Missions endpoint - placeholder"}
