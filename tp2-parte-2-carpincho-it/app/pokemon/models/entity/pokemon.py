from typing import TYPE_CHECKING, Optional

from pydantic import HttpUrl
from sqlmodel import Field, Relationship, SQLModel

from app.pokemon.models.entity.equipo import Integrante
from app.pokemon.models.entity.generacion import GeneracionPokemon
from app.pokemon.models.entity.movimiento import (
    MovimientoHuevo,
    MovimientoMaquina,
    MovimientoNivel,
)
from app.pokemon.models.entity.tipo import TipoPokemon

if TYPE_CHECKING:
    from app.pokemon.models.entity.estadistica import Estadistica
    from app.pokemon.models.entity.generacion import Generacion
    from app.pokemon.models.entity.movimiento import Movimiento
    from app.pokemon.models.entity.tipo import Tipo


class Evolucion(SQLModel, table=True):
    id: int = Field(primary_key=True)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    pokemon: Optional["Pokemon"] = Relationship(back_populates="evoluciones")
    nombre: str


class HabilidadPokemon(SQLModel, table=True):
    pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
    # pokemon: "Pokemon | None" = Relationship(back_populates="habilidades")

    habilidad_id: int = Field(foreign_key="habilidad.id", primary_key=True)
    # habilidad: "Habilidad | None" = Relationship()


class Habilidad(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    pokemons: list["Pokemon"] | None = Relationship(link_model=HabilidadPokemon)


class Pokemon(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    altura: float
    peso: float

    estadistica_id: int = Field(nullable=True, foreign_key="estadistica.id")  # 1:1
    estadisticas: Optional["Estadistica"] = Relationship()  # 1:1

    evoluciones: list["Evolucion"] | None = Relationship(
        back_populates="pokemon"
    )  # 1:N
    integrantes: list["Integrante"] | None = Relationship(
        back_populates="pokemon"
    )  # 1:N

    generaciones: list["Generacion"] | None = Relationship(
        link_model=GeneracionPokemon, back_populates="pokemons"
    )  # N:M

    tipos: list["Tipo"] | None = Relationship(
        link_model=TipoPokemon, back_populates="pokemons"
    )  # N:M

    habilidades: list["Habilidad"] | None = Relationship(
        link_model=HabilidadPokemon, back_populates="pokemons"
    )  # N:M
    movimientos_huevo: list["Movimiento"] | None = Relationship(
        link_model=MovimientoHuevo, back_populates="pokemon_por_huevo"
    )  # N:M
    movimientos_maquina: list["Movimiento"] | None = Relationship(
        link_model=MovimientoMaquina, back_populates="pokemon_por_maquina"
    )  # N:M
    movimientos_nivel: list["Movimiento"] | None = Relationship(
        link_model=MovimientoNivel, back_populates="pokemon_por_nivel"
    )  # N:M
