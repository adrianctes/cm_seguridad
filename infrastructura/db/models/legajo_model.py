from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from infrastructura.db.session import Base


class LegajoModel(Base):
    __tablename__ = "legajo"

    # 🔹 PK
    id = Column(Integer, primary_key=True, index=True)
    # 🔹 Datos personales
    apellido = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    sexo = Column(String(1), nullable=False)
    cuil = Column(String(20), unique=True, nullable=False)
   
    # 🔹 Laborales

    activo = Column(Boolean, default=True)
    sac =Column(Boolean, default=False)

    # 🔹 FK
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    modalidad_liquidacion_id = Column(Integer, ForeignKey("modalidad_liquidacion.id"), nullable=False)

    # 🔹 Relaciones (opcional pero recomendado)
    categoria = relationship("CategoriaModel", back_populates="legajos")
    modalidad_liquidacion = relationship("ModalidadLiquidacionModel", back_populates="legajos")

    # 🔹 Relación con conceptos del empleado (preliquidación)
    #conceptos = relationship("LegajoConceptoModel", back_populates="legajo")

    # 🔹 Relación con liquidaciones generadas
    #liquidaciones = relationship("LiquidacionGeneradaModel", back_populates="legajo")