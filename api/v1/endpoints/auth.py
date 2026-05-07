# api/routes/auth_routes.py

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from application.dtos.dto_auth import (
    Login,
    TokenResponse
)

from application.services.auth_service import AuthService
from core.dependencias import get_usuario_repository


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data: Login,
    repo=Depends(get_usuario_repository)
):

    service = AuthService(repo)

    try:
        return service.login(data)

    except Exception as ex:
        raise HTTPException(
            status_code=401,
            detail=str(ex)
        )