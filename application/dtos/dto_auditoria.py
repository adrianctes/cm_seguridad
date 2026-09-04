from datetime import datetime
from pydantic import BaseModel

from  domain.enums.auditoria_entidad import    EntidadAuditoriaEnum
from domain.enums.auditoria_accion import     AccionAuditoriaEnum


class AuditoriaUsuarioCreateDto(BaseModel):
    usuario_id: int
    accion: AccionAuditoriaEnum
    entidad: EntidadAuditoriaEnum
    entidad_id: int | None = None
    descripcion: str | None = None
    datos_anteriores: dict | None = None
    datos_nuevos: dict | None = None
    ip: str | None = None
    user_agent: str | None = None


class AuditoriaUsuarioResponseDto(BaseModel):
    id: int
    usuario_id: int
    accion: str
    entidad: str
    entidad_id: int | None
    descripcion: str | None
    datos_anteriores: dict | None
    datos_nuevos: dict | None
    ip: str | None
    user_agent: str | None
    fecha_hora: datetime