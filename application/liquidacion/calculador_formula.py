from application.liquidacion.formula_engine import FormulaEngine
from decimal import Decimal

from decimal import Decimal


class CalculadorFormula:

    def __init__(self):
        self.engine = FormulaEngine()

    def calcular(
        self,
        item,
        detalle,
        anios_antiguedad
    ):
       
        variables = self.obtener_variables(detalle)
        variables["ANIOS_ANTIGUEDAD"] = anios_antiguedad
        variables["PORC_ANT"] = Decimal("0.01")

        try:

            item.resultado = self.engine.calcular(
                item.formula,
                variables
            )
            if item.clasificacion_tipo == "C":
                item.haber =  item.resultado
                       
            elif item.clasificacion_tipo == "D":
                    item.retencion =  item.resultado
            item.total = item.resultado

            return True

        except Exception as ex:

            print(
                f"NO CALCULADO {item.codigo}:",
                ex
            )

            return False

    def obtener_variables(self, detalle):

        variables = {}

        for item in detalle:

            variables[item.abreviatura] = item.haber

        return variables

   