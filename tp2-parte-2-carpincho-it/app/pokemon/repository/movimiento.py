from typing import Optional

from sqlalchemy.orm import selectinload

from app.pokemon.models.entity.movimiento import Movimiento
from app.utils.repository import BaseRepository, Filter


class MovimientoRepository(BaseRepository[Movimiento]):
    entity = Movimiento

    def get_all(
        self,
        tipo: Optional[int] = None,
        nombre_parcial: Optional[str] = None,
        entity_filters: Filter | None = None,
    ) -> list[Movimiento]:

        statement = self._build_filtered_statement(entity_filters)
        statement.options(
            selectinload(Movimiento.pokemon_por_huevo),
            selectinload(Movimiento.pokemon_por_maquina),
            selectinload(Movimiento.pokemon_por_nivel),
        )

        if tipo is not None:
            statement = statement.where(Movimiento.tipo_id == tipo)
        if nombre_parcial is not None:
            statement = statement.where(Movimiento.nombre.ilike(f"%{nombre_parcial}%"))
        movimientos = self.session.exec(statement).all()

        return movimientos
