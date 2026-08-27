from  application.politicas.datos_fijos_liquidacion .politica_normal import PoliticaNormal
from  application.politicas.datos_fijos_liquidacion.politica_sac import PoliticaSAC
from  application.politicas.datos_fijos_liquidacion.politica_suplementaria import PoliticaSuplementaria
from domain.enums.tipo_liquidacion import TipoLiquidacion

class PoliticaFactory:

    @staticmethod
    def crear(tipo_liquidacion: int):

        match TipoLiquidacion(tipo_liquidacion):

            case TipoLiquidacion.NORMAL:
                return PoliticaNormal()

            case TipoLiquidacion.SAC:
                return PoliticaSAC()

            case TipoLiquidacion.SUPLEMENTARIA:
                return PoliticaSuplementaria()

        raise ValueError(
            f"Tipo de liquidación inválido: {tipo_liquidacion}"
        )