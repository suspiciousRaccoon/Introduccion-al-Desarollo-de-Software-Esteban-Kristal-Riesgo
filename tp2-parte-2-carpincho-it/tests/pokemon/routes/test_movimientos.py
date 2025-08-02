from pprint import pprint

from fastapi.testclient import TestClient

URL = "api/movimientos"


class TestMovimientoRouter:

    def test_get_movimiento(self, client: TestClient):
        data = client.get(URL + "/1/").json()
        assert data["nombre"] == "Destructor"
        assert data["id"] == 1

    def test_get_movimientos(self, client: TestClient):
        data = client.get(URL).json()
        assert len(data) == 10  # default
        assert data[0]["id"] == 1
        assert data[1]["id"] == 2

    def test_get_movimientos_pagination(self, client):
        data = client.get(URL + "?limit=50&offset=1").json()
        assert len(data) == 50  # default
        assert data[0]["id"] == 2

    def test_get_movimientos_filtros(self, client: TestClient):
        data = client.get(URL + "?nombre_parcial='Destruc'").json()
        for movimiento in data:
            assert "Destruc" in movimiento["nombre"]

        data = client.get(URL + "?tipo=1").json()
        for movimiento in data:
            assert movimiento["tipo"]["id"] == 1
