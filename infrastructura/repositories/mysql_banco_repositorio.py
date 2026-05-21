from infrastructura.db.models.banco_model import BancoModel

class MySQLBancoRepository:

    def __init__(self, db):
        self.db = db

   
    def listar(self):
        return self.db.query(BancoModel).all()

    
  