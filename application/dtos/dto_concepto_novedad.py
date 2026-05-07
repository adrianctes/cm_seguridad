from pydantic import BaseModel
from typing import Optional
from datetime import date


class ConceptoNovedadBase(BaseModel):
    legajo_id: int
    concepto_id: int
    fecha_desde: Optional[date] = None
    fecha_hasta: Optional[date] = None
    valor: Optional[float] = None


class ConceptoNovedadCreate(ConceptoNovedadBase):
    pass


class ConceptoNovedadUpdate(BaseModel):
    fecha_desde: Optional[date] = None
    fecha_hasta: Optional[date] = None
    valor: Optional[float] = None


class ConceptoNovedadResponse(ConceptoNovedadBase):
    id: int

    class Config:
        from_attributes = True