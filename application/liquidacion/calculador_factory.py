from application.liquidacion.calculador_fijo import CalculadorFijo
from application.liquidacion.calculador_formula import CalculadorFormula
class CalculadorFactory:

    def obtener(self, item):

        match item.tipo_calculo:

            case "FIJO":
                return CalculadorFijo()

            case "FORMULA":
                return CalculadorFormula()

            case "PORCENTAJE":
                return "CalculadorPorcentaje"()

            case _:
                raise Exception(
                    f"Tipo {item.tipo_calculo} no soportado."
                )