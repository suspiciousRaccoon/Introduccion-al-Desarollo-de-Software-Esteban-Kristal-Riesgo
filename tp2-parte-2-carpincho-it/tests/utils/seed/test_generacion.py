from sqlmodel import Session, select
from app.pokemon.models.entity.generacion import Generacion
from app.utils.sqlite_seed.generacion import load_generaciones
from sqlalchemy import Engine


def test_load_generaciones(sqlite_database: Engine):
    session = Session(sqlite_database)
    load_generaciones(session)

    generaciones = session.exec(select(Generacion)).all()

    assert generaciones == [
        Generacion(id=1, nombre="Generación I"),
        Generacion(id=2, nombre="Generación II"),
        Generacion(id=3, nombre="Generación III"),
        Generacion(id=4, nombre="Generación IV"),
        Generacion(id=5, nombre="Generación V"),
        Generacion(id=6, nombre="Generación VI"),
        Generacion(id=7, nombre="Generación VII"),
        Generacion(id=8, nombre="Generación VIII"),
    ]
