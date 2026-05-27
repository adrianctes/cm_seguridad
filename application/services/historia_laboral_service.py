from domain.entities.historia_laboral_entity import HistoriaLaboral
from domain.repositories.historia_laboral_interface import IHistoriaLaboral
from domain.repositories.legajo_repositorio_interface import ILegajoRepository

class HistoriaLaboralService:

    def __init__(self, repo: IHistoriaLaboral, repo_legajo:ILegajoRepository):
        self.repo = repo
        self.repo_legajo = repo_legajo

    # =========================================
    # CREATE
    # =========================================
    def crear_movimiento(
        self,
        data
        ):

        try:
            historia = HistoriaLaboral(
                legajo_id=data.legajo_id,
                tipo_id=data.tipo_id,
                fecha=data.fecha,
                observacion=data.observacion
            )

            movimientos = self.repo.obtener_ultimo_movimiento(data.legajo_id)

            ultimo = None

            if movimientos:
                ultimo = movimientos

            # ==========================
            # ALTA
            # ==========================
           
            if data.tipo_id == 1:
                    if ultimo:
                        raise Exception(
                            "Movimiento de ALTA ya existe."
                        )

                # ==========================
                # BAJA
                # ==========================

            elif data.tipo_id == 2:
                if not ultimo:
                    raise Exception(
                        "El legajo no posee movimientos para dar de BAJA."
                    )
                if ultimo.tipo_id == 2:
                    raise Exception(
                        "El legajo ya está de baja"
                    )
                if data.fecha < ultimo.fecha:
                          raise Exception("La fecha no puede ser menor al último movimiento")

            # ==========================
            # REINGRESO
            # ==========================

            elif data.tipo_id == 3:
                if not ultimo:
                    raise Exception(
                        "El legajo no posee historial"
                    )

                if ultimo.tipo_id != 2:
                    raise Exception(
                        "Debe existir una baja previa"
                    )
                if data.fecha < ultimo.fecha:
                          raise Exception("La fecha no puede ser menor al último movimiento")


                        
             
            resultado = self.repo.crear(historia)



            self.repo_legajo.actualizar_fecha_ingreso_actual(
                legajo_id=data.legajo_id,
                fecha=data.fecha
            )

            self.repo.db.commit()

            return resultado

        except Exception as ex:

            self.repo.db.rollback()

            raise ex    

       

    # =========================================
    # READ
    # =========================================

    def listar_por_legajo(
        self,
        legajo_id: int
    ):

        return self.repo.listar_por_legajo(legajo_id)

    def obtener_por_id(
        self,
        movimiento_id: int
    ):

        movimiento = self.repo.obtener_por_id(
            movimiento_id
        )

        if not movimiento:
            raise Exception(
                "Movimiento no encontrado"
            )

        return movimiento

    def obtener_ultimo_movimiento(
        self,
        legajo_id: int
    ):

        return self.repo.obtener_ultimo_movimiento(
            legajo_id
        )

    def listar_por_tipo(
        self,
        tipo_movimiento_id: int
    ):

        return self.repo.listar_por_tipo(
            tipo_movimiento_id
        )

    # =========================================
    # UPDATE
    # =========================================

    def editar_movimiento(
        self,
        movimiento_id: int,
        data
    ):

        movimiento = self.repo.obtener_por_id(
            movimiento_id
        )

        if not movimiento:
            raise Exception(
                "Movimiento no encontrado"
            )

        movimiento.tipo_movimiento_id = (
            data.tipo_movimiento_id
        )

        movimiento.fecha = data.fecha

        movimiento.observacion = (
            data.observacion
        )

        self.repo.guardar()

        return movimiento

    # =========================================
    # DELETE
    # =========================================

    def eliminar_movimiento(
        self,
        movimiento_id: int
    ):

        movimiento = self.repo.obtener_por_id(
            movimiento_id
        )

        if not movimiento:
            raise Exception(
                "Movimiento no encontrado"
            )

        self.repo.eliminar(movimiento)

        return True