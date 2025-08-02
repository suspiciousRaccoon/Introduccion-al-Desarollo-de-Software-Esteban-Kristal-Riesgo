from pydantic import HttpUrl
from app.pokemon.models.generacion import Generacion
from app.pokemon.models.movimiento import Movimiento, PokemonResumido
from app.pokemon.models.tipo import Tipo
from app.utils.types import Database


def test_load_movimientos(database: Database):
    assert database["movimientos"][143] == Movimiento(
        id=144,
        nombre="Transformación",
        generacion=Generacion(id=1, nombre="Generación I"),
        tipo=Tipo(id=1, nombre="Normal"),
        categoria="estado",
        potencia=0,
        precision=0,
        puntos_de_poder=10,
        efecto="User becomes a copy of the target until it leaves battle.",
        pokemon_por_huevo=[],
        pokemon_por_nivel=[
            PokemonResumido(
                id=132,
                nombre="ditto",
                imagen=HttpUrl(
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/%3Cbuilt-in%20function%20id%3E.png"
                ),
                altura=3.0,
                peso=40.0,
            ),
            PokemonResumido(
                id=151,
                nombre="mew",
                imagen=HttpUrl(
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/%3Cbuilt-in%20function%20id%3E.png"
                ),
                altura=4.0,
                peso=40.0,
            ),
        ],
        pokemon_por_maquina=[],
    )
