from typing import Optional
from fastapi import APIRouter
from app.pokemon.models.schema.movimiento import (
    MovimientoPublic,
    MovimientoResumidoPublic,
)
from app.pokemon.service.movimiento import MovimientoService
from app.utils.dependencies import Session
from app.utils.repository import Filter

router = APIRouter()


@router.get("/{movimiento_id}", response_model=MovimientoPublic)
def get_movimiento(movimiento_id: int, session: Session) -> MovimientoPublic:
    return MovimientoService(session).get_movimiento(movimiento_id)


@router.get("/", response_model=list[MovimientoResumidoPublic])
def get_movimientos(
    session: Session,
    limit: int = 10,
    offset: int = 0,
    tipo: Optional[int] = None,
    nombre_parcial: Optional[str] = None,
) -> list[MovimientoResumidoPublic]:
    return MovimientoService(session).get_movimientos(
        tipo, nombre_parcial, filters=Filter(limit=limit, offset=offset)
    )
