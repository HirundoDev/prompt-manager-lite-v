"""
Sistema de autenticación JWT
===========================

Manejo de autenticación y autorización para el dashboard servidor.
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from .config import settings

# Configurar encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

class TokenData(BaseModel):
    """Datos del token JWT."""
    user_id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    scopes: list[str] = []

class Token(BaseModel):
    """Respuesta de token."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verificar contraseña."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generar hash de contraseña."""
    return pwd_context.hash(password)

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Crear token de acceso JWT."""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: Dict[str, Any]) -> str:
    """Crear token de refresh JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """Verificar y decodificar token JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            credentials.credentials, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        
        # Verificar que es un token de acceso
        if payload.get("type") != "access":
            raise credentials_exception
        
        user_id: str = payload.get("sub")
        username: str = payload.get("username")
        email: str = payload.get("email")
        scopes: list = payload.get("scopes", [])
        
        if user_id is None:
            raise credentials_exception
            
        token_data = TokenData(
            user_id=user_id,
            username=username,
            email=email,
            scopes=scopes
        )
        
    except JWTError:
        raise credentials_exception
    
    return token_data

def verify_refresh_token(token: str) -> TokenData:
    """Verificar token de refresh."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid refresh token",
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        # Verificar que es un token de refresh
        if payload.get("type") != "refresh":
            raise credentials_exception
        
        user_id: str = payload.get("sub")
        username: str = payload.get("username")
        email: str = payload.get("email")
        scopes: list = payload.get("scopes", [])
        
        if user_id is None:
            raise credentials_exception
            
        return TokenData(
            user_id=user_id,
            username=username,
            email=email,
            scopes=scopes
        )
        
    except JWTError:
        raise credentials_exception

def create_token_pair(user_data: Dict[str, Any]) -> Token:
    """Crear par de tokens (access + refresh)."""
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(
        data=user_data,
        expires_delta=access_token_expires
    )
    
    refresh_token = create_refresh_token(data=user_data)
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

# Dependency para requerir autenticación
async def get_current_user(token_data: TokenData = Depends(verify_token)) -> TokenData:
    """Dependency para obtener usuario actual autenticado."""
    return token_data

# Dependency para requerir permisos específicos
def require_scopes(required_scopes: list[str]):
    """Dependency factory para requerir scopes específicos."""
    def check_scopes(current_user: TokenData = Depends(get_current_user)) -> TokenData:
        for scope in required_scopes:
            if scope not in current_user.scopes:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Insufficient permissions. Required scope: {scope}"
                )
        return current_user
    return check_scopes
