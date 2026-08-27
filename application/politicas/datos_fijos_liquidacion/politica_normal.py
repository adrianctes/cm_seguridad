
from application.politicas.datos_fijos_liquidacion.politica_interface import IPolitica

from domain.entities.datos_fijos_liquidacion_entity import (
    DatosFijosLiquidacion
)

from application.politicas.datos_fijos_liquidacion.politica_datos_fijos_entidad import PoliticaDatosFijosEntidad


class PoliticaNormal(IPolitica):

     

    def validar(
        self,
        entidad: DatosFijosLiquidacion
    ):

        if entidad.periodo is None:
            raise ValueError(
                "Debe ingresar el período."
        )

    def filtros(
            self,
            entidad: DatosFijosLiquidacion
        ) -> dict:

            payload = {
                "tipo_liquidacion_id": entidad.tipo_liquidacion_id,
                "modalidad_liquidacion_id": entidad.modalidad_liquidacion_id,
            }
    
            if entidad.periodo:
                payload["periodo"] = entidad.periodo

            if entidad.numero:
                 payload["numero"] = entidad.numero
    
            return payload


    
            '''    if (
                self.politica.numero_minimo is not None
                and
                entidad.numero < self.politica.numero_minimo
            ):

                raise ValueError(
                    f"El número mínimo permitido es "
                    f"{self.politica.numero_minimo}."
                )

            if (
                self.politica.numero_maximo is not None
                and
                entidad.numero > self.politica.numero_maximo
            ):

                raise ValueError(
                    f"El número máximo permitido es "
                    f"{self.politica.numero_maximo}."
                )'''
        