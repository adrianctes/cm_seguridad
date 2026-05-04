# app/infrastructure/db/session.py

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from core.config import settings

# 🔹 URL de conexión
# ejemplo: mysql+mysqlconnector://root:root123@localhost:3306/liquidaciones
DATABASE_URL = settings.DATABASE_URL

# 🔹 Engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_timeout=10,
    connect_args={
        "connect_timeout": 5
    }
)

# 🔹 Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# 🔹 Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()