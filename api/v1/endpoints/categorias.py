from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.dtos.dto_categoria import CategoriaResponse
from application.services.categoria_service import CategoriaService
from core.dependencias import get_categoria_repository

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("", response_model=list[CategoriaResponse])
def listar(repo = Depends(get_categoria_repository)):
    try:
        service = CategoriaService(repo)
        return service.listar()
        

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )