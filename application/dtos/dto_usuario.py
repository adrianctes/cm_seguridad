# application/dtos/usuario_dto.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UsuarioUpdate(BaseModel):
    username : str
    nombre: str
    apellido:str
    rol: str 
    activo:  bool

class UsuarioUpdatePassword(BaseModel):
    id: int
    password:str

class UsuarioResponse(BaseModel):
    id: int
    username: str
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    rol: Optional[str] = None
    activo: bool
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class UsuarioCreate(BaseModel):
    username: str
    password: str
    nombre: str | None = None
    apellido: str | None = None
    rol: str | None = None
    activo : bool

from pydantic import BaseModel


class CambiarPasswordDTO(BaseModel):
    password_actual: str
    password_nueva: str
    password_confirmacion : str