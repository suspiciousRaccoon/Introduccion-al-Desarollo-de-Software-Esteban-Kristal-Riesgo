from app.pokemon.models.movimiento import Movimiento, MovimientoResumido
from app.utils.types import Database


class MovimientoRepository:
    def __init__(self, database: Database):
        self.database = database

    def get(self, movimiento_id: int) -> Movimiento | None:
        for movimiento in self.database["movimientos"]:
            if movimiento.id == movimiento_id:
                return movimiento
        return None

    def get_all(self) -> list[MovimientoResumido]:
        return self.database["movimientos"]
