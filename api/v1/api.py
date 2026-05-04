from fastapi import APIRouter
from api.v1.endpoints import legajos,conceptos

api_router = APIRouter()

api_router.include_router(legajos.router)
api_router.include_router(conceptos.router)