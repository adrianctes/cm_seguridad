# domain/repositories/usuario_repository.py

from abc import ABC, abstractmethod
from domain.entities.usuario_entity import Usuario


class UsuarioRepository(ABC):

    @abstractmethod
    def guardar(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_por_id(self, usuario_id: int):
        pass

    @abstractmethod
    def obtener_por_username(self, username: str):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def eliminar(self, usuario_id: int):
        pass