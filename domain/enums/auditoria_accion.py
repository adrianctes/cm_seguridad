from enum import Enum


class AccionAuditoriaEnum(str, Enum):
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"

    CREAR = "CREAR"
    MODIFICAR = "MODIFICAR"
    ELIMINAR = "ELIMINAR"
    CONSULTAR = "CONSULTAR"

    LIQUIDAR = "LIQUIDAR"
    CONFIRMAR = "CONFIRMAR"
    ANULAR = "ANULAR"

    IMPRIMIR = "IMPRIMIR"
    EXPORTAR = "EXPORTAR"
