from pydantic import computed_field

from app.pokemon.models.schema.base import Schema
from app.pokemon.models.schema.estadistica import EstadisticaPublic
from app.pokemon.models.schema.generacion import GeneracionPublic
from app.pokemon.models.schema.movimiento import (
    MovimientoResumidoPublic,
    PokemonResumidoPublic,
)
from app.pokemon.models.schema.tipo import PokemonTipoPublic
from app.utils.images import get_pokemon_image_url


class EvolucionPublic(Schema):
    id: int
    nombre: str

    @computed_field
    @property
    def imagen(self) -> str:
        return get_pokemon_image_url(self.id)


class HabilidadPublic(Schema):
    id: int
    nombre: str


class PokemonPublic(PokemonResumidoPublic):
    generaciones: list[GeneracionPublic]
    tipos: list[PokemonTipoPublic]
    habilidades: list[HabilidadPublic]
    estadisticas: EstadisticaPublic
    evoluciones: list[EvolucionPublic]
    movimientos_huevo: list[MovimientoResumidoPublic]
    movimientos_maquina: list[MovimientoResumidoPublic]
    movimientos_nivel: list[MovimientoResumidoPublic]
