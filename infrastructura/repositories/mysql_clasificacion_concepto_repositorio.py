from infrastructura.db.models.clasificacion_concepto_model import ClasificacionConceptoModel

class MySQLClasificacionConceptoRepository:

    def __init__(self, db):
        self.db = db

   
    def listar(self):
        return self.db.query(ClasificacionConceptoModel).all()
