from fastapi import APIRouter, Depends, HTTPException
from typing import List

from application.dtos.dto_novedad import (
    NovedadCreate,
    NovedadUpdate,
    NovedadResponse
)

from application.services.novedad_service import NovedadService
from core.dependencias import get_novedad_repository


router = APIRouter(
    prefix="/legajos",
    tags=["Legajo-novedades"]
)

@router.get("/{legajo_id}/novedades", response_model=List[NovedadResponse])
def listar_novedades_legajo(
    legajo_id: int,
    repo=Depends(get_novedad_repository)
):
    try:
        service = NovedadService(repo)
        return service.listar(legajo_id)

    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

@router.post("/{legajo_id}/novedades", response_model=NovedadResponse)
def crear_novedad_legajo(
    legajo_id: int,
    data: NovedadCreate,
    repo=Depends(get_novedad_repository)
):
    try:
        service = NovedadService(repo)
        return service.crear(legajo_id, data)

    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
@router.put("/{legajo_id}/novedades/{novedad_id}", response_model=NovedadResponse)
def actualizar_novedad_legajo(
    legajo_id: int,
    novedad_id: int,
    data: NovedadUpdate,
    repo=Depends(get_novedad_repository)
):
    try:
        service = NovedadService(repo)
        return service.actualizar(novedad_id, data)

    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
@router.delete("/{legajo_id}/novedades/{novedad_id}")
def eliminar_novedad_legajo(
    novedad_id: int,
    repo=Depends(get_novedad_repository)
):
    try:
        service = NovedadService(repo)
        return service.eliminar(novedad_id)

    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
@router.get("/{legajo_id}/novedades/activas", response_model=List[NovedadResponse])
def listar_activas(
    legajo_id: int,
    repo=Depends(get_novedad_repository)
):
    try:
        service = NovedadService(repo)
        return service.listar_activas(legajo_id)

    except Exception as ex:
        raise HTTPException(500, str(ex))

@router.get("/{legajo_id}/novedades/ultima", response_model=NovedadResponse)
def ultima_novedad(
    legajo_id: int,
    repo=Depends(get_novedad_repository)
):
    try:
        service = NovedadService(repo)
        return service.ultima(legajo_id)

    except Exception as ex:
        raise HTTPException(500, str(ex))