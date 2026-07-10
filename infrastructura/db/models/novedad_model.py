from sqlalchemy import Column, Integer, Date, Float
from infrastructura.db.session import Base


class NovedadModel(Base):
    __tablename__ = "legajo_novedad"

    id = Column(Integer, primary_key=True, index=True)
    legajo_id = Column(Integer)
    concepto_id = Column(Integer)
    fecha_desde = Column(Date)
    fecha_hasta = Column(Date)
    valor = Column(Float)
    cantidad = Column(Float)
    activo = Column(Integer)

 