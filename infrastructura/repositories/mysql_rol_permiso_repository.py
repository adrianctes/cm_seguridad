from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructura.db.models.permiso_model import PermisoModel
from infrastructura.db.models.rol_permiso_model import RolPermisoModel
from application.dtos.dto_rol_permisos import RolPermisoCreate
from domain.entities.usuario_entity import Usuario
from domain.repositories.rol_permisos_repositorio_interface import IRolPermisosRepository



class MySQLRolPermisoRepository(IRolPermisosRepository):

    def __init__(self, db):
        self.db = db


    def guardar_permisos_rol(
            self,
            rol: str,
            permisos_ids: list[int],
        ):
            pass

    def listar_permisos(self):
        return (
            self.db
            .query(PermisoModel)
            .filter(PermisoModel.activo == True)
            .order_by(PermisoModel.orden.asc())
            .all()
        )

    def listar_permisos_por_rol(
        self,
        rol: str,
    ) -> list[RolPermisoModel]:

        result =  self.db.execute(
            select(RolPermisoModel.permiso_id)
            .where(
            RolPermisoModel.rol == rol
            )
            .order_by(
                RolPermisoModel.permiso_id
            )
        )

        return result.scalars().all()

    def obtener_codigos_por_rol(self, rol: str) -> list[str]:

        resultados = (
            self.db.query(PermisoModel.codigo)
            .join(
                RolPermisoModel,
                RolPermisoModel.permiso_id == PermisoModel.id
            )
            .filter(
                RolPermisoModel.rol == rol,
                PermisoModel.activo == True
            )
            .order_by(PermisoModel.id)
            .all()
        )

        return [
            codigo
            for codigo, in resultados
        ]

    def crear(
        self,
        data: RolPermisoCreate,
    ) -> RolPermisoModel:

        rol_permiso = RolPermisoModel(
            rol=data.rol,
            permiso_id=data.permiso_id,
        )

        self.db.add(rol_permiso)

        self.db.commit()

        self.db.refresh(rol_permiso)

        return rol_permiso

    def actualizar_permisos_rol(
        self,
        rol: str,
        permisos_ids: list[int],
    ):
        # Eliminar permisos actuales del rol
        self.db.query(RolPermisoModel).filter(
            RolPermisoModel.rol == rol
        ).delete(
            synchronize_session=False
        )

        # Crear los nuevos permisos
        nuevos = [
            RolPermisoModel(
                rol=rol,
                permiso_id=permiso_id
            )
            for permiso_id in permisos_ids
        ]

        self.db.add_all(nuevos)

        self.db.commit()

        return True

    def eliminar(
        self,
        rol_permiso_id: int,
    ) -> bool:

        result =  self.db.execute(
            delete(RolPermisoModel)
            .where(
                RolPermisoModel.id == rol_permiso_id
            )
        )

        self.db.commit()

        return result.rowcount > 0

    def tiene_permiso(
            self,
            rol: str,
            codigo: str,
        ) -> bool:
            pass