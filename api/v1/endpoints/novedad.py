from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import date

from application.dtos.dto_novedad import NovedadCreate, NovedadResponse,NovedadUpdate
from application.services.concepto_novedad_service import NovedadService
from core.dependencias import get_novedad_repository

router = APIRouter(prefix="/novedades")


# 🔹 Crear
@router.post("", response_model=NovedadResponse)
def crear(
    data: NovedadCreate,
    repo =   Depends(get_novedad_repository)
):
   
    service = NovedadService(repo)
    try:
  
      return service.crear(data)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )

# 🔹 Obtener por ID
@router.get("/{id}", response_model=NovedadResponse)
def obtener(
    id: int,
    repo = Depends(get_novedad_repository)
):
    service = NovedadService(repo)
    try:
      return service.obtener(id)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
# 🔹 Obtener por PERIODO
@router.get("", response_model=List[NovedadResponse])
def obtener_por_periodo(
    fecha: date,
    tipo_busqueda: str | None = None,
    busqueda: str | None = None,
    repo = Depends(get_novedad_repository)
):
    service = NovedadService(repo)
    try:
             
        return service.obtener_por_periodo(fecha, tipo_busqueda, busqueda)
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    

# 🔹 Listar por legajo
@router.get("/legajos/{legajo_id}", response_model=List[NovedadResponse])
def listar_por_legajo(
    legajo_id: int,
    repo = Depends(get_novedad_repository)
):
    service = NovedadService(repo)
    try:
      return service.listar_por_legajo(legajo_id)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    


# 🔹 Listar vigentes (🔥 clave)
@router.get("/vigentes/{legajo_id}", response_model=List[NovedadResponse])
def listar_vigentes(
    legajo_id: int,
    fecha: date,
    service: NovedadService = Depends(get_novedad_repository)
):
    return service.listar_vigentes(legajo_id, fecha)


# 🔹 Actualizar
@router.put("/{id}", response_model=NovedadResponse)
def actualizar(
    id: int,
    data: NovedadUpdate,
    repo = Depends(get_novedad_repository)
):
 
    service = NovedadService(repo)
    try:
      return service.actualizar(id, data)
    except Exception as ex:
        print(ex.args)
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    


# 🔹 Eliminar
@router.delete("/{id}")
def eliminar(
    id: int,
    repo = Depends(get_novedad_repository)
):
    service = NovedadService(repo)
    try:
      return service.eliminar(id)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    