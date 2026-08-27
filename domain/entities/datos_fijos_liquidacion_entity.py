from datetime import date, datetime


class DatosFijosLiquidacion:

    def __init__(
        self,
        id: int | None = None,
        fecha_carga: datetime | None = None,
        tipo_liquidacion_id: int | None = None,
        tipo_liquidacion: str | None = None,
        modalidad_liquidacion_id: int | None = None,
        modalidad_liquidacion: str | None = None,
        periodo: int | None = None,
        numero :int | None = None,
        fecha_desde: date | None = None,
        fecha_hasta: date | None = None,
        periodo_pago: int | None = None,
        fecha_pago: date | None = None,
        estado: str | None = None,
    ):

        self.id = id
        self.fecha_carga = fecha_carga
        self.tipo_liquidacion_id = tipo_liquidacion_id
        self.tipo_liquidacion = tipo_liquidacion
        self.modalidad_liquidacion_id = modalidad_liquidacion_id
        self.modalidad_liquidacion = modalidad_liquidacion
        self.periodo = periodo
        self.numero = numero
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.periodo_pago = periodo_pago
        self.fecha_pago = fecha_pago
        self.estado = estado