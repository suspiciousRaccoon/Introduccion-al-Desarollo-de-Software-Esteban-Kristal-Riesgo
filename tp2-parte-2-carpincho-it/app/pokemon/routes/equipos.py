from fastapi import APIRouter

from app.pokemon.models.entity.equipo import Equipo
from app.pokemon.models.schema.equipo import (
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoIntegrateMovimientoAdd,
    EquipoPublic,
    EquipoResumidoPublic,
    EquipoUpsert,
    IntegrantePublic,
)
from app.pokemon.models.schema.movimiento import MovimientoResumidoPublic
from app.pokemon.service.equipo import EquipoService
from app.utils.dependencies import Session
from app.utils.repository import Filter

router = APIRouter()


@router.get("/{equipo_id}", response_model=EquipoPublic)
def get_equipo(equipo_id: int, session: Session) -> Equipo:
    return EquipoService(session).get_equipo_por_id(equipo_id)


@router.get("/", response_model=list[EquipoResumidoPublic])
def get_equipos(
    session: Session, limit: int = 10, offset: int = 0
) -> list[EquipoResumidoPublic]:
    return EquipoService(session).get_equipos(
        filters=Filter(limit=limit, offset=offset)
    )


@router.post("/", response_model=EquipoPublic)
def create_equipo(equipo: EquipoUpsert, session: Session) -> EquipoPublic:
    equipo_creado = EquipoService(session).create_equipo(equipo)
    return equipo_creado


@router.put("/{equipo_id}", response_model=EquipoPublic)
def update_equipo(
    equipo_id: int, equipo: EquipoUpsert, session: Session
) -> EquipoPublic:
    equipo_actualizado = EquipoService(session).update_equipo(equipo_id, equipo)
    return equipo_actualizado


@router.delete("/{equipo_id}", response_model=EquipoPublic)
def delete_equipo(equipo_id: int, session: Session) -> EquipoPublic:
    equipo_eliminado = EquipoService(session).delete_equipo(equipo_id)
    return equipo_eliminado


@router.get("/{equipo_id}/integrantes/{integrante_id}", response_model=IntegrantePublic)
def get_integrante(
    equipo_id: int,
    integrante_id: int,
    session: Session,
):
    integrante = EquipoService(session).get_integrante(equipo_id, integrante_id)
    return integrante


@router.post("/{equipo_id}/integrantes", response_model=IntegrantePublic)
def add_integrante(
    equipo_id: int,
    integrante: EquipoIntegranteAdd,
    session: Session,
) -> IntegrantePublic:
    integrante_creado = EquipoService(session).add_integrante(equipo_id, integrante)
    return integrante_creado


@router.post(
    "/{equipo_id}/integrantes/{integrante_id}/movimientos",
    response_model=MovimientoResumidoPublic,
)
def add_movimiento(
    equipo_id: int,
    integrante_id: int,
    movimiento: EquipoIntegrateMovimientoAdd,
    session: Session,
) -> MovimientoResumidoPublic:
    movimiento_agregado = EquipoService(session).add_movimiento_a_integrante(
        equipo_id, integrante_id, movimiento.id_movimiento
    )
    return movimiento_agregado


@router.put(
    "/{equipo_id}/integrantes/{integrante_id}/", response_model=IntegrantePublic
)
def update_integrante(
    equipo_id: int,
    integrante_id: int,
    integrante: EquipoIntegranteUpdate,
    session: Session,
) -> IntegrantePublic:
    integrante_actualizado = EquipoService(session).update_integrante(
        equipo_id, integrante_id, integrante
    )
    return integrante_actualizado


@router.delete(
    "/{equipo_id}/integrantes/{integrante_id}/", response_model=IntegrantePublic
)
def delete_integrante(
    equipo_id: int, integrante_id: int, session: Session
) -> IntegrantePublic:
    integrante_eliminado = EquipoService(session).delete_integrante(
        equipo_id, integrante_id
    )
    return integrante_eliminado
