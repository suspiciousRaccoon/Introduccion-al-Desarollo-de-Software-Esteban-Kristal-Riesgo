import pytest
from fastapi import HTTPException

from app.pokemon.models.equipo import (
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoResumido,
    EquipoUpsert,
)
from app.pokemon.service.equipo import EquipoService
from app.utils.types import Database


class TestEquipoService:
    def test_create_equipo(self, database: Database):
        data = EquipoUpsert(nombre="Rocket", id_generacion=1)
        equipo = EquipoService(database).create_equipo(data)
        assert equipo.id == 1
        assert equipo.generacion.id == 1
        assert equipo.nombre == "Rocket"

    def test_exception_create_equipo_duplicate_name(self, database: Database):
        data = EquipoUpsert(nombre="Rocket", id_generacion=1)
        EquipoService(database).create_equipo(data)
        with pytest.raises(HTTPException) as exc_info:
            EquipoService(database).create_equipo(data)

        assert "El nombre de equipo ya fue registrado" in str(exc_info.value)

    def test_get_equipo(self, database: Database):
        service = EquipoService(database)
        data = EquipoUpsert(nombre="Rocket", id_generacion=1)
        service.create_equipo(data)

        equipo = service.get_equipo_por_id(1)
        assert equipo.id == 1
        assert equipo.generacion.id == 1
        assert equipo.nombre == "Rocket"

    def test_exception_get_equipo(self, database: Database):
        with pytest.raises(HTTPException) as exc_info:
            EquipoService(database).get_equipo_por_id(99999999999)

        assert "Equipo no encontrado" in str(exc_info.value)

    def test_get_equipos(self, database: Database):
        service = EquipoService(database)
        data1 = EquipoUpsert(nombre="Rocket", id_generacion=1)
        data2 = EquipoUpsert(nombre="Rocket2", id_generacion=2)
        service.create_equipo(data1)
        service.create_equipo(data2)

        equipos = service.get_equipos()
        assert len(equipos) == 2
        for equipo in equipos:
            assert isinstance(equipo, EquipoResumido)

    def test_update_equipo(self, database: Database):
        service = EquipoService(database)
        data1 = EquipoUpsert(nombre="Rocket", id_generacion=1)
        data2 = EquipoUpsert(nombre="Rocket2", id_generacion=2)
        service.create_equipo(data1)
        service.update_equipo(1, data2)
        equipo = service.get_equipo_por_id(1)

        assert equipo.id == 1
        assert equipo.nombre == "Rocket2"
        assert equipo.generacion.id == 2

    def test_delete_equipo(self, database: Database):
        service = EquipoService(database)
        data1 = EquipoUpsert(nombre="Rocket", id_generacion=1)
        service.create_equipo(data1)
        service.delete_equipo(1)
        with pytest.raises(HTTPException) as exc_info:
            service.get_equipo_por_id(1)

        assert "Equipo no encontrado" in str(exc_info.value)

    def test_add_integrante(self, database: Database):
        service = EquipoService(database)
        data1 = EquipoUpsert(nombre="Rocket", id_generacion=1)
        service.create_equipo(data1)
        data2 = EquipoIntegranteAdd(apodo="saur", id_pokemon=1)
        service.add_integrante(1, data2)

        equipo = service.get_equipo_por_id(1)
        assert len(equipo.integrantes) == 1
        assert equipo.integrantes[0].id == 1
        assert equipo.integrantes[0].apodo == "saur"
        assert equipo.integrantes[0].pokemon.id == 1

    def test_add_integrante_invalid_pokemon(self, database: Database):
        service = EquipoService(database)
        data1 = EquipoUpsert(nombre="Rocket", id_generacion=1)
        service.create_equipo(data1)
        data2 = EquipoIntegranteAdd(apodo="fake", id_pokemon=999999)

        with pytest.raises(HTTPException) as exc_info:
            service.add_integrante(1, data2)

        assert "Los datos del integrante no son validos" in str(exc_info.value)

    def test_add_integrante_invalid_generacion(self, database: Database):
        service = EquipoService(database)
        data1 = EquipoUpsert(nombre="Rocket", id_generacion=1)
        service.create_equipo(data1)

        data2 = EquipoIntegranteAdd(apodo="waxy", id_pokemon=607)  # Litwick gen 5

        with pytest.raises(HTTPException) as exc_info:
            service.add_integrante(1, data2)

        assert "El integrante no pertenece a la generacion del equipo" in str(
            exc_info.value
        )

    def test_get_integrante(self, database: Database):
        service = EquipoService(database)
        service.create_equipo(EquipoUpsert(nombre="Rocket", id_generacion=5))
        service.add_integrante(1, EquipoIntegranteAdd(apodo="waxy", id_pokemon=607))

        integrante = service.get_integrante(1, 1)
        assert integrante.id == 1
        assert integrante.pokemon.id == 607
        assert integrante.apodo == "waxy"

    def test_add_movmimiento_integrante(self, database: Database):
        service = EquipoService(database)
        service.create_equipo(EquipoUpsert(nombre="Rocket", id_generacion=5))
        service.add_integrante(1, EquipoIntegranteAdd(apodo="waxy", id_pokemon=607))

        integrante = service.add_movimiento_a_integrante(1, 1, 1)
        assert len(integrante.movimientos) == 1
        assert integrante.movimientos[0].id == 1

    def test_update_intgrante(self, database: Database):
        service = EquipoService(database)
        service.create_equipo(EquipoUpsert(nombre="Rocket", id_generacion=5))
        service.add_integrante(1, EquipoIntegranteAdd(apodo="waxy", id_pokemon=607))

        update_data = EquipoIntegranteUpdate(apodo="waxier", movimientos=[])
        service.update_integrante(1, 1, update_data)

        assert service.get_integrante(1, 1).apodo == "waxier"

    def test_delete_integrante(self, database: Database):
        service = EquipoService(database)
        service.create_equipo(EquipoUpsert(nombre="Rocket", id_generacion=5))
        service.add_integrante(1, EquipoIntegranteAdd(apodo="waxy", id_pokemon=607))

        service.delete_integrante(1, 1)
        with pytest.raises(HTTPException) as exc_info:
            service.get_integrante(1, 1)

        assert "Los datos del integrante no son validos" in str(exc_info.value)
