# application/services/auth_service.py

from core.security import (
    verify_password,
    create_access_token
)
from domain.repositories.usuario_repositorio_interface import UsuarioRepository


class AuthService:

    def __init__(self, repo:UsuarioRepository) :
         self.repo = repo


    def login(self, data):

        usuario = self.repo.obtener_por_username(
            data.username
        )
   
        if not usuario:
            raise Exception("Usuario inválido")

        if not usuario.activo:
            raise Exception("Usuario inactivo")

        password_ok = verify_password(
            data.password,
            usuario.password_hash
        )

        if not password_ok:
            raise Exception("Password incorrecta")

        token = create_access_token({
            "sub": usuario.username,
            "user_id": usuario.id
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }