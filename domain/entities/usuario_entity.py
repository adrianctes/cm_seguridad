# domain/entities/usuario.py

class Usuario:

    def __init__(
        self,
        id=None,
        username=None,
        password_hash=None,
        nombre = None,
        apellido = None,
        rol= None,
        activo=True,
        created_at=None
    ):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.activo = activo
        self.created_at = created_at