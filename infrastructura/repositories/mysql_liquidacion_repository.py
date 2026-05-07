from sqlalchemy.orm import Session, joinedload
from domain.entities.liquidacion import Liquidacion
from domain.repositories.liquidacion_repositorio_interface import LiquidacionRepository
from infrastructura.db.models.liquidacion_model import LiquidacionModel
from sqlalchemy.exc import SQLAlchemyError

class MySQLLiquidacionRepository(LiquidacionRepository):

    def __init__(self, db: Session):
        self.db = db

    def crear(self, liquidacion: Liquidacion) -> Liquidacion:
        model = LiquidacionModel(
            legajo_id=liquidacion.legajo_id,
            concepto_id=liquidacion.concepto_id,
            valor=liquidacion.valor,
            tipo_liquidacion_id=liquidacion.tipo_liquidacion_id
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return Liquidacion(
            id=model.id,
            legajo_id=model.legajo_id,
            concepto_id=model.concepto_id,
            valor=model.valor,
            tipo_liquidacion_id=model.tipo_liquidacion_id
        )
    def actualizar(self, data: Liquidacion):
        model =  self.db.query(LiquidacionModel).get(data.id)
        if not model:
            return None

        model.valor=data.valor

        try:
            self.db.commit()
            self.db.refresh(model)
            return model
        except SQLAlchemyError as e:
            error_msg = str(e.orig).replace('"', '').replace(")", "").split(",")[1]
            raise Exception(error_msg)    


    def obtener_por_id(self, id: int) -> Liquidacion:
        model = self.db.query(LiquidacionModel).get(id)
        if not model:
            return None

        return Liquidacion(
            id=model.id,
            legajo_id=model.legajo_id,
            concepto_id=model.concepto_id,
            valor=model.valor,
            tipo_liquidacion_id=model.tipo_liquidacion_id
        )

    def listar_por_legajo(self, legajo_id: int):
        modelos = (
                self.db.query(LiquidacionModel)
                .options(joinedload(LiquidacionModel.concepto))  # 🔥 clave
                .filter(LiquidacionModel.legajo_id == legajo_id)
                .all()
            )

        return [
            Liquidacion(
                id=m.id,
                legajo_id=m.legajo_id,
                concepto_id=m.concepto_id,
                concepto=m.concepto,
                valor=m.valor,
                tipo_liquidacion_id=m.tipo_liquidacion_id
            )
            for m in modelos
        ]

    def eliminar(self, id: int):
        model = self.db.query(LiquidacionModel).get(id)
        if model:
            self.db.delete(model)
            self.db.commit()