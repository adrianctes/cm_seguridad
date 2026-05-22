from infrastructura.db.models.historia_laboral_model import HistoriaLaboralModel


class MySQLHistoriaLaboralRepository:

    def __init__(self, db):

        self.db = db

    # =========================================
    # CREATE
    # =========================================

    def crear(self, historia):

        self.db.add(historia)

        self.db.commit()

        self.db.refresh(historia)

        return historia

    # =========================================
    # READ
    # =========================================

    def listar_por_legajo(self, legajo_id: int):

        return (
            self.db.query(HistoriaLaboralModel)
            .filter(
                HistoriaLaboralModel.legajo_id == legajo_id
            )
            .order_by(
                HistoriaLaboralModel.fecha.desc()
            )
            .all()
        )

    def obtener_por_id(self, movimiento_id: int):

        return (
            self.db.query(HistoriaLaboralModel)
            .filter(
                HistoriaLaboralModel.id == movimiento_id
            )
            .first()
        )

    def obtener_ultimo_movimiento(
        self,
        legajo_id: int
    ):

        return (
            self.db.query(HistoriaLaboralModel)
            .filter(
                HistoriaLaboralModel.legajo_id == legajo_id
            )
            .order_by(
                HistoriaLaboralModel.fecha.desc()
            )
            .first()
        )

    def listar_por_tipo(
        self,
        tipo_movimiento_id: int
    ):

        return (
            self.db.query(HistoriaLaboralModel)
            .filter(
                HistoriaLaboralModel.tipo_movimiento_id
                == tipo_movimiento_id
            )
            .all()
        )

    # =========================================
    # UPDATE
    # =========================================

    def guardar(self):

        self.db.commit()

    # =========================================
    # DELETE
    # =========================================

    def eliminar(self, historia):

        self.db.delete(historia)

        self.db.commit()