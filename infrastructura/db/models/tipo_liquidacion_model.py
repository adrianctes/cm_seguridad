from sqlalchemy import Column, Integer, String
from infrastructura.db.session import Base
from sqlalchemy.orm import relationship

class TipoLiquidacionModel(Base):

    __tablename__ = "tipo_liquidacion"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    datos_fijos_liquidacion = relationship(
        "DatosFijosLiquidacionModel",
        back_populates="tipo_liquidacion"
    )