from decimal import Decimal


class LiquidacionDetalle:

    def __init__(
        self,
        concepto_id: int,
        cantidad: Decimal,
        valor: Decimal,
        haber: Decimal,
        retencion: Decimal,
        total: Decimal,
        id: int | None = None,
        liquidacion_id: int | None = None,
    ):
        self.id = id
        self.liquidacion_id = liquidacion_id
        self.concepto_id = concepto_id
        self.cantidad = cantidad
        self.valor = valor
        self.haber = haber
        self.retencion = retencion
        self.total = total