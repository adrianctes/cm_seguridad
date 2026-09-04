from datetime import datetime

from sqlalchemy import select

from infrastructura.db.models.auditoria import (
    AuditoriaModel
)


class MySqlAuditoriaRepository:

    def __init__(self, db):
        self.db = db

    def crear(self, auditoria: AuditoriaModel):
        self.db.add(auditoria)
        self.db.commit()
        self.db.refresh(auditoria)

        return auditoria

    def listar_por_usuario(
        self,
        usuario_id: int
    ):
        stmt = (
            select(AuditoriaModel)
            .where(
                AuditoriaModel.usuario_id == usuario_id
            )
            .order_by(
                AuditoriaModel.fecha_hora.desc()
            )
        )

        return self.db.execute(stmt).scalars().all()

    def listar_desde_fecha(
        self,
        fecha_desde: datetime
    ):
        stmt = (
            select(AuditoriaModel)
            .where(
                AuditoriaModel.fecha_hora >= fecha_desde
            )
            .order_by(
                AuditoriaModel.fecha_hora.desc()
            )
        )

        return self.db.execute(stmt).scalars().all()

    def listar_por_usuario_desde_fecha(
        self,
        usuario_id: int,
        fecha_desde: datetime
    ):
        stmt = (
            select(AuditoriaModel)
            .where(
                AuditoriaModel.usuario_id == usuario_id,
                AuditoriaModel.fecha_hora >= fecha_desde
            )
            .order_by(
                AuditoriaModel.fecha_hora.desc()
            )
        )

        return self.db.execute(stmt).scalars().all()