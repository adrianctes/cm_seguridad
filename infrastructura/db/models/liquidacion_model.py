from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base

class LiquidacionModel(Base):
    __tablename__ = "liquidacion"

    id = Column(Integer, primary_key=True, index=True)
    legajo_id = Column(Integer, nullable=False)
    concepto_id =Column(Integer, ForeignKey("concepto.id"), nullable=False)
    valor = Column(Float, nullable=False)
    tipo_liquidacion_id = Column(Integer, nullable=False)

    concepto = relationship(
        "ConceptoModel",
        back_populates="liquidaciones"   # 🔥 clave
    )