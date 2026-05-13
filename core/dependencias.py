# core/dependencies.py

from urllib import request

from fastapi import Depends
from infrastructura.db.session import get_db
from infrastructura.repositories.mysql_concepto_novedad_repository import MySQLConceptoNovedadRepository
from infrastructura.repositories.mysql_concepto_repository import MySQLConceptoRepository
from infrastructura.repositories.mysql_legajo_repository import MySQLLegajoRepository
from infrastructura.repositories.mysql_liquidacion_repository import MySQLLiquidacionRepository
from infrastructura.repositories.mysql_usuario_repository import MySQLUsuarioRepository
from infrastructura.repositories.mysql_categoria_repository import MySQLCategoriaRepository
from infrastructura.repositories.mysql_modalidad_repository import MySQLModalidadLiquidacionRepository
from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from jose import JWTError, jwt
from fastapi import Depends
from fastapi import HTTPException, status


def get_categoria_repository(db = Depends(get_db)):
    return MySQLCategoriaRepository(db)

def get_modalidad_liquidacion_repository(db = Depends(get_db)):
    return MySQLModalidadLiquidacionRepository(db)

def get_legajo_repository(db = Depends(get_db)):
    return MySQLLegajoRepository(db)

def get_concepto_repository(db = Depends(get_db)):
    return MySQLConceptoRepository(db)

def get_liquidacion_repository(db = Depends(get_db)):
    return MySQLLiquidacionRepository(db)

def get_concepto_novedad_repository(db = Depends(get_db)):
    return MySQLConceptoNovedadRepository(db)

def get_usuario_repository(db = Depends(get_db)):
    return MySQLUsuarioRepository(db)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):


    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falta token de autenticación",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )