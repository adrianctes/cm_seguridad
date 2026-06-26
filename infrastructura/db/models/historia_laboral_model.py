from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from infrastructura.db.session import Base



class HistoriaLaboralModel(Base):

    __tablename__ = "historia_laboral"

    # =========================================
    # PK
    # =========================================

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # =========================================
    # FK
    # =========================================

    legajo_id = Column(
        Integer,
        ForeignKey(
            "legajo.id",
            ondelete="RESTRICT"
        ),
        nullable=False
    )    

    tipo_id = Column(
        Integer,
        nullable=False
    )

    # =========================================
    # DATOS
    # =========================================

    fecha = Column(
        DateTime,
        nullable=False
    )

    observacion = Column(
        Text,
        nullable=True
    )

    # =========================================
    # RELACIONES
    # =========================================

    legajo = relationship(
        "LegajoModel",
        back_populates="historia_laboral"
    )
   