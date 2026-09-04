from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from application.services.auditoria_service  import (
    AuditoriaService,
)

from application.dtos.dto_auditoria  import (
    AuditoriaUsuarioCreateDto,
    AuditoriaUsuarioResponseDto,
)
from core.dependencias import get_auditoria_repository


router = APIRouter(
    prefix="/auditoria",
    tags=["Auditoría"]
)
@router.post(
    "",
    response_model=AuditoriaUsuarioResponseDto
)
def crear(
    data: AuditoriaUsuarioCreateDto,
    repo = Depends(get_auditoria_repository)): 
    service = AuditoriaService(repo)  
    return service.crear(
        usuario_id=data.usuario_id,
        accion=data.accion,
        entidad=data.entidad,
        entidad_id=data.entidad_id,
        descripcion=data.descripcion,
        datos_anteriores=data.datos_anteriores,
        datos_nuevos=data.datos_nuevos,
        ip=data.ip,
        user_agent=data.user_agent,
    )
@router.get(
    "/usuario/{usuario_id}",
    response_model=list[AuditoriaUsuarioResponseDto]
)
def listar_por_usuario(
    usuario_id: int,
    repo = Depends(get_auditoria_repository)): 
    service = AuditoriaService(repo)  
    return service.listar_por_usuario(usuario_id)

@router.get(
    "/desde/{fecha}",
    response_model=list[AuditoriaUsuarioResponseDto]
)
def listar_desde_fecha(
    fecha: datetime,
    repo = Depends(get_auditoria_repository)): 
    service = AuditoriaService(repo)  
    return service.listar_desde_fecha(fecha)

@router.get(
    "/usuario/{usuario_id}/desde/{fecha}",
    response_model=list[AuditoriaUsuarioResponseDto]
)
def listar_por_usuario_desde_fecha(
    usuario_id: int,
    fecha: datetime,
    repo = Depends(get_auditoria_repository)): 
    try:
        service = AuditoriaService(repo)
        return service.listar_desde_fecha( usuario_id, fecha)
            
    except Exception as ex:
            print(ex.args)
            raise HTTPException(
                status_code=500,
                detail=str(ex.args)
            )