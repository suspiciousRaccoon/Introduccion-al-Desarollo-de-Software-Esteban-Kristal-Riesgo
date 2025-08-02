from typing import Any

from app.pokemon.exceptions import (
    EquipoExists,
    EquipoNotFound,
    GeneracionNotFound,
    InvalidGeneration,
    InvalidIntegranteGeneracion,
    InvalidPokemonIntegrate,
    MaxIntegranteNumber,
    MovimientoNotFound,
)
from app.pokemon.models.equipo import (
    Equipo,
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoResumido,
    EquipoUpsert,
    Integrante,
)
from app.pokemon.repository.equipo import EquipoRepository, IntegranteRepository
from app.pokemon.repository.generacion import GeneracionRepository
from app.pokemon.repository.movimiento import MovimientoRepository
from app.pokemon.repository.pokemon import PokemonRepository
from app.utils.types import Database


class EquipoService:
    def __init__(self, database: Database):
        self.database = database
        self.equipo_repository = EquipoRepository(database)
        self.integrante_repository = IntegranteRepository(database)
        self.generacion_repository = GeneracionRepository(database)
        self.pokemon_repository = PokemonRepository(database)
        self.movimiento_repository = MovimientoRepository(database)

    def validate_generacion(self, generacion_id: int) -> None:
        generacion = self.generacion_repository.get(generacion_id)
        # tecnicamente lo podemos hacer con un FieldValidator en el modelo pero no lo vimos,
        # asi que lo hacemos aca en el service
        if generacion is None:
            raise GeneracionNotFound

    def get_equipo_por_id(self, equipo_id: int) -> Equipo:
        equipo = self.equipo_repository.get(equipo_id)
        if equipo is None:
            raise EquipoNotFound
        return equipo

    def get_equipos(self) -> list[EquipoResumido]:
        return self.equipo_repository.get_all()

    def create_equipo(self, data: EquipoUpsert) -> Equipo:
        self.validate_generacion(data.id_generacion)

        equipo = self.equipo_repository.get_por_nombre(data.nombre)
        if equipo is not None:
            raise EquipoExists

        return self.equipo_repository.create(data)

    def update_equipo(self, equipo_id: int, data: EquipoUpsert) -> Equipo:
        generacion = data.id_generacion
        self.validate_generacion(generacion)

        equipo = self.get_equipo_por_id(equipo_id)

        for integrante in equipo.integrantes:
            if generacion not in integrante.pokemon.generacion:
                raise InvalidGeneration

        return self.equipo_repository.update(equipo_id, data)

    def delete_equipo(self, equipo_id: int) -> Equipo:
        validated_id = self.get_equipo_por_id(equipo_id).id
        return self.equipo_repository.delete(validated_id)

    def add_integrante(self, equipo_id: int, data: EquipoIntegranteAdd) -> Integrante:
        equipo = self.get_equipo_por_id(equipo_id)

        if len(equipo.integrantes) >= 6:
            raise MaxIntegranteNumber

        pokemon = self.pokemon_repository.get(data.id_pokemon)

        if pokemon is None:
            raise InvalidPokemonIntegrate

        valid_generacion = False
        for generacion in pokemon.generaciones:
            if generacion.id <= equipo.generacion.id:
                valid_generacion = True
                break
        if not valid_generacion:
            raise InvalidIntegranteGeneracion

        return self.integrante_repository.create(equipo.id, data)

    def get_integrante(self, equipo_id: int, integrante_id: int) -> Integrante:
        integrante = self.integrante_repository.get(equipo_id, integrante_id)
        if integrante is None:
            raise InvalidPokemonIntegrate
        return integrante

    def add_movimiento_a_integrante(
        self, equipo_id: int, integrante_id: int, movimiento_id: int
    ) -> Integrante:
        integrante = self.get_integrante(equipo_id, integrante_id)
        new_movimiento = self.movimiento_repository.get(movimiento_id)

        if new_movimiento is None:
            raise MovimientoNotFound
        movimiento_ids = [movimiento.id for movimiento in integrante.movimientos]
        movimiento_ids.append(new_movimiento.id)

        data = EquipoIntegranteUpdate(
            apodo=integrante.apodo, movimientos=movimiento_ids
        )

        return self.integrante_repository.update(equipo_id, integrante.id, data)

    def update_integrante(
        self, equipo_id: int, integrante_id: int, data: EquipoIntegranteUpdate
    ) -> Integrante:
        integrante = self.get_integrante(equipo_id, integrante_id)
        return self.integrante_repository.update(equipo_id, integrante.id, data)

    def delete_integrante(self, equipo_id: int, integrante_id: int) -> Integrante:
        integrante = self.get_integrante(equipo_id, integrante_id)
        return self.integrante_repository.delete(equipo_id, integrante.id)
