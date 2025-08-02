import pytest
from fastapi import HTTPException

from app.pokemon.models.pokemon import Pokemon
from app.pokemon.service.pokemon import PokemonService


class TestPokemonService:
    def test_get_pokemon(self, database):
        pokemon = PokemonService(database).get_pokemon(1)
        assert pokemon.id == 1
        assert "saur" in pokemon.nombre

    def test_exception_get_pokemon(self, database):
        with pytest.raises(HTTPException) as exc_info:
            PokemonService(database).get_pokemon(99999999999)

        assert "Pokemon no encontrado" in str(exc_info.value)

    def test_get_pokemons(self, database):
        pokemons = PokemonService(database).get_pokemons(1)
        assert len(pokemons) > 0
        for pokemons in pokemons:
            assert isinstance(pokemons, Pokemon)

    def test_get_pokemons_filters(self, database):
        pokemons = PokemonService(database).get_pokemons(nombre_parcial="saur")
        for pokemon in pokemons:
            assert "saur" in pokemon.nombre
        pokemons = PokemonService(database).get_pokemons(tipo=1)  # normal
        for pokemon in pokemons:
            found = False
            for tipo in pokemon.tipos:
                if tipo.nombre.lower() == "normal":
                    found = True
            assert found
