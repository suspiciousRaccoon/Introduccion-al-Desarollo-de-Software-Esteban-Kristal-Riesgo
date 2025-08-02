from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.utils.dependencies import get_session
from app.pokemon.models.schema.tipo import TipoPublic
from app.pokemon.service.tipo import TipoService

router = APIRouter()


@router.get("/", response_model=list[TipoPublic])
def get_tipos(session: Session = Depends(get_session)):
    tipos = TipoService(session).get_all()
    return [TipoPublic(id=tipo.id, nombre=tipo.nombre) for tipo in tipos]
