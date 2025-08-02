from fastapi.testclient import TestClient


class TestTipoRouter:
    def test_get_tipos(self, client: TestClient):
        response = client.get("/api/tipos")
        assert response.status_code == 200
        assert len(response.json()) > 0
