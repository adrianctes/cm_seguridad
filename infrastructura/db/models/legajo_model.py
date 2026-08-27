from decimal import Decimal

from sqlalchemy import Column, DateTime, Integer, Numeric, String,  Boolean, ForeignKey
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base


class LegajoModel(Base):
    __tablename__ = "legajo"

    # 🔹 PK
    id = Column(Integer, primary_key=True, index=True)
    # 🔹 Datos personales
    cuil =  Column(String(13), nullable=True)
    apellido = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    sexo = Column(String(1), nullable=False)
    activo = Column(Boolean, default=True)
    sac =Column(Boolean, default=False)
    telefono = Column(String(15), nullable=False)
    cbu  = Column(String(22), nullable=False)
    fecha_ingreso_actual = Column( DateTime,   nullable=True)
   
    # 🔹 FK
    banco_id =  Column(Integer, ForeignKey("banco.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    modalidad_liquidacion_id = Column(Integer, ForeignKey("modalidad_liquidacion.id"), nullable=False)
    modalidad_pago_id = Column(Integer,  nullable=False)
    valor_modalidad_pago = Column(Numeric(10, 2), nullable=False)

    # 🔹 Relaciones (opcional pero recomendado)
    categoria = relationship("CategoriaModel", back_populates="legajos")
    modalidad_liquidacion = relationship("ModalidadLiquidacionModel", back_populates="legajos")
    banco = relationship("BancoModel", back_populates="legajos")

    historia_laboral = relationship(
        "HistoriaLaboralModel",
        back_populates="legajo",
        cascade="all, delete-orphan"
    )
    conceptos = relationship(
        "LegajoConceptoModel",
        back_populates="legajo",
        cascade="all, delete-orphan"
    )
    # 🔹 Relación con conceptos del empleado (preliquidación)
    #conceptos = relationship("LegajoConceptoModel", back_populates="legajo")

    # 🔹 Relación con liquidaciones generadas
    liquidacion = relationship("LiquidacionModel", back_populates="legajo")