from fastapi import FastAPI
from api.v1.api import api_router
from core.middleware.auth_middleware import AuthMiddleware

app = FastAPI(
    title="Sistema de gestion de CM",
    version="1.0.0"
)
app.add_middleware(AuthMiddleware)
# 🔹 incluir rutas
app.include_router(api_router, prefix="/api/v1")