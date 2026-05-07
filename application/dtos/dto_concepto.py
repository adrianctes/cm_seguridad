from pydantic import BaseModel, Field
from typing import Optional

class ConceptoBase(BaseModel):
    codigo: str = Field(..., max_length=2)
    nombre: str = Field(..., max_length=100)
    tipo: str = Field(..., max_length=1)
    es_remunerativo: Optional[bool] = True
    activo: Optional[bool] = True
    requiere_novedad: Optional[bool] = None

class ConceptoCreate(ConceptoBase):
    pass

class ConceptoUpdate(BaseModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    es_remunerativo: Optional[bool] = None
    activo: Optional[bool] = None
    requiere_novedad: Optional[bool] = None

class ConceptoResponse(ConceptoBase):
    id: int

    class Config:
        from_attributes = True

