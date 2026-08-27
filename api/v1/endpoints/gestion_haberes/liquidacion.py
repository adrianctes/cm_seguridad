from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.dtos.dto_legajo import LegajoResponse
from application.dtos.dto_liquidacion import (
    LiquidacionCreate,
    LiquidacionListadoResponse,
    LiquidacionRequest,
    LiquidacionResponse,
    LiquidacionCalculoResponse,
    LiquidacionVisualizacionResponse
)
from application.services.legajo_service import LegajoService
from core.dependencias import (
        get_concepto_repository,
        get_datos_fijos_liquidacion_repository,
        get_liquidacion_repository, 
        get_legajo_repository,
        get_legajo_concepto_repository,
        get_novedad_repository,
        
        )
from application.services.proceso_liquidacion_service import ProcesoLiquidacionService
from application.services.liquidacion_service import LiquidacionService
from typing import List

router = APIRouter(prefix="/liquidaciones")

@router.get(
    "/legajos-disponibles",
    response_model=list[LegajoResponse]
)
async def buscar_legajos_disponibles(
    datos_fijos_id: int,

    repo_legajo=Depends(get_legajo_repository),

    repo_datos_fijos=Depends(
        get_datos_fijos_liquidacion_repository
    )
):

    service = LegajoService(
        repo_legajo
    )

    try:

        return service.buscar_legajos_disponibles_para_liquidacion(repo_datos_fijos,
            datos_fijos_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.post("", status_code=200)
def crear_liquidacion(
    data: LiquidacionCreate,
    repo =Depends(get_liquidacion_repository)

):
    service = LiquidacionService(repo)
    try:
      return service.crear(data)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
    

@router.get(
    "/{liquidacion_id}",
    response_model=LiquidacionVisualizacionResponse
)
def obtener_por_id(
    liquidacion_id: int,
    repo=Depends(get_liquidacion_repository)
):

    service = LiquidacionService(repo)

    try:

        return service.obtener_por_id(
            liquidacion_id
        )

    except ValueError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
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

@router.get(
    "/datos-fijos/{datos_fijo_id}",
    response_model=List[LiquidacionListadoResponse]
)
def listar_por_datos_fijos(
    datos_fijo_id: int,
    repo=Depends(get_liquidacion_repository)
):

    service = LiquidacionService(repo)

    try:

        return service.listar_por_datos_fijos(
            datos_fijo_id
        )

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

@router.post(
    "/liquidar",
   response_model=LiquidacionCalculoResponse
)
async def liquidar(
    request: LiquidacionRequest,
    repo_liquidacion=Depends(get_liquidacion_repository),
    repo_datos_fijos=Depends(get_datos_fijos_liquidacion_repository),
    repo_legajo=Depends(get_legajo_repository),
    repo_legajo_concepto=Depends(get_legajo_concepto_repository),
    repo_concepto=Depends(get_concepto_repository),
    repo_novedad=Depends(get_novedad_repository),
):

    service = ProcesoLiquidacionService(
        repo_datos_fijos,
        repo_legajo,
        repo_legajo_concepto,
        repo_concepto,
        repo_novedad,
        repo_liquidacion
    )

    return service.liquidar(
        request.datos_fijos_id,
        request.legajo_id
    )