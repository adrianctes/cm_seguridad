from domain.entities.historia_laboral_entity import HistoriaLaboral
from infrastructura.db.models.historia_laboral_model import HistoriaLaboralModel


class MySQLHistoriaLaboralRepository:

    def __init__(self, db):

        self.db = db

    # =========================================
    # CREATE
    # =========================================

    def crear(self, historia:HistoriaLaboral ):

        try:

            model = HistoriaLaboralModel(

                legajo_id=historia.legajo_id,

                tipo_id=historia.tipo_id,

                fecha=historia.fecha,

                observacion=historia.observacion            
            )

            self.db.add(model)
            self.db.flush()

            return model

        except Exception as ex:

            self.db.rollback()

            print("ERROR SQL:", repr(ex))

            raise ex

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
                HistoriaLaboralModel.id.desc()
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
                HistoriaLaboralModel.id.desc()
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