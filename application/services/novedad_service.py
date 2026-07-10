# application/services/legajo_novedad_service.py

from datetime import date
from typing import Optional, List

from application.dtos.dto_novedad import (
    NovedadCreate,
    NovedadUpdate
)


class NovedadService:

    def __init__(self, repo):
        self.repo = repo

    # 📥 LISTAR POR LEGAJO
    def listar(self, legajo_id: int):
        return self.repo.listar_por_legajo(legajo_id)

    # ➕ CREAR NOVEDAD
    def crear(self, legajo_id: int, data: NovedadCreate):
        self._validar_fechas(data.fecha_desde, data.fecha_hasta)

        novedad = {
            "legajo_id": legajo_id,
            "tipo": data.tipo,
            "fecha_desde": data.fecha_desde,
            "fecha_hasta": data.fecha_hasta,
            "descripcion": data.descripcion,
            "activo": True
        }

        # (opcional) validación de solapamiento
        self._validar_solapamiento(legajo_id, data.fecha_desde, data.fecha_hasta)

        return self.repo.crear(novedad)

    # ✏️ ACTUALIZAR NOVEDAD
    def actualizar(self, novedad_id: int, data: NovedadUpdate):

        novedad = self.repo.obtener_por_id(novedad_id)
        if not novedad:
            raise Exception("Novedad no encontrada")

        update_data = data.model_dump(exclude_unset=True)

        if "fecha_desde" in update_data or "fecha_hasta" in update_data:
            self._validar_fechas(
                update_data.get("fecha_desde", novedad.fecha_desde),
                update_data.get("fecha_hasta", novedad.fecha_hasta)
            )

        return self.repo.actualizar(novedad_id, update_data)

    # 🗑️ ELIMINAR (soft delete)
    def eliminar(self, novedad_id: int):
        novedad = self.repo.obtener_por_id(novedad_id)

        if not novedad:
            raise Exception("Novedad no encontrada")

        return self.repo.actualizar(novedad_id, {"activo": False})

    # 📌 ACTIVAS
    def listar_activas(self, legajo_id: int):
        return self.repo.listar_activas(legajo_id)

    # 🕒 ÚLTIMA NOVEDAD
    def ultima(self, legajo_id: int):
        return self.repo.ultima_por_legajo(legajo_id)

    # -------------------------------------------------
    # 🧠 VALIDACIONES DE NEGOCIO
    # -------------------------------------------------

    def _validar_fechas(self, desde: date, hasta: Optional[date]):
        if hasta and desde > hasta:
            raise Exception("La fecha 'desde' no puede ser mayor a 'hasta'")

    def _validar_solapamiento(
        self,
        legajo_id: int,
        desde: date,
        hasta: Optional[date]
    ):
        """
        Evita que existan dos novedades en el mismo rango de fechas.
        """

        existentes = self.repo.listar_por_legajo(legajo_id)

        for n in existentes:
            if not n.activo:
                continue

            # lógica de solapamiento
            if hasta and n.fecha_hasta:
                if not (hasta < n.fecha_desde or desde > n.fecha_hasta):
                    raise Exception("Existe solapamiento de fechas con otra novedad")

            elif not hasta or not n.fecha_hasta:
                if desde == n.fecha_desde:
                    raise Exception("Existe una novedad en la misma fecha")