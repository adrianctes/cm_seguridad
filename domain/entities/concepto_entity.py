from typing import Optional

class Concepto:
     
    def __init__(
        self,
        id: Optional[int],
        codigo: str,
        nombre: str,
        tipo: str,
        es_remunerativo: bool = True,
        activo: bool = True,
        requiere_novedad: Optional[bool] = None
    ):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.es_remunerativo = es_remunerativo
        self.activo = activo
        self.requiere_novedad = requiere_novedad