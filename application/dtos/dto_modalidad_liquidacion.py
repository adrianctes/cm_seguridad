from decimal import Decimal

from pydantic import BaseModel

class ModalidadLiquidacionResponse(BaseModel):
    id: int
    nombre: str
 

    class Config:
        from_attributes = True

class LiquidacionUpdateValor(BaseModel):
    valor: Decimal 