from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.pokemon.models.entity.pokemon import Pokemon
    from app.pokemon.models.entity.movimiento import Movimiento


class Debilidad(SQLModel, table=True):
    tipo_id: int = Field(nullable=False, foreign_key="tipo.id", primary_key=True)
    # tipo: Optional["Tipo"] = Relationship(
    #     back_populates="debilidades",
    #     sa_relationship_kwargs=dict(foreign_keys="[Debilidad.tipo_id]"),
    # )
    debilidad_id: int = Field(nullable=False, foreign_key="tipo.id", primary_key=True)
    # debilidad: Optional["Tipo"] = Relationship(
    #     sa_relationship_kwargs=dict(foreign_keys="[Debilidad.debilidad_id]")
    # )


class TipoPokemon(SQLModel, table=True):
    tipo_id: int = Field(foreign_key="tipo.id", primary_key=True)
    # tipo: Optional["Tipo"] = Relationship(back_populates="pokemons")

    pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
    # pokemon: Optional["Pokemon"] = Relationship(back_populates="tipos")


class Tipo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimientos: list["Movimiento"] | None = Relationship(back_populates="tipo")

    pokemons: list["Pokemon"] | None = Relationship(
        back_populates="tipos", link_model=TipoPokemon
    )
    debilidades: list["Tipo"] = Relationship(
        link_model=Debilidad,
        sa_relationship_kwargs=dict(
            primaryjoin="Tipo.id==Debilidad.tipo_id",
            secondaryjoin="Tipo.id==Debilidad.debilidad_id",
        ),
    )
