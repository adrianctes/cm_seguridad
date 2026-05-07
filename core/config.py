# app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # 🔹 Base de datos
    DATABASE_URL: str = (
        "mysql+pymysql://root:advenir2069@localhost:3306/cm_seguridad"
    )

    # 🔹 JWT
    SECRET_KEY: str = "MI_SECRET_KEY_SUPER_SEGURA"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()