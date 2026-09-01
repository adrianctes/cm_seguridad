from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from infrastructura.db.session import Base


class LiquidacionDetalleModel(Base):

    __tablename__ = "liquidacion_detalle"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    liquidacion_id = Column(
        Integer,
        ForeignKey("liquidacion.id"),
        nullable=False
    )

    concepto_id = Column(
        Integer,
        ForeignKey("concepto.id"),
        nullable=False
    )

    legajo_novedad_id = Column(
        Integer,
        ForeignKey("legajo_novedad.id"),
        nullable=True
    )

    cantidad = Column(
        Numeric(10, 2),
        nullable=False
    )

    valor = Column(
        Numeric(10, 2),
        nullable=False
    )

    haber = Column(
        Numeric(10, 2),
        nullable=False
    )

    retencion = Column(
        Numeric(10, 2),
        nullable=False
    )

    total = Column(
        Numeric(10, 2),
        nullable=False
    )

    # Liquidación
    liquidacion = relationship(
        "LiquidacionModel",
        back_populates="lineas_liquidacion"
    )

    # Concepto
    concepto = relationship(
        "ConceptoModel",
        lazy="joined"
    )

    # Novedad
    novedad = relationship(
        "NovedadModel",
        lazy="joined"
    )