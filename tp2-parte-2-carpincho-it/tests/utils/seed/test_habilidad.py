from sqlmodel import Session, select
from app.pokemon.models.entity.pokemon import Habilidad

from sqlalchemy import Engine

from app.utils.sqlite_seed.habilidad import load_habilidades


def test_load_habilidad(sqlite_database: Engine):
    session = Session(sqlite_database)
    load_habilidades(session)

    habilidad = session.exec(select(Habilidad)).first()
    assert habilidad.id == 1
    assert habilidad.nombre == "Hedor"  # stentch
