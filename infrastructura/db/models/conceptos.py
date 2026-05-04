from sqlalchemy import Column, Integer, String, Boolean
from infrastructura.db.session import Base

class ConceptoModel(Base):
    __tablename__ = "concepto"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(2), nullable=False)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(1), nullable=False)
    es_remunerativo = Column(Boolean, default=True)
    activo = Column(Boolean, default=True)
    requiere_novedad = Column(Boolean, nullable=True)