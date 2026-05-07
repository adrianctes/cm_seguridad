from abc import ABC, abstractmethod
from typing import List
from domain.entities.concepto_novedad_entity import ConceptoNovedad


class ConceptoNovedadRepository(ABC):

    @abstractmethod
    def crear(self, novedad: ConceptoNovedad) -> ConceptoNovedad:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> ConceptoNovedad:
        pass

    @abstractmethod
    def listar_por_legajo(self, legajo_id: int) -> List[ConceptoNovedad]:
        pass

    @abstractmethod
    def listar_vigentes(self, legajo_id: int, fecha):
        pass

    @abstractmethod
    def actualizar(self, novedad: ConceptoNovedad) -> ConceptoNovedad:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass