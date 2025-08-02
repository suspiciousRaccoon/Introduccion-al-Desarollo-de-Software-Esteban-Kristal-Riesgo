from pydantic import BaseModel

from app.pokemon.models.equipo import Equipo
from app.pokemon.models.generacion import Generacion
from app.pokemon.models.movimiento import Movimiento
from app.pokemon.models.pokemon import Pokemon
from app.pokemon.models.tipo import Tipo


Database = dict[
    str, list[BaseModel | Generacion | Equipo | Movimiento | Tipo | Pokemon]
]
