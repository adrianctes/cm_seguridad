from fastapi import APIRouter
from api.v1.endpoints import (legajos,
                              conceptos,
                              liquidacion,
                              concepto_novedad,
                              usuario,
                              auth)
api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(legajos.router)
api_router.include_router(usuario.router)
api_router.include_router(conceptos.router)
api_router.include_router(liquidacion.router)
api_router.include_router(concepto_novedad.router)
