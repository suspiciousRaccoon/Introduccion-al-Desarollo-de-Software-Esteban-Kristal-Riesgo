from app.pokemon.models.movimiento import Movimiento, MovimientoResumido
from app.pokemon.repository.movimiento import MovimientoRepository
from app.utils.types import Database


def test_get_movimiento_existente(database: Database):
    repo = MovimientoRepository(database)
    movimiento = repo.get(1)
    assert isinstance(movimiento, Movimiento)
    assert movimiento.id == 1
    assert movimiento.nombre != ""


def test_get_movimiento_inexistente(database: Database):
    repo = MovimientoRepository(database)
    movimiento = repo.get(9999)
    assert movimiento is None


def test_get_all_movimientos_resumidos(database: Database):
    repo = MovimientoRepository(database)
    movimientos = repo.get_all()
    assert isinstance(movimientos, list)
    assert all(isinstance(m, MovimientoResumido) for m in movimientos)
    assert len(movimientos) > 0
