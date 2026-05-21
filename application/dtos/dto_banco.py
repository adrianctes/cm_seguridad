from pydantic import BaseModel

class BancoResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True