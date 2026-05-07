# application/services/usuario_service.py

from core.security import hash_password

from domain.entities.usuario_entity import Usuario
from domain.repositories.usuario_repositorio_interface import (
    UsuarioRepository
)


class UsuarioService:

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    # 🔹 Crear
    def crear(self, data):

        existente = self.repo.obtener_por_username(
            data.username
        )

        if existente:
            raise Exception(
                "El username ya existe"
            )

        usuario = Usuario(
            id=None,
            username=data.username,
            password_hash=hash_password(
                data.password
            ),
            activo=data.activo
        )

        return self.repo.guardar(usuario)

    # 🔹 Listar
    def listar(self):

        return self.repo.listar()

    # 🔹 Obtener por ID
    def obtener_por_id(self, usuario_id: int):

        return self.repo.obtener_por_id(usuario_id)

    # 🔹 Obtener por username
    def obtener_por_username(self, username: str):

        return self.repo.obtener_por_username(
            username
        )

    # 🔹 Actualizar
    def actualizar(self, usuario_id: int, data):

        usuario = self.repo.obtener_por_id(
            usuario_id
        )

        if not usuario:
            return None

        # 🔹 Validar username duplicado
        if data.username is not None:

            existente = (
                self.repo.obtener_por_username(
                    data.username
                )
            )

            if (
                existente and
                existente.id != usuario_id
            ):
                raise Exception(
                    "El username ya existe"
                )

            usuario.username = data.username

        # 🔹 Actualizar password
        if data.password is not None:

            usuario.password_hash = hash_password(
                data.password
            )

        # 🔹 Actualizar activo
        if data.activo is not None:

            usuario.activo = data.activo

        return self.repo.guardar(usuario)

    # 🔹 Eliminar
    def eliminar(self, usuario_id: int):

        return self.repo.eliminar(usuario_id)