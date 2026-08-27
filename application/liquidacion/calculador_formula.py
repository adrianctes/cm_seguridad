from application.liquidacion.formula_engine import FormulaEngine

class CalculadorFormula:

    def __init__(self):

        self.engine = FormulaEngine()

    def calcular(
        self,
        item,
        detalle,
        ANIOS_ANTIGUEDAD
    ):

     
        variables = self.obtener_variables(
            detalle,
        )
          
        variables['ANIOS_ANTIGUEDAD']= ANIOS_ANTIGUEDAD
        variables['PORC_ANT']= 0.01

        item.haber = self.engine.calcular(
            item.formula,
            variables
        )

        item.total = item.haber

    from decimal import Decimal


    def obtener_variables(
        self,
        detalle,
    
    ):

        variables = {}

        #
        # Conceptos ya calculados
        #

        for item in detalle:

            variables[item.codigo] = item.haber

    

        return variables