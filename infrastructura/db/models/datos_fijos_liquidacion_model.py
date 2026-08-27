
from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from infrastructura.db.models.tipo_liquidacion_model import TipoLiquidacionModel
from infrastructura.db.models.modalidad_liquidacion_model import ModalidadLiquidacionModel
from infrastructura.db.session import Base

class DatosFijosLiquidacionModel(Base):

    __tablename__ = "datos_fijos_liquidacion"


    id = Column(Integer, primary_key=True, index=True)

    fecha_carga = Column(DateTime, nullable=False)

    tipo_liquidacion_id = Column(
            Integer,
            ForeignKey("tipo_liquidacion.id"),
            nullable=False
        )
    

    modalidad_liquidacion_id = Column(
        Integer,
        ForeignKey("modalidad_liquidacion.id"),
        nullable=False
    )

    periodo = Column(String(8), nullable=False, index=True)

    numero =   Column(Integer, nullable=True)

    fecha_desde = Column(Date, nullable=False)

    fecha_hasta = Column(Date, nullable=False)

    periodo_pago = Column(Integer, nullable=True)

    fecha_pago = Column(Date, nullable=True)


    estado = Column(String, nullable=True, default="ABIERTO")


    tipo_liquidacion = relationship(
            "TipoLiquidacionModel",
            back_populates="datos_fijos_liquidacion"
        )
    
    modalidad_liquidacion = relationship(
        "ModalidadLiquidacionModel",
        back_populates="datos_fijos_liquidacion"
    )
