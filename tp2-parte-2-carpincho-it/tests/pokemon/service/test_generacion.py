from unittest.mock import MagicMock, PropertyMock, patch

import pytest

from app.pokemon.models.entity.generacion import Generacion
from app.pokemon.service.generacion import GeneracionService


class TestGeneracionService:
    @patch("app.pokemon.service.generacion.GeneracionRepository")
    def test_get_generations(self, mock_repo_class):
        generaciones = [
            Generacion(id=1, nombre="Generación I"),
            Generacion(id=2, nombre="Generación II"),
            Generacion(id=3, nombre="Generación III"),
            Generacion(id=4, nombre="Generación IV"),
            Generacion(id=5, nombre="Generación V"),
            Generacion(id=6, nombre="Generación VI"),
            Generacion(id=7, nombre="Generación VII"),
            Generacion(id=8, nombre="Generación VIII"),
        ]

        mock_repo_instance = MagicMock()
        mock_repo_instance.get_all.return_value = generaciones
        mock_repo_class.return_value = mock_repo_instance

        service = GeneracionService(session=MagicMock())
        result = service.get_generations()

        assert result == generaciones
        mock_repo_instance.get_all.assert_called_once()
