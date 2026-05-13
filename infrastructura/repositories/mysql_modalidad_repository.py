from infrastructura.db.models.modalidad_liquidacion import ModalidadLiquidacionModel

class MySQLModalidadLiquidacionRepository:

    def __init__(self, db):
        self.db = db

   
    def listar(self):
        return self.db.query(ModalidadLiquidacionModel).all()