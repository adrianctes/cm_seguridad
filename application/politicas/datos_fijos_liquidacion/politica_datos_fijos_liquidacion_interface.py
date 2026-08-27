from abc import ABC
from abc import abstractmethod

from  .politica_datos_fijos_entidad import PoliticaDatosFijosEntidad

class IPoliticaDatosFijosRepository(ABC):

    @abstractmethod
    def obtener(
        self,
        tipo_liquidacion_id: int,
        modalidad_liquidacion_id: int
    ) -> PoliticaDatosFijosEntidad | None:
        pass