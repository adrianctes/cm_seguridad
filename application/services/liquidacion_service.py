from application.dtos.dto_modalidad_liquidacion import LiquidacionUpdateValor
from domain.entities.liquidacion import Liquidacion
from domain.repositories.liquidacion_repositorio_interface import LiquidacionRepository


class LiquidacionService:

    def __init__(self, repo: LiquidacionRepository):
        self.repo = repo

    def crear(self, data):
        liquidacion = Liquidacion(
            id=None,
            legajo_id=data.legajo_id,
            concepto_id=data.concepto_id,
            valor=data.valor,
            tipo_liquidacion_id=data.tipo_liquidacion_id
        )
    
        return self.repo.crear(liquidacion)
    
    def actualizar(self, id: int, data: LiquidacionUpdateValor):
        liquidacion = self.repo.obtener_por_id(id)

        if not liquidacion:
            raise Exception("Liquidación no encontrada")

        liquidacion.valor = data.valor

        return self.repo.actualizar(liquidacion)

    def obtener(self, id: int):
        return self.repo.obtener_por_id(id)

    def listar_por_legajo(self, legajo_id: int):
        return self.repo.listar_por_legajo(legajo_id)

    def eliminar(self, id: int):
        self.repo.eliminar(id)