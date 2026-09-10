from fastapi import APIRouter, Depends, HTTPException
from application.dtos.dto_banco import BancoResponse
from application.services.banco_service import BancoService
from core.dependencias import get_banco_repository

router = APIRouter(prefix="/bancos", tags=["Bancos"])

@router.get("", response_model=list[BancoResponse])
def listar(repo = Depends(get_banco_repository)):
    try:
        service = BancoService(repo)
        return service.listar()
        

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )