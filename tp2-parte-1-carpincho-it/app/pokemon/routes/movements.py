from fastapi import APIRouter
from app.pokemon.models.movimiento import Movimiento, MovimientoResumido
from app.pokemon.service.movimiento import MovimientoService
from app.utils.dependencies import Database

router = APIRouter()


@router.get("/{movimiento_id}")
def get_movimiento(db: Database, movimiento_id: int) -> Movimiento:
    return MovimientoService(db).get_movimiento(movimiento_id)


@router.get("/")
def get_movimientos(db: Database) -> list[MovimientoResumido]:
    return MovimientoService(db).get_movimientos()
