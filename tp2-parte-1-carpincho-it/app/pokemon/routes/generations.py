from fastapi import APIRouter
from app.pokemon.models.generacion import Generacion
from app.pokemon.service.generacion import GeneracionService
from app.utils.dependencies import Database

router = APIRouter()


@router.get("/")
def get_generaciones(db: Database) -> list[Generacion]:
    return GeneracionService(db).get_generations()
