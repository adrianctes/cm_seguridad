from sqlalchemy import Column, Integer, Date, Float
from infrastructura.db.session import Base


class ConceptoNovedadModel(Base):
    __tablename__ = "concepto_novedad"

    id = Column(Integer, primary_key=True, index=True)
    legajo_id = Column(Integer)
    concepto_id = Column(Integer)
    fecha_desde = Column(Date)
    fecha_hasta = Column(Date)
    valor = Column(Float)