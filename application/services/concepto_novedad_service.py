from fastapi import HTTPException

from domain.entities.concepto_novedad_entity import ConceptoNovedad

class ConceptoNovedadService:

    def __init__(self, repo):
        self.repo = repo

    def crear(self, data):
        novedad = ConceptoNovedad(
            id=None,
            legajo_id=data.legajo_id,
            concepto_id=data.concepto_id,
            fecha_desde=data.fecha_desde,
            fecha_hasta=data.fecha_hasta,
            valor=data.valor
        )
        return self.repo.crear(novedad)

    def obtener(self, id: int):
        novedad = self.repo.obtener_por_id(id)
        if not novedad:
            raise HTTPException(status_code=404, detail="No encontrado")
        return novedad

    def listar_por_legajo(self, legajo_id: int):
        return self.repo.listar_por_legajo(legajo_id)

    def listar_vigentes(self, legajo_id: int, fecha):
        return self.repo.listar_vigentes(legajo_id, fecha)

    def actualizar(self, id: int, data):
        novedad = self.repo.obtener_por_id(id)

        if not novedad:
            raise HTTPException(status_code=404, detail="No encontrado")

        if data.fecha_desde is not None:
            novedad.fecha_desde = data.fecha_desde

        if data.fecha_hasta is not None:
            novedad.fecha_hasta = data.fecha_hasta

        if data.valor is not None:
            novedad.valor = data.valor

        return self.repo.actualizar(novedad)

    def eliminar(self, id: int):
        ok = self.repo.eliminar(id)
        if not ok:
            raise HTTPException(status_code=404, detail="No encontrado")
        return {"message": "Eliminado"}