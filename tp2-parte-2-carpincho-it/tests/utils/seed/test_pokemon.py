from sqlalchemy import Engine
from sqlmodel import Session


from app.pokemon.models.entity.pokemon import Pokemon
from app.utils.sqlite_seed.generacion import load_generaciones
from app.utils.sqlite_seed.habilidad import load_habilidades
from app.utils.sqlite_seed.movimiento import load_movimientos
from app.utils.sqlite_seed.pokemon import (
    load_pokemons,
    load_pokemon_estadisticas,
    load_pokemon_evoluciones,
    load_pokemon_habilidades,
    load_pokemon_tipos,
    load_pokemon_movimientos,
)
from app.utils.sqlite_seed.tipo import load_debilidades, load_tipos


def test_load_pokemon(sqlite_database: Engine):
    session = Session(sqlite_database)
    load_generaciones(session)
    load_tipos(session)
    load_debilidades(session)
    load_movimientos(session)
    load_habilidades(session)
    load_pokemons(session)
    load_pokemon_estadisticas(session)
    load_pokemon_tipos(session)
    load_pokemon_habilidades(session)
    load_pokemon_evoluciones(session)
    load_pokemon_movimientos(session)

    pokemon = session.get(Pokemon, 133)  # eevee
    assert pokemon.id == 133
    assert pokemon.nombre == "eevee"
    assert len(pokemon.generaciones) == 8
    assert pokemon.generaciones[-1].id == 8
    assert pokemon.tipos[0].id == 1
    assert len(pokemon.habilidades) == 3
    assert pokemon.estadisticas.ataque == 55
    assert len(pokemon.evoluciones) == 8 and pokemon.evoluciones[0].nombre == "vaporeon"
    assert pokemon.movimientos_huevo
    assert pokemon.movimientos_nivel
    assert pokemon.movimientos_maquina
    assert pokemon.movimientos_maquina[0].id == 6  # pay day
