from pydantic import HttpUrl, computed_field

from app.pokemon.models.schema.base import Schema
from app.pokemon.models.schema.estadistica import EstadisticaPublic
from app.pokemon.models.schema.generacion import GeneracionPublic
from app.pokemon.models.schema.movimiento import MovimientoResumidoPublic
from app.pokemon.models.schema.tipo import PokemonTipoPublic
from app.utils.images import get_pokemon_image_url


class PokemonEquipoPublic(Schema):
    id: int
    nombre: str
    estadisticas: EstadisticaPublic
    generaciones: list[GeneracionPublic]
    tipos: list[PokemonTipoPublic]

    @computed_field
    @property
    def imagen(self) -> str:
        return get_pokemon_image_url(self.id)


class IntegrantePublic(Schema):
    id: int
    apodo: str
    pokemon: PokemonEquipoPublic
    movimientos: list[MovimientoResumidoPublic] | list


class EquipoPublic(Schema):
    id: int
    nombre: str
    generacion: GeneracionPublic
    integrantes: list[IntegrantePublic]


class PokemonIntegrantePublic(Schema):
    integrante: list[IntegrantePublic]


class EquipoResumidoPublic(Schema):
    id: int
    nombre: str
    generacion: GeneracionPublic
    cant_integrantes: int


# # # # # # # # # # # # # # # # # # # #


class EquipoUpsert(Schema):
    nombre: str
    id_generacion: int


class EquipoIntegranteAdd(Schema):
    id_pokemon: int
    apodo: str


class EquipoIntegrateMovimientoAdd(Schema):
    id_movimiento: int


class EquipoIntegranteUpdate(Schema):
    apodo: str
    movimientos: list[int]
