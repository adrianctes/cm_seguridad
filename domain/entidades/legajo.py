from datetime import date


class Legajo:

    def __init__(
        self,
        id: int,
        apellido: str,
        nombre: str,
        sexo: str,
        cuil: str,
        categoria_id: int,
       # modalidad_liquidacion_id: int,
        activo: bool = True,
        sac: bool =True
    ):
        self.id = id
        self.apellido = apellido
        self.nombre = nombre
        self.sexo= sexo
        self.cuil = cuil
        self.categoria_id = categoria_id
       # self.modalidad_liquidacion_id = modalidad_liquidacion_id
        self.activo = activo
        self.sac = sac

    # 🔹 Regla de negocio
    def esta_activo(self) -> bool:
        return self.activo

    # 🔹 Lógica de negocio
    def calcular_antiguedad(self, fecha: date) -> int:
        return (fecha - self.fecha_ingreso).days // 365

    # 🔹 Regla de negocio
    def puede_liquidar(self) -> bool:
        return self.activo is True