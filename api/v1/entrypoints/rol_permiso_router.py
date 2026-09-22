
from fastapi import APIRouter, Depends, HTTPException, status

from application.dtos.dto_rol_permisos import (
    PermisoResponse,
    RolPermisoCreate,
    RolPermisoResponse,
    PermisosRolResponse,
    PermisosRolUpdate,
)

from application.services.rol_permiso_service import (
    RolPermisoService,
)

from core.dependencias import get_rol_permisos_repository


router = APIRouter(
    prefix="/permisos",
    tags=["Permisos"],
)

@router.get(
    "",
    response_model=list[PermisoResponse]
)
def listar_permisos(
    repo=Depends(get_rol_permisos_repository)
):

    try:

        service = RolPermisoService(repo)

        return  service.listar_permisos()
      


    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(ex),
        )


@router.get(
    "/roles/{rol}",
    response_model=PermisosRolResponse,
)
def listar_permisos_por_rol(
    rol: str,
    repo=Depends(get_rol_permisos_repository)
):

    try:

        service = RolPermisoService(repo)

        permisos_ids = service.listar_por_rol(rol)

        return {
            "rol": rol,
            "permisos_ids": permisos_ids,
        }

    except ValueError as ex:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )


@router.post(
    "",
    response_model=RolPermisoResponse,
    status_code=status.HTTP_201_CREATED,
)
async def crear_rol_permiso(
    data: RolPermisoCreate,
    repo=Depends(get_rol_permisos_repository)
):

    try:

        service = RolPermisoService(repo)

        return await service.crear(data)

    except ValueError as ex:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )

@router.put(
    "/roles/{rol}",
    status_code=status.HTTP_200_OK,
)
async def actualizar_permisos_rol(
    rol: str,
    data: PermisosRolUpdate,
    repo=Depends(get_rol_permisos_repository)
):

    try:

        service = RolPermisoService(repo)

        service.actualizar_permisos_rol(
            rol,
            data.permisos_ids,
        )

        return {
            "ok": True,
            "mensaje": "Permisos guardados correctamente",
        }

    except ValueError as ex:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        )



# ============================================================
# DELETE /api/v1/permisos/{rol_permiso_id}
# Eliminar asignación
# ============================================================

@router.delete(
    "/{rol_permiso_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def eliminar_rol_permiso(
    rol_permiso_id: int,
    repo=Depends(get_rol_permisos_repository)
):

    try:

        service = RolPermisoService(repo)

        await service.eliminar(
            rol_permiso_id
        )

    except ValueError as ex:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(ex),
        )

