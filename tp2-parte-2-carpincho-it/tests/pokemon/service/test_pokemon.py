import pytest
from fastapi import HTTPException
from sqlmodel import Session

from app.pokemon.models.entity.pokemon import Pokemon
from app.pokemon.models.schema.pokemon import PokemonPublic
from app.pokemon.service.pokemon import PokemonService


class TestPokemonService:

    def test_get_pokemon(self, session: Session):
        pokemon = PokemonService(session).get_pokemon(1)
        assert pokemon.id == 1
        assert "saur" in pokemon.nombre.lower()

    def test_exception_get_pokemon(self, session: Session):
        with pytest.raises(HTTPException) as exc_info:
            PokemonService(session).get_pokemon(999999999)

        assert "Pokemon no encontrado" in str(exc_info.value)

    def test_get_pokemons(self, session: Session):
        pokemons = PokemonService(session).get_pokemons()
        assert len(pokemons) > 0
        for pokemon in pokemons:
            assert isinstance(pokemon, Pokemon)

    def test_get_pokemons_filters(self, session: Session):
        pokemons = PokemonService(session).get_pokemons(nombre_parcial="saur")
        assert len(pokemons) > 0
        for pokemon in pokemons:
            assert "saur" in pokemon.nombre.lower()

        pokemons = PokemonService(session).get_pokemons(tipo=1)
        assert len(pokemons) > 0
        for pokemon in pokemons:
            assert any(tipo.id == 1 for tipo in pokemon.tipos)
