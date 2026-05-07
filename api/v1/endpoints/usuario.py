# api/routes/usuario_routes.py

from fastapi import APIRouter, Depends, HTTPException

from application.dtos.dto_usuario import (
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioResponse
)

from application.services.usuario_service import UsuarioService
from core.dependencias import get_usuario_repository



router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post("/", response_model=UsuarioResponse)
def crear(
    data: UsuarioCreate,
    repo=Depends(get_usuario_repository)
):
    service = UsuarioService(repo)

    try:
        return service.crear(data)

    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )


@router.get("/", response_model=list[UsuarioResponse])
def listar(
    repo=Depends(get_usuario_repository)
):
    service = UsuarioService(repo)

    try:
        return service.listar()

    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_por_id(
    usuario_id: int,
    repo=Depends(get_usuario_repository)
):
    service = UsuarioService(repo)

    try:
        usuario = service.obtener_por_id(usuario_id)

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return usuario

    except HTTPException:
        raise

    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar(
    usuario_id: int,
    data: UsuarioUpdate,
    repo=Depends(get_usuario_repository)
):
    service = UsuarioService(repo)

    try:
        usuario = service.actualizar(usuario_id, data)

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return usuario

    except HTTPException:
        raise

    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )


@router.delete("/{usuario_id}")
def eliminar(
    usuario_id: int,
    repo=Depends(get_usuario_repository)
):
    service = UsuarioService(repo)

    try:
        service.eliminar(usuario_id)

        return {
            "message": "Usuario eliminado correctamente"
        }

    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )