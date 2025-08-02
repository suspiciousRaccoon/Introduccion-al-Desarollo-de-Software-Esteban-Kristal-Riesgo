from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.pokemon.models.entity.movimiento import MovimientoIntegrante

if TYPE_CHECKING:
    from app.pokemon.models.entity.generacion import Generacion
    from app.pokemon.models.entity.movimiento import Movimiento
    from app.pokemon.models.entity.pokemon import Pokemon


class Equipo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    generacion_id: int = Field(nullable=False, foreign_key="generacion.id")
    generacion: Optional["Generacion"] = Relationship(
        back_populates="equipos", sa_relationship_kwargs={"lazy": "selectin"}
    )

    integrantes: list["Integrante"] | None = Relationship(
        back_populates="equipo", cascade_delete=True
    )


class Integrante(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    apodo: str = Field(unique=True)
    equipo_id: int = Field(nullable=False, foreign_key="equipo.id")
    equipo: Equipo | None = Relationship(
        back_populates="integrantes", sa_relationship_kwargs={"lazy": "selectin"}
    )

    pokemon_id: int = Field(nullable=False, foreign_key="pokemon.id")
    pokemon: Optional["Pokemon"] = Relationship(
        back_populates="integrantes", sa_relationship_kwargs={"lazy": "selectin"}
    )

    movimientos: list["Movimiento"] | None = Relationship(
        back_populates="integrantes",
        link_model=MovimientoIntegrante,
        sa_relationship_kwargs={"lazy": "selectin"},
    )
