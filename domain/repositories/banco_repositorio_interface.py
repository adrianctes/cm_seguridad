from abc import ABC, abstractmethod


class IBancoRepository(ABC):

    @abstractmethod
    def listar(self):
        pass
