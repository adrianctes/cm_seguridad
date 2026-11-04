from datetime import date
from decimal import Decimal
from typing import Optional


class LegajoConcepto:

    def __init__(
        self,
        valor_unidad: Decimal,
        cantidad : Decimal,
        activo: bool = True,
        legajo_id:  Optional[int] = None,
        concepto_id: Optional[int] = None,
        id: Optional[int] = None
    ):

        self.id = id
        self.legajo_id = legajo_id
        self.concepto_id = concepto_id
        self.valor_unidad = valor_unidad
        self.cantidad = cantidad
        self.activo = activo