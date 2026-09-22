from core.roles import ROLES_VALIDOS
from application.dtos.dto_rol_permisos import RolReponseDTO


class RolService:

    @staticmethod
    def listar_roles() -> list[RolReponseDTO]:
        return [
            RolReponseDTO(
                key=rol,
                text=rol
            )
            for rol in ROLES_VALIDOS
        ]