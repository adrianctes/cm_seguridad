from pydantic import BaseModel

class ClasificacionResponse(BaseModel):
    id: int
    codigo: str
    nombre: str
    tipo :str

    class Config:
        from_attributes = True