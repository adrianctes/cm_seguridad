from sqlalchemy import Column, ForeignKey, Integer, Numeric, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from infrastructura.db.session import Base


class LiquidacionModel(Base):
    __tablename__ = "liquidacion"

    __table_args__ = (
        UniqueConstraint(
            "legajo_id",
            "datos_fijos_liquidacion_id",
            name="uq_liquidacion_legajo_datos_fijos"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    legajo_id = Column(
        Integer,
        ForeignKey("legajo.id"),
        nullable=False
    )

    datos_fijos_liquidacion_id = Column(
        Integer,
        ForeignKey("datos_fijos_liquidacion.id"),
        nullable=False
    )

    tipo_liquidacion_id = Column(
        Integer,
        nullable=False
    )

    fecha = Column(
        DateTime,
        nullable=False,
        default=datetime.now
    )

    total_haberes = Column(
        Numeric(10, 2),
        nullable=False
    )

    total_retenciones = Column(
        Numeric(10, 2),
        nullable=False
    )

    total_neto = Column(
        Numeric(10, 2),
        nullable=False
    )

    # -------------------------
    # Relaciones
    # -------------------------

    legajo = relationship(
        "LegajoModel",
        back_populates="liquidacion"
    )

    lineas_liquidacion = relationship(
        "LiquidacionDetalleModel",
        back_populates="liquidacion",
        cascade="all, delete-orphan"
    )

    datos_fijos_liquidacion = relationship(
        "DatosFijosLiquidacionModel"
    )
