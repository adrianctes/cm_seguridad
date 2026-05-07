# domain/entities/usuario.py

class Usuario:

    def __init__(
        self,
        id=None,
        username=None,
        password_hash=None,
        activo=True,
        created_at=None
    ):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.activo = activo
        self.created_at = created_at