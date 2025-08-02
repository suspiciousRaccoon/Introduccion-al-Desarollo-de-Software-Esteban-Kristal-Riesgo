from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.pokemon.models.entity.pokemon import Pokemon
    from app.pokemon.models.entity.equipo import Integrante
    from app.pokemon.models.entity.tipo import Tipo
    from app.pokemon.models.entity.generacion import Generacion


class MovimientoMaquina(SQLModel, table=True):
    pokemon_id: int = Field(nullable=False, foreign_key="pokemon.id", primary_key=True)
    # pokemon: Pokemon | None = Relationship(back_populates="movimientos_maquina")

    movimiento_id: int = Field(
        nullable=False, foreign_key="movimiento.id", primary_key=True
    )
    # movimiento: Movimiento | None = Relationship(back_populates="pokemon_por_huevo")


class MovimientoNivel(SQLModel, table=True):
    pokemon_id: int = Field(nullable=False, foreign_key="pokemon.id", primary_key=True)
    # pokemon: Pokemon | None = Relationship(back_populates="movimientos_nivel")

    movimiento_id: int = Field(
        nullable=False, foreign_key="movimiento.id", primary_key=True
    )
    # movimiento: "Movimiento | None" = Relationship(back_populates="pokemon_por_huevo")


class MovimientoHuevo(SQLModel, table=True):
    pokemon_id: int = Field(nullable=False, foreign_key="pokemon.id", primary_key=True)
    # pokemon: Pokemon | None = Relationship(back_populates="movimientos_huevo")

    movimiento_id: int = Field(
        nullable=False, foreign_key="movimiento.id", primary_key=True
    )
    # movimiento: Movimiento | None = Relationship(back_populates="pokemon_por_huevo")


class MovimientoIntegrante(SQLModel, table=True):
    integrante_id: int = Field(
        nullable=False, foreign_key="integrante.id", primary_key=True
    )
    # integrante: Integrante | None = Relationship(back_populates="movimientos")

    movimiento_id: int = Field(
        nullable=False, foreign_key="movimiento.id", primary_key=True
    )
    # movimiento: Movimiento | None = Relationship(back_populates="integrantes")


class Movimiento(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    categoria: str
    potencia: int
    precision: int
    puntos_de_poder: int
    efecto: str
    tipo_id: int = Field(nullable=False, foreign_key="tipo.id")
    tipo: Optional["Tipo"] = Relationship(back_populates="movimientos")
    generacion_id: int = Field(nullable=False, foreign_key="generacion.id")
    generacion: Optional["Generacion"] = Relationship(back_populates="movimientos")
    pokemon_por_huevo: list["Pokemon"] | None = Relationship(
        back_populates="movimientos_huevo", link_model=MovimientoHuevo
    )
    pokemon_por_nivel: list["Pokemon"] | None = Relationship(
        back_populates="movimientos_nivel", link_model=MovimientoNivel
    )
    pokemon_por_maquina: list["Pokemon"] | None = Relationship(
        back_populates="movimientos_maquina", link_model=MovimientoMaquina
    )
    integrantes: list["Integrante"] | None = Relationship(
        back_populates="movimientos", link_model=MovimientoIntegrante
    )
