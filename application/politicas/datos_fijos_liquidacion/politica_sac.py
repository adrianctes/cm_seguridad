from application.politicas.datos_fijos_liquidacion.politica_interface import IPolitica


class PoliticaSAC(IPolitica):

    async def validar(self, request):

        mes = int(str(request.periodo)[4:6])

        if mes not in (6, 12):
            raise ValueError(
                "El SAC solamente puede liquidarse en junio o diciembre."
            )

        if request.numero != 1:
            raise ValueError(
                "El SAC solamente admite número 1."
            )

        if request.modalidad != "MENSUAL":
            raise ValueError(
                "El SAC únicamente puede ser mensual."
            )