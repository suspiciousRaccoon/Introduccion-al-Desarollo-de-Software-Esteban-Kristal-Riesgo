from fastapi import HTTPException
import pytest
from app.pokemon.models.movimiento import Movimiento
from app.pokemon.service.movimiento import MovimientoService


class TestMovimientoService:
    def test_get_movimiento(self, database):
        movimiento = MovimientoService(database).get_movimiento(1)
        assert movimiento.id == 1

    def test_exception_get_movimiento(self, database):
        with pytest.raises(HTTPException) as exc_info:
            MovimientoService(database).get_movimiento(99999999999)

        assert "Movimiento no encontrado" in str(exc_info.value)

    def test_get_movimientos(self, database):
        movimientos = MovimientoService(database).get_movimientos()
        assert len(movimientos) > 0
        for movimiento in movimientos:
            assert isinstance(movimiento, Movimiento)
