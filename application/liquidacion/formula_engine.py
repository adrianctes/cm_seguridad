"""from decimal import Decimal
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

        print(expresion)

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

        raise Exception("Expresión no permitida")"""
from decimal import Decimal
import ast
import operator
import re


from decimal import Decimal
import ast
import operator
import re


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

        # -----------------------------------------
        # 1. Resolver alternativas
        # -----------------------------------------

        expresion = self._resolver_alternativas(
            formula,
            variables
        )

        print("EXPRESIÓN RESUELTA:", expresion)

        # -----------------------------------------
        # 2. Reemplazar variables
        # -----------------------------------------

        for nombre, valor in variables.items():

            expresion = re.sub(
                rf"\b{re.escape(nombre)}\b",
                str(valor),
                expresion
            )

        print("EXPRESIÓN FINAL:", expresion)

        # -----------------------------------------
        # 3. Evaluar
        # -----------------------------------------

        return self._evaluar(
            ast.parse(
                expresion,
                mode="eval"
            ).body
        )

    def _resolver_alternativas(
        self,
        formula: str,
        variables: dict
    ) -> str:

        print("FORMULA:", formula)
        print("VARIABLES:", variables)

        patron = r"\[([A-Za-z0-9_]+(?:\|[A-Za-z0-9_]+)+)\]"

        def reemplazar(match):

            alternativas = match.group(1).split("|")

            print(
                "ALTERNATIVAS:",
                alternativas
            )

            for nombre in alternativas:

                if nombre in variables:

                    print(
                        "USANDO VARIABLE:",
                        nombre
                    )

                    return nombre

            raise ValueError(
                "No se puede resolver ninguna alternativa: "
                f"{alternativas}"
            )

        resultado = re.sub(
            patron,
            reemplazar,
            formula
        )

        return resultado

    def _evaluar(self, nodo):

        if isinstance(nodo, ast.Constant):

            return Decimal(
                str(nodo.value)
            )

        elif isinstance(nodo, ast.BinOp):

            operador = self.OPERADORES.get(
                type(nodo.op)
            )

            if operador is None:
                raise Exception(
                    "Operador no permitido"
                )

            return operador(
                self._evaluar(nodo.left),
                self._evaluar(nodo.right)
            )

        elif isinstance(nodo, ast.UnaryOp):

            operador = self.OPERADORES.get(
                type(nodo.op)
            )

            if operador is None:
                raise Exception(
                    "Operador no permitido"
                )

            return operador(
                self._evaluar(nodo.operand)
            )

        raise Exception(
            "Expresión no permitida"
        )

        if isinstance(nodo, ast.Constant):

            return Decimal(
                str(nodo.value)
            )

        elif isinstance(nodo, ast.BinOp):

            return self.OPERADORES[type(nodo.op)](
                self._evaluar(nodo.left),
                self._evaluar(nodo.right)
            )

        elif isinstance(nodo, ast.UnaryOp):

            return self.OPERADORES[type(nodo.op)](
                self._evaluar(nodo.operand)
            )

        raise Exception(
            "Expresión no permitida"
        )