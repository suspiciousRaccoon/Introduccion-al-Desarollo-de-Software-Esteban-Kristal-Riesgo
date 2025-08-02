from app.pokemon.models.pokemon import Pokemon
from app.pokemon.repository.pokemon import PokemonRepository
from app.utils.types import Database


def test_get_pokemon_existente(database: Database):
    repo = PokemonRepository(database)
    pokemon = repo.get(1)
    assert isinstance(pokemon, Pokemon)
    assert pokemon.id == 1
    assert "bulb" in pokemon.nombre.lower()


def test_get_pokemon_inexistente(database: Database):
    repo = PokemonRepository(database)
    pokemon = repo.get(9999)
    assert pokemon is None


def test_get_all_sin_filtros(database: Database):
    repo = PokemonRepository(database)
    pokemons = repo.get_all()
    assert isinstance(pokemons, list)
    assert all(isinstance(p, Pokemon) for p in pokemons)
    assert len(pokemons) > 0


def test_get_all_filtrado_por_nombre(database: Database):
    repo = PokemonRepository(database)
    pokemons = repo.get_all(nombre_parcial="saur")
    assert all("saur" in pokemon.nombre.lower() for pokemon in pokemons)


def test_get_all_filtrado_por_tipo(database: Database):
    repo = PokemonRepository(database)
    tipo_agua = 11
    pokemons = repo.get_all(tipo=tipo_agua)
    assert all(
        any(tipos.id == tipo_agua for tipos in pokemon.tipos) for pokemon in pokemons
    )
