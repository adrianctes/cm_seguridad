from domain.entidades.legajo import Legajo
from domain.repositorios.legajo_repositorio import LegajoRepository


class LegajoService:

    def __init__(self, legajo_repo: LegajoRepository):
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
            activo=True
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
       

    # =========================
    # 🔹 LISTAR
    # =========================
    def listar(self):
        try:
           return self.legajo_repo.listar()
        except Exception as e:
            raise Exception(str(e))

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
        legajo = self.obtener(legajo_id)

        legajo.activo = False

        return self.legajo_repo.guardar(legajo)

