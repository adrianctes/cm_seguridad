from sqlalchemy.exc import SQLAlchemyError
from domain.repositories.legajo_repositorio_interface import ILegajoRepository
from domain.entities.legajo_entity import Legajo
from infrastructura.db.models.legajo_model import LegajoModel
from infrastructura.db.models.categoria_model import CategoriaModel
from sqlalchemy.orm import joinedload

from infrastructura.db.models.liquidacion_model import LiquidacionModel
from infrastructura.db.models.modalidad_liquidacion_model import ModalidadLiquidacionModel


class MySQLLegajoRepository(ILegajoRepository):

    def __init__(self, db):
        self.db = db

    def obtener_por_id(self, legajo_id: int):
        try :
            model = self.db.query(LegajoModel).filter_by(id=legajo_id).first()
            if not model:
                raise ValueError("Legajo no encontrado")
            
            return self._to_entity(model)
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(f"Error legajo no existe {error_msg}.")    

    def obtener_por_cuil(self, cuil: str):
        model = self.db.query(LegajoModel).filter_by(cuil=cuil).first()
        return self._to_entity(model)

    def listar(self):
        try:
            modelos = (
                self.db.query(LegajoModel)
                .options(joinedload(LegajoModel.categoria)) 
                .options(joinedload(LegajoModel.modalidad_liquidacion))
                .all()
    )
    
            return [self._to_entity(m) for m in modelos]

        except SQLAlchemyError as e:
            raise Exception("Error al consultar legajos en base de datos")

    def listar_activos(self):
        try:
            modelos = (
                self.db.query(LegajoModel)
                .options(joinedload(LegajoModel.categoria)) 
                .options(joinedload(LegajoModel.modalidad_liquidacion))
                .filter(LegajoModel.activo == 1)
                .all()
    )

            return [self._to_entity(m) for m in modelos]

        except SQLAlchemyError as e:
            raise Exception("Error al consultar legajos en base de datos")

    def listar_por_modalidad(
            self,
            modalidad_liquidacion_id: int
        ):
          
            registros = (

                self.db.query(LegajoModel)

                .filter(

                    LegajoModel.modalidad_liquidacion_id
                    == modalidad_liquidacion_id,

                    LegajoModel.activo == True

                )

                .all()

            )

            return [
                self._to_entity(x)
                for x in registros
            ]
        
    def buscar_legajos_disponibles_para_liquidacion(
        self,
        modalidad_liquidacion_id: int,
        datos_fijos_liquidacion_id: int
    ):

        subquery = (
            self.db.query(LiquidacionModel.legajo_id)
            .filter(
                LiquidacionModel.datos_fijos_liquidacion_id
                == datos_fijos_liquidacion_id
            )
        )

        return (
            self.db.query(LegajoModel)
            .filter(
                LegajoModel.modalidad_liquidacion_id
                == modalidad_liquidacion_id,
                ~LegajoModel.id.in_(subquery)
            )
            .all()
        )

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
        model.telefono = legajo.telefono
        model.categoria_id = legajo.categoria_id
        model.modalidad_liquidacion_id = legajo.modalidad_liquidacion_id
        model.banco_id = legajo.banco_id
        model.cbu = legajo.cbu
        model.modalidad_pago_id = legajo.modalidad_pago_id
        model.valor_modalidad_pago = legajo.valor_modalidad_pago
       # model.categoria =legajo.categoria
        #model.modalidad_liquidacion =legajo.modalidad_liquidacion
       
    
        try:
            if model.id is None :
              self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
           
        except SQLAlchemyError as e:
            print(e)
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)    


        return self._to_entity(model)

    def eliminar(self, legajo_id: int):

        legajo = (
            self.db.query(LegajoModel)
            .filter(LegajoModel.id == legajo_id)
            .first()
        )

        if not legajo:
            raise Exception("Legajo no encontrado")

        self.db.delete(legajo)

        self.db.commit()
    
    # 🔥 mapper interno
    def _to_entity(self, m: LegajoModel):
        categoria = None
        modalidad_liquidacion = None

        if m.categoria_id:
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
                modalidad_liquidacion_id= m.modalidad_liquidacion_id,
                categoria=categoria,
                modalidad_liquidacion=modalidad_liquidacion,
                activo=m.activo,
                sac = m.sac,
                telefono =  m.telefono,
                banco = m.banco,
                banco_id = m.banco_id,
                cbu = m.cbu,
                fecha_ingreso_actual = m.fecha_ingreso_actual,
                modalidad_pago_id = m.modalidad_pago_id,
                valor_modalidad_pago = m.valor_modalidad_pago
            )
    
    def actualizar_fecha_ingreso_actual(
        self,
        legajo_id,
        fecha,
        activo
    ):
        
        try: 
            model = (
                self.db.query(LegajoModel)
                .filter_by(id=legajo_id)
                .first()
            )

            if not model:
                raise Exception(
                    "Legajo no encontrado"
                )

            model.fecha_ingreso_actual = fecha
            model.activo = activo
            self.db.flush()
            return model
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)    