from app.pokemon.models.generacion import Generacion
from app.pokemon.repository.generacion import GeneracionRepository
from app.utils.types import Database


def test_get_generacion_existente(database: Database):
    repo = GeneracionRepository(database)
    generacion = repo.get(1)
    assert isinstance(generacion, Generacion)
    assert generacion.id == 1
    assert "generación" in generacion.nombre.lower()


def test_get_generacion_inexistente(database: Database):
    repo = GeneracionRepository(database)
    generacion = repo.get(999)
    assert generacion is None


def test_get_all_generaciones(database: Database):
    repo = GeneracionRepository(database)
    generaciones = repo.get_all()
    assert isinstance(generaciones, list)
    assert len(generaciones) >= 1
    assert all(isinstance(g, Generacion) for g in generaciones)
