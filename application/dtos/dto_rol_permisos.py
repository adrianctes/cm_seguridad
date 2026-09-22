
from pydantic import BaseModel, ConfigDict


# ============================================================
# ROLES
# ============================================================

class RolReponseDTO(BaseModel):
    key: str
    text: str


# ============================================================
# CREAR ASIGNACIÓN ROL-PERMISO
# ============================================================

class RolPermisoCreate(BaseModel):
    rol: str
    permiso_id: int


# ============================================================
# RESPUESTA ASIGNACIÓN ROL-PERMISO
# ============================================================

class RolPermisoResponse(BaseModel):
    id: int
    rol: str
    permiso_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


# ============================================================
# PERMISOS DE UN ROL
# ============================================================

class PermisosRolResponse(BaseModel):
    rol: str
    permisos_ids: list[int]


# ============================================================
# ACTUALIZAR PERMISOS DE UN ROL
# ============================================================

class PermisosRolUpdate(BaseModel):
    permisos_ids: list[int]


class PermisoResponse(BaseModel):

    id: int
    modulo: str
    accion: str
    codigo: str
    nombre: str
    activo: bool

    model_config = ConfigDict(
        from_attributes=True
    )


