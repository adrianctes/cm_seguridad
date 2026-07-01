from pydantic import BaseModel, Field
from typing import Optional


# =========================
# CONCEPTO RESPONSE
# =========================
class ConceptoResponse(BaseModel):
    id: int
    codigo: str
    nombre: str

    class Config:
        from_attributes = True


# =========================
# BASE
# =========================
class LegajoConceptoBase(BaseModel):
    concepto_id: int

    valor: float = Field(
        default=0,
        ge=0
    )

    cantidad : float = Field(
        default=0,
        ge=0
    )

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
    concepto_id: Optional[int] = None

    valor: Optional[float] = Field(
        default=None,
        ge=0
    )

    cantidad: Optional[float] = Field(
        default=None,
        ge=0
    )

    activo: Optional[bool] = None



# =========================
# RESPONSE
# =========================
class LegajoConceptoResponse(BaseModel):
    id: int
    legajo_id: int
    valor: float
    cantidad:float
    activo: bool

    concepto: ConceptoResponse

    class Config:
        from_attributes = True