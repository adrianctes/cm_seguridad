from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint
)

from infrastructura.db.session import Base


class RolPermisoModel(Base):
    __tablename__ = "rol_permisos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    rol = Column(
        String(45),
        nullable=False,
        index=True
    )

    permiso_id = Column(
        Integer,
        ForeignKey(
            "permisos.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "rol",
            "permiso_id",
            name="uq_rol_permiso"
        ),
    )