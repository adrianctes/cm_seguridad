from infrastructura.db.models.conceptos_model import ConceptoModel
from sqlalchemy import func, select
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
                tipo_calculo=data.tipo_calculo,
                formula = data.formula,
                activo=data.activo,
                es_novedad=data.es_novedad,
                abreviatura=data.abreviatura,
                unidad_medida=data.unidad_medida,
                secuencia=data.secuencia
            )

            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)
            return model

        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)

    def listar(self, params: dict):

        query = self.db.query(ConceptoModel)

        activo = params.get("activo")
        busqueda = params.get("busqueda")

        # FILTRO POR ACTIVO
        if activo is not None:
            query = query.filter(
                ConceptoModel.activo == activo
            )

        # BÚSQUEDA POR CÓDIGO O NOMBRE
        if busqueda:
            busqueda = busqueda.strip()

            query = query.filter(
                (ConceptoModel.codigo.ilike(f"%{busqueda}%")) |
                (ConceptoModel.nombre.ilike(f"%{busqueda}%"))
            )

        return query.all()

    def listar_novedades(self, params: dict):
    
            query = self.db.query(ConceptoModel)
    
            activo = params.get("activo")
            busqueda = params.get("busqueda")
            es_novedad= True
            query = query.filter(
                                ConceptoModel.es_novedad== es_novedad
                            )
    
            # FILTRO POR ACTIVO
            if activo is not None:
                query = query.filter(
                    ConceptoModel.activo == activo
                )
    
            # BÚSQUEDA POR CÓDIGO O NOMBRE
            if busqueda:
                busqueda = busqueda.strip()
    
                query = query.filter(
                    (ConceptoModel.codigo.ilike(f"%{busqueda}%")) |
                    (ConceptoModel.nombre.ilike(f"%{busqueda}%"))
                )
                
    
            return query.all()
        
    
    def obtener(self, id: int):
        return self.db.query(ConceptoModel).filter_by(id=id).first()

    def obtener_ultimo_codigo(self) -> int:
        stmt = select(func.max(ConceptoModel.codigo))
        ultimo_codigo = self.db.execute(stmt).scalar_one()

        return ultimo_codigo or 1
      
    def obtener_secuencia_maxima(self):
        # FOR UPDATE serializa la lectura del máximo frente a creaciones concurrentes
        return (
            self.db.query(func.max(ConceptoModel.secuencia))
            .with_for_update()
            .scalar()
        )

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
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)    