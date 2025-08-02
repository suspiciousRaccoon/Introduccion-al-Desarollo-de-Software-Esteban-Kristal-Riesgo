from fastapi.testclient import TestClient

from app.pokemon.models.schema.equipo import (
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoIntegrateMovimientoAdd,
    EquipoUpsert,
)

URL = "api/equipos"


class TestMovimientoRouter:

    def test_get_equipo_none(self, client: TestClient):
        data = client.get(URL + "/1/")
        assert data.status_code == 404

    def test_create_equipo(self, client: TestClient):
        data = EquipoUpsert(nombre="rocket", id_generacion=1)
        response = client.post(URL, json=data.model_dump())
        equipo = response.json()
        assert response.status_code == 200
        assert equipo["id"] == 1
        assert equipo["nombre"] == "rocket"
        assert equipo["integrantes"] == []
        assert equipo["generacion"]["id"] == 1

    def test_get_equipo(self, client: TestClient):
        data = EquipoUpsert(nombre="rocket", id_generacion=1)
        client.post(URL, json=data.model_dump())
        response = client.get(URL + "/1/")
        equipo = response.json()
        assert response.status_code == 200
        assert equipo["id"] == 1
        assert equipo["nombre"] == "rocket"
        assert equipo["integrantes"] == []
        assert equipo["generacion"]["id"] == 1

    def test_get_equipos(self, client: TestClient):
        client.post(
            URL, json=EquipoUpsert(nombre="rocket", id_generacion=1).model_dump()
        )
        client.post(URL, json=EquipoUpsert(nombre="AAAA", id_generacion=5).model_dump())

        data = client.get(URL).json()

        assert data[0]["nombre"] == "rocket"
        assert data[1]["nombre"] == "AAAA"

    def test_create_equipo_duplicate(self, client: TestClient):
        data = EquipoUpsert(nombre="rocket", id_generacion=1)
        response = client.post(URL, json=data.model_dump())
        assert response.status_code == 200
        response = client.post(URL, json=data.model_dump())
        assert response.status_code != 200

    def test_update_equipo(self, client: TestClient):
        data = EquipoUpsert(nombre="rocket", id_generacion=1)
        response = client.post(URL, json=data.model_dump())

        assert response.status_code == 200
        assert response.json()["nombre"] == "rocket"

        data2 = EquipoUpsert(nombre="AAAAAA", id_generacion=4)
        response = client.post(URL, json=data2.model_dump())
        assert response.status_code == 200
        data = response.json()
        assert data["nombre"] == "AAAAAA"
        assert data["generacion"]["id"] == 4

    def test_delete_equipo(self, client: TestClient):
        data = EquipoUpsert(nombre="rocket", id_generacion=1)
        client.post(URL, json=data.model_dump())

        client.delete(URL + "/1/")

        assert client.get(URL + "/1/").status_code == 404

    def test_add_integrante(self, client: TestClient):
        equipo_data = EquipoUpsert(nombre="rocket", id_generacion=1)
        client.post(URL, json=equipo_data.model_dump())

        data = EquipoIntegranteAdd(apodo="bu", id_pokemon=1)
        response = client.post(URL + "/1/integrantes/", json=data.model_dump())
        assert response.status_code == 200

    def test_integrante_and_get_equipo(self, client: TestClient):
        equipo_data = EquipoUpsert(nombre="rocket", id_generacion=1)
        client.post(URL, json=equipo_data.model_dump())

        data = EquipoIntegranteAdd(apodo="bu", id_pokemon=1)
        response = client.post(URL + "/1/integrantes/", json=data.model_dump())
        assert response.status_code == 200

        reponse = client.get(URL + "/1/")
        assert reponse.json()["integrantes"][0]["apodo"] == "bu"

    def test_add_movimiento(self, client: TestClient):
        client.post(
            URL, json=EquipoUpsert(nombre="rocket", id_generacion=1).model_dump()
        )
        client.post(
            URL + "/1/integrantes/",
            json=EquipoIntegranteAdd(apodo="bu", id_pokemon=1).model_dump(),
        )

        data = EquipoIntegrateMovimientoAdd(id_movimiento=74)  # growth
        response = client.post(
            URL + "/1/integrantes/1/movimientos", json=data.model_dump()
        )
        assert response.status_code == 200
        assert response.json()["id"] == 74

        reponse = client.get(URL + "/1/")
        assert reponse.json()["integrantes"][0]["movimientos"][0]["id"] == 74

    def test_update_integrante(self, client: TestClient):
        client.post(
            URL, json=EquipoUpsert(nombre="rocket", id_generacion=1).model_dump()
        )
        client.post(
            URL + "/1/integrantes/",
            json=EquipoIntegranteAdd(apodo="bu", id_pokemon=1).model_dump(),
        )

        data = EquipoIntegranteUpdate(apodo="ub", movimientos=[74, 75])
        response = client.put(URL + "/1/integrantes/1/", json=data.model_dump())
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["apodo"] == "ub"
        assert response_data["movimientos"][0]["id"] == 74
        assert response_data["movimientos"][1]["id"] == 75

        equipo_data = client.get(URL + "/1/").json()
        assert equipo_data["integrantes"][0]["movimientos"][0]["id"] == 74
        assert equipo_data["integrantes"][0]["movimientos"][1]["id"] == 75

    def test_delete_integrante(self, client: TestClient):
        client.post(
            URL, json=EquipoUpsert(nombre="rocket", id_generacion=1).model_dump()
        )
        client.post(
            URL + "/1/integrantes/",
            json=EquipoIntegranteAdd(apodo="bu", id_pokemon=1).model_dump(),
        )

        response = client.delete(
            URL + "/1/integrantes/1/",
        )
        assert response.status_code == 200
        assert response.json()["apodo"] == "bu"
