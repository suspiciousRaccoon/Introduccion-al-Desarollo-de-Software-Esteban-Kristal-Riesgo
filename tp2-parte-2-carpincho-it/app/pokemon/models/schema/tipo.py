from sqlmodel import SQLModel
from app.pokemon.models.schema.base import Schema


class TipoPublic(Schema):
    id: int
    nombre: str


class PokemonTipoPublic(TipoPublic):
    debilidades: list[TipoPublic]
