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

        print("================================")
        print("CONCEPTO:", item.codigo)
        print("FORMULA:", item.formula)
        print("VARIABLES:", variables)
        print("================================")

        try:

            item.haber = self.engine.calcular(
                item.formula,
                variables
            )

            item.total = item.haber

            print(
                f"CALCULADO {item.codigo}:",
                item.total
            )

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

            variables[item.codigo] = item.haber

        return variables

   