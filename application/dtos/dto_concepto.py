from pydantic import BaseModel, Field
from typing import Literal, Optional

class ConceptoBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    clasificacion_concepto_id : int
    tipo_calculo: str = Field(..., max_length=10)
    formula: Optional[str] = Field(None, max_length=100)
    activo: Optional[bool] = None
    es_novedad: Optional[bool] = None
    orden : Optional[int] = None
    abreviatura: str = Field(..., max_length=10)
    unidad_medida: Literal["DIA", "HORA", "IMPORTE"] = Field(...)



class ConceptoCreate(ConceptoBase):
      pass
   

class ConceptoUpdate(ConceptoBase):
    codigo: int = Field(...)
    secuencia: int = Field(...)
    

class ConceptoResponse(ConceptoBase):
    id: int
    codigo: int = Field(...)
    secuencia: int = Field(...)

    class Config:
        from_attributes = True

