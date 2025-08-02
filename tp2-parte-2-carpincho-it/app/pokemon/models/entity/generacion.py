from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.pokemon.models.entity.pokemon import Pokemon
    from app.pokemon.models.entity.movimiento import Movimiento
    from app.pokemon.models.entity.equipo import Equipo


class GeneracionPokemon(SQLModel, table=True):
    pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
    # pokemon: Pokemon | None = Relationship(back_populates="generaciones")

    generacion_id: int = Field(foreign_key="generacion.id", primary_key=True)
    # generacion: Generacion | None = Relationship()


class Generacion(SQLModel, table=True):
    id: int = Field(primary_key=True, nullable=False)
    nombre: str
    movimientos: list["Movimiento"] | None = Relationship(back_populates="generacion")
    pokemons: list["Pokemon"] | None = Relationship(
        back_populates="generaciones", link_model=GeneracionPokemon
    )
    equipos: list["Equipo"] | None = Relationship(back_populates="generacion")
