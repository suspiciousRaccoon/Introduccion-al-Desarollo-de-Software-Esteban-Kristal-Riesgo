from pydantic import BaseModel


class Tipo(BaseModel):
    id: int
    nombre: str


class PokemonTipo(Tipo):
    debilidades: list[Tipo]
