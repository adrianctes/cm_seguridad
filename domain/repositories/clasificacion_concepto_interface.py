from abc import ABC, abstractmethod

class IClasificacionConceptoRepository(ABC):

    @abstractmethod
    def listar(self):
        pass
