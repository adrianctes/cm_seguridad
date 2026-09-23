""" # application/services/auth_service.py

from core.security import (
    verify_password,
    create_access_token
)
from domain.repositories.usuario_repositorio_interface import IUsuarioRepository
from domain.repositories.rol_permisos_repositorio_interface import IRolPermisosRepository


class AuthService:

    def __init__(self, repo:IUsuarioRepository, 
                       repo_permiso : IRolPermisosRepository) :
        self.repo = repo
        self.repo_permisos = repo_permiso


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
            raise Exception("Usuario o contraseña incorrectos")

        token = create_access_token({
            "sub": usuario.username,
            "user_id": usuario.id
        })

        permisos = self.repo_permisos.obtener_codigos_por_rol(
        usuario.rol
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "rol": usuario.rol,
                "permisos": permisos
            }
        }

class AuthService:

    def __init__(
        self,
        repo: IUsuarioRepository,
        repo_permiso: IRolPermisosRepository
    ):
        self.repo = repo
        self.repo_permisos = repo_permiso

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
            raise Exception("Usuario o contraseña incorrectos")

        # =====================================================
        # DETERMINAR SI DEBE CAMBIAR LA CONTRASEÑA
        # =====================================================
        requiere_cambio_password = (
            data.password == "newReset123"
        )

        # =====================================================
        # TOKEN
        # =====================================================
        token = create_access_token({
            "sub": usuario.username,
            "user_id": usuario.id
        })

        # =====================================================
        # PERMISOS
        # =====================================================
        permisos = self.repo_permisos.obtener_codigos_por_rol(
            usuario.rol
        )

        return {
            "access_token": token,
            "token_type": "bearer",

            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "rol": usuario.rol,
                "permisos": permisos
            },
            "requiere_cambio_password": requiere_cambio_password
        } """
from core.security import (
    verify_password,
    create_access_token
)

from core.config import settings

from domain.repositories.usuario_repositorio_interface import (
    IUsuarioRepository
)

from domain.repositories.rol_permisos_repositorio_interface import (
    IRolPermisosRepository
)


class AuthService:

    def __init__(
        self,
        repo: IUsuarioRepository,
        repo_permiso: IRolPermisosRepository
    ):
        self.repo = repo
        self.repo_permisos = repo_permiso


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
            raise Exception(
                "Usuario o contraseña incorrectos"
            )

        # =====================================================
        # PASSWORD TEMPORAL
        # =====================================================

        requiere_cambio_password = (
            data.password == settings.NEW_RESET_PASSWORD
        )

        # =====================================================
        # TOKEN
        # =====================================================

        token = create_access_token({
            "sub": usuario.username,
            "user_id": usuario.id
        })

        # =====================================================
        # PERMISOS
        # =====================================================

        permisos = self.repo_permisos.obtener_codigos_por_rol(
            usuario.rol
        )

        return {
            "access_token": token,
            "token_type": "bearer",

            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "rol": usuario.rol,
                "permisos": permisos
            },

            "requiere_cambio_password": (
                requiere_cambio_password
            )
        }
