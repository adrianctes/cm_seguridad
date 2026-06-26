from pydantic import BaseModel

class ClasificacionResponse(BaseModel):
    id: int
    codigo: str
    nombre: str
    tipo :str
    orden: int

    class Config:
        from_attributes = True