from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import date

from application.dtos.dto_concepto_novedad import ConceptoNovedadCreate, ConceptoNovedadResponse, ConceptoNovedadUpdate
from application.services.concepto_novedad_service import ConceptoNovedadService
from core.dependencias import get_concepto_novedad_repository

router = APIRouter(prefix="/concepto-novedad")


# 🔹 Crear
@router.post("/", response_model=ConceptoNovedadResponse)
def crear(
    data: ConceptoNovedadCreate,
    repo =   Depends(get_concepto_novedad_repository)
):
    service = ConceptoNovedadService(repo)
    try:
      return service.crear(data)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )


# 🔹 Obtener por ID
@router.get("/{id}", response_model=ConceptoNovedadResponse)
def obtener(
    id: int,
    repo = Depends(get_concepto_novedad_repository)
):
    service = ConceptoNovedadService(repo)
    try:
      return service.obtener(id)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    


# 🔹 Listar por legajo
@router.get("/legajo/{legajo_id}", response_model=List[ConceptoNovedadResponse])
def listar_por_legajo(
    legajo_id: int,
    repo = Depends(get_concepto_novedad_repository)
):
    service = ConceptoNovedadService(repo)
    try:
      return service.listar_por_legajo(legajo_id)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    


# 🔹 Listar vigentes (🔥 clave)
@router.get("/vigentes/{legajo_id}", response_model=List[ConceptoNovedadResponse])
def listar_vigentes(
    legajo_id: int,
    fecha: date,
    service: ConceptoNovedadService = Depends(get_concepto_novedad_repository)
):
    return service.listar_vigentes(legajo_id, fecha)


# 🔹 Actualizar
@router.put("/{id}", response_model=ConceptoNovedadResponse)
def actualizar(
    id: int,
    dto: ConceptoNovedadUpdate,
    service: ConceptoNovedadService = Depends(get_concepto_novedad_repository)
):
    return service.actualizar(id, dto)


# 🔹 Eliminar
@router.delete("/{id}")
def eliminar(
    id: int,
    repo = Depends(get_concepto_novedad_repository)
):
    service = ConceptoNovedadService(repo)
    try:
      return service.eliminar(id)
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )    