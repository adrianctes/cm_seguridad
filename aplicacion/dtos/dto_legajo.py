from pydantic import BaseModel, Field, constr
from datetime import date
from typing import Optional

from aplicacion.dtos.dto_categoria import CategoriaResponse
from aplicacion.dtos.dto_modalidad_liquidacion import ModalidadLiquidacionResponse


# 🔹 Base (campos comunes)
class LegajoBase(BaseModel):
    apellido: str = Field(..., max_length=100)
    nombre: str = Field(..., max_length=100)
    cuil: constr(pattern=r'^\d{2}-?\d{8}-?\d{1}$')
    sexo: constr(pattern=r'^[MF]$')
    categoria_id: int
    modalidad_liquidacion_id: int
    activo: bool = True
    sac: Optional[bool] = None


# 🔹 DTO de creación (request)
class LegajoCreate(LegajoBase):
        fecha_ingreso: date
   


# 🔹 DTO de actualización (parcial)
class LegajoUpdate(BaseModel):
    apellido: Optional[str] = None
    nombre: Optional[str] = None
    sexo: Optional[str] = None
    categoria_id: Optional[int] = None
    modalidad_liquidacion_id: Optional[int] = None
    activo: Optional[bool] = None
    sac: Optional[bool] = None


# 🔹 DTO de respuesta (response)
class LegajoResponse(LegajoBase):
    id: int
    categoria: CategoriaResponse | None = None  
    modalidad_liquidacion: ModalidadLiquidacionResponse | None = None  

    class Config:
        from_attributes = True 