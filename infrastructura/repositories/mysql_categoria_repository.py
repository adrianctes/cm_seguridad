from infrastructura.db.models.categoria_model import CategoriaModel

class MySQLCategoriaRepository:

    def __init__(self, db):
        self.db = db

   
    def listar(self):
        return self.db.query(CategoriaModel).all()

    
  