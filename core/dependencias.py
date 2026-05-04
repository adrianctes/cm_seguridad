# core/dependencies.py

from fastapi import Depends
from infrastructura.db.session import get_db
from infrastructura.repositorios.mysql_concepto_repository import MySQLConceptoRepository
from infrastructura.repositorios.mysql_legajo_repository import MySQLLegajoRepository

def get_legajo_repository(db = Depends(get_db)):
    return MySQLLegajoRepository(db)

def get_concepto_repository(db = Depends(get_db)):
    return MySQLConceptoRepository(db)