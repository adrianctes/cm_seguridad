from datetime import date

def calcular_anios(
    fecha_ingreso: date,
    fecha_liquidacion: date
):

    anios = (
        fecha_liquidacion.year -
        fecha_ingreso.year
    )

    if (
        fecha_liquidacion.month,
        fecha_liquidacion.day
    ) < (
        fecha_ingreso.month,
        fecha_ingreso.day
    ):
        anios -= 1

    return anios