class ConceptoNovedad:
    def __init__(
        self,
        id=None,
        legajo_id=None,
        concepto_id=None,
        fecha_desde=None,
        fecha_hasta=None,
        valor=None
    ):
        self.id = id
        self.legajo_id = legajo_id
        self.concepto_id = concepto_id
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.valor = valor