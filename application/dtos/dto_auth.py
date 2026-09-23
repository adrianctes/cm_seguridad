# application/dtos/auth_dto.py

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class UsuarioLoginResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    rol: str
    permisos: list[str] = []    


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: UsuarioLoginResponse
    requiere_cambio_password: bool = False
