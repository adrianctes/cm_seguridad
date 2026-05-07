# core/dependencies.py

from fastapi import Depends
from infrastructura.db.session import get_db
from infrastructura.repositories.mysql_concepto_repository import MySQLConceptoRepository
from infrastructura.repositories.mysql_legajo_repository import MySQLLegajoRepository
from infrastructura.repositories.mysql_liquidacion_repository import MySQLLiquidacionRepository

def get_legajo_repository(db = Depends(get_db)):
    return MySQLLegajoRepository(db)

def get_concepto_repository(db = Depends(get_db)):
    return MySQLConceptoRepository(db)

def get_liquidacion_repository(db = Depends(get_db)):
    return MySQLLiquidacionRepository(db)