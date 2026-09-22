from core.roles import ROLES_VALIDOS

class AutorizacionService:

    def __init__(self, repository):
        self.repository = repository

    def listar_permisos(self):
        return self.repository.listar_permisos()

    def listar_permisos_por_rol(self, rol: str):

        self._validar_rol(rol)

        return self.repository.listar_permisos_por_rol(rol)

    def obtener_ids_por_rol(self, rol: str):

        self._validar_rol(rol)

        return self.repository.obtener_ids_por_rol(rol)

    def guardar_permisos_rol(
        self,
        rol: str,
        permisos_ids: list[int]
    ):

        self._validar_rol(rol)

        self.repository.guardar_permisos_rol(
            rol=rol,
            permisos_ids=permisos_ids or []
        )

    def tiene_permiso(
        self,
        rol: str,
        codigo: str
    ) -> bool:

        if not rol or not codigo:
            return False

        return self.repository.tiene_permiso(
            rol=rol,
            codigo=codigo
        )

    def _validar_rol(self, rol: str):

        if rol not in ROLES_VALIDOS:
            raise ValueError(
                f"Rol no válido: {rol}"
            )