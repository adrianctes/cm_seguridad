from application.politicas.datos_fijos_liquidacion.politica_factory import PoliticaFactory
from domain.enums.tipo_liquidacion import TipoLiquidacion

class PoliticaService:

    def __init__(self):
        pass

    def validar(self, request):

        tipo_liquidacion = None

        for tipo in TipoLiquidacion:
            if request.tipo_liquidacion_id == tipo.value:
                tipo_liquidacion = tipo
                break

        if tipo_liquidacion is None:
            raise ValueError(
                "Tipo de liquidación inválido."
            )

        regla = PoliticaFactory.crear(tipo_liquidacion)
   
        regla.validar(request)

        return regla