from sqlalchemy.orm import Session

from domain.repositories.legajo_conceptos_repositorio_interface import (
    ILegajoConceptoRepository
)

from domain.entities.legajo_concepto_entity import (
    LegajoConcepto
)

from infrastructura.db.models.legajo_concepto_model import (
    LegajoConceptoModel
)


class MySQLLegajoConceptoRepository(
    ILegajoConceptoRepository
):

    def __init__(self, db: Session):
        self.db = db

    def crear(
        self,
        entity: LegajoConcepto
    ):

        model = LegajoConceptoModel(
            legajo_id=entity.legajo_id,
            concepto_id=entity.concepto_id,
            valor=entity.valor,
            activo=entity.activo
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return model

    def obtener(
        self,
        id: int
    ):

        return (
            self.db.query(
                LegajoConceptoModel
            )
            .filter(
                LegajoConceptoModel.id == id
            )
            .first()
        )

    def listar(
        self,
        legajo_id=None
    ):

        query = (
            self.db.query(
                LegajoConceptoModel
            )
        )

        if legajo_id:

            query = query.filter(
                LegajoConceptoModel.legajo_id
                == legajo_id
            )

        return query.all()

    def actualizar(
        self,
        id,
        entity
    ):

        model = self.obtener(id)

        if not model:
            return None

        model.concepto_id = entity.concepto_id
        model.valor = entity.valor
        model.activo = entity.activo

        self.db.commit()
        self.db.refresh(model)

        return model

    def eliminar(
        self,
        id
    ):

        model = self.obtener(id)

        if not model:
            return False

        self.db.delete(model)

        self.db.commit()

        return True