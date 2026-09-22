from pydantic import ConfigDict

from application.dtos.dto_rol_permisos import RolPermisoCreate
from domain.repositories.rol_permisos_repositorio_interface import (
    IRolPermisosRepository,
)


class RolPermisoService:

    def __init__(
        self,
        repo: IRolPermisosRepository
    ):
       self.repo = repo   

    def listar_permisos(self):

        return  self.repo.listar_permisos()

    def listar_por_rol(
        self,
        rol: str,
    ):


        return self.repo.listar_permisos_por_rol(rol)

    async def crear(
        self,
        data: RolPermisoCreate,
    ):

        return await self.repo.crear(data)

    def actualizar_permisos_rol(
        self,
        rol: str,
        permisos_ids: list[int],
    ):
        return self.repo.actualizar_permisos_rol(
            rol,
            permisos_ids
        )

    async def eliminar(
        self,
        rol_permiso_id: int,
    ):

        eliminado = await self.repo.eliminar(
            rol_permiso_id
        )

        if not eliminado:
            raise ValueError(
                "La asignación rol-permiso no existe"
            )

        return True


