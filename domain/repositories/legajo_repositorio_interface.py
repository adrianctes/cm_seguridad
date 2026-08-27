from abc import ABC, abstractmethod
import datetime
from typing import List, Optional

from domain.entities.legajo_entity import Legajo


class ILegajoRepository(ABC):

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
    def listar_activos(self) -> List[Legajo]:
        pass

    @abstractmethod
    def listar_por_modalidad(self) -> List[Legajo]:
            pass
    

    @abstractmethod
    def guardar(self, legajo: Legajo) -> Legajo:
        pass

    @abstractmethod
    def eliminar(self, legajo_id: int) -> None:
        pass
   
    @abstractmethod
    def actualizar_fecha_ingreso_actual(
        self,
        legajo_id: int,
        fecha: datetime,
        valor: bool
        ):pass
    
