# core/dependencies.py

from fastapi import Depends
from infrastructura.db.session import get_db
from infrastructura.repositorios.mysql_legajo_repository import MySQLLegajoRepository

def get_legajo_repository(db = Depends(get_db)):
    return MySQLLegajoRepository(db)