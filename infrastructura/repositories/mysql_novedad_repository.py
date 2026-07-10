from datetime import date

from infrastructura.db.models.conceptos_model import ConceptoModel
from infrastructura.db.models.legajo_model import LegajoModel
from sqlalchemy.orm import Session
from sqlalchemy import select
from domain.entities.novedad_entity import Novedad
from domain.repositories.legajo_novedad_repositorio_interface import LegajoNovedadRepository
from infrastructura.db.models.novedad_model import NovedadModel


class MySQLNovedadRepository(LegajoNovedadRepository):

    def __init__(self, db: Session):
        self.db = db

    # 🔹 Crear
    def crear(self, novedad: Novedad) -> Novedad:
        try:
            model = NovedadModel(
                legajo_id=novedad.legajo_id,
                concepto_id=novedad.concepto_id,
                fecha_desde=novedad.fecha_desde,
                fecha_hasta=novedad.fecha_hasta,
                valor=novedad.valor,
                cantidad = novedad.cantidad,
                activo = novedad.activo
            )
            print(model)
            self.db.add(model)
            self.db.commit()
            self.db.refresh(model)

            return self._to_entity(model)
        except Exception as ex:
            print(ex.args)
            raise ex.args

    # 🔹 Obtener por ID
    def obtener_por_id(self, id: int) -> Novedad:
        model = self.db.get(NovedadModel, id)
        return self._to_entity(model) if model else None
    
    # 🔹 Obtener por PERIODO
    def obtener_por_periodo(self, anio: int, mes: int):
        from datetime import date

        fecha_inicio = date(anio, mes, 1)
        fecha_fin = date(anio + 1, 1, 1) if mes == 12 else date(anio, mes + 1, 1)

        stmt = (
            select(
                NovedadModel.id,
                NovedadModel.fecha_desde,
                NovedadModel.fecha_hasta,
                NovedadModel.cantidad,
                NovedadModel.valor,
                NovedadModel.activo,
              

                LegajoModel.id.label("legajo_id"),
                LegajoModel.apellido,
                LegajoModel.nombre,
               

                ConceptoModel.id.label("concepto_id"),
                ConceptoModel.codigo.label("codigo_concepto"),
                ConceptoModel.nombre.label("concepto")
            )
            .join(LegajoModel, LegajoModel.id == NovedadModel.legajo_id)
            .join(ConceptoModel, ConceptoModel.id == NovedadModel.concepto_id)
            .where(
                NovedadModel.fecha_desde >= fecha_inicio,
                NovedadModel.fecha_desde < fecha_fin
            )
        )

        rows = self.db.execute(stmt).mappings().all()

        return rows
    # 🔹 Listar por legajo
    def listar_por_legajo(self, legajo_id: int):
        modelos = (
            self.db.query(NovedadModel)
            .filter(NovedadModel.legajo_id == legajo_id)
            .all()
        )

        return [self._to_entity(m) for m in modelos]

    # 🔹 Listar vigentes (🔥 clave para liquidación)
    def listar_vigentes(self, legajo_id: int, fecha):
        modelos = (
            self.db.query(NovedadModel)
            .filter(NovedadModel.legajo_id == legajo_id)
            .filter(NovedadModel.fecha_desde <= fecha)
            .filter(
                (NovedadModel.fecha_hasta == None) |
                (NovedadModel.fecha_hasta >= fecha)
            )
            .all()
        )

        return [self._to_entity(m) for m in modelos]

    # 🔹 Actualizar
    def actualizar(self, novedad: Novedad):
        model = self.db.get(NovedadModel, novedad.id)

        if not model:
            return None
     
        model.legajo_id = novedad.legajo_id
        model.concepto_id = novedad.concepto_id
        model.fecha_desde = novedad.fecha_desde
        model.fecha_hasta = novedad.fecha_hasta
        model.valor = novedad.valor
        model.cantidad = novedad.cantidad

        self.db.commit()
        self.db.refresh(model)

        return self._to_entity(model)

    # 🔹 Eliminar
    def eliminar(self, id: int) -> bool:
        model = self.db.get(NovedadModel, id)

        if not model:
            return False

        self.db.delete(model)
        self.db.commit()

        return True

    # 🔹 Mapper interno
    def _to_entity(self, model: NovedadModel) -> Novedad:
        return Novedad(
            id=model.id,
            legajo_id=model.legajo_id,
            concepto_id=model.concepto_id,
            fecha_desde=model.fecha_desde,
            fecha_hasta=model.fecha_hasta,
            valor=model.valor,
            cantidad = model.cantidad,
            activo = model.activo
        )