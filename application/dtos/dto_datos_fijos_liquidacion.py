from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class DatosFijosLiquidacionBase(BaseModel):
    fecha_carga: datetime
    tipo_liquidacion_id: int
    modalidad_liquidacion_id: int
    periodo: int
    numero : int
    fecha_desde: date
    fecha_hasta: date
    periodo_pago:  Optional[int] = None
    fecha_pago:  Optional[date] = None
    estado:  Optional[str] = None


class DatosFijosLiquidacionCreate(DatosFijosLiquidacionBase):
    pass


class DatosFijosLiquidacionUpdate(DatosFijosLiquidacionBase):
    pass


class DatosFijosLiquidacionResponse(DatosFijosLiquidacionBase):
    id: int
    tipo_liquidacion: str
    modalidad_liquidacion: str

    class Config:
        from_attributes = True