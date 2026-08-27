from domain.entities.legajo_entity import Legajo
from domain.repositories.datos_fijos_liquidacion_repository_interface import IDatosFijosLiquidacionRepository
from domain.repositories.legajo_repositorio_interface import ILegajoRepository


class LegajoService:

    def __init__(self, legajo_repo: ILegajoRepository):
        self.legajo_repo = legajo_repo

    # =========================
    # 🔹 CREAR
    # =========================
    def crear(self, data):
        #existente = self.legajo_repo.obtener_por_cuil(data.cuil)
        #if existente:
        #    raise ValueError("Ya existe un legajo con ese CUIL")
      
        legajo = Legajo(
            id=None,
            apellido=data.apellido,
            nombre=data.nombre,
            sexo=data.sexo,
            cuil=data.cuil,
            categoria_id=data.categoria_id,
            categoria =  None,
            modalidad_liquidacion_id=data.modalidad_liquidacion_id,
            modalidad_liquidacion= None,
            banco_id= data.banco_id,
            modalidad_pago_id = data.modalidad_pago_id,
            valor_modalidad_pago = data.valor_modalidad_pago
        )
      
        return  self.legajo_repo.guardar(legajo)
    # =========================
    # 🔹 OBTENER
    # =========================
    def obtener(self, legajo_id: int):
        
            legajo = self.legajo_repo.obtener_por_id(legajo_id)
            
            if not legajo:
                raise ValueError("Legajo no encontrado")
            return legajo
       
    def buscar_legajos_disponibles_para_liquidacion(
        self,
        repo_datos_fijos: IDatosFijosLiquidacionRepository,
        datos_fijos_liquidacion_id: int
    ):

        datos_fijos = repo_datos_fijos.obtener(
            datos_fijos_liquidacion_id
        )

        if not datos_fijos:
            raise ValueError(
                "No existen los datos fijos de liquidación."
            )

        return self.legajo_repo.buscar_legajos_disponibles_para_liquidacion(
            modalidad_liquidacion_id=
                datos_fijos.modalidad_liquidacion_id,

            datos_fijos_liquidacion_id=
                datos_fijos_liquidacion_id
        )
    
    # =========================
    # 🔹 LISTAR
    # =========================
    def listar(self):
        try:
           return self.legajo_repo.listar()
        except Exception as e:
            raise Exception(str(e))
    
    def listar_activos(self):
        try:
           return self.legajo_repo.listar_activos()
        except Exception as e:
            raise Exception(str(e))

    def listar_por_modalidad(
        self,
        modalidad_liquidacion_id: int
    ):
        return self.legajo_repo.listar_por_modalidad(
            modalidad_liquidacion_id
        )
    
    # =========================
    # 🔹 ACTUALIZAR
    # =========================
    def actualizar(self, legajo_id: int, data):
        legajo = self.obtener(legajo_id)

        for key, value in data.dict(exclude_unset=True).items():
            setattr(legajo, key, value)

        return self.legajo_repo.guardar(legajo)

    # =========================
    # 🔹 ELIMINAR (soft)
    # =========================
    def eliminar(self, legajo_id: int): 
        self.legajo_repo.eliminar(legajo_id)

    # =========================
    # LEGAJO CONCEPTOS 
    # =========================
    def listar_legajo_conceptos(self, legajo_id : int):
        try:
           return self.legajo_repo.listar_legajo_conceptos(legajo_id)
        except Exception as e:
            raise Exception(str(e))
    


