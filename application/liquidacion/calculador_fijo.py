class CalculadorFijo:

    def calcular(
        self,
        item,
        detalle,
        anios_antiguedad
    ):

        valor = item.valor * item.cantidad

        if item.clasificacion_tipo == "C":
            item.haber = valor

        elif item.clasificacion_tipo == "D":
            item.retencion = valor

        item.total = valor

        return True