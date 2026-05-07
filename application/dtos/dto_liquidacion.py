from pydantic import BaseModel, Field
from typing import Optional

from application.dtos.dto_concepto import ConceptoResponse


# 🔹 Base
class LiquidacionBase(BaseModel):
    legajo_id: int = Field(..., gt=0)
    concepto_id: int = Field(..., gt=0)
    valor: float = Field(..., description="Importe del concepto")
    tipo_liquidacion_id: int = Field(..., gt=0)


# 🔹 Create
class LiquidacionCreate(LiquidacionBase):
    pass


# 🔹 Update
class LiquidacionUpdate(BaseModel):
    #legajo_id: Optional[int] = Field(None, gt=0)
    #concepto_id: Optional[int] = Field(None, gt=0)
    valor: float
    #tipo_liquidacion_id: Optional[int] = Field(None, gt=0)


# 🔹 Response
class LiquidacionResponse(LiquidacionBase):
    id: int
    concepto: ConceptoResponse | None = None  
    class Config:
        from_attributes = True