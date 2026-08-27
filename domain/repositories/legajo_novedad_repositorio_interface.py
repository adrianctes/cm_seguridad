from abc import ABC, abstractmethod
from datetime import date
from typing import List
from domain.entities.novedad_entity import Novedad


class LegajoNovedadRepository(ABC):

    @abstractmethod
    def crear(self, novedad: Novedad) -> Novedad:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Novedad:
        pass

    @abstractmethod
    def obtener_por_periodo(self, fecha : date,
                                  tipo_busqueda: str | None = None,
                                  busqueda: str | None = None,) -> List[Novedad]:
        pass
 
    @abstractmethod
    def listar_por_legajo(self, legajo_id: int) -> List[Novedad]:
        pass

    @abstractmethod
    def listar_vigentes(self, legajo_id: int, fecha):
        pass

    @abstractmethod
    def actualizar(self, novedad: Novedad) -> Novedad:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass