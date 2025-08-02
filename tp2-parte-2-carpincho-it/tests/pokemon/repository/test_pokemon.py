from app.pokemon.models.entity.pokemon import Pokemon
from app.pokemon.repository.pokemon import PokemonRepository
from sqlmodel import Session


def test_get_pokemon_existente(session: Session):
    repo = PokemonRepository(session)
    pokemon = repo.get(1)
    assert isinstance(pokemon, Pokemon)
    assert pokemon.id == 1
    assert "bulb" in pokemon.nombre.lower()


def test_get_pokemon_inexistente(session: Session):
    repo = PokemonRepository(session)
    pokemon = repo.get(9999)
    assert pokemon is None


def test_get_all_sin_filtros(session: Session):
    repo = PokemonRepository(session)
    pokemons = repo.get_all()
    assert isinstance(pokemons, list)
    assert all(isinstance(p, Pokemon) for p in pokemons)
    assert len(pokemons) > 0


def test_get_all_filtrado_por_nombre(session: Session):
    repo = PokemonRepository(session)
    pokemons = repo.get_all(nombre_parcial="saur")
    assert all("saur" in pokemon.nombre.lower() for pokemon in pokemons)


def test_get_all_filtrado_por_tipo(session: Session):
    repo = PokemonRepository(session)
    tipo_agua = 11
    pokemons = repo.get_all(tipo=tipo_agua)
    assert all(
        any(tipos.id == tipo_agua for tipos in pokemon.tipos) for pokemon in pokemons
    )


def test_unique_ids(session: Session):
    repo = PokemonRepository(session)
    ids = repo.get_unique_movimiento_ids(1)
    assert ids == {
        13,
        14,
        15,
        526,
        22,
        29,
        33,
        34,
        36,
        38,
        45,
        580,
        70,
        72,
        73,
        74,
        75,
        76,
        77,
        590,
        79,
        80,
        92,
        99,
        102,
        104,
        111,
        113,
        115,
        117,
        124,
        130,
        133,
        148,
        156,
        164,
        173,
        174,
        182,
        188,
        189,
        200,
        202,
        203,
        204,
        206,
        207,
        210,
        213,
        214,
        216,
        218,
        219,
        230,
        235,
        237,
        241,
        249,
        263,
        267,
        270,
        275,
        290,
        311,
        320,
        331,
        345,
        363,
        388,
        402,
        412,
        437,
        438,
        445,
        447,
        474,
        496,
        497,
    }
