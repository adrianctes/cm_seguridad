from dataclasses import dataclass


@dataclass
class PoliticaDatosFijosRequestDto:

    tipo_liquidacion_id: int

    modalidad_liquidacion_id: int