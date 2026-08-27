from decimal import Decimal
import ast
import operator


class FormulaEngine:

    OPERADORES = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }

    def calcular(
        self,
        formula: str,
        variables: dict
    ) -> Decimal:
       
        expresion = formula

        # Reemplazar variables
        for nombre, valor in variables.items():

            expresion = expresion.replace(
                nombre,
                str(valor)
            )

        return self._evaluar(
            ast.parse(
                expresion,
                mode="eval"
            ).body
        )

    def _evaluar(self, nodo):

        if isinstance(nodo, ast.Constant):

            return Decimal(str(nodo.value))

        elif isinstance(nodo, ast.BinOp):

            return self.OPERADORES[type(nodo.op)](
                self._evaluar(nodo.left),
                self._evaluar(nodo.right)
            )

        elif isinstance(nodo, ast.UnaryOp):

            return self.OPERADORES[type(nodo.op)](
                self._evaluar(nodo.operand)
            )

        raise Exception("Expresión no permitida")