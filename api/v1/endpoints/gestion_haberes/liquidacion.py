from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import os
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
        get_current_user,
        get_datos_fijos_liquidacion_repository,
        get_liquidacion_repository, 
        get_legajo_repository,
        get_legajo_concepto_repository,
        get_novedad_repository,
        
        )
from application.services.proceso_liquidacion_service import ProcesoLiquidacionService
from application.services.liquidacion_service import LiquidacionService
from typing import List

from infrastructura.pdf.liquidacion_impresion import LiquidacionImpresion

router = APIRouter(prefix="/liquidaciones")

@router.get(
    "/legajos-disponibles",
    response_model=list[LegajoResponse]
)
async def buscar_legajos_disponibles(
    datos_fijos_id: int,
    current_user=Depends(get_current_user),
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
    repo =Depends(get_liquidacion_repository),
    current_user=Depends(get_current_user)

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
    repo=Depends(get_liquidacion_repository),
    current_user=Depends(get_current_user)
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
    repo =Depends(get_liquidacion_repository),
    current_user=Depends(get_current_user)
):
    service = LiquidacionService(repo)
    return service.obtener(legajo_id)

@router.get("/legajo/{legajo_id}", response_model=List[LiquidacionResponse])
def listar_por_legajo(
    legajo_id: int,
    repo =Depends(get_liquidacion_repository),
    current_user=Depends(get_current_user)
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
    repo=Depends(get_liquidacion_repository),
    current_user=Depends(get_current_user),
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
    current_user=Depends(get_current_user)
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

@router.get("/{liquidacion_id}/pdf")
def imprimir_liquidacion(
    liquidacion_id: int,
    repo=Depends(get_liquidacion_repository),
    current_user=Depends(get_current_user)
):

    try:

        service = LiquidacionService(repo)

        data = service.obtener_por_id(
            liquidacion_id
        )

        if not data:
            raise HTTPException(
                status_code=404,
                detail="No se encontró la liquidación."
            )

        # ---------------------------------------------
        # Pydantic -> diccionario
        # ---------------------------------------------

        data = data.model_dump()

        # ---------------------------------------------
        # Ruta del PDF
        # ---------------------------------------------

        ruta = os.path.abspath(
            f"liquidacion_{liquidacion_id}.pdf"
        )

        # ---------------------------------------------
        # Generar PDF
        # ---------------------------------------------

        impresion = LiquidacionImpresion(
            data,
            ruta
        )

        impresion.generar()

        # ---------------------------------------------
        # Devolver PDF
        # ---------------------------------------------

        return FileResponse(
            path=ruta,
            media_type="application/pdf",
            filename=f"liquidacion_{liquidacion_id}.pdf",
            headers={
                "Content-Disposition": (
                    f'inline; filename="liquidacion_{liquidacion_id}.pdf"'
                )
            }
        )

    except HTTPException:
        raise

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )
import secrets
import time
tokens_pdf = {}
@router.get("/{liquidacion_id}/pdf-token")
def generar_token_pdf(
    liquidacion_id: int,
    current_user=Depends(get_current_user)
):

    token = secrets.token_urlsafe(32)

    tokens_pdf[token] = {
        "liquidacion_id": liquidacion_id,
        "expira": time.time() + 60
    }

    return {
        "url": (
            f"/api/v1/liquidaciones/"
            f"pdf-temporal/{token}"
        )
    }

@router.get("/pdf-temporal/{token}")
def obtener_pdf_temporal(
    token: str,
    repo=Depends(get_liquidacion_repository)
):

    # ---------------------------------------------
    # Buscar token temporal
    # ---------------------------------------------

    datos = tokens_pdf.get(token)

    if not datos:
        raise HTTPException(
            status_code=404,
            detail="Token de PDF inválido."
        )

    # ---------------------------------------------
    # Verificar expiración
    # ---------------------------------------------

    if time.time() > datos["expira"]:

        del tokens_pdf[token]

        raise HTTPException(
            status_code=404,
            detail="El enlace del PDF expiró."
        )

    # ---------------------------------------------
    # Obtener liquidación
    # ---------------------------------------------

    liquidacion_id = datos["liquidacion_id"]

    # Token de un solo uso
    del tokens_pdf[token]

    service = LiquidacionService(repo)

    data = service.obtener_por_id(
        liquidacion_id
    )

    if not data:
        raise HTTPException(
            status_code=404,
            detail="No se encontró la liquidación."
        )

    # ---------------------------------------------
    # Pydantic → dict
    # ---------------------------------------------

    data = data.model_dump()

    # ---------------------------------------------
    # Generar PDF
    # ---------------------------------------------

    ruta = os.path.abspath(
        f"liquidacion_{liquidacion_id}.pdf"
    )

    impresion = LiquidacionImpresion(
        data,
        ruta
    )

    impresion.generar()

    # ---------------------------------------------
    # Devolver PDF
    # ---------------------------------------------

    return FileResponse(
        path=ruta,
        media_type="application/pdf",
        filename=f"liquidacion_{liquidacion_id}.pdf",
        headers={
            "Content-Disposition": "inline"
        }
    )