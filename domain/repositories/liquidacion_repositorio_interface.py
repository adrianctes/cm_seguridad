from abc import ABC, abstractmethod
from typing import List
from domain.entities.liquidacion import Liquidacion

class LiquidacionRepository(ABC):

    @abstractmethod
    def crear(self, liquidacion: Liquidacion) -> Liquidacion:
        pass
    @abstractmethod
    def actualizar(self, id: int, liquidacion : Liquidacion):
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Liquidacion:
        pass

    @abstractmethod
    def listar_por_legajo(self, legajo_id: int) -> List[Liquidacion]:
        pass

    @abstractmethod
    def eliminar(self, id: int):
        pass