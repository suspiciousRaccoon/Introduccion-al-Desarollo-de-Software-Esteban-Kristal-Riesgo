from fastapi.testclient import TestClient

URL = "api/pokemon"


class TestPokemonRouter:

    def test_get_pokemon(self, client: TestClient):
        data = client.get(URL + "/1/").json()
        assert data["nombre"] == "bulbasaur"
        assert data["id"] == 1

    def test_get_pokemons(self, client: TestClient):
        data = client.get(URL).json()
        assert len(data) == 10  # default
        assert data[0]["id"] == 1
        assert data[1]["id"] == 2

    def test_get_pokemon_filtros(self, client: TestClient):
        data = client.get(URL + "?nombre_parcial='saur'").json()
        for pokemon in data:
            assert "saur" in pokemon["nombre"]

        data = client.get(URL + "?tipo=1").json()
        for pokemon in data:
            assert any(tipo["id"] == 1 for tipo in pokemon["tipos"])

        data = client.get(URL + "?nombre_parcial='saur'?tipo=12").json()
        for pokemon in data:
            assert "saur" in pokemon["nombre"]
            assert any(tipo["id"] == 12 for tipo in pokemon["tipos"])

    def test_filtrar_pokemon_por_generacion(self, client: TestClient):
        response = client.get("/api/pokemon?generaciones=1")
        assert response.status_code == 200
        pokemons = response.json()
        for pokemon in pokemons:
            assert any(generacion["id"] == 1 for generacion in pokemon["generaciones"])
