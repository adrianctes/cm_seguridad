from domain.entities.concepto_entity import Concepto
from domain.repositories.concepto_repositorio_interface import IConceptoRepository

class ConceptoService:

    def __init__(self, repo:IConceptoRepository):
        self.repo = repo

    # 🔹 Crear
    def crear(self, data):
        # Secuencia: máximo existente + 10; si no hay conceptos, comienza en 10
        secuencia = (self.repo.obtener_secuencia_maxima() or 0) + 10
        codigo =   (self.repo.obtener_ultimo_codigo()) + 1
        concepto = Concepto(
            codigo=codigo,
            nombre=data.nombre,
            clasificacion_concepto_id = data.clasificacion_concepto_id,
            tipo_calculo=data.tipo_calculo,
            formula= data.formula,
            activo=data.activo,
            es_novedad=data.es_novedad,
            orden = data.orden,
            abreviatura = data.abreviatura,
            unidad_medida = data.unidad_medida,
            secuencia = secuencia
        )
        print(concepto) 
        return self.repo.crear(concepto)

    # 🔹 Listar
    def listar(self, params: dict):
        return self.repo.listar(params)
    
        # 🔹 Listar novedades
    def listar_novedades(self, params: dict):
        return self.repo.listar_novedades(params)
    
     
    # 🔹 Obtener por ID
    def obtener(self, id: int):
        concepto = self.repo.obtener(id)
        
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
        self.repo.eliminar(concepto_id)
      