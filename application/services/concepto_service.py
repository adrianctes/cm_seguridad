from domain.entities.concepto_entity import Concepto
from domain.repositories.concepto_repositorio_interface import IConceptoRepository

class ConceptoService:

    def __init__(self, repo:IConceptoRepository):
        self.repo = repo

    # 🔹 Crear
    def crear(self, data):
        concepto = Concepto(
            id = None,
            codigo=data.codigo,
            nombre=data.nombre,
            tipo=data.tipo,
            es_remunerativo=data.es_remunerativo,
            activo=data.activo,
            requiere_novedad=data.requiere_novedad
        )

        return self.repo.crear(concepto)

    # 🔹 Listar
    def listar(self):
        return self.repo.listar()

    # 🔹 Obtener por ID
    def obtener(self, concepto_id: int):
        concepto = self.repo.obtener(concepto_id)
        if not concepto:
            raise ValueError("Concepto no encontrado")
        return concepto

    # 🔹 Actualizar (PATCH)
    def actualizar(self, concepto_id: int, data):
        concepto = self.repo.actualizar(concepto_id, data)
        if not concepto:
            raise ValueError("Concepto no encontrado")
        return concepto

    # 🔹 Eliminar
    def eliminar(self, concepto_id: int):
        concepto = self.repo.eliminar(concepto_id)
        if not concepto:
            raise ValueError("Concepto no encontrado")
        return concepto