"""
API endpoints para autenticación
================================

Endpoints para login, registro, refresh tokens y gestión de usuarios.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from app.core.auth import (
    verify_password, get_password_hash, create_token_pair, 
    verify_refresh_token, Token
)

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str

@router.post("/login", response_model=Token)
async def login(user_data: UserLogin):
    """Autenticar usuario y devolver tokens."""
    # Por ahora, autenticación mock
    if user_data.username == "admin" and user_data.password == "admin":
        token_data = {
            "sub": "user_1",
            "username": user_data.username,
            "email": "admin@mightytask.com",
            "scopes": ["read", "write", "admin"]
        }
        return create_token_pair(token_data)
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas"
    )

@router.post("/register", response_model=Token)
async def register(user_data: UserRegister):
    """Registrar nuevo usuario."""
    # Implementar registro de usuario
    # Por ahora, registro mock
    token_data = {
        "sub": "user_new",
        "username": user_data.username,
        "email": user_data.email,
        "scopes": ["read", "write"]
    }
    return create_token_pair(token_data)

@router.post("/refresh", response_model=Token)
async def refresh_token(request: RefreshTokenRequest):
    """Renovar token de acceso usando refresh token."""
    token_data = verify_refresh_token(request.refresh_token)
    
    new_token_data = {
        "sub": token_data.user_id,
        "username": token_data.username,
        "email": token_data.email,
        "scopes": token_data.scopes
    }
    
    return create_token_pair(new_token_data)
