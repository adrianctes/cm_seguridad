from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


# =========================================
# CREATE / UPDATE
# =========================================

class HistoriaLaboral(BaseModel):

    tipo_movimiento_id: int = Field(
        ...,
        gt=0
    )

    fecha: datetime

    observacion: str | None = Field(
        default=None,
        max_length=1000
    )


# =========================================
# RESPONSE
# =========================================

class HistoriaLaboralResponse(BaseModel):

    id: int

    legajo_id: int

    tipo_id: int

    fecha: datetime

    observacion: str | None

    class Config:

        from_attributes = True