from pydantic import BaseModel, HttpUrl

from app.pokemon.models.estadistica import Estadistica
from app.pokemon.models.generacion import Generacion
from app.pokemon.models.movimiento import MovimientoResumido, PokemonResumido
from app.pokemon.models.tipo import PokemonTipo


class Habilidad(BaseModel):
    id: int
    nombre: str


class Evolucion(BaseModel):
    id: int
    nombre: str
    imagen: HttpUrl


class Pokemon(PokemonResumido):
    generaciones: list[Generacion] | None = None
    tipos: list[PokemonTipo] | None = None
    habilidades: list[Habilidad] | None = None
    estadisticas: Estadistica | None = None
    evoluciones: list[Evolucion] | None = None
    movimientos_huevo: list[MovimientoResumido] | None = None
    movimientos_maquina: list[MovimientoResumido] | None = None
    movimientos_nivel: list[MovimientoResumido] | None = None
