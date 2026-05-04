from fastapi import APIRouter
from api.v1.endpoints import legajos

api_router = APIRouter()

api_router.include_router(legajos.router)