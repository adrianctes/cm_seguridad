from fastapi import APIRouter, Depends, HTTPException
from typing import List

from application.dtos.dto_legajo import (
    LegajoCreate,
    LegajoUpdate,
    LegajoResponse
)
from application.services.legajo_service import LegajoService
from core.dependencias import get_current_user, get_legajo_repository

router = APIRouter(
    prefix="/legajos",
    tags=["Legajos"])


# 🔹 CREAR
@router.post("", response_model=LegajoResponse)
def crear_legajo(
    data: LegajoCreate,
    repo = Depends(get_legajo_repository)
):
    service = LegajoService(repo)
    try:
      return service.crear(data)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )

# 🔹 OBTENER
@router.get("/{legajo_id}", response_model=LegajoResponse)
def obtener_legajo(
    legajo_id: int,
    repo = Depends(get_legajo_repository)
):
    service = LegajoService(repo)
    return service.obtener(legajo_id)


# 🔹 LISTAR
@router.get("", response_model=List[LegajoResponse])
async def listar_legajos(repo = Depends(get_legajo_repository)):
    try:
        service = LegajoService(repo)
        return service.listar()
        

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )



# 🔹 ACTUALIZAR
@router.put("/{legajo_id}", response_model=LegajoResponse)
def actualizar_legajo(
    legajo_id: int,
    data: LegajoUpdate,
    repo = Depends(get_legajo_repository)
):
    try:
        service = LegajoService(repo)
        return service.actualizar(legajo_id, data)
    except Exception as ex:
            raise HTTPException(
                status_code=400,
                detail=str(ex)
            )

# 🔹 ELIMINAR (soft delete)
@router.delete("/{legajo_id}", response_model=LegajoResponse)
def eliminar_legajo(
    legajo_id: int,
    repo = Depends(get_legajo_repository)
):
        try :
            service = LegajoService(repo)
            return service.eliminar(legajo_id)
        except Exception as ex:
            raise HTTPException(
                status_code=400,
                detail=str(ex)
            )
