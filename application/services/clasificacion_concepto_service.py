from domain.repositories.clasificacion_concepto_interface import IClasificacionConceptoRepository

class ClasificacionConceptoService:

    def __init__(self, repo:IClasificacionConceptoRepository):
        self.repo = repo

    # 🔹 Listar
    def listar(self):
        return self.repo.listar()
