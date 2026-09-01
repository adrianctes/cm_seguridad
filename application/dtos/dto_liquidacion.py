from decimal import Decimal
from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field
from application.dtos.dto_legajo import LegajoResponse


# ============================================================
# REQUEST - SOLICITUD DE LIQUIDACIÓN
# ============================================================

class LiquidacionRequest(BaseModel):
    """
    Datos necesarios para ejecutar el cálculo
    de una liquidación.
    """

    datos_fijos_id: int = Field(..., gt=0)
    legajo_id: int = Field(..., gt=0)


# ============================================================
# BASE - LIQUIDACIÓN
# ============================================================

class LiquidacionBase(BaseModel):

    legajo_id: int = Field(..., gt=0)

    datos_fijos_liquidacion_id: int = Field(..., gt=0)

    tipo_liquidacion_id: int = Field(..., gt=0)


# ============================================================
# DETALLE DE LIQUIDACIÓN
# ============================================================

class LiquidacionDetalleDto(BaseModel):

    legajo_novedad_id: int | None = Field(default=None, gt=0)

    concepto_id: int = Field(..., gt=0)

    cantidad: Decimal

    valor: Decimal

    haber: Decimal

    retencion: Decimal

    total: Decimal


# ============================================================
# CREATE - PERSISTIR LIQUIDACIÓN
# ============================================================

class LiquidacionCreate(LiquidacionBase):

    lineas: list[LiquidacionDetalleDto]


# ============================================================
# RESPONSE - LIQUIDACIÓN PERSISTIDA
# ============================================================

class LiquidacionResponse(LiquidacionBase):

    id: int

    legajo: LegajoResponse | None = None

    total_haberes: Decimal

    total_retenciones: Decimal

    total_neto: Decimal

    class Config:
        from_attributes = True


# ============================================================
# DETALLE DEL CÁLCULO DE LIQUIDACIÓN
# ============================================================

class LiquidacionDetalleResponse(BaseModel):

    concepto_id: int

    codigo: str

    concepto: str

    clasificacion_codigo: str

    clasificacion_nombre: str

    clasificacion_tipo: str

    cantidad: Decimal

    valor: Decimal

    tipo_calculo: str

    formula: Optional[str] = None

    novedad_id : Optional[int] = None

    es_novedad: bool

    orden: int

    haber: Decimal

    retencion: Decimal

    total: Decimal


# ============================================================
# TOTALES DEL CÁLCULO
# ============================================================

class LiquidacionTotalesResponse(BaseModel):

    haberes: Decimal

    descuentos: Decimal


# ============================================================
# RESPONSE - RESULTADO DEL CÁLCULO
# ============================================================

class LiquidacionCalculoResponse(BaseModel):

    detalle: list[LiquidacionDetalleResponse]

    totales: LiquidacionTotalesResponse

    neto: Decimal


class LiquidacionDetalleVisualizacionResponse(BaseModel):

    id: int

    concepto_id: int

    codigo: str

    concepto: str

    cantidad: Decimal

    valor: Decimal

    haber: Decimal

    retencion: Decimal

    total: Decimal

    class Config:
        from_attributes = True

class LiquidacionListadoResponse(BaseModel):

    id: int

    fecha: datetime

    periodo: int

    modalidad: str

    numero: int

    legajo_id: int


    ayn: str

    total_haberes: Decimal
    total_retenciones: Decimal
    total_neto: Decimal


    class Config:
        from_attributes = True


class LiquidacionVisualizacionResponse(BaseModel):

    id: int

    fecha: datetime

    periodo: int

    modalidad: str

    numero: int

    legajo_id: int

    ayn: str

    total_haberes: Decimal
    total_retenciones: Decimal
    total_neto: Decimal

    lineas: list[LiquidacionDetalleVisualizacionResponse]

    class Config:
        from_attributes = True