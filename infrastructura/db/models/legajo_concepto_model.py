from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
    Numeric
)
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base

class LegajoConceptoModel(Base):

    __tablename__ = "legajo_concepto"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

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


    # La columna real en BD se llama "valor_unitario" (decimal(10,2), NULL); el contrato de la API es "valor_unidad"
    valor_unidad = Column(
        "valor_unitario",
        Numeric(10, 2),
        nullable=True
    )
    
    cantidad = Column(
        Numeric(12, 2),
        nullable=False,
        default=1.0
    )

    activo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    # relaciones
    legajo = relationship(
        "LegajoModel",
        back_populates="conceptos"
    )

    concepto = relationship(
        "ConceptoModel",
        back_populates="legajos"
    )

conceptos = relationship(
    "LegajoConceptoModel",
    back_populates="legajo",
    cascade="all, delete-orphan"
)

concepto = relationship("ConceptoModel")

clasificacion_conceptos = relationship(
        "ClasificacionConceptoModel",
        back_populates="legajo_conceptos"
    )
