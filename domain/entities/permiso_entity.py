class Permiso:

    def __init__(
        self,
        id: int | None = None,
        modulo: str = "",
        accion: str = "",
        codigo: str = "",
        nombre: str = "",
        activo: bool = True,
    ):
        self.id = id
        self.modulo = modulo
        self.accion = accion
        self.codigo = codigo
        self.nombre = nombre
        self.activo = activo