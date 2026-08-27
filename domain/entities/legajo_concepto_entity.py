from datetime import date
from decimal import Decimal
from typing import Optional


class LegajoConcepto:

    def __init__(
        self,
        legajo_id: int,
        concepto_id: int,
        valor: Decimal,
        cantidad : Decimal,
        activo: bool = True,
        id: Optional[int] = None
    ):

        self.id = id
        self.legajo_id = legajo_id
        self.concepto_id = concepto_id
        self.valor = valor
        self.cantidad = cantidad
        self.activo = activo