from datetime import date
from decimal import Decimal
import json

from dataclasses import asdict

from application.liquidacion.liquidacion_builde import LiquidacionBuilder
from application.liquidacion.motor_liquidacion import MotorLiquidacion
from application.liquidacion.calcular_anios_antiguedad import calcular_anios
from application.liquidacion.resultado_builder import ResultadoBuilder


class ProcesoLiquidacionService:

    def __init__(
        self,
        repo_datos_fijos,
        repo_legajo,
        repo_legajo_concepto,
        repo_concepto,
        repo_novedad,
        repo_liquidacion
    ):

        self.repo_datos_fijos = repo_datos_fijos
        self.repo_legajo = repo_legajo
        self.repo_legajo_concepto = repo_legajo_concepto
        self.repo_concepto = repo_concepto
        self.repo_novedad = repo_novedad
        self.repo_liquidacion = repo_liquidacion

        self.motor = MotorLiquidacion()
        self.builder = LiquidacionBuilder()
        self.resultado_builder = ResultadoBuilder()
   
     

    def liquidar(
        self,
        datos_fijos_id: int,
        legajo_id: int
    ):

        # 1 - Obtener Datos Fijos
        datos_fijos = self.repo_datos_fijos.obtener(datos_fijos_id)


        if not datos_fijos:
            raise Exception("No existen los datos fijos.")

        if datos_fijos.estado != "ABIERTO":
            raise Exception("La liquidación se encuentra cerrada.")

        # 2 - Obtener Legajo
        legajo = self.repo_legajo.obtener_por_id(legajo_id)
        

        if not legajo:
            raise Exception("Legajo inexistente.")
        
        fecha_liquidacion = date.today()
        fecha_ingreso_actual =  date(2025, 6, 1) #legajo.fecha_ingreso_actual
        ANIOS_ANTIGUEDAD = calcular_anios(fecha_ingreso_actual, fecha_liquidacion)
   
        legajo_conceptos = self.repo_legajo_concepto.listar(legajo_id)

       
        # 4 - Obtener Novedades
        novedades = self.repo_novedad.listar_por_fechas(
            legajo.id,
            datos_fijos.fecha_desde,
            datos_fijos.fecha_hasta
        )


        items = self.builder.construir(
            legajo_conceptos,
            novedades
        )

                   
        self.motor.calcular(items, ANIOS_ANTIGUEDAD)
        return self.resultado_builder.construir(
            items
        )
        for item in items:
                    print(
                        json.dumps(
                            asdict(item),
                            indent=4,
                            ensure_ascii=False,
                            default=str
                        )
                    )
            
   