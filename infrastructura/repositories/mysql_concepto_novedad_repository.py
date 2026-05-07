from sqlalchemy.orm import Session
from domain.entities.concepto_novedad_entity import ConceptoNovedad
from domain.repositories.concepto_novedad_repositorio_interface import ConceptoNovedadRepository
from infrastructura.db.models.concepto_novedad_model import ConceptoNovedadModel


class MySQLConceptoNovedadRepository(ConceptoNovedadRepository):

    def __init__(self, db: Session):
        self.db = db

    # 🔹 Crear
    def crear(self, novedad: ConceptoNovedad) -> ConceptoNovedad:
        model = ConceptoNovedadModel(
            legajo_id=novedad.legajo_id,
            concepto_id=novedad.concepto_id,
            fecha_desde=novedad.fecha_desde,
            fecha_hasta=novedad.fecha_hasta,
            valor=novedad.valor
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    # 🔹 Obtener por ID
    def obtener_por_id(self, id: int) -> ConceptoNovedad:
        model = self.db.get(ConceptoNovedadModel, id)
        return self._to_entity(model) if model else None

    # 🔹 Listar por legajo
    def listar_por_legajo(self, legajo_id: int):
        modelos = (
            self.db.query(ConceptoNovedadModel)
            .filter(ConceptoNovedadModel.legajo_id == legajo_id)
            .all()
        )

        return [self._to_entity(m) for m in modelos]

    # 🔹 Listar vigentes (🔥 clave para liquidación)
    def listar_vigentes(self, legajo_id: int, fecha):
        modelos = (
            self.db.query(ConceptoNovedadModel)
            .filter(ConceptoNovedadModel.legajo_id == legajo_id)
            .filter(ConceptoNovedadModel.fecha_desde <= fecha)
            .filter(
                (ConceptoNovedadModel.fecha_hasta == None) |
                (ConceptoNovedadModel.fecha_hasta >= fecha)
            )
            .all()
        )

        return [self._to_entity(m) for m in modelos]

    # 🔹 Actualizar
    def actualizar(self, novedad: ConceptoNovedad):
        model = self.db.get(ConceptoNovedadModel, novedad.id)

        if not model:
            return None

        model.legajo_id = novedad.legajo_id
        model.concepto_id = novedad.concepto_id
        model.fecha_desde = novedad.fecha_desde
        model.fecha_hasta = novedad.fecha_hasta
        model.valor = novedad.valor

        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    # 🔹 Eliminar
    def eliminar(self, id: int) -> bool:
        model = self.db.get(ConceptoNovedadModel, id)

        if not model:
            return False

        self.db.delete(model)
        self.db.commit()

        return True

    # 🔹 Mapper interno
    def _to_entity(self, model: ConceptoNovedadModel) -> ConceptoNovedad:
        return ConceptoNovedad(
            id=model.id,
            legajo_id=model.legajo_id,
            concepto_id=model.concepto_id,
            fecha_desde=model.fecha_desde,
            fecha_hasta=model.fecha_hasta,
            valor=model.valor
        )