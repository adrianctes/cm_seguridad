from fastapi import APIRouter, Depends, HTTPException
from application.dtos.dto_clasifiacion_concepto import ClasificacionResponse
from application.services.clasificacion_concepto_service import ClasificacionConceptoService
from core.dependencias import get_clasificacion_concepto_repository

router = APIRouter(prefix="/clasificacion-conceptos", tags=["Clasificacion_conceptos"])

@router.get("", response_model=list[ClasificacionResponse])
def listar(repo = Depends(get_clasificacion_concepto_repository)):
    try:

        service = ClasificacionConceptoService(repo)
        return service.listar()
        

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )