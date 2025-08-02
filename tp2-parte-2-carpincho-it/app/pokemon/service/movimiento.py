from typing import Optional

from sqlmodel import Session

from app.pokemon.exceptions import MovimientoNotFound
from app.pokemon.models.entity.movimiento import Movimiento
from app.pokemon.repository.movimiento import MovimientoRepository
from app.utils.repository import Filter


class MovimientoService:
    def __init__(self, session: Session):
        self.repository = MovimientoRepository(session)

    def get_movimiento(self, movimiento_id: int) -> Movimiento:
        movimiento = self.repository.get(movimiento_id)
        if movimiento is None:
            raise MovimientoNotFound
        return movimiento

    def get_movimientos(
        self,
        tipo: Optional[int] = None,
        nombre_parcial: Optional[str] = None,
        filters: Filter | None = None,
    ) -> list[Movimiento]:
        return self.repository.get_all(
            tipo=tipo, nombre_parcial=nombre_parcial, entity_filters=filters
        )
