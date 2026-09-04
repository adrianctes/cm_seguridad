from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Integer,
    JSON,
    String,
)
from sqlalchemy.sql import func

from infrastructura.db.session import Base


class AuditoriaModel(Base):
    __tablename__ = "auditoria_usuario"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    usuario_id = Column(
        Integer,
        nullable=False
    )

    accion = Column(
        String(50),
        nullable=False
    )

    entidad = Column(
        String(100),
        nullable=False
    )

    entidad_id = Column(
        BigInteger,
        nullable=True
    )

    descripcion = Column(
        String(500),
        nullable=True
    )

    datos_anteriores = Column(
        JSON,
        nullable=True
    )

    datos_nuevos = Column(
        JSON,
        nullable=True
    )

    ip = Column(
        String(45),
        nullable=True
    )

    user_agent = Column(
        String(500),
        nullable=True
    )

    fecha_hora = Column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp()
    )