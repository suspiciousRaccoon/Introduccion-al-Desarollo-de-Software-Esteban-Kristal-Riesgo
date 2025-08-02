from sqlmodel import Session, select

from app.pokemon.models.entity.movimiento import Movimiento

from app.utils.sqlite_seed.generacion import load_generaciones
from app.utils.sqlite_seed.tipo import load_tipos
from app.utils.sqlite_seed.movimiento import load_movimientos
from sqlalchemy import Engine


def test_load_movimientos(sqlite_database: Engine):

    session = Session(sqlite_database)
    load_tipos(session)
    load_generaciones(session)
    load_movimientos(session)

    movimiento = session.exec(select(Movimiento).where(Movimiento.id == 144)).one()

    assert movimiento.id == 144
    assert movimiento.nombre == "Transformación"
    assert movimiento.generacion.id == 1
    assert movimiento.tipo.id == 1
    assert (
        movimiento.efecto == "User becomes a copy of the target until it leaves battle."
    )
    # these are empty due to load_pokemon_movimientos no being called yet
    assert len(movimiento.pokemon_por_huevo) == 0
    assert len(movimiento.pokemon_por_maquina) == 0
    assert len(movimiento.pokemon_por_nivel) == 0

    # this would be valid if the relationships were assigned
    # assert movimiento.pokemon_por_nivel[0].id == 132  # ditto
    # assert movimiento.pokemon_por_nivel[1].id == 151  # mew
