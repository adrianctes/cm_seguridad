from dataclasses import dataclass


@dataclass
class PoliticaDatosFijosEntidad:

    id: int | None

    tipo_liquidacion_id: int

    modalidad_liquidacion_id: int

    requiere_periodo: bool

    requiere_numero: bool

    numero_minimo: int | None

    numero_maximo: int | None

    permite_repetir_numero: bool