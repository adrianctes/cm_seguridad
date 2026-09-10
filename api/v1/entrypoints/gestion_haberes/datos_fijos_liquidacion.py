from datetime import date

from fastapi import APIRouter, Depends, HTTPException

from application.dtos.dto_datos_fijos_liquidacion import  DatosFijosLiquidacionCreate, DatosFijosLiquidacionResponse, DatosFijosLiquidacionUpdate
from application.services.datos_fijos_liquidacion_service import DatosFijosLiquidacionService
from core.dependencias import (get_datos_fijos_liquidacion_repository)

router = APIRouter(
    prefix="/datos-fijos-liquidacion",
    tags=["datos_fijos"]
)


@router.post("", status_code=200
)
async def crear(
    data: DatosFijosLiquidacionCreate,
    repo_datos_fijos=Depends(get_datos_fijos_liquidacion_repository)    
    ):
    try:

        service = DatosFijosLiquidacionService(repo_datos_fijos)

        await service.crear(data)

    except ValueError as ex:
        print(ex.args)
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
    

    except Exception as ex:
   
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

@router.put(
    "/{id}",
    response_model=DatosFijosLiquidacionResponse,
    status_code=200
)

def actualizar(
    id: int,
    data: DatosFijosLiquidacionUpdate,
    repo=Depends(get_datos_fijos_liquidacion_repository)
):
    try:
        
 
        service = DatosFijosLiquidacionService(repo)
        return service.actualizar(id, data)

    except ValueError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

@router.delete(
    "/{id}",
    status_code=200
)
def eliminar(
    id: int,
    repo=Depends(get_datos_fijos_liquidacion_repository)
):
    try:
        
        service = DatosFijosLiquidacionService(repo)
        return service.eliminar(id)

    except ValueError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

@router.get("", response_model=list[DatosFijosLiquidacionResponse])
def listar(
    periodo: int | None = None,
    estado: str| None = None,
    modalidad: str | None = None,
    repo=Depends(get_datos_fijos_liquidacion_repository)):
    try:
        params = {
            "periodo": periodo,
            "modalidad": modalidad,
            "estado": estado
        }

        service = DatosFijosLiquidacionService(repo)
        
        return service.listar_por_periodo(params)

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )



@router.get("/{id}", response_model=DatosFijosLiquidacionResponse)
def obtener(id: int, repo=Depends(get_datos_fijos_liquidacion_repository)):
    try:
        service = DatosFijosLiquidacionService(repo)
        return service.obtener(id)

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )