from pydantic import BaseModel

class CategoriaResponse(BaseModel):
    id: int
    nombre: str
    descripcion :str

    class Config:
        from_attributes = True