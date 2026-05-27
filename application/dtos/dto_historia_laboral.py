from datetime import datetime
from pydantic import BaseModel, Field


class HistoriaLaboral(BaseModel):

    legajo_id: int

    tipo_id: int = Field(
        ...,
        gt=0
    )

    fecha: datetime

    observacion: str | None = Field(
        default=None,
        max_length=1000
    )


class HistoriaLaboralResponse(BaseModel):

    id: int

    legajo_id: int

    tipo_id: int

    fecha: datetime

    observacion: str | None

    class Config:
        from_attributes = True