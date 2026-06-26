# historia_laboral_router.py

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from application.dtos.dto_historia_laboral import HistoriaLaboral, HistoriaLaboralResponse
from application.services.historia_laboral_service import HistoriaLaboralService
from core.dependencias import  get_historia_laboral_repository
from core.dependencias import  get_legajo_repository


router = APIRouter(
    prefix="",
    tags=["Historia Laboral"]
)

@router.get(
    "/legajos/{legajo_id}/historia-laboral"
)
def listar_historial_legajo(

    legajo_id: int,

    repo=Depends(
        get_historia_laboral_repository
    ),

    repo_legajo=Depends(
        get_legajo_repository
    )
):

    service = HistoriaLaboralService(
        repo,
        repo_legajo
    )

    try:

        return service.listar_por_legajo(
            legajo_id
        )

    except Exception as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )
   
# =====================================================
# OBTENER MOVIMIENTO POR ID
# =====================================================

@router.get(
    "/historia-laboral/{id}"
)
def obtener_movimiento(
    id: int,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Retorna un movimiento puntual
    """

    pass

# =====================================================
# CREAR MOVIMIENTO
# =====================================================
@router.post(
    "/historia-laboral", response_model=HistoriaLaboralResponse
)
def crear_movimiento(
    data: HistoriaLaboral,
    repo=Depends(
        get_historia_laboral_repository
    ),

    repo_legajo=Depends(
        get_legajo_repository
    )
): 

    service = HistoriaLaboralService(repo, repo_legajo)
    try :
        return service.crear_movimiento(data)
    except Exception as ex:
        print(ex)
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
# =====================================================
# EDITAR MOVIMIENTO
# =====================================================
@router.put(
    "/historia-laboral/{id}"
)
def editar_movimiento(
    id: int,
    data,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Edita un movimiento existente
    """

    pass
# =====================================================
# ELIMINAR MOVIMIENTO
# =====================================================
@router.delete(
    "/historia-laboral/{id}"
)
def eliminar_movimiento(
    id: int,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Elimina un movimiento
    """

    pass
# =====================================================
# ULTIMO MOVIMIENTO DEL LEGAJO
# =====================================================
@router.get(
    "/legajos/{legajo_id}/historia-laboral/ultimo"
)
def obtener_ultimo_movimiento(
    legajo_id: int,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Obtiene el último movimiento
    del legajo
    """

    pass
# =====================================================
# MOVIMIENTOS POR TIPO
# =====================================================
@router.get(
    "/historia-laboral/tipo/{tipo_id}"
)
def listar_por_tipo(
    tipo_id: int,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Lista movimientos por tipo
    """

    pass
# =====================================================
# MOVIMIENTOS ENTRE FECHAS
# =====================================================
@router.get(
    "/historia-laboral"
)
def listar_por_fecha(
    fecha_desde: str,
    fecha_hasta: str,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Lista movimientos entre fechas
    """

    pass
# =====================================================
# HISTORIAL ACTIVO DEL LEGAJO
# =====================================================
@router.get(
    "/legajos/{legajo_id}/historia-laboral/activo"
)
def historial_activo(
    legajo_id: int,
    repo = Depends(get_historia_laboral_repository)
):

    """
    Retorna movimientos activos/vigentes
    """

    pass