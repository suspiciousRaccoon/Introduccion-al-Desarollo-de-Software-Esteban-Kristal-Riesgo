from app.pokemon.models.entity.movimiento import Movimiento

from app.pokemon.repository.movimiento import MovimientoRepository
from sqlmodel import Session


def test_get_movimiento_existente(session: Session):
    repo = MovimientoRepository(session)
    movimiento = repo.get(1)
    assert isinstance(movimiento, Movimiento)
    assert movimiento.id == 1
    assert movimiento.nombre != ""


def test_get_movimiento_inexistente(session: Session):
    repo = MovimientoRepository(session)
    movimiento = repo.get(9999)
    assert movimiento is None


def test_get_all_movimientos(session: Session):
    repo = MovimientoRepository(session)
    movimientos = repo.get_all()
    assert isinstance(movimientos, list)
    assert len(movimientos) > 1


def test_get_all_movimientos_resumidos_con_filtros(session: Session):
    repo = MovimientoRepository(session)

    tipo_id = 1
    movimientos_tipo = repo.get_all(tipo=tipo_id)
    assert all(movimiento.tipo.id == tipo_id for movimiento in movimientos_tipo)

    nombre_parcial = "ra"
    movimientos_nombre = repo.get_all(nombre_parcial=nombre_parcial)
    assert all(
        nombre_parcial.lower() in movimiento.nombre.lower()
        for movimiento in movimientos_nombre
    )

    combinados = repo.get_all(tipo=tipo_id, nombre_parcial=nombre_parcial)
    assert all(
        movimiento.tipo.id == tipo_id
        and nombre_parcial.lower() in movimiento.nombre.lower()
        for movimiento in combinados
    )
