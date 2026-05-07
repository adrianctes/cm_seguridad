# application/services/usuario_service.py

from domain.entities.usuario_entity import Usuario
from domain.repositories.usuario_repositorio_interface import UsuarioRepository


class UsuarioService:

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    # 🔹 Crear
    def crear(self, data):

        usuario = Usuario(
            id=None,
            username=data.username,
            password_hash=data.password_hash,
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

        return self.repo.obtener_por_username(username)

    # 🔹 Actualizar
    def actualizar(self, usuario_id: int, data):

        usuario = self.repo.obtener_por_id(usuario_id)

        if not usuario:
            return None

        if data.username is not None:
            usuario.username = data.username

        if data.password_hash is not None:
            usuario.password_hash = data.password_hash

        if data.activo is not None:
            usuario.activo = data.activo

        return self.repo.guardar(usuario)

    # 🔹 Eliminar
    def eliminar(self, usuario_id: int):

        return self.repo.eliminar(usuario_id)