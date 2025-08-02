from pydantic import BaseModel, HttpUrl

from app.pokemon.models.generacion import Generacion
from app.pokemon.models.tipo import Tipo


class MovimientoResumido(BaseModel):
    id: int
    nombre: str
    generacion: Generacion
    tipo: Tipo
    categoria: str
    potencia: int
    precision: int
    puntos_de_poder: int
    efecto: str


class PokemonResumido(BaseModel):
    id: int
    imagen: HttpUrl
    nombre: str
    altura: float
    peso: float


class Movimiento(MovimientoResumido):
    pokemon_por_huevo: list[PokemonResumido] | None = None
    pokemon_por_nivel: list[PokemonResumido] | None = None
    pokemon_por_maquina: list[PokemonResumido] | None = None
