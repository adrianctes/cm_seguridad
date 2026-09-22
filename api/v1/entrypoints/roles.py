from fastapi import APIRouter
from application.dtos.dto_rol_permisos import RolReponseDTO
from application.services.roles_service import RolService

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.get(
    "",
    response_model=list[RolReponseDTO]
)
async def listar_roles():
    return RolService.listar_roles()