from decimal import Decimal

from pydantic import BaseModel, Field
from typing import Optional

from pydantic import BaseModel, Field
from typing import Optional

class ConceptoResponse(BaseModel):
    id: int 
    codigo : int 
    nombre :str
    unidad_medida: str

    class Config:
            from_attributes = True

# =========================
# BASE
# =========================
class LegajoConceptoBase(BaseModel):
   # legajo_id : int
    concepto_id: int 
    cantidad : Decimal = Field(default=0,ge=0)
    valor_unidad: Decimal = Field( default=0,ge=0)
    activo: bool = True



# =========================
# CREATE
# =========================
class LegajoConceptoCreate(LegajoConceptoBase):
    pass


# =========================
# UPDATE
# =========================
class LegajoConceptoUpdate(BaseModel):
    id: int 
    valor_unidad: Decimal = Field(
        default=None,
        ge=0
    )

    cantidad: Decimal = Field(
        default=None,
        ge=0
    )
  

    activo: bool = None



# =========================
# RESPONSE
# =========================
class LegajoConceptoResponse(BaseModel):
    id: int
    legajo_id: int
    valor_unidad: Decimal
    cantidad:Decimal
    activo: bool
    concepto: ConceptoResponse

    class Config:
        from_attributes = True