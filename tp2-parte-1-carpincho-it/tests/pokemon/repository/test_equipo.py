import pytest

from app.pokemon.models.equipo import (
    Equipo,
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoResumido,
    EquipoUpsert,
)
from app.pokemon.repository.equipo import EquipoRepository, IntegranteRepository
from app.utils.types import Database


class TestEquipoRepository:
    def test_create_equipo_exitoso(self, database: Database):
        repo = EquipoRepository(database)
        generacion = database["generaciones"][0]
        assert generacion.id == 1
        data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=generacion.id)
        nuevo_equipo = repo.create(data)

        assert isinstance(nuevo_equipo, Equipo)
        assert nuevo_equipo.nombre == "Equipo Rocket"
        assert nuevo_equipo.generacion.id == generacion.id

    def test_create_equipo_nombre_duplicado(self, database: Database):
        repo = EquipoRepository(database)
        generacion = database["generaciones"][0]
        data1 = EquipoUpsert(nombre="Equipo Rocket", id_generacion=generacion.id)
        data2 = EquipoUpsert(nombre="Equipo Rocket", id_generacion=generacion.id)
        repo.create(data1)
        with pytest.raises(ValueError) as exc_info:
            repo.create(data2)

        assert "Ya existe un equipo con ese nombre" in str(exc_info.value)

    def test_get_equipo_creado(self, database: Database):
        repo = EquipoRepository(database)
        generacion = database["generaciones"][0]
        data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=generacion.id)
        repo.create(data)
        equipo = repo.get_por_nombre("equipo rocket")

        assert equipo is not None
        assert equipo.nombre == "Equipo Rocket"

    def test_get_equipo_existente(self, database: Database):
        repo = EquipoRepository(database)
        generacion = database["generaciones"][0]
        data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=generacion.id)
        repo.create(data)
        equipo = repo.get(1)
        assert equipo is not None
        assert equipo.nombre == "Equipo Rocket"

    def test_get_all_equipos(self, database: Database):
        repo = EquipoRepository(database)
        generacion = database["generaciones"][0]
        data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=generacion.id)
        repo.create(data)
        equipos = repo.get_all()
        assert len(equipos) == 1
        assert isinstance(equipos[0], EquipoResumido)
        assert equipos[0].nombre == "Equipo Rocket"

    def test_get_por_nombre_inexistente(self, database: Database):
        repo = EquipoRepository(database)
        assert repo.get_por_nombre("equipo fantasma") is None


class TestIntegranteRepository:
    def test_get_integrante_none(self, database: Database):
        repo_equipo = EquipoRepository(database)
        repo = IntegranteRepository(database)
        equipo_data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=1)
        repo_equipo.create(equipo_data)
        assert repo.get(0, 9999) is None

    def test_create_integrate(self, database: Database):
        repo_equipo = EquipoRepository(database)
        repo = IntegranteRepository(database)
        equipo_data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=1)
        repo_equipo.create(equipo_data)
        integrante_data = EquipoIntegranteAdd(id_pokemon=133, apodo="eev")
        integrante = repo.create(1, integrante_data)

        assert integrante.apodo == "eev"
        assert integrante.id == 1
        assert integrante.pokemon.id == 133
        assert integrante.movimientos == []

    def test_update_integrante(self, database: Database):
        repo_equipo = EquipoRepository(database)
        repo = IntegranteRepository(database)
        equipo_data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=1)
        repo_equipo.create(equipo_data)
        integrante_data = EquipoIntegranteAdd(id_pokemon=133, apodo="eev")
        integrante = repo.create(1, integrante_data)

        updated_integrante = repo.update(
            1, 1, EquipoIntegranteUpdate(apodo="vee", movimientos=[608])
        )
        assert updated_integrante.apodo == "vee"
        assert updated_integrante.movimientos[0].id == 608

    def test_delete_integrante(self, database: Database):
        repo_equipo = EquipoRepository(database)
        repo = IntegranteRepository(database)
        equipo_data = EquipoUpsert(nombre="Equipo Rocket", id_generacion=1)
        repo_equipo.create(equipo_data)
        integrante_data = EquipoIntegranteAdd(id_pokemon=133, apodo="eev")
        integrante = repo.create(1, integrante_data)

        deleted_integrante = repo.delete(1, 1)

        assert deleted_integrante.id == 1
        assert deleted_integrante.apodo == "eev"
        assert repo.get(1, 1) is None
