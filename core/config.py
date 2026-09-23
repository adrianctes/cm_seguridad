# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # =====================================================
    # BASE DE DATOS
    # =====================================================

    DATABASE_URL: str


    # =====================================================
    # JWT
    # =====================================================

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


    # =====================================================
    # PASSWORD TEMPORAL
    # =====================================================

    NEW_RESET_PASSWORD: str


    # =====================================================
    # CONFIGURACIÓN
    # =====================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()