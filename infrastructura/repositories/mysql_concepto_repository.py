from infrastructura.db.models.conceptos import ConceptoModel
from sqlalchemy.exc import SQLAlchemyError

class MySQLConceptoRepository:

    def __init__(self, db):
        self.db = db

    def crear(self, data):
        try:
            model = ConceptoModel(
                codigo=data.codigo,
                nombre=data.nombre,
                tipo=data.tipo,
                es_remunerativo=data.es_remunerativo,
                activo=data.activo,
                requiere_novedad=data.requiere_novedad
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

    def obtener(self, concepto_id: int):
        return self.db.query(ConceptoModel).filter_by(id=concepto_id).first()

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