from fastapi import APIRouter
from app.pokemon.models.pokemon import Pokemon
from app.pokemon.service.pokemon import PokemonService
from app.utils.dependencies import Database

router = APIRouter()


@router.get("/{pokemon_id}")
def get_pokemon(db: Database, pokemon_id: int) -> Pokemon:
    return PokemonService(db).get_pokemon(pokemon_id)


@router.get("/")
def get_pokemons(
    db: Database, tipo: int | None = None, nombre_parcial: str | None = None
) -> list[Pokemon]:
    return PokemonService(db).get_pokemons(tipo, nombre_parcial)
