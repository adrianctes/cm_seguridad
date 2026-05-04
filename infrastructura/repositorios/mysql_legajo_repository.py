from sqlalchemy.exc import SQLAlchemyError
from domain.entidades.modalidad_liquidacion import ModalidadLiquidacion
from domain.repositorios.legajo_repositorio import LegajoRepository
from domain.entidades.legajo import Legajo
from infrastructura.db.models.legajo_model import LegajoModel
from infrastructura.db.models.categoria_model import CategoriaModel
from sqlalchemy.orm import joinedload

from infrastructura.db.models.modalidad_liquidacion import ModalidadLiquidacionModel


class MySQLLegajoRepository(LegajoRepository):

    def __init__(self, db):
        self.db = db

    def obtener_por_id(self, legajo_id: int):
        model = self.db.query(LegajoModel).filter_by(id=legajo_id).first()
        return self._to_entity(model)

    def obtener_por_cuil(self, cuil: str):
        model = self.db.query(LegajoModel).filter_by(cuil=cuil).first()
        return self._to_entity(model)

    def listar(self):
        #try:
            modelos = (
                self.db.query(LegajoModel)
                .options(joinedload(LegajoModel.categoria)) 
                .options(joinedload(LegajoModel.modalidad_liquidacion))  # 🔥 clav
                .all()
    )
    
            return [self._to_entity(m) for m in modelos]

        #except SQLAlchemyError as e:
        #    raise Exception("Error al consultar legajos en base de datos")
        
    def guardar(self, legajo: Legajo):
        if legajo.id:
            model = self.db.query(LegajoModel).get(legajo.id)
        else:
            model = LegajoModel()

        model.apellido = legajo.apellido
        model.nombre = legajo.nombre
        model.sexo = legajo.sexo
        model.cuil = legajo.cuil
        model.activo = legajo.activo
        model.sac =legajo.sac
        model.categoria_id = legajo.categoria_id
        model.modalidad_liquidacion_id = legajo.modalidad_liquidacion_id
      
        try:
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
     
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(f"Error al crear legajo en base de datos {error_msg}")    


        return self._to_entity(model)

    # 🔥 mapper interno
    def _to_entity(self, m: LegajoModel):
        categoria = None

        if m.categoria:
            categoria = CategoriaModel(
                id=m.categoria.id,
                nombre = m.categoria.nombre,
                descripcion=m.categoria.descripcion
            )
        if m.modalidad_liquidacion:
            modalidad_liquidacion = ModalidadLiquidacionModel(
                id=m.modalidad_liquidacion.id,
                nombre = m.modalidad_liquidacion.nombre
            ) 

            return Legajo(
                id=m.id,
                apellido=m.apellido,
                nombre=m.nombre,
                sexo=m.sexo,
                cuil=m.cuil,
                categoria_id=m.categoria_id,
                categoria=categoria,
                modalidad_liquidacion_id= m.modalidad_liquidacion_id,
                modalidad_liquidacion=modalidad_liquidacion,
                activo=m.activo,
                sac = m.sac
            )
    