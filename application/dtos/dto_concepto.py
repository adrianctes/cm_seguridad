from pydantic import BaseModel, Field
from typing import Optional

class ConceptoBase(BaseModel):
    codigo: str = Field(..., max_length=6)
    nombre: str = Field(..., max_length=100)
    clasificacion_concepto_id : int
    tipo_calculo: str
    formula: Optional[str] = None
    activo: Optional[bool] = None
    es_novedad: Optional[bool] = None
    modalidad_pago_id :Optional[int] = None
    orden : Optional[int] = None

  

class ConceptoCreate(ConceptoBase):
    pass

class ConceptoUpdate(ConceptoBase):
      pass

class ConceptoResponse(ConceptoBase):
    id: int

    class Config:
        from_attributes = True

