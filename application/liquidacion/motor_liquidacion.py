from application.liquidacion.calculador_factory import CalculadorFactory

class MotorLiquidacion:

    def __init__(self):
        self.factory = CalculadorFactory()

    def calcular(
        self,
        items,
        anios_antiguedad
    ):

        detalle = []

        for item in items:

            print(
                "PROCESANDO:",
                item.codigo,
                item.tipo_calculo
            )

            calculador = self.factory.obtener(item)

            resultado = calculador.calcular(
                item,
                detalle,
                anios_antiguedad
            )

            print(
                "RESULTADO:",
                item.codigo,
                resultado
            )

            if resultado:
                detalle.append(item)

        print("========== DETALLE FINAL ==========")

        for item in detalle:
            print(
                item.codigo,
                item.haber,
                item.total
            )

        print("===================================")

        return detalle