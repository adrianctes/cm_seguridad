from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.dtos.dto_liquidacion import LiquidacionCreate, LiquidacionResponse, LiquidacionUpdate
from application.dtos.dto_modalidad_liquidacion import LiquidacionUpdateValor
from domain.entities.liquidacion import Liquidacion
from core.dependencias import get_liquidacion_repository
from application.services.liquidacion_service import LiquidacionService
from typing import List

router = APIRouter(prefix="/liquidacion")


@router.post("/", response_model=LiquidacionResponse)
def crear_liquidacion(
    data: LiquidacionCreate,
    repo =Depends(get_liquidacion_repository)

):
    service = LiquidacionService(repo)
    try:
      return service.crear(data)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )
    
@router.patch("/{id}", response_model=LiquidacionResponse)
def actualizar_valor(
    id: int,
    data: LiquidacionUpdateValor,
    repo = Depends(get_liquidacion_repository)
):
    service = LiquidacionService(repo)

    try:
        result = service.actualizar(id, data)

        if not result:
            raise HTTPException(status_code=404, detail="Liquidación no encontrada")

        return result

    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

# 🔹 OBTENER
@router.get("/{id}", response_model=LiquidacionResponse)
def obtener_legajo(
    legajo_id: int,
    repo =Depends(get_liquidacion_repository)
):
    service = LiquidacionService(repo)
    return service.obtener(legajo_id)




@router.get("/legajo/{legajo_id}", response_model=List[LiquidacionResponse])
def listar_por_legajo(
    legajo_id: int,
    repo =Depends(get_liquidacion_repository)
):

    service = LiquidacionService(repo)
    try:
       return service.listar_por_legajo(legajo_id)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )


@router.delete("/{id}")
def eliminar(id: int, 
             repo: LiquidacionService = Depends(get_liquidacion_repository)):
    
    service = LiquidacionService(repo)
    
    try :
        service.eliminar(id)
        return {"message": "Eliminado"}
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )