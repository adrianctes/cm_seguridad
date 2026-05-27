class HistoriaLaboral:

    def __init__(
        self,
        legajo_id: int,
        tipo_id: int,
        fecha,
        observacion: str = None,
        id: int = None
    ):

        self.id = id

        self.legajo_id = legajo_id

        self.tipo_id = tipo_id

        self.fecha = fecha

        self.observacion = observacion