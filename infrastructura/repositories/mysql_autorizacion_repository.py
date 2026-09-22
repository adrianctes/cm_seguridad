from sqlalchemy import delete, select

from domain.entities.permiso_entity import Permiso
from domain.repositories.rol_permisos_repositorio_interface import (
    AutorizacionRepository
)

from infrastructura.db.models.permiso_model import PermisoModel
from infrastructura.db.models.rol_permiso_model import RolPermisoModel


class MySQLAutorizacionRepository(AutorizacionRepository):

    def __init__(self, db):
        self.db = db

    def listar_permisos(self):

        stmt = (
            select(PermisoModel)
            .where(
                PermisoModel.activo == True
            )
            .order_by(
                PermisoModel.modulo,
                PermisoModel.id
            )
        )

        result = self.db.execute(stmt)

        models = result.scalars().all()

        return [
            self._to_entity(model)
            for model in models
        ]

    def listar_permisos_por_rol(
        self,
        rol: str
    ):

        stmt = (
            select(PermisoModel)
            .join(
                RolPermisoModel,
                RolPermisoModel.permiso_id == PermisoModel.id
            )
            .where(
                RolPermisoModel.rol == rol,
                PermisoModel.activo == True
            )
            .order_by(
                PermisoModel.modulo,
                PermisoModel.id
            )
        )

        result = self.db.execute(stmt)

        models = result.scalars().all()

        return [
            self._to_entity(model)
            for model in models
        ]

    def obtener_ids_por_rol(
        self,
        rol: str
    ):

        stmt = (
            select(RolPermisoModel.permiso_id)
            .where(
                RolPermisoModel.rol == rol
            )
        )

        result = self.db.execute(stmt)

        return result.scalars().all()

    def guardar_permisos_rol(
        self,
        rol: str,
        permisos_ids: list[int]
    ):

        # Eliminar permisos actuales
        stmt = (
            delete(RolPermisoModel)
            .where(
                RolPermisoModel.rol == rol
            )
        )

        self.db.execute(stmt)

        # Insertar nuevos permisos
        for permiso_id in permisos_ids:

            model = RolPermisoModel(
                rol=rol,
                permiso_id=permiso_id
            )

            self.db.add(model)

        self.db.commit()

    def tiene_permiso(
        self,
        rol: str,
        codigo: str
    ) -> bool:

        stmt = (
            select(RolPermisoModel.id)
            .join(
                PermisoModel,
                PermisoModel.id == RolPermisoModel.permiso_id
            )
            .where(
                RolPermisoModel.rol == rol,
                PermisoModel.codigo == codigo,
                PermisoModel.activo == True
            )
        )

        result = self.db.execute(stmt)

        return result.scalar_one_or_none() is not None

    def _to_entity(
        self,
        model: PermisoModel
    ):

        return Permiso(
            id=model.id,
            modulo=model.modulo,
            accion=model.accion,
            codigo=model.codigo,
            nombre=model.nombre,
            activo=model.activo
        )