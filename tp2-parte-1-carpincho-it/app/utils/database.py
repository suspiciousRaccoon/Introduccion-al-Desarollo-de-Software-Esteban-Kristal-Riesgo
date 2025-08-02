from fastapi import FastAPI
from pydantic import BaseModel

from app.pokemon.models.equipo import Equipo
from app.pokemon.models.generacion import Generacion
from app.pokemon.models.movimiento import Movimiento
from app.pokemon.models.pokemon import Pokemon
from app.pokemon.models.tipo import Tipo
from app.utils.seed.generacion import load_generaciones
from app.utils.seed.movimiento import load_movimientos
from app.utils.seed.pokemon import (
    load_pokemon_estadisticas,
    load_pokemon_evoluciones,
    load_pokemon_habilidades,
    load_pokemon_movimientos,
    load_pokemon_tipos,
    load_pokemons,
)
from app.utils.seed.tipo import load_tipos
from app.utils.types import Database


def create_database() -> Database:
    return {"pokemons": [], "movimientos": [], "equipos": [], "generaciones": []}


def init_database(app: FastAPI) -> Database:
    """
    Initializes a database in a FastAPI app's state and returns it
    """
    app.state.database = create_database()
    return app.state.database


def seed_database(database: Database) -> None:
    load_generaciones(database)
    load_tipos(database)
    load_movimientos(database)
    load_pokemons(database)
    load_pokemon_estadisticas(database)
    load_pokemon_tipos(database)
    load_pokemon_habilidades(database)
    load_pokemon_evoluciones(database)
    load_pokemon_movimientos(database)
