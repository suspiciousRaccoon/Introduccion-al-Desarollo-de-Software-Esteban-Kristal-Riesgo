from app.pokemon.models.tipo import Tipo
from app.utils.database import create_database
from app.utils.seed.tipo import load_tipos


def test_load_tyipos():
    database = create_database()
    load_tipos(database)
    assert database["tipos"] == [
        Tipo(id=1, nombre="Normal"),
        Tipo(id=2, nombre="Lucha"),
        Tipo(id=3, nombre="Volador"),
        Tipo(id=4, nombre="Veneno"),
        Tipo(id=5, nombre="Tierra"),
        Tipo(id=6, nombre="Roca"),
        Tipo(id=7, nombre="Bicho"),
        Tipo(id=8, nombre="Fantasma"),
        Tipo(id=9, nombre="Acero"),
        Tipo(id=10, nombre="Fuego"),
        Tipo(id=11, nombre="Agua"),
        Tipo(id=12, nombre="Planta"),
        Tipo(id=13, nombre="Eléctrico"),
        Tipo(id=14, nombre="Psíquico"),
        Tipo(id=15, nombre="Hielo"),
        Tipo(id=16, nombre="Dragón"),
        Tipo(id=17, nombre="Siniestro"),
        Tipo(id=18, nombre="Hada"),
        Tipo(id=10001, nombre="???"),  #
    ]
