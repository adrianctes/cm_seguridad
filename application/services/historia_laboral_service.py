from domain.entities.historia_laboral_entity import HistoriaLaboral
from domain.repositories.historia_laboral_interface import IHistoriaLaboral


class HistoriaLaboralService:

    def __init__(self, repo: IHistoriaLaboral):
        self.repo = repo

    # =========================================
    # CREATE
    # =========================================

    def crear_movimiento(
        self,
        legajo_id: int,
        data
    ):

        historia = HistoriaLaboral(
            legajo_id=legajo_id,
            tipo_movimiento_id=data.tipo_movimiento_id,
            fecha=data.fecha,
            observacion=data.observacion
        )

        return self.repo.crear(historia)

    # =========================================
    # READ
    # =========================================

    def listar_por_legajo(
        self,
        legajo_id: int
    ):

        return self.repo.listar_por_legajo(legajo_id)

    def obtener_por_id(
        self,
        movimiento_id: int
    ):

        movimiento = self.repo.obtener_por_id(
            movimiento_id
        )

        if not movimiento:
            raise Exception(
                "Movimiento no encontrado"
            )

        return movimiento

    def obtener_ultimo_movimiento(
        self,
        legajo_id: int
    ):

        return self.repo.obtener_ultimo_movimiento(
            legajo_id
        )

    def listar_por_tipo(
        self,
        tipo_movimiento_id: int
    ):

        return self.repo.listar_por_tipo(
            tipo_movimiento_id
        )

    # =========================================
    # UPDATE
    # =========================================

    def editar_movimiento(
        self,
        movimiento_id: int,
        data
    ):

        movimiento = self.repo.obtener_por_id(
            movimiento_id
        )

        if not movimiento:
            raise Exception(
                "Movimiento no encontrado"
            )

        movimiento.tipo_movimiento_id = (
            data.tipo_movimiento_id
        )

        movimiento.fecha = data.fecha

        movimiento.observacion = (
            data.observacion
        )

        self.repo.guardar()

        return movimiento

    # =========================================
    # DELETE
    # =========================================

    def eliminar_movimiento(
        self,
        movimiento_id: int
    ):

        movimiento = self.repo.obtener_por_id(
            movimiento_id
        )

        if not movimiento:
            raise Exception(
                "Movimiento no encontrado"
            )

        self.repo.eliminar(movimiento)

        return True