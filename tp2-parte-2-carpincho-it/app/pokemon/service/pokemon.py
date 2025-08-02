from typing import Optional

from sqlmodel import Session

from app.pokemon.exceptions import PokemonNotFound
from app.pokemon.models.entity.movimiento import Movimiento
from app.pokemon.models.entity.pokemon import Pokemon
from app.pokemon.repository.pokemon import PokemonRepository
from app.utils.repository import Filter


class PokemonService:
    def __init__(self, session: Session):
        self.session = session
        self.repository = PokemonRepository(session)

    def get_pokemon(self, pokemon_id: int) -> Pokemon:
        pokemon = self.repository.get(pokemon_id)
        if pokemon is None:
            raise PokemonNotFound
        return pokemon

    def get_pokemons(
        self,
        tipo: Optional[int] = None,
        nombre_parcial: Optional[str] = None,
        generacion: Optional[int] = None,
        filters: Filter | None = None,
    ) -> list[Pokemon]:
        return self.repository.get_all(
            tipo, nombre_parcial, generacion, entity_filters=filters
        )

    def get_pokemon_movimientos(
        self, pokemon_id: int, nombre_parcial: str
    ) -> list[Movimiento]:
        results = self.repository.get_unique_movimientos(pokemon_id, nombre_parcial)
        return results
