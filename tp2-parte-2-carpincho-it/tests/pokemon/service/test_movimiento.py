from unittest.mock import MagicMock
from fastapi import HTTPException
import pytest
from app.pokemon.exceptions import MovimientoNotFound
from app.pokemon.models.entity.movimiento import Movimiento
from app.pokemon.models.schema.generacion import GeneracionPublic
from app.pokemon.models.schema.movimiento import MovimientoResumidoPublic
from app.pokemon.models.schema.tipo import TipoPublic
from app.pokemon.service.movimiento import MovimientoService


class TestMovimientoService:
    def test_get_movimiento_existente(self):
        mock_repo = MagicMock()
        fake_movimiento = Movimiento(id=1, nombre="Placaje")
        mock_repo.get.return_value = fake_movimiento

        service = MovimientoService(session=None)
        service.repository = mock_repo

        result = service.get_movimiento(1)
        assert result == fake_movimiento
        mock_repo.get.assert_called_once_with(1)

    def test_get_movimiento_inexistente(self):
        mock_repo = MagicMock()
        mock_repo.get.return_value = None

        service = MovimientoService(session=None)
        service.repository = mock_repo

        with pytest.raises(HTTPException) as exc_info:
            service.get_movimiento(999)

        assert exc_info.value.status_code == 404
        assert "Movimiento no encontrado" in str(exc_info.value.detail)

    def test_get_movimientos(self):
        mock_repo = MagicMock()
        fake_generacion = GeneracionPublic(id=1, nombre="Generación I")
        fake_tipo = TipoPublic(id=1, nombre="Normal", debilidades=[])
        fake_list = [
            MovimientoResumidoPublic(
                id=1,
                nombre="Placaje",
                categoria="Físico",
                potencia=40,
                precision=100,
                puntos_de_poder=35,
                efecto="Ninguno",
                generacion=fake_generacion,
                tipo=fake_tipo,
            )
        ]
        mock_repo.get_all.return_value = fake_list

        service = MovimientoService(session=None)
        service.repository = mock_repo

        result = service.get_movimientos()
        assert isinstance(result, list)
        assert all(
            isinstance(movimiento, MovimientoResumidoPublic) for movimiento in result
        )
        assert result == fake_list
