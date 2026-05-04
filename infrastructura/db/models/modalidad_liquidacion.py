from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base


class ModalidadLiquidacionModel(Base):
    __tablename__ = "modalidad_liquidacion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
 
    legajos = relationship("LegajoModel", back_populates="modalidad_liquidacion")