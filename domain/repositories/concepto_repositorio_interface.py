from abc import ABC, abstractmethod
from typing import Optional


class IConceptoRepository(ABC):

    @abstractmethod
    def crear(self, data):
        pass

    @abstractmethod
    def listar(self, params: dict):
        pass

    @abstractmethod
    def listar_novedades(self, params: dict):
            pass 

    @abstractmethod
    def obtener(self, concepto_id: int):
        pass

    @abstractmethod
    def obtener_ultimo_codigo(self)-> int:
        pass

    @abstractmethod
    def obtener_secuencia_maxima(self) -> Optional[int]:
        pass

    @abstractmethod
    def actualizar(self, concepto_id: int, data):
        pass

    @abstractmethod
    def eliminar(self, concepto_id: int):
        pass