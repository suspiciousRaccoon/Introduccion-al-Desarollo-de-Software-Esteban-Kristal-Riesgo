import os

from sqlmodel import Session, create_engine, select

from app.pokemon.models.entity.pokemon import Pokemon
from app.utils.sqlite_seed.generacion import load_generaciones
from app.utils.sqlite_seed.habilidad import load_habilidades
from app.utils.sqlite_seed.movimiento import load_movimientos
from app.utils.sqlite_seed.pokemon import (
    load_pokemon_estadisticas,
    load_pokemon_evoluciones,
    load_pokemon_habilidades,
    load_pokemon_movimientos,
    load_pokemon_tipos,
    load_pokemons,
)
from app.utils.sqlite_seed.tipo import load_debilidades, load_tipos

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SQLITE_FILE_PATH = os.path.join(root, "database.db")


ENGINE = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def database_is_seeded(session: Session) -> bool:
    try:
        pokemon = session.exec(select(Pokemon)).first()
        return pokemon is not None
    except Exception as error:
        raise Exception(
            f"Error when checking if the database is seeded, does the database contain migrations? \n {SQLITE_FILE_PATH}\n{error}"
        )


def seed_sqlite_database(session: Session) -> None:
    if database_is_seeded(session):
        print("Database already seeded!")
        return

    print("Seeding database...")
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
    print("Seeding finished!")
