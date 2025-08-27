"""
API endpoints para estadísticas del dashboard
=============================================
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.auth import get_current_user, TokenData

router = APIRouter()

class DashboardStats(BaseModel):
    total_projects: int
    active_projects: int
    total_sessions: int
    completed_missions: int
    storage_used_mb: float
    last_activity: str

@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(current_user: TokenData = Depends(get_current_user)):
    """Obtiene estadísticas generales del dashboard."""
    return DashboardStats(
        total_projects=3,
        active_projects=1,
        total_sessions=15,
        completed_missions=8,
        storage_used_mb=245.6,
        last_activity="2025-08-26T20:34:00"
    )
