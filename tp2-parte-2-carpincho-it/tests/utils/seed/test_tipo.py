from sqlmodel import Session, select
from app.pokemon.models.entity.tipo import Tipo
from app.utils.sqlite_seed.tipo import load_tipos, load_debilidades

from sqlalchemy import Engine


def test_load_tipos(sqlite_database: Engine):
    session = Session(sqlite_database)
    load_tipos(session)
    load_debilidades(session)

    tipo = session.get(Tipo, 1)

    assert tipo
    assert tipo.id == 1
    assert tipo.nombre == "Normal"

    tipo_12 = session.get(Tipo, 12)
    assert tipo_12
    assert tipo_12.id == 12
    assert tipo_12.nombre == "Planta"

    # weak to Flying, Bug, Ice, Poison, Fire
    assert len(tipo_12.debilidades) == 5
    assert tipo_12.debilidades == [
        Tipo(nombre="Volador", id=3),
        Tipo(nombre="Veneno", id=4),
        Tipo(nombre="Bicho", id=7),
        Tipo(nombre="Fuego", id=10),
        Tipo(nombre="Hielo", id=15),
    ]
    # Flying has lowest id
    assert tipo_12.debilidades[0].id == 3

    all_tipos = session.exec(select(Tipo)).all()
    assert all_tipos[-1].nombre == "???"
    assert all_tipos[0].nombre == "Normal"
    assert len(all_tipos) == 19


#         REFERENCE
#         Tipo(id=1, nombre="Normal"),
#         Tipo(id=2, nombre="Lucha"),
#         Tipo(id=3, nombre="Volador"),
#         Tipo(id=4, nombre="Veneno"),
#         Tipo(id=5, nombre="Tierra"),
#         Tipo(id=6, nombre="Roca"),
#         Tipo(id=7, nombre="Bicho"),
#         Tipo(id=8, nombre="Fantasma"),
#         Tipo(id=9, nombre="Acero"),
#         Tipo(id=10, nombre="Fuego"),
#         Tipo(id=11, nombre="Agua"),
#         Tipo(id=12, nombre="Planta"),
#         Tipo(id=13, nombre="Eléctrico"),
#         Tipo(id=14, nombre="Psíquico"),
#         Tipo(id=15, nombre="Hielo"),
#         Tipo(id=16, nombre="Dragón"),
#         Tipo(id=17, nombre="Siniestro"),
#         Tipo(id=18, nombre="Hada"),
#         Tipo(id=10001, nombre="???"),
#
