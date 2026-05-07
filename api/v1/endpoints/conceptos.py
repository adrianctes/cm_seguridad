from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.dtos.dto_concepto import ConceptoCreate, ConceptoResponse, ConceptoUpdate
from application.services.concepto_service import ConceptoService
from core.dependencias import get_concepto_repository

router = APIRouter(prefix="/conceptos", tags=["Conceptos"])


@router.post("/", response_model=ConceptoResponse)
def crear(data: ConceptoCreate,
    repo = Depends(get_concepto_repository)
):
    service = ConceptoService(repo)
    try:
      return service.crear(data)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )
   


@router.get("/", response_model=list[ConceptoResponse])
def listar(db: Session = Depends(get_concepto_repository)):
    pass
    #repo = MySQLConceptoRepository(db)
    #return repo.listar()


@router.get("/{concepto_id}", response_model=ConceptoResponse)
def obtener(concepto_id: int, db: Session = Depends(get_concepto_repository)):
    pass
    #repo = MySQLConceptoRepository(db)
    #concepto = repo.obtener(concepto_id)

    #if not concepto:
    #    raise HTTPException(status_code=404, detail="Concepto no encontrado")

    #return concepto


@router.patch("/{concepto_id}", response_model=ConceptoResponse)
def actualizar(concepto_id: int, data: ConceptoUpdate, db: Session = Depends(get_concepto_repository)):
    #repo = MySQLConceptoRepository(db)
    #concepto = repo.actualizar(concepto_id, data)

    #if not concepto:
    #    raise HTTPException(status_code=404, detail="Concepto no encontrado")

    #return concepto
    pass


@router.delete("/{concepto_id}")
def eliminar(concepto_id: int, db: Session = Depends(get_concepto_repository)):
    pass
    #repo = MySQLConceptoRepository(db)
    #concepto = repo.eliminar(concepto_id)

    #if not concepto:
    #    raise HTTPException(status_code=404, detail="Concepto no encontrado")

    return {"message": "Concepto eliminado"}