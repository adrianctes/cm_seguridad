# infrastructura/db/models/usuario_model.py

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from infrastructura.db.session import Base


class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    activo = Column(Boolean, default=True)
    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )