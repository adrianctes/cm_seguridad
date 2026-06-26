from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base


class ClasificacionConceptoModel(Base):
    __tablename__ = "clasificacion_concepto"

    id = Column(Integer, primary_key=True)
    codigo = Column(String(6), nullable=False)
    nombre = Column(String(60), nullable=False)
    tipo= Column(String(1), nullable=False)
    orden = Column(Integer, nullable=False)

    concepto = relationship("ConceptoModel", back_populates="clasificacion_concepto")