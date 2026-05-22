from abc import ABC
from abc import abstractmethod


class IHistoriaLaboral(ABC):

    # =========================================
    # CREATE
    # =========================================

    @abstractmethod
    def crear_movimiento(
        self,
        legajo_id: int,
        data
    ):
        pass

    # =========================================
    # READ
    # =========================================

    @abstractmethod
    def obtener_por_id(
        self,
        movimiento_id: int
    ):
        pass

    @abstractmethod
    def listar_por_legajo(
        self,
        legajo_id: int
    ):
        pass

    @abstractmethod
    def obtener_ultimo_movimiento(
        self,
        legajo_id: int
    ):
        pass

    @abstractmethod
    def listar_por_tipo(
        self,
        tipo_movimiento_id: int
    ):
        pass

    @abstractmethod
    def listar_entre_fechas(
        self,
        fecha_desde,
        fecha_hasta
    ):
        pass

    # =========================================
    # UPDATE
    # =========================================

    @abstractmethod
    def editar_movimiento(
        self,
        movimiento_id: int,
        data
    ):
        pass

    # =========================================
    # DELETE
    # =========================================

    @abstractmethod
    def eliminar_movimiento(
        self,
        movimiento_id: int
    ):
        pass