from fastapi import APIRouter, Depends, HTTPException
from typing import Any, List

from fastapi.responses import JSONResponse

from application.dtos.dto_legajo_concepto import (
    LegajoConceptoCreate,
    LegajoConceptoUpdate,
    LegajoConceptoResponse
)
from application.services.legajo_concepto_service import LegajoConceptoService
from core.dependencias import get_legajo_concepto_repository

router = APIRouter(
    prefix="/legajos",
    tags=["Legajo-conceptos"])

@router.get("/{legajo_id}/conceptos",  response_model=List[LegajoConceptoResponse])
def listar_conceptos_legajo(
    legajo_id: int,
    repo = Depends(get_legajo_concepto_repository)): 
    try:
        service = LegajoConceptoService(repo)
        return service.listar(legajo_id)
        
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex.args)
        )


@router.post("/{legajo_id}/conceptos")
def crear_concepto_legajo( legajo_id: int,
    data: LegajoConceptoCreate,                      
    repo = Depends(get_legajo_concepto_repository)):
    try:
      
        service = LegajoConceptoService(repo)
        return service.crear(legajo_id,data)
        
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


@router.put("/{legajo_id}/conceptos/{concepto_legajo_id}")
def actualizar_concepto_legajo(legajo_id: int,
    concepto_legajo_id : int,                           
    data: LegajoConceptoUpdate,                      
    repo = Depends(get_legajo_concepto_repository)):
    try:
      
        service = LegajoConceptoService(repo)
        return service.actualizar(concepto_legajo_id,data)
        
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

@router.delete("/{legajo_id}/conceptos/{concepto_legajo_id}")
def eliminar_concepto_legajo(
    concepto_legajo_id : int,                                          
    repo = Depends(get_legajo_concepto_repository)):
    try:
      
        service = LegajoConceptoService(repo)
        return service.eliminar(concepto_legajo_id)
        
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )