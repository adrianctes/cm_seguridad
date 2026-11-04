from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base

class ConceptoModel(Base):
    __tablename__ = "concepto"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer, nullable=True, unique=True)
    nombre = Column(String(100), nullable=False)
    orden = Column(Integer, nullable=True)
    tipo_calculo = Column(String(10), nullable=True)
    formula = Column(String(60), nullable=True)
    activo = Column(Boolean, default=True, server_default="1")
    es_novedad = Column(Boolean, nullable=True, default=True, server_default="1")
    clasificacion_concepto_id = Column(Integer, ForeignKey("clasificacion_concepto.id"), nullable=False)
    abreviatura = Column(String(10), nullable=True)
    secuencia = Column(Integer, nullable=True)
    unidad_medida = Column(
        "unidad_medida",
        Enum("DIA", "HORA", "IMPORTE", name="unidad_medida"),
        nullable=True
    )
    clasificacion_concepto = relationship("ClasificacionConceptoModel", back_populates="concepto")
    #liquidaciones = relationship("LiquidacionModel", back_populates="concepto")
    legajos = relationship("LegajoConceptoModel", back_populates="concepto")
