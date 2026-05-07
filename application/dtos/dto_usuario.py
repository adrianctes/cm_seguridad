# application/dtos/usuario_dto.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UsuarioCreate(BaseModel):
    username: str
    password_hash: str
    activo: bool = True


class UsuarioUpdate(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None
    activo: Optional[bool] = None


class UsuarioResponse(BaseModel):
    id: int
    username: str
    activo: bool
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True