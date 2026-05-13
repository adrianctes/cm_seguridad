from abc import ABC, abstractmethod


class ICategoriaRepository(ABC):

    @abstractmethod
    def listar(self):
        pass
