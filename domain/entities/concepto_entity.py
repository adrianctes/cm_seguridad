from typing import Optional

class Concepto:
     
    def __init__(
        self,
        codigo: str,
        nombre: str,
        clasificacion_concepto_id :int,
        tipo_calculo: str,
        formula :Optional[str] = None,
        activo: bool = True,
        es_novedad: Optional[bool] = None,
        orden:  Optional[int]= None,
        modalidad_pago_id :  Optional[int]= None,
        id: Optional[int]= None
    ):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.orden = orden
        self.clasificacion_concepto_id = clasificacion_concepto_id
        self.modalidad_pago_id = modalidad_pago_id
        self.tipo_calculo = tipo_calculo
        self.formula = formula
        self.activo = activo
        self.es_novedad = es_novedad