from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base


class CategoriaModel(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(60), nullable=False)
    descripcion = Column(String(100), nullable=False)

    legajos = relationship("LegajoModel", back_populates="categoria")
    
