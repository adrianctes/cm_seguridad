from infrastructura.db.models.conceptos_model import ConceptoModel
from sqlalchemy.exc import SQLAlchemyError

class MySQLConceptoRepository:

    def __init__(self, db):
        self.db = db

    def crear(self, data):
        try:
            model = ConceptoModel(
                codigo=data.codigo,
                nombre=data.nombre,
                orden = data.orden,
                clasificacion_concepto_id = data.clasificacion_concepto_id,
                modalidad_pago_id = data.modalidad_pago_id,
                tipo_calculo=data.tipo_calculo,
                formula = data.formula,
                activo=data.activo,
                es_novedad=data.es_novedad
            )

            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return model

        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)

    def listar(self):
        return self.db.query(ConceptoModel).all()
    
    
    def obtener(self, id: int):
        return self.db.query(ConceptoModel).filter_by(id=id).first()
    
   
    def obtener_por_modalidad_pago(self,modalidad_pago_id: int, es_novedad:bool=False):
        query = self.db.query(ConceptoModel)

        if modalidad_pago_id is not None:

            query = query.filter(
                ConceptoModel.modalidad_pago_id.in_(
                    [modalidad_pago_id, 0]
                ),
                ConceptoModel.es_novedad == es_novedad
            )

        return query.all()

    def actualizar(self, concepto_id: int, data):
        model = self.obtener(concepto_id)
        if not model:
            return None

        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(model, key, value)

        try:
            self.db.commit()
            self.db.refresh(model)
            return model
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)    

    def eliminar(self, concepto_id: int):
        model = self.obtener(concepto_id)
        if not model:
            return None
        try:
            self.db.delete(model)
            self.db.commit()
            return model
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)    