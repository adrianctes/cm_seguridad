from domain.entities.concepto_entity import Concepto
from domain.repositories.concepto_repositorio_interface import IConceptoRepository

class ConceptoService:

    def __init__(self, repo:IConceptoRepository):
        self.repo = repo

    # 🔹 Crear
    def crear(self, data):
        concepto = Concepto(
            codigo=data.codigo,
            nombre=data.nombre,
            clasificacion_concepto_id = data.clasificacion_concepto_id,
            tipo_calculo=data.tipo_calculo,
            formula= data.formula,
            activo=data.activo,
            es_novedad=data.es_novedad,
            modalidad_pago_id = data.modalidad_pago_id,
            orden = data.orden
        )
     
        return self.repo.crear(concepto)

    # 🔹 Listar
    def listar(self):
        return self.repo.listar()

    # 🔹 Obtener por ID
    def obtener(self, id: int):
        concepto = self.repo.obtener(id)
        print(concepto.__dict__)
        if not concepto:
            raise ValueError("Concepto no encontrado")
        return concepto

    # 🔹 Actualizar (PUT)
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