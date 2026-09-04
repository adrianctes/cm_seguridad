@dataclass
class Auditoria:
    usuario_id: int

    accion: AccionAuditoriaEnum
    entidad: EntidadAuditoriaEnum

    entidad_id: int | None = None

    descripcion: str | None = None

    datos_anteriores: dict | None = None
    datos_nuevos: dict | None = None

    ip: str | None = None
    user_agent: str | None = None

    fecha_hora: datetime | None = None