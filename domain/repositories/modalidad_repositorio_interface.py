from abc import ABC, abstractmethod


class IModalidadRepository(ABC):

    @abstractmethod
    def listar(self):
        pass

   