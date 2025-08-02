from app.pokemon.models.generacion import Generacion
from app.utils.database import create_database
from app.utils.seed.generacion import load_generaciones


def test_get_generaciones():
    database = create_database()
    load_generaciones(database)
    assert database["generaciones"] == [
        Generacion(id=1, nombre="Generación I"),
        Generacion(id=2, nombre="Generación II"),
        Generacion(id=3, nombre="Generación III"),
        Generacion(id=4, nombre="Generación IV"),
        Generacion(id=5, nombre="Generación V"),
        Generacion(id=6, nombre="Generación VI"),
        Generacion(id=7, nombre="Generación VII"),
        Generacion(id=8, nombre="Generación VIII"),
    ]
