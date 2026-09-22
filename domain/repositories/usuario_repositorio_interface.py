# domain/repositories/usuario_repository.py

from abc import ABC, abstractmethod
from domain.entities.usuario_entity import Usuario


class IUsuarioRepository(ABC):

    @abstractmethod
    def guardar(self, usuario: Usuario):
        pass

    @abstractmethod
    async def obtener_por_id(self, usuario_id: int):
        pass

    @abstractmethod
    def obtener_por_username(self, username: str):
        pass

    @abstractmethod
    def cambiar_estado(self,  usuario: Usuario):
        pass

    @abstractmethod
    async def cambiar_password(self,  usuario_id:int, password_hash: str):
        pass

    @abstractmethod
    def listar(self,  
               busqueda: str | None = None,
               activo: bool | None = None):
        pass

    @abstractmethod
    def eliminar(self, usuario_id: int):
        pass