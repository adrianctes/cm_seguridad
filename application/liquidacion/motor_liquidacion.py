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

            calculador = self.factory.obtener(item)

            resultado = calculador.calcular(
                item,
                detalle,
                anios_antiguedad
            )

           
            if resultado:
                detalle.append(item)

      

        '''for item in detalle:
            print(
                item.codigo,
                item.haber,
                item.total
            )'''


        return detalle