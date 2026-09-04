from datetime import datetime
from domain.entities.auditoria_entity import  Auditoria
from domain.enums.auditoria_accion import AccionAuditoriaEnum
from domain.enums.auditoria_entidad import EntidadAuditoriaEnum

class AuditoriaService:

    def __init__(self, repository):
        self.repository = repository

    def crear(
        self,
        usuario_id: int,
        accion: AccionAuditoriaEnum,
        entidad: EntidadAuditoriaEnum,
        entidad_id: int | None = None,
        descripcion: str | None = None,
        datos_anteriores: dict | None = None,
        datos_nuevos: dict | None = None,
        ip: str | None = None,
        user_agent: str | None = None,
    ):
        auditoria = Auditoria(
            usuario_id=usuario_id,
            accion=accion,
            entidad=entidad,
            entidad_id=entidad_id,
            descripcion=descripcion,
            datos_anteriores=datos_anteriores,
            datos_nuevos=datos_nuevos,
            ip=ip,
            user_agent=user_agent,
        )

        return self.repository.crear(auditoria)

    def listar_por_usuario(
        self,
        usuario_id: int
    ):
        return self.repository.listar_por_usuario(
            usuario_id
        )

    def listar_desde_fecha(
        self,
        fecha_desde: datetime
    ):
        return self.repository.listar_desde_fecha(
            fecha_desde
        )

    def listar_por_usuario_desde_fecha(
        self,
        usuario_id: int,
        fecha_desde: datetime
    ):
        return self.repository.listar_por_usuario_desde_fecha(
            usuario_id,
            fecha_desde
        )