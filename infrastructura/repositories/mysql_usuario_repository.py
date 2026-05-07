# infrastructura/repositories/mysql_usuario_repository.py

from domain.entities.usuario_entity import Usuario
from domain.repositories.usuario_repositorio_interface import UsuarioRepository
from infrastructura.db.models.usuario_model import UsuarioModel


class MySQLUsuarioRepository(UsuarioRepository):

    def __init__(self, db):
        self.db = db

    def guardar(self, usuario: Usuario):

        if usuario.id:
            model = self.db.query(UsuarioModel).get(usuario.id)
        else:
            model = UsuarioModel()

        model.username = usuario.username
        model.password_hash = usuario.password_hash
        model.activo = usuario.activo

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    def obtener_por_id(self, usuario_id: int):

        model = (
            self.db.query(UsuarioModel)
            .filter(UsuarioModel.id == usuario_id)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def obtener_por_username(self, username: str):

        model = (
            self.db.query(UsuarioModel)
            .filter(UsuarioModel.username == username)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def listar(self):

        models = self.db.query(UsuarioModel).all()

        return [self._to_entity(model) for model in models]

    def eliminar(self, usuario_id: int):

        model = (
            self.db.query(UsuarioModel)
            .filter(UsuarioModel.id == usuario_id)
            .first()
        )

        if model:
            self.db.delete(model)
            self.db.commit()

    def _to_entity(self, model):

        return Usuario(
            id=model.id,
            username=model.username,
            password_hash=model.password_hash,
            activo=model.activo,
            created_at=model.created_at
        )