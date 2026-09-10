# infrastructura/repositories/mysql_usuario_repository.py

from sqlalchemy import or_, select, update

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
        model.nombre = usuario.nombre,
        model.apellido= usuario.apellido
        model.activo = usuario.activo
        model.rol =usuario.rol

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    def obtener_por_id(self, usuario_id: int):

        stmt = (
        select(UsuarioModel)
        .where(UsuarioModel.id == usuario_id)
        )

        result =  self.db.execute(stmt)

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return  self._to_entity(model)

    def obtener_por_username(self, username: str):

        model = (
            self.db.query(UsuarioModel)
            .filter(UsuarioModel.username == username)
            .first()
        )

        if not model:
            return None

        return self._to_entity(model)

    def listar(
        self,
        busqueda: str | None = None,
        activo: bool | None = None,
    ):
        stmt = select(UsuarioModel)

        if busqueda:
            texto = f"%{busqueda}%"

            stmt = stmt.where(
                or_(
                    UsuarioModel.username.like(texto),
                    UsuarioModel.nombre.like(texto),
                    UsuarioModel.apellido.like(texto),
                )
            )

        if activo is not None:
            stmt = stmt.where(
                UsuarioModel.activo == activo
            )

        result =  self.db.execute(stmt)

        models = result.scalars().all()

        return [
            self._to_entity(model)
            for model in models
        ]

    def cambiar_estado(
    self,
    usuario: Usuario
    ):
        stmt = (
            update(UsuarioModel)
            .where(UsuarioModel.id == usuario.id)
            .values(activo=usuario.activo)
        )

        self.db.execute(stmt)
        self.db.commit()

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
            nombre= model.nombre,
            apellido = model.apellido,
            rol =model.rol,
            activo=model.activo,
            created_at=model.created_at
        )


    def cambiar_password(
        self,
        usuario_id: int,
        password_hash: str,
    ) -> None:

        stmt = (
            update(UsuarioModel)
            .where(UsuarioModel.id == usuario_id)
            .values(password_hash=password_hash)
        )

        self.db.execute(stmt)
        self.db.commit()