from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ItemLiquidacion:

    concepto_id: int

    codigo: str
    concepto: str

    #clasificacion_id: int  | None
    clasificacion_codigo: str
    clasificacion_nombre: str
    clasificacion_tipo: str

    cantidad: Decimal
    valor: Decimal

    tipo_calculo: str
    formula: str | None

    es_novedad: bool

    orden: int

    haber: Decimal = 0
    retencion: Decimal = 0
    total: Decimal = 0