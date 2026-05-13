from domain.entities.concepto_entity import Concepto
from domain.repositories.modalidad_repositorio_interface import IModalidadRepository

class ModalidadLiquidacionService:

    def __init__(self, repo:IModalidadRepository):
        self.repo = repo

    # 🔹 Listar
    def listar(self):
        return self.repo.listar()

  