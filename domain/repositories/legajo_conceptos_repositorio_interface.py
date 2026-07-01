from abc import ABC, abstractmethod

from domain.entities.legajo_concepto_entity import LegajoConcepto


class ILegajoConceptoRepository(ABC):

    @abstractmethod
    def crear(
        self,
        entity: LegajoConcepto
    ) -> LegajoConcepto:
        pass

    @abstractmethod
    def actualizar(
        self,
        id: int,
        entity: LegajoConcepto
    ) -> LegajoConcepto:
        pass

    @abstractmethod
    def obtener(
        self,
        id: int
    ) -> LegajoConcepto | None:
        pass

    @abstractmethod
    def listar(
        self,
        legajo_id: int
    ) -> list[LegajoConcepto]:
        pass

    @abstractmethod
    def eliminar(
        self,
        id: int
    ) -> bool:
        pass