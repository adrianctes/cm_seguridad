# application/services/usuario_service.py

from core.security import hash_password,verify_password

from domain.entities.usuario_entity import Usuario
from domain.repositories.usuario_repositorio_interface import (
    UsuarioRepository
)


class UsuarioService:

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    # 🔹 Crear
    def crear(self, data):

        existente = self.repo.obtener_por_username(
            data.username
        )

        if existente:
            raise Exception(
                "El username ya existe"
            )

        usuario = Usuario(
            id=None,
            username=data.username,
            nombre=data.nombre,
            apellido=data.apellido,
            password_hash=hash_password(
                data.password
            ),
            activo=data.activo,
            rol=data.rol
        )

        return self.repo.guardar(usuario)

    # 🔹 Listar
    def listar(self,
                busqueda: str | None = None,
                activo: bool | None = None,):

        return self.repo.listar( busqueda=busqueda,
                                 activo=activo)

    # 🔹 Obtener por ID
    def obtener_por_id(self, usuario_id: int):

        return self.repo.obtener_por_id(usuario_id)

    # 🔹 Obtener por username
    def obtener_por_username(self, username: str):

        return self.repo.obtener_por_username(
            username
        )

    # 🔹 Actualizar
    def actualizar(self, usuario_id: int, data):

        usuario = self.repo.obtener_por_id(
            usuario_id
        )

        if not usuario:
            return None

        # 🔹 Validar username duplicado
        if data.username is not None:

            existente = (
                self.repo.obtener_por_username(
                    data.username
                )
            )

            if (
                existente and
                existente.id != usuario_id
            ):
                raise Exception(
                    "El username ya existe"
                )

            usuario.username = data.username
            usuario.nombre = data.nombre
            usuario.apellido = data.apellido
            usuario.activo = data.activo
 
        """  # 🔹 Actualizar password
        if data.password is not None:

            usuario.password_hash = hash_password(
                data.password
            ) """

        return self.repo.guardar(usuario)


    def cambiar_estado(
        self,
        usuario_id: int,
        activo: bool
    ):
        usuario =  self.repo.obtener_por_id(usuario_id)
   
        if not usuario:
            raise ValueError("Usuario no encontrado")

        usuario.activo = activo

        self.repo.cambiar_estado(usuario)

    def cambiar_password(
            self,
            usuario_id: int,
            password_actual: str,
            password_nueva: str,
            password_confirmacion :str
        ) -> None:

        if password_nueva != password_confirmacion:
            raise Exception(
                "Las nuevas contraseñas no coinciden"
            )

        usuario = self.repo.obtener_por_id(
                usuario_id
        )


        if usuario is None:
                raise Exception(
                    "Usuario no encontrado"
                )

        print("PASSWORD RECIBIDO:", password_actual)
        print("HASH BD:", usuario.password_hash)

        print(
            "VERIFICACION:",
            verify_password(
                password_actual,
                usuario.password_hash
            )
        )
            
            # Validar nueva contraseña
        if not verify_password(
            password_actual,
            usuario.password_hash
            ):
                raise Exception(
                    "La contraseña actual es incorrecta"
                )


             # Validar nueva contraseña
        if len(password_nueva) < 6:
                raise Exception(
                    "La nueva contraseña debe tener al menos 6 caracteres"
                )

            # Generar nuevo hash
        nuevo_hash = hash_password(password_nueva)
                
                # Actualizar
        self.repo.cambiar_password(
                    usuario_id=usuario_id,
                    password_hash=nuevo_hash,
                )

   # 🔹 Eliminar
    def eliminar(self, usuario_id: int):

        return self.repo.eliminar(usuario_id)