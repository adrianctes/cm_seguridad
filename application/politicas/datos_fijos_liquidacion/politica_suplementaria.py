
from application.politicas.datos_fijos_liquidacion.politica_interface import IPolitica

class PoliticaSuplementaria(IPolitica):

    async def validar(self, request):

        if request.numero < 1:
            raise ValueError(
                "Número inválido."
            )