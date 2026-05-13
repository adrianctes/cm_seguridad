from fastapi import APIRouter, Depends
from api.v1.endpoints import (categorias,
                              modalidad,
                              legajos,
                              conceptos,
                              liquidacion,
                              concepto_novedad,
                              usuario,
                              auth)
from core.dependencias import get_current_user
api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(legajos.router,
                          dependencies=[Depends(get_current_user)])
api_router.include_router(usuario.router,
                           dependencies=[Depends(get_current_user)])
api_router.include_router(conceptos.router,
                           dependencies=[Depends(get_current_user)])
api_router.include_router(liquidacion.router,
                           dependencies=[Depends(get_current_user)])
api_router.include_router(concepto_novedad.router,
                           dependencies=[Depends(get_current_user)])

api_router.include_router(categorias.router)
api_router.include_router(modalidad.router)
