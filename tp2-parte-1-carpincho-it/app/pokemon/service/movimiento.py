from typing import Any

from app.pokemon.exceptions import MovimientoNotFound
from app.pokemon.models.movimiento import Movimiento, MovimientoResumido
from app.pokemon.repository.movimiento import MovimientoRepository
from app.utils.types import Database


class MovimientoService:
    def __init__(self, database: Database):
        self.database = database
        self.repository = MovimientoRepository(database)

    def get_movimiento(self, movimiento_id: int) -> Movimiento:
        movimiento = self.repository.get(movimiento_id)
        if movimiento is None:
            raise MovimientoNotFound
        return movimiento

    def get_movimientos(self) -> list[MovimientoResumido]:
        return self.repository.get_all()
