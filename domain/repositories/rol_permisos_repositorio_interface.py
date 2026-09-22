from abc import ABC, abstractmethod


class IRolPermisosRepository(ABC):

    @abstractmethod
    def listar_permisos(self):
        pass

    @abstractmethod
    def listar_permisos_por_rol(self, rol: str):
        pass

    @abstractmethod
    def guardar_permisos_rol(
        self,
        rol: str,
        permisos_ids: list[int],
    ):
        pass

    @abstractmethod
    def tiene_permiso(
        self,
        rol: str,
        codigo: str,
    ) -> bool:
        pass