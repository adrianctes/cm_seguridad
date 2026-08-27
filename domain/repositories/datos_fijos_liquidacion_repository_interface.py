from abc import ABC, abstractmethod

from domain.entities.datos_fijos_liquidacion_entity import DatosFijosLiquidacion


class IDatosFijosLiquidacionRepository(ABC):

    
    @abstractmethod
    def obtener(self, id: int) -> DatosFijosLiquidacion | None:
        pass

    @abstractmethod
    def crear(
        self,
        datos_fijos_liquidacion: DatosFijosLiquidacion
    ) -> DatosFijosLiquidacion:
        pass

    @abstractmethod
    def actualizar(
        self,
        datos_fijos_liquidacion: DatosFijosLiquidacion
    ) -> DatosFijosLiquidacion:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass


    @abstractmethod
    def listar_por_periodo(self, periodo:str) -> list[DatosFijosLiquidacion]:
        pass


    