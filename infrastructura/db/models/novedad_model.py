from sqlalchemy import Column, Integer, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base


class NovedadModel(Base):

    __tablename__ = "legajo_novedad"

    id = Column(Integer, primary_key=True, index=True)

    legajo_id = Column(
        Integer,
        ForeignKey("legajo.id"),
        nullable=False
    )

    concepto_id = Column(
        Integer,
        ForeignKey("concepto.id"),
        nullable=False
    )

    fecha_desde = Column(Date)
    fecha_hasta = Column(Date)

    valor = Column(Numeric(15, 2), nullable=False)
    cantidad = Column(Numeric(10, 2), nullable=False)
    activo = Column(Integer)

    legajo = relationship(
        "LegajoModel"
    )

    concepto = relationship(
        "ConceptoModel"
    )