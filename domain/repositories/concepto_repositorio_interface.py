from abc import ABC, abstractmethod


class IConceptoRepository(ABC):

    @abstractmethod
    def crear(self, data):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener(self, concepto_id: int):
        pass

    @abstractmethod
    def actualizar(self, concepto_id: int, data):
        pass

    @abstractmethod
    def eliminar(self, concepto_id: int):
        pass