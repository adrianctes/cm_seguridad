from pydantic import BaseModel, Field, constr
from datetime import date
from typing import Optional

from application.dtos.dto_categoria import CategoriaResponse
from application.dtos.dto_modalidad_liquidacion import ModalidadLiquidacionResponse


# 🔹 Base (campos comunes)
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class LegajoBase(BaseModel):
    cuil: str
    apellido: str = Field(..., max_length=100)
    nombre: str = Field(..., max_length=100)   
    sexo: str
    categoria_id: int
    modalidad_liquidacion_id: int

    activo: bool = True
    sac: Optional[bool] = None
    telefono: Optional[str] = None

    # =========================
    # VALIDACIONES PERSONALIZADAS
    # =========================
    @field_validator("cuil")
    @classmethod
    def validar_cuil(cls, v):
        import re
        if not re.match(r"^\d{2}-?\d{8}-?\d{1}$", v):
            raise ValueError("CUIL inválido. Formato esperado: XXXXXXXXXXX")
        return v
    
    @field_validator("apellido")
    @classmethod
    def apellido_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El apellido es obligatorio")
        return v

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El nombre es obligatorio")
        return v

    

    @field_validator("sexo")
    @classmethod
    def validar_sexo(cls, v):
        if v not in ("M", "F"):
            raise ValueError("Sexo debe ser M o F")
        return v

    @field_validator("telefono")
    @classmethod
    def validar_telefono(cls, v):
        if v and len(v) < 6:
            raise ValueError("Teléfono inválido")
        return v


# 🔹 DTO de creación (request)
class LegajoCreate(LegajoBase):
        pass
        #fecha_ingreso: date
   


# 🔹 DTO de actualización (parcial)
class LegajoUpdate(LegajoBase):
      pass


# 🔹 DTO de respuesta (response)
class LegajoResponse(LegajoBase):
    id: int
    categoria: CategoriaResponse | None = None  
    modalidad_liquidacion: ModalidadLiquidacionResponse | None = None  

    class Config:
        from_attributes = True 