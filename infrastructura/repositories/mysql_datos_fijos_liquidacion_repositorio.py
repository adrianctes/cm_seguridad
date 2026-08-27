from sqlalchemy.orm import Session
from sqlalchemy import select

from domain.entities.datos_fijos_liquidacion_entity import DatosFijosLiquidacion
from domain.repositories.datos_fijos_liquidacion_repository_interface import (
    IDatosFijosLiquidacionRepository,
)
from infrastructura.db.models.datos_fijos_liquidacion_model import (
    DatosFijosLiquidacionModel,
)


class MySQLDatosFijosLiquidacionRepository(
    IDatosFijosLiquidacionRepository
):

    def __init__(self, db: Session):
        self.db = db

    def obtener(self, id: int) -> DatosFijosLiquidacion | None:

        registro = (
            self.db.query(DatosFijosLiquidacionModel)
            .filter(DatosFijosLiquidacionModel.id == id)
            .first()
        )

        if registro is None:
            return None

        return self._to_entity(registro)

    def obtener_ultimo_periodo_anterior(
        self,
        tipo_liquidacion_id: int,
        modalidad_liquidacion_id: int,
        periodo: int,
    ):

        stmt = (
            select(DatosFijosLiquidacionModel)
            .where(
                DatosFijosLiquidacionModel.tipo_liquidacion_id == tipo_liquidacion_id,
                DatosFijosLiquidacionModel.modalidad_liquidacion_id == modalidad_liquidacion_id,
                DatosFijosLiquidacionModel.periodo < periodo,
            )
            .order_by(
                DatosFijosLiquidacionModel.periodo.desc()
            )
            .limit(1)
        )

        print("====================================")
        print("STMT:")
        print(stmt)

        try:
            result =  self.db.execute(stmt)

            print("RESULT:")
            print(result)

            anterior = result.scalars().first()

            print("ANTERIOR:")
            print(anterior)

            return anterior

        except Exception as e:
            print("====================================")
            print("ERROR EN obtener_ultimo_periodo_anterior")
            print(type(e).__name__)
            print(str(e))
            print("====================================")

            raise
 


    def listar_por_periodo(
        self,
        params: dict    ) -> DatosFijosLiquidacion | None:
     
        query = self.db.query(DatosFijosLiquidacionModel)

        if params.get("periodo"):
            query = query.filter(
                DatosFijosLiquidacionModel.periodo == params["periodo"]
            )

        if params.get("modalidad"):
            query = query.filter(
                DatosFijosLiquidacionModel.modalidad_liquidacion_id == int(params["modalidad"])
            )

        if params.get("estado"):
            query = query.filter(
                DatosFijosLiquidacionModel.estado == params["estado"]
            )

        registros = query.all()

        if registros is None:
            return None

        return [self._to_entity(m) for m in registros]

    def existe(self, payload: dict,
               excluir_id: int | None = None) -> bool:

        try:
            condiciones = []

            if "tipo_liquidacion_id" in payload:
                condiciones.append(
                    DatosFijosLiquidacionModel.tipo_liquidacion_id
                    == payload["tipo_liquidacion_id"]
                )

            if "modalidad_liquidacion_id" in payload:
                condiciones.append(
                    DatosFijosLiquidacionModel.modalidad_liquidacion_id
                    == payload["modalidad_liquidacion_id"]
                )

            if "periodo" in payload:
                condiciones.append(
                    DatosFijosLiquidacionModel.periodo
                    == payload["periodo"]
                )

            if "numero" in payload:
                condiciones.append(
                    DatosFijosLiquidacionModel.numero
                    == payload["numero"]
                )
            
            query = (
                self.db
                .query(DatosFijosLiquidacionModel)
                .filter(*condiciones)
            )

            if excluir_id is not None:
                query = query.filter(
                    DatosFijosLiquidacionModel.id != excluir_id
                )
   
            resultado = query.first()

            print(resultado)

            print("RESULTADO:", resultado)

            return resultado is not None

        except Exception as e:
            import traceback

            print("========== ERROR ==========")
            print(type(e).__name__)
            print(str(e))
            traceback.print_exc()
            print("===========================")

            raise
    
    def existe_periodo(
        self,
        tipo_liquidacion_id: int,
        periodo: int
    ) -> bool:

        return (
            self.db.query(DatosFijosLiquidacionModel)
            .filter(
                DatosFijosLiquidacionModel.tipo_liquidacion_id == tipo_liquidacion_id,
                DatosFijosLiquidacionModel.periodo == periodo,
            )
            .first()
            is not None
        )

    def crear(
        self,
        datos: DatosFijosLiquidacion
    ):

        model = DatosFijosLiquidacionModel(
            fecha_carga=datos.fecha_carga,
            tipo_liquidacion_id =datos.tipo_liquidacion_id,
            modalidad_liquidacion_id=datos.modalidad_liquidacion_id,
            periodo=datos.periodo,
            numero = datos.numero,
            fecha_desde=datos.fecha_desde,
            fecha_hasta=datos.fecha_hasta,
            periodo_pago=datos.periodo_pago,
            fecha_pago=datos.fecha_pago,
            estado = datos.estado
        )
    
        try: 
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)

           # return self._to_entity(model)
        except Exception as ex:

            import traceback
      
            self.db.rollback()

            print("ERROR SQL:", repr(ex))
            print("========== ERROR ==========")
            print(type(ex).__name__)
            print(str(ex))
            traceback.print_exc()
            print("===========================")
            raise ex

    def actualizar(
        self,
        datos: DatosFijosLiquidacion
    ) -> DatosFijosLiquidacion:

        model = self.db.get(
            DatosFijosLiquidacionModel,
            datos.id
        )

        model.fecha_carga = datos.fecha_carga
        model.modalidad_liquidacion_id = datos.modalidad_liquidacion_id
        model.periodo = datos.periodo
        model.fecha_desde = datos.fecha_desde
        model.fecha_hasta = datos.fecha_hasta
        model.periodo_pago = datos.periodo_pago
        model.fecha_pago = datos.fecha_pago
        model.estado = datos.estado

        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    def eliminar(self, id: int) -> bool:

        model = self.db.get(
            DatosFijosLiquidacionModel,
            id
        )

        if model is None:
            return False

        self.db.delete(model)
        self.db.commit()

        return True

    def _to_entity(
        self,
        model: DatosFijosLiquidacionModel
    ) -> DatosFijosLiquidacion:
   
        return DatosFijosLiquidacion(
            id=model.id,
            fecha_carga=model.fecha_carga,
            tipo_liquidacion_id= model.tipo_liquidacion_id,
            tipo_liquidacion=model.tipo_liquidacion.nombre,
            modalidad_liquidacion_id=model.modalidad_liquidacion_id,
            modalidad_liquidacion=model.modalidad_liquidacion.nombre,
            periodo=model.periodo,
            numero = model.numero,
            fecha_desde=model.fecha_desde,
            fecha_hasta=model.fecha_hasta,
            periodo_pago=model.periodo_pago,
            fecha_pago=model.fecha_pago,
            estado = model.estado
        )