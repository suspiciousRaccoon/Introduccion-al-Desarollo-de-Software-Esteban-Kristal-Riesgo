from fastapi.testclient import TestClient


class TestApp:
    def test_healthcheck(self, client: TestClient):
        response = client.get("/healthcheck")
        assert response.json() == {"status": "ok ฅ^•ﻌ•^ฅ"}
