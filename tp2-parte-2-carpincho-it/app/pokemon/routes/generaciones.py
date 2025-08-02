from fastapi import APIRouter

from app.pokemon.models.schema.generacion import GeneracionPublic
from app.pokemon.service.generacion import GeneracionService
from app.utils.dependencies import Session

router = APIRouter()


@router.get("/", response_model=list[GeneracionPublic])
def get_generaciones(session: Session) -> list[GeneracionPublic]:
    return GeneracionService(session).get_generations()
