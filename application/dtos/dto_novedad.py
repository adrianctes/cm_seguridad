# application/dtos/dto_legajo_novedad.py

from decimal import Decimal

from pydantic import BaseModel, computed_field
from datetime import date
from typing import Optional


# 📥 CREATE DTO
class NovedadCreate(BaseModel):
    legajo_id: int
    concepto_id : int
    fecha_desde: date
    fecha_hasta:date
    cantidad: Decimal
    valor : Decimal
    activo: bool
    


# ✏️ UPDATE DTO
class NovedadUpdate(NovedadCreate):
    pass


# 📤 RESPONSE DTO
class NovedadResponse(BaseModel):
    id: int
    legajo_id: int
    fecha_desde: date
    fecha_hasta:date = None
    cantidad: Optional[Decimal] = None
    valor : Optional[Decimal] = None
    activo: Optional[bool] = None
    concepto_id : int
    codigo_concepto:Optional[str] = None
    concepto : Optional[str] = None
    apellido : Optional[str] = None
    nombre : Optional[str] = None
    liquidacion_detalle_id : Optional[int] = None

    @computed_field
    @property
    def ayn(self) -> str:
        return f"{self.apellido or ''} {self.nombre or ''}".strip()
    
    class Config:
        from_attributes = True



# ⚠️ VALIDACIÓN DTO (opcional)
class NovedadValidacion(BaseModel):
    legajo_id: int
    fecha_desde: date
    fecha_hasta: Optional[date] = None