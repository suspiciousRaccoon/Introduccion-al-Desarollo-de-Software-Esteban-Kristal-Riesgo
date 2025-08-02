from pydantic import BaseModel, HttpUrl

from app.pokemon.models.generacion import Generacion
from app.pokemon.models.movimiento import MovimientoResumido
from app.pokemon.models.tipo import PokemonTipo


class Estadistica(BaseModel):
    ataque: int
    defensa: int
    ataque_especial: int
    defensa_especial: int
    puntos_de_golpe: int
    velocidad: int


class PokemonEquipo(BaseModel):
    id: int
    imagen: HttpUrl
    nombre: str
    estadisticas: Estadistica
    generacion: Generacion
    tipos: list[PokemonTipo]


class Integrante(BaseModel):
    id: int
    apodo: str
    pokemon: PokemonEquipo
    movimientos: list[MovimientoResumido] | list


class Equipo(BaseModel):
    id: int
    nombre: str
    generacion: Generacion
    integrantes: list[Integrante]


class PokemonIntegrante(BaseModel):
    integrante: list[Integrante]


class EquipoResumido(BaseModel):
    id: int
    nombre: str
    generacion: Generacion
    cant_integrantes: int


class EquipoUpsert(BaseModel):
    nombre: str
    id_generacion: int


class EquipoIntegranteAdd(BaseModel):
    id_pokemon: int
    apodo: str


class EquipoIntegrateMovimientoAdd(BaseModel):
    id_movimiento: int


class EquipoIntegranteUpdate(BaseModel):
    apodo: str
    movimientos: list[int]
