from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.dtos.dto_modalidad_liquidacion import ModalidadLiquidacionResponse
from application.services.modalidad_liquidacion_service import ModalidadLiquidacionService
from core.dependencias import get_modalidad_liquidacion_repository

router = APIRouter(prefix="/modalidades", tags=["Modalidades"])

@router.get("", response_model=list[ModalidadLiquidacionResponse])
def listar(repo = Depends(get_modalidad_liquidacion_repository)):
    try:
        service = ModalidadLiquidacionService(repo)
        return service.listar()
        

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )