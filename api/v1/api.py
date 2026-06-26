from fastapi import APIRouter, Depends
from api.v1.endpoints import (auth,
                              bancos,
                              categorias,
                              clasificacion_concepto,
                              conceptos,
                              concepto_novedad,
                              historia_laboral,
                              legajos,
                              liquidacion,
                              modalidad,
                              usuario,
                             )
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

api_router.include_router(bancos.router)
api_router.include_router(categorias.router)
api_router.include_router(modalidad.router)
api_router.include_router(historia_laboral.router)
api_router.include_router(clasificacion_concepto.router)

