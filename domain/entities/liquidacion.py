from domain.entities.concepto_entity import Concepto


class Liquidacion:
    def __init__(
        self,
        id: int = None,
        legajo_id: int = None,
        concepto_id: int = None,
        concepto : Concepto  | None = None,
        valor: float = 0,
        tipo_liquidacion_id: int = None,
    ):
        self.id = id
        self.legajo_id = legajo_id
        self.concepto_id = concepto_id
        self.concepto = concepto
        self.valor = valor
        self.tipo_liquidacion_id = tipo_liquidacion_id
         