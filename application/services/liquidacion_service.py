from decimal import Decimal

from application.dtos.dto_liquidacion import LiquidacionDetalleVisualizacionResponse, LiquidacionListadoResponse, LiquidacionVisualizacionResponse
from application.dtos.dto_modalidad_liquidacion import LiquidacionUpdateValor
from domain.entities.liquidacion import Liquidacion
from domain.repositories.liquidacion_repositorio_interface import LiquidacionRepository
from domain.entities.liquidacion_detalle import LiquidacionDetalle



class LiquidacionService:

    def __init__(self, repo: LiquidacionRepository):
        self.repo = repo

    def crear(self, data):
        

        existente = self.repo.buscar_por_legajo_y_datos_fijos(
            data.legajo_id,
            data.datos_fijos_liquidacion_id
        )

        if existente:
            raise ValueError(
                "El legajo ya tiene una liquidación registrada para estos datos fijos."
            )

        # =====================================================
        # Crear entidad principal
        # =====================================================

        liquidacion = Liquidacion(
            legajo_id=data.legajo_id,
            datos_fijos_liquidacion_id=data.datos_fijos_liquidacion_id,
            tipo_liquidacion_id=data.tipo_liquidacion_id,
            total_haberes=Decimal("0"),
            total_retenciones=Decimal("0"),
            total_neto=Decimal("0"),
        )

        # =====================================================
        # Inicializar detalles
        # =====================================================

        liquidacion.lineas_liquidacion = []

        total_haberes = Decimal("0")
        total_retenciones = Decimal("0")

        # =====================================================
        # Crear líneas
        # =====================================================

        for linea in data.lineas:

            total_haberes += linea.haber
            total_retenciones += linea.retencion

            detalle = LiquidacionDetalle(
                concepto_id=linea.concepto_id,
                cantidad=linea.cantidad,
                valor=linea.valor,
                haber=linea.haber,
                retencion=linea.retencion,
                total=linea.total,
                legajo_novedad_id = linea.legajo_novedad_id
            )

           

            liquidacion.lineas_liquidacion.append(detalle)

        # =====================================================
        # Calcular totales
        # =====================================================

        total_neto = total_haberes - total_retenciones

        # =====================================================
        # Asignar totales a la entidad
        # =====================================================

        liquidacion.total_haberes = total_haberes
        liquidacion.total_retenciones = total_retenciones
        liquidacion.total_neto = total_neto

        # =====================================================
        # Persistir
        # =====================================================

        return self.repo.crear(liquidacion)
            
    def obtener_por_id(self, liquidacion_id: int):

        liquidacion = self.repo.obtener_por_id(liquidacion_id)

        if not liquidacion:
            raise ValueError(
                "No se encontró la liquidación."
            )

        datos_fijos = liquidacion.datos_fijos_liquidacion
        legajo = liquidacion.legajo

        return LiquidacionVisualizacionResponse(

            id=liquidacion.id,

            fecha=liquidacion.fecha,

            periodo=datos_fijos.periodo,

            modalidad=datos_fijos.modalidad_liquidacion.nombre,

            numero=datos_fijos.numero,

            legajo_id=legajo.id,

            ayn=f"{legajo.apellido} {legajo.nombre}",

            total_haberes=liquidacion.total_haberes,

            total_retenciones=liquidacion.total_retenciones,

            total_neto=liquidacion.total_neto,

            lineas=[
                LiquidacionDetalleVisualizacionResponse(

                    id=linea.id,

                    concepto_id=linea.concepto_id,

                    codigo=linea.concepto.codigo,

                    concepto=linea.concepto.nombre,

                    cantidad=linea.cantidad,

                    valor=linea.valor,

                    haber=linea.haber,

                    retencion=linea.retencion,

                    total=linea.total

                )

                for linea in liquidacion.lineas_liquidacion
            ]
        )

    def listar_por_legajo(self, legajo_id: int):
        return self.repo.listar_por_legajo(legajo_id)

    def listar_por_datos_fijos(self, datos_fijo_id):

        resultados = self.repo.listar_por_datos_fijos(
            datos_fijo_id
        )

        respuesta = []

        for liquidacion, datos_fijos, legajo in resultados:

            respuesta.append(
                LiquidacionListadoResponse(
                    id=liquidacion.id,

                    fecha=liquidacion.fecha,

                    periodo=datos_fijos.periodo,

                    modalidad=datos_fijos.modalidad_liquidacion.nombre,

                    numero=datos_fijos.numero,

                    legajo_id=legajo.id,


                    ayn=f"{legajo.apellido}, {legajo.nombre}",

                    total_haberes=liquidacion.total_haberes,

                    total_retenciones=liquidacion.total_retenciones,

                    total_neto=liquidacion.total_neto
                )
            )

        return respuesta

    def eliminar(self, id: int):
        self.repo.eliminar(id)

   