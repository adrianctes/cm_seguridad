from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.dtos.dto_concepto import ConceptoCreate, ConceptoResponse, ConceptoUpdate
from application.services.concepto_service import ConceptoService
from core.dependencias import get_concepto_repository

router = APIRouter(prefix="/conceptos", tags=["Conceptos"])

@router.post("", response_model=ConceptoResponse)
def crear(data: ConceptoCreate,
    repo = Depends(get_concepto_repository)
):
    service = ConceptoService(repo)

    try:
      return service.crear(data)
    except Exception as ex:
        print(ex)
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )
   

@router.get("", response_model=list[ConceptoResponse])
def listar( repo = Depends(get_concepto_repository)):
    service = ConceptoService(repo)
    try:
      return service.listar()
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )
   
@router.get("/{id}", response_model=ConceptoResponse)
def obtener(id: int, repo = Depends(get_concepto_repository)):
    service = ConceptoService(repo)
    try:
      return service.obtener(id)
    except Exception as ex:
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )
   

@router.put("/{concepto_id}", response_model=ConceptoResponse)
def actualizar(concepto_id: int, data: ConceptoUpdate, repo = Depends(get_concepto_repository)):
   
    service = ConceptoService(repo)

    try:
      return service.actualizar(concepto_id, data)
    except Exception as ex:
        print(ex)
        raise HTTPException(
            status_code=422,
            detail=str(ex)
        )
    


@router.delete("/{concepto_id}")
def eliminar(concepto_id: int, db: Session = Depends(get_concepto_repository)):
    pass
    #repo = MySQLConceptoRepository(db)
    #concepto = repo.eliminar(concepto_id)

    #if not concepto:
    #    raise HTTPException(status_code=404, detail="Concepto no encontrado")

    return {"message": "Concepto eliminado"}