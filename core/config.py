# app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:advenir2069@localhost:3306/cm_seguridad"

settings = Settings()