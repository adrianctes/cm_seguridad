from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.legajo_entity import Legajo


class LegajoRepository(ABC):

    @abstractmethod
    def obtener_por_id(self, legajo_id: int) -> Optional[Legajo]:
        pass

    @abstractmethod
    def obtener_por_cuil(self, cuil: str) -> Optional[Legajo]:
        pass

    @abstractmethod
    def listar(self) -> List[Legajo]:
        pass

    @abstractmethod
    def guardar(self, legajo: Legajo) -> Legajo:
        pass

   # @abstractmethod
   # def eliminar(self, legajo_id: int) -> None:
   #     pass