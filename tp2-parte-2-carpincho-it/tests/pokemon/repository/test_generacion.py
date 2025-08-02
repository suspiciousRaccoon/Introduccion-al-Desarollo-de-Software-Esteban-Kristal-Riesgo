from sqlmodel import Session
from app.pokemon.models.entity.generacion import Generacion
from app.pokemon.repository.generacion import GeneracionRepository


def test_get_generacion_existente(session: Session):
    repo = GeneracionRepository(session)
    generacion = repo.get(1)
    assert isinstance(generacion, Generacion)
    assert generacion.id == 1
    assert "generación" in generacion.nombre.lower()


def test_get_generacion_inexistente(session: Session):
    repo = GeneracionRepository(session)
    generacion = repo.get(999)
    assert generacion is None


def test_get_all_generaciones(session: Session):
    repo = GeneracionRepository(session)
    generaciones = repo.get_all()
    assert isinstance(generaciones, list)
    assert len(generaciones) >= 1
    assert all(isinstance(g, Generacion) for g in generaciones)
