from fastapi.testclient import TestClient

URL = "api/generaciones"


class TestGeneracionRouter:

    def test_get_generacion(self, client: TestClient):
        data = client.get(URL).json()

        assert data == [
            {"id": 1, "nombre": "Generación I"},
            {"id": 2, "nombre": "Generación II"},
            {"id": 3, "nombre": "Generación III"},
            {"id": 4, "nombre": "Generación IV"},
            {"id": 5, "nombre": "Generación V"},
            {"id": 6, "nombre": "Generación VI"},
            {"id": 7, "nombre": "Generación VII"},
            {"id": 8, "nombre": "Generación VIII"},
        ]
