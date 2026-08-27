class CalculadorFijo:

    def calcular(
        self,
        item,
        detalle,
        ANIOS_ATIGUEDAD
    ):

        valor = item.valor * item.cantidad
        if item.clasificacion_tipo == 'C':
            item.haber = valor
        elif  item.clasificacion_tipo == 'D':
               item.retencion = valor


        item.total =valor