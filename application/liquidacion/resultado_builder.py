from dataclasses import asdict

class ResultadoBuilder:

    def construir(self, items):

        # Ordenar:
        # 1 - Haberes (C)
        # 2 - Descuentos (D)
        # 3 - Orden del concepto
        items.sort(
            key=lambda x: (
                0 if x.clasificacion_tipo == "C" else 1,
                x.orden
            )
        )

        haberes = sum(
            item.total
            for item in items
            if item.clasificacion_tipo == "C"
        )

        descuentos = sum(
            item.total
            for item in items
            if item.clasificacion_tipo == "D"
        )

        return {
            "detalle": [
                asdict(item)
                for item in items
            ],
            "totales": {
                "haberes": haberes,
                "descuentos": descuentos
            },
            "neto": haberes - descuentos
        }