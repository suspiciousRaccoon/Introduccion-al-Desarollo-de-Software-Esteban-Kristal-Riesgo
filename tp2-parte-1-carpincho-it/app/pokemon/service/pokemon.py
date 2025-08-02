from typing import Any

from app.pokemon.exceptions import PokemonNotFound
from app.pokemon.models.pokemon import Pokemon
from app.pokemon.repository.pokemon import PokemonRepository
from app.utils.types import Database


class PokemonService:
    def __init__(self, database: Database):
        self.database = database
        self.repository = PokemonRepository(database)

    def get_pokemon(self, pokemon_id: int) -> Pokemon:
        pokemon = self.repository.get(pokemon_id)
        if pokemon is None:
            raise PokemonNotFound
        return pokemon

    def get_pokemons(
        self, tipo: int | None = None, nombre_parcial: str | None = None
    ) -> list[Pokemon]:
        return self.repository.get_all(tipo, nombre_parcial)
