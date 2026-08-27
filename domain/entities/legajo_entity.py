from datetime import date
from decimal import Decimal
from domain.entities.banco_entity import Banco
from domain.entities.categoria_entity import Categoria
from domain.entities.modalidad_liquidacion_entity import ModalidadLiquidacion


class Legajo:

    def __init__(
        self,
        id: int,
        apellido: str,
        nombre: str,
        sexo: str,
        cuil: str,
        categoria_id: int,
        modalidad_liquidacion_id: int,
        categoria : Categoria  | None = None,
        modalidad_liquidacion : ModalidadLiquidacion | None = None,
        activo: bool = False,
        sac: bool =True,
        telefono: str = None,
        banco_id: int  | None = None,
        banco: Banco  | None = None,
        cbu : str  | None = None,
        fecha_ingreso_actual :  date | None = None,
        modalidad_pago_id:  int| None = None,
        valor_modalidad_pago: Decimal  | None = None,
    ):
        self.id = id
        self.apellido = apellido
        self.nombre = nombre
        self.sexo= sexo
        self.cuil = cuil
        self.categoria_id = categoria_id
        self.categoria= categoria
        self.modalidad_liquidacion_id = modalidad_liquidacion_id
        self.modalidad_liquidacion = modalidad_liquidacion
        self.activo = activo
        self.sac = sac
        self.telefono = telefono
        self.banco_id = banco_id
        self.banco = banco
        self.cbu = cbu
        self.fecha_ingreso_actual = fecha_ingreso_actual
        self.modalidad_pago_id = modalidad_pago_id
        self.valor_modalidad_pago = valor_modalidad_pago

    # 🔹 Regla de negocio
    def esta_activo(self) -> bool:
        return self.activo

    # 🔹 Lógica de negocio
    def calcular_antiguedad(self, fecha: date) -> int:
        return (fecha - self.fecha_ingreso).days // 365

    # 🔹 Regla de negocio
    def puede_liquidar(self) -> bool:
        return self.activo is True