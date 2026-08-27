from datetime import date

from fastapi import HTTPException

from domain.entities.novedad_entity import Novedad

class NovedadService:

    def __init__(self, repo):
        self.repo = repo

    def crear(self, data):
     
        novedad = Novedad(
            id=None,
            legajo_id=data.legajo_id,
            concepto_id=data.concepto_id,
            fecha_desde=data.fecha_desde,
            fecha_hasta=data.fecha_hasta,
            valor=data.valor,
            cantidad = data.cantidad
        )
   
        return self.repo.crear(novedad)

    def obtener(self, id: int):
        novedad = self.repo.obtener_por_id(id)
        if not novedad:
            raise HTTPException(status_code=404, detail="No encontrado")
        return novedad
    
    def obtener_por_periodo(self, fecha: date,
                                  tipo_busqueda: str | None = None,
                                  busqueda: str | None = None ):
        
        novedades = self.repo.obtener_por_periodo(fecha, tipo_busqueda, busqueda)

        if not novedades:
            raise HTTPException(status_code=404, detail="No encontrado")
        return novedades

    def listar_por_legajo(self, legajo_id: int):
        return self.repo.listar_por_legajo(legajo_id)

    def listar_vigentes(self, legajo_id: int, fecha):
        return self.repo.listar_vigentes(legajo_id, fecha)

    def actualizar(self, id: int, data):
        novedad = self.repo.obtener_por_id(id)

        if not novedad:
            raise HTTPException(status_code=404, detail="No encontrado")

        novedad.legajo_id = data.legajo_id
        novedad.concepto_id = data.concepto_id
        novedad.fecha_desde = data.fecha_desde
        novedad.fecha_hasta = data.fecha_hasta
        novedad.valor = data.valor
        novedad.cantidad = data.cantidad

        return self.repo.actualizar(novedad)

    def eliminar(self, id: int):
        ok = self.repo.eliminar(id)
        if not ok:
            raise HTTPException(status_code=404, detail="No encontrado")
        return {"message": "Eliminado"}