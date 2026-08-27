from decimal import Decimal

from domain.entities.concepto_entity import Concepto
from domain.entities.datos_fijos_liquidacion_entity import DatosFijosLiquidacion


class Liquidacion:
    def __init__(
        self,
        id: int = None,
        legajo_id: int = None,
        datos_fijos_liquidacion_id: int   = None,
        tipo_liquidacion_id: int = None,
        total_haberes : Decimal = None,
        total_retenciones:Decimal = None,
        total_neto :Decimal = None
    ):
        self.id = id
        self.legajo_id = legajo_id
        self.datos_fijos_liquidacion_id = datos_fijos_liquidacion_id
        self.tipo_liquidacion_id = tipo_liquidacion_id
        self.total_haberes = total_haberes,
        self.total_retenciones =total_retenciones,
        self.total_neto = total_neto

  
         