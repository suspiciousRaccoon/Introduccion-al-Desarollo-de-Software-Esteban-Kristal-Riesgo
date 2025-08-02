from typing import Optional

from fastapi import APIRouter

from app.pokemon.models.entity.movimiento import MovimientoNivel
from app.pokemon.models.schema.movimiento import MovimientoResumidoPublic
from app.pokemon.models.schema.pokemon import PokemonPublic
from app.pokemon.service.pokemon import PokemonService
from app.utils.dependencies import Session
from app.utils.repository import Filter

router = APIRouter()


@router.get("/{pokemon_id}", response_model=PokemonPublic)
def get_pokemon(pokemon_id: int, session: Session) -> PokemonPublic:
    return PokemonService(session).get_pokemon(pokemon_id)


@router.get("/", response_model=list[PokemonPublic])
def get_pokemons(
    session: Session,
    limit: int = 10,
    offset: int = 0,
    tipo: Optional[int] = None,
    generacion: Optional[int] = None,
    nombre_parcial: Optional[str] = None,
) -> list[PokemonPublic]:
    return PokemonService(session).get_pokemons(
        tipo, nombre_parcial, generacion, filters=Filter(limit=limit, offset=offset)
    )


@router.get("/{pokemon_id}/movimientos", response_model=list[MovimientoResumidoPublic])
def get_pokemon_movimientos(
    pokemon_id: int,
    session: Session,
    nombre_parcial: Optional[str] = None,
) -> list[MovimientoNivel]:
    return PokemonService(session).get_pokemon_movimientos(pokemon_id, nombre_parcial)
