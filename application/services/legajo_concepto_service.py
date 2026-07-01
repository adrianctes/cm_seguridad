from application.dtos.dto_legajo_concepto import (
    LegajoConceptoCreate,
    LegajoConceptoUpdate
)

from domain.entities.legajo_concepto_entity import (
    LegajoConcepto
)

from domain.repositories.legajo_conceptos_repositorio_interface import ILegajoConceptoRepository

class LegajoConceptoService:

    def __init__(self, repo:ILegajoConceptoRepository):
        self.repo = repo

    # =========================
    # CREAR
    # =========================
    def crear(
        self,
        legajo_id : int,
        data: LegajoConceptoCreate
    ):

        entity = LegajoConcepto(
            legajo_id=legajo_id,
            concepto_id=data.concepto_id,
            valor=data.valor,
            activo=data.activo
        )

        return self.repo.crear(entity)

    # =========================
    # OBTENER
    # =========================
    def obtener(
        self,
        id: int
    ):

        item = self.repo.obtener(id)

        if not item:
            raise Exception(
                "Concepto de legajo no encontrado"
            )

        return item

    # =========================
    # LISTAR
    # =========================
    def listar(
        self,
        legajo_id: int 
    ):

        return self.repo.listar(
            legajo_id
        )

    # =========================
    # ACTUALIZAR
    # =========================
    def actualizar(
        self,
        id: int,
        data: LegajoConceptoUpdate
    ):

        actual = self.repo.obtener(id)

        if not actual:
            raise Exception(
                "Concepto de legajo no encontrado"
            )

        entity = LegajoConcepto(
            id=id,
            legajo_id=actual.legajo_id,

            concepto_id=(
                data.concepto_id
                if data.concepto_id is not None
                else actual.concepto_id
            ),
        

            valor=(
                data.valor
                if data.valor is not None
                else actual.valor
            ),

            activo=(
                data.activo
                if data.activo is not None
                else actual.activo
            )
        )

        return self.repo.actualizar(
            id,
            entity
        )

    # =========================
    # ELIMINAR
    # =========================
    def eliminar(
        self,
        id: int
    ):

        eliminado = self.repo.eliminar(id)

        if not eliminado:
            raise Exception(
                "Concepto de legajo no encontrado"
            )

        return {
            "message": "Eliminado correctamente"
        }