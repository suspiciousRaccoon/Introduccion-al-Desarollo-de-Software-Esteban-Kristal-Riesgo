from fastapi import APIRouter

from app.pokemon.models.equipo import (
    Equipo,
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoIntegrateMovimientoAdd,
    EquipoResumido,
    EquipoUpsert,
    Integrante,
)
from app.pokemon.models.movimiento import MovimientoResumido
from app.pokemon.service.equipo import EquipoService
from app.utils.dependencies import Database

router = APIRouter()


@router.get("/{equipo_id}")
def get_equipo(db: Database, equipo_id: int) -> Equipo:
    return EquipoService(db).get_equipo_por_id(equipo_id)


@router.get("/")
def get_equipos(db: Database) -> list[EquipoResumido]:
    return EquipoService(db).get_equipos()


@router.post("/")
def create_equipo(db: Database, equipo: EquipoUpsert) -> Equipo:
    equipo_creado = EquipoService(db).create_equipo(equipo)
    return equipo_creado


@router.put("/{equipo_id}")
def update_equipo(db: Database, equipo_id: int, equipo: EquipoUpsert) -> Equipo:
    equipo_actualizado = EquipoService(db).update_equipo(equipo_id, equipo)
    return equipo_actualizado


@router.delete("/{equipo_id}")
def delete_equipo(db: Database, equipo_id: int) -> Equipo:
    equipo_eliminado = EquipoService(db).delete_equipo(equipo_id)
    return equipo_eliminado


@router.post("/{equipo_id}/integrantes")
def add_integrante(
    db: Database, equipo_id: int, integrante: EquipoIntegranteAdd
) -> Integrante:
    integrante_creado = EquipoService(db).add_integrante(equipo_id, integrante)
    return integrante_creado


@router.post("/{equipo_id}/integrantes/{integrante_id}/movimientos")
def add_movimiento(
    db: Database,
    equipo_id: int,
    integrante_id: int,
    movimiento: EquipoIntegrateMovimientoAdd,
) -> MovimientoResumido:
    movimiento_agregado = EquipoService(db).add_movimiento_a_integrante(
        equipo_id, integrante_id, movimiento.id_movimiento
    )
    return movimiento_agregado


@router.put("/{equipo_id}/integrantes/{integrante_id}/")
def update_integrante(
    db: Database, equipo_id: int, integrante_id: int, integrante: EquipoIntegranteUpdate
) -> Integrante:
    integrante_actualizado = EquipoService(db).update_integrante(
        equipo_id, integrante_id, integrante
    )
    return integrante_actualizado


@router.delete("/{equipo_id}/integrantes/{integrante_id}/")
def delete_integrante(db: Database, equipo_id: int, integrante_id: int) -> Integrante:
    integrante_eliminado = EquipoService(db).delete_integrante(equipo_id, integrante_id)
    return integrante_eliminado
