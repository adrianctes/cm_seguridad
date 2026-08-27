from abc import ABC
from abc import abstractmethod

from domain.entities.datos_fijos_liquidacion_entity import DatosFijosLiquidacion


class IPolitica(ABC):

    @abstractmethod
    def validar(
        self,
        entidad: DatosFijosLiquidacion
    ) -> None:
        pass