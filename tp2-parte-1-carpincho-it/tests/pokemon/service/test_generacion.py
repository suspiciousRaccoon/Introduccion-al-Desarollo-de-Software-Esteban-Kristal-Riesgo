from unittest.mock import MagicMock, PropertyMock, patch

from app.pokemon.models.generacion import Generacion
from app.pokemon.service.generacion import GeneracionService


class TestGeneracionService:
    @patch(
        "app.pokemon.service.generacion.GeneracionRepository", new_callable=PropertyMock
    )
    def test(self, mock_repo: PropertyMock, mock_db: MagicMock):
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

        mock_repo.return_value.get_all = lambda: generaciones

        service = GeneracionService(mock_db)
        assert service.get_generations() == generaciones
