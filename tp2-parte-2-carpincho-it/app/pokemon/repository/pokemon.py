from sqlalchemy.orm import selectinload
from sqlmodel import select

from app.pokemon.models.entity.generacion import Generacion
from app.pokemon.models.entity.movimiento import (
    Movimiento,
    MovimientoHuevo,
    MovimientoMaquina,
    MovimientoNivel,
)
from app.pokemon.models.entity.pokemon import Pokemon
from app.utils.repository import BaseRepository, Filter


class PokemonRepository(BaseRepository[Pokemon]):
    entity = Pokemon

    def get_all(
        self,
        tipo: int | None = None,
        nombre_parcial: str | None = None,
        generacion: int | None = None,
        entity_filters: Filter | None = None,
    ) -> list[Pokemon]:
        statement = self._build_filtered_statement(entity_filters=entity_filters)

        statement = statement.options(
            selectinload(Pokemon.movimientos_maquina),
            selectinload(Pokemon.movimientos_nivel),
            selectinload(Pokemon.movimientos_huevo),
            selectinload(Pokemon.tipos),
            selectinload(Pokemon.habilidades),
            selectinload(Pokemon.generaciones),
            selectinload(Pokemon.estadisticas),
            selectinload(Pokemon.evoluciones),
            selectinload(Pokemon.integrantes),
        )

        if tipo is not None:
            statement = statement.where(Pokemon.tipos.any(id=tipo))

        if nombre_parcial is not None:
            statement = statement.where(Pokemon.nombre.ilike(f"%{nombre_parcial}%"))

        if generacion is not None:
            statement = statement.where(
                Pokemon.generacion.any(Generacion.id == generacion)
            )
        return self.session.exec(statement).all()

    def get_unique_movimiento_ids(self, pokemon_id: int) -> set[int]:
        select_m_huevo = select(MovimientoHuevo.movimiento_id).where(
            MovimientoHuevo.pokemon_id == pokemon_id
        )
        select_m_nivel = select(MovimientoNivel.movimiento_id).where(
            MovimientoNivel.pokemon_id == pokemon_id
        )
        select_m_maquina = select(MovimientoMaquina.movimiento_id).where(
            MovimientoMaquina.pokemon_id == pokemon_id
        )

        statement = select_m_huevo.union(select_m_nivel, select_m_maquina)
        result = self.session.scalars(statement).all()
        return set(result)

    def get_unique_movimientos(
        self, pokemon_id: int, nombre_parcial: str | None = None
    ) -> list[Movimiento]:
        unique_movement_ids = self.get_unique_movimiento_ids(pokemon_id)

        statement = select(Movimiento).where(
            Movimiento.id.in_(unique_movement_ids),
        )

        if nombre_parcial is not None:
            statement = statement.where(
                Movimiento.nombre.ilike(f"%{nombre_parcial}%"),
            )

        return self.session.scalars(statement).all()
