from sqlalchemy.orm import Session, joinedload
from domain.entities.liquidacion import Liquidacion
from domain.repositories.liquidacion_repositorio_interface import LiquidacionRepository
from infrastructura.db.models.datos_fijos_liquidacion_model import DatosFijosLiquidacionModel
from infrastructura.db.models.legajo_model import LegajoModel
from infrastructura.db.models.liquidacion_detalle_model import LiquidacionDetalleModel
from infrastructura.db.models.liquidacion_model import LiquidacionModel
from sqlalchemy.exc import SQLAlchemyError

class MySQLLiquidacionRepository(LiquidacionRepository):

    def __init__(self, db: Session):
        self.db = db

    def crear(self, liquidacion: Liquidacion) -> Liquidacion:


        model = LiquidacionModel(
            legajo_id=liquidacion.legajo_id,
            datos_fijos_liquidacion_id=liquidacion.datos_fijos_liquidacion_id,
            tipo_liquidacion_id=liquidacion.tipo_liquidacion_id,
            total_haberes=liquidacion.total_haberes,
            total_retenciones=liquidacion.total_retenciones,
            total_neto=liquidacion.total_neto
        )

        for linea in liquidacion.lineas_liquidacion:

            detalle_model = LiquidacionDetalleModel(
                concepto_id=linea.concepto_id,
                legajo_novedad_id = linea.legajo_novedad_id,
                cantidad=linea.cantidad,
                valor=linea.valor,
                haber=linea.haber,
                retencion=linea.retencion,
                total=linea.total

            )

            model.lineas_liquidacion.append(detalle_model)

        self.db.add(model)

        self.db.commit()

        self.db.refresh(model)

        return #self._to_entity(model)

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

    def buscar_por_legajo_y_datos_fijos(
        self,
        legajo_id: int,
        datos_fijos_liquidacion_id: int
    ) -> LiquidacionModel | None:

        return (
            self.db.query(LiquidacionModel)
            .filter(
                LiquidacionModel.legajo_id == legajo_id,
                LiquidacionModel.datos_fijos_liquidacion_id
                    == datos_fijos_liquidacion_id
            )
            .first()
        )

    def obtener_legajos_liquidados(
        self,
        datos_fijos_liquidacion_id: int
    ):
        return (
            self.db.query(LiquidacionModel.legajo_id)
            .filter(
                LiquidacionModel.datos_fijos_liquidacion_id
                == datos_fijos_liquidacion_id
            )
            .all()
        )


    def obtener_por_id(self, liquidacion_id: int):

        return (
            self.db.query(LiquidacionModel)
            .options(
                joinedload(
                    LiquidacionModel.lineas_liquidacion
                ).joinedload(
                    LiquidacionDetalleModel.concepto
                ),

                joinedload(
                    LiquidacionModel.legajo
                ),

                joinedload(
                    LiquidacionModel.datos_fijos_liquidacion
                )
            )
            .filter(
                LiquidacionModel.id == liquidacion_id
            )
            .first()
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

    def listar_por_datos_fijos(self, datos_fijo_id: int):

        return (
            self.db.query(
                LiquidacionModel,
                DatosFijosLiquidacionModel,
                LegajoModel
            )
            .join(
                DatosFijosLiquidacionModel,
                LiquidacionModel.datos_fijos_liquidacion_id
                == DatosFijosLiquidacionModel.id
            )
            .join(
                LegajoModel,
                LiquidacionModel.legajo_id
                == LegajoModel.id
            )
            .filter(
                LiquidacionModel.datos_fijos_liquidacion_id
                == datos_fijo_id
            )
            .order_by(
                LegajoModel.apellido,
                LegajoModel.nombre
            )
            .all()
        )

    def eliminar(self, id: int):
        model = self.db.query(LiquidacionModel).get(id)
        if model:
            self.db.delete(model)
            self.db.commit()