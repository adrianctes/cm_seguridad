from application.liquidacion.calculador_factory import CalculadorFactory


class MotorLiquidacion:

    def __init__(self):
        self.factory = CalculadorFactory()

    def calcular(self,items, anios_antiguedad):

        detalle = []

        for item in items:

            calculador = self.factory.obtener(item)

            calculador.calcular(
                item,
                detalle,
                anios_antiguedad
            )

            detalle.append(item)

        