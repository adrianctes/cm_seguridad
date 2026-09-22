from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    UniqueConstraint
)

from infrastructura.db.session import Base


class PermisoModel(Base):
    __tablename__ = "permisos"

    id = Column(Integer, primary_key=True, index=True)

    modulo = Column(
        String(50),
        nullable=False
    )

    accion = Column(
        String(50),
        nullable=False
    )

    codigo = Column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )

    activo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    orden = Column(Integer, nullable=False, default=0, index=True)

    __table_args__ = (
        UniqueConstraint(
            "modulo",
            "accion",
            name="uq_permiso_modulo_accion"
        ),
    )