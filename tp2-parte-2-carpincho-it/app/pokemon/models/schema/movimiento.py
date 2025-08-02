from pydantic import computed_field

from app.pokemon.models.schema.base import Schema
from app.pokemon.models.schema.generacion import GeneracionPublic
from app.pokemon.models.schema.tipo import TipoPublic
from app.utils.images import get_pokemon_image_url


# this is here to avoid circular imports
class PokemonResumidoPublic(Schema):
    id: int
    nombre: str
    altura: float
    peso: float

    @computed_field
    @property
    def imagen(self) -> str:
        return get_pokemon_image_url(self.id)


class MovimientoResumidoPublic(Schema):
    id: int
    nombre: str
    categoria: str
    potencia: int
    precision: int
    puntos_de_poder: int
    efecto: str
    generacion: GeneracionPublic
    tipo: TipoPublic | None


class MovimientoPublic(MovimientoResumidoPublic):
    pokemon_por_huevo: list[PokemonResumidoPublic] = None
    pokemon_por_nivel: list[PokemonResumidoPublic] = None
    pokemon_por_maquina: list[PokemonResumidoPublic] = None
