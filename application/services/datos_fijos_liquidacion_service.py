from application.dtos.dto_datos_fijos_liquidacion import (
    DatosFijosLiquidacionCreate,
    DatosFijosLiquidacionUpdate,
)
from domain.entities.datos_fijos_liquidacion_entity import DatosFijosLiquidacion
from application.politicas.datos_fijos_liquidacion.politica_service import PoliticaService

class DatosFijosLiquidacionService:

    politica_service =None

    def __init__(self, repo_datos_fijos):
        
        self.repo_datos_fijos = repo_datos_fijos
        self.politica_service = PoliticaService()
                 
    def listar_por_periodo(self, params: dict):
     
        return self.repo_datos_fijos.listar_por_periodo(params)

    def obtener(self, id: int):
        dato = self.repo_datos_fijos.obtener(id)

        if dato is None:
            raise ValueError("La liquidación no existe.")

        return dato

    async def crear(self, dto: DatosFijosLiquidacionCreate ):

        entidad = DatosFijosLiquidacion(
            id=None,
            fecha_carga=dto.fecha_carga,
            modalidad_liquidacion_id=dto.modalidad_liquidacion_id,
            tipo_liquidacion_id = dto.tipo_liquidacion_id,
            periodo=dto.periodo,
            numero = dto.numero,
            fecha_desde=dto.fecha_desde,
            fecha_hasta=dto.fecha_hasta,
            periodo_pago=dto.periodo_pago,
            fecha_pago=dto.fecha_pago,
        )
  
        regla = self.politica_service.validar(entidad)
      
        payload = regla.filtros(entidad)

        existe =  self.repo_datos_fijos.existe(payload)

        print("RESULTADO EXISTE:", existe)

       
        if existe:
                raise ValueError(
                    "Ya existe una liquidación con ese período y número."
                )

        # =====================================================
        # 3. BUSCAR ÚLTIMO PERÍODO ANTERIOR EXISTENTE
        # =====================================================

        anterior =  self.repo_datos_fijos.obtener_ultimo_periodo_anterior(
            tipo_liquidacion_id=entidad.tipo_liquidacion_id,
            modalidad_liquidacion_id=entidad.modalidad_liquidacion_id,
            periodo=entidad.periodo,
        )
        print("anterior", anterior) 
        # =====================================================
        # 4. VALIDAR ESTADO DEL PERÍODO ANTERIOR
        # =====================================================

        if anterior:

            print(
                "ÚLTIMO PERÍODO ANTERIOR:",
                anterior.periodo
            )

            if anterior.estado == "ABIERTO":

                raise ValueError(
                    f"No se puede crear la liquidación "
                    f"{entidad.periodo} porque el período anterior "
                    f"{anterior.periodo} se encuentra abierto."
                )

        # =====================================================
        # 5. CREAR
        # =====================================================


        self.repo_datos_fijos.crear(entidad)


    def actualizar(self, id: int, dto: DatosFijosLiquidacionUpdate):

        dato = self.repo_datos_fijos.obtener(id)

        if dato is None:
            raise ValueError("La liquidación no existe.")

        dato.fecha_carga = dto.fecha_carga
        dato.modalidad_liquidacion_id = dto.modalidad_liquidacion_id
        dato.tipo_liquidacion_id = dto.tipo_liquidacion_id
        dato.periodo = dto.periodo
        dato.numero =dto.numero
        dato.fecha_desde = dto.fecha_desde
        dato.fecha_hasta = dto.fecha_hasta
        dato.periodo_pago = dto.periodo_pago
        dato.fecha_pago = dto.fecha_pago
        dato.estado =  dto.estado

        regla = self.politica_service.validar(dato)
              
        payload = regla.filtros(dato)
        print(payload)
        
        existe =  self.repo_datos_fijos.existe(payload, id)

        if existe:
            raise ValueError(
                "Ya existe una liquidación con ese período y número."
            )

        return self.repo_datos_fijos.actualizar(dato)

    def eliminar(self, id: int):

        dato = self.repo_datos_fijos.obtener(id)

        if dato is None:
            raise ValueError("La liquidación no existe.")

        self.repo_datos_fijos.eliminar(id)

        return {"mensaje": "Registro eliminado correctamente."}