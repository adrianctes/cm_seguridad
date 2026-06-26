from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base

class ConceptoModel(Base):
    __tablename__ = "concepto"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(2), nullable=False)
    nombre = Column(String(100), nullable=False)
    orden =  Column(Integer, nullable=False)
    tipo_calculo = Column(String(1), nullable=False)
    formula = Column(String(100), nullable=True)
    activo = Column(Boolean, default=True)
    es_novedad = Column(Boolean, nullable=True,  server_default="0")
    modalidad_pago_id =  Column(Integer, nullable=True)
    clasificacion_concepto_id =  Column(Integer, ForeignKey("clasificacion_concepto.id"), nullable=False)
    clasificacion_concepto = relationship("ClasificacionConceptoModel", back_populates="concepto")
    liquidaciones = relationship("LiquidacionModel", back_populates="concepto")
