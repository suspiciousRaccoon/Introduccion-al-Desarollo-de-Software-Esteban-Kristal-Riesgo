from sqlmodel import Session

from app.pokemon.exceptions import (
    EquipoExists,
    EquipoNotFound,
    GeneracionNotFound,
    InvalidGeneration,
    InvalidIntegranteGeneracion,
    InvalidPokemonIntegranteApodo,
    InvalidPokemonIntegrate,
    InvalidPokemonMovimiento,
    MaxIntegranteNumber,
    MovimientoNotFound,
)
from app.pokemon.models.entity.equipo import Equipo, Integrante
from app.pokemon.models.schema.equipo import (
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoResumidoPublic,
    EquipoUpsert,
)
from app.pokemon.repository.equipo import EquipoRepository, IntegranteRepository
from app.pokemon.repository.generacion import GeneracionRepository
from app.pokemon.repository.movimiento import MovimientoRepository
from app.pokemon.repository.pokemon import PokemonRepository
from app.utils.repository import Filter


class EquipoService:
    def __init__(self, session: Session):
        self.session = session
        self.equipo_repository = EquipoRepository(session)
        self.integrante_repository = IntegranteRepository(session)
        self.generacion_repository = GeneracionRepository(session)
        self.pokemon_repository = PokemonRepository(session)
        self.movimiento_repository = MovimientoRepository(session)

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

    def get_equipos(self, filters: Filter | None = None) -> list[EquipoResumidoPublic]:
        equipos = self.equipo_repository.get_all_with_filter(entity_filters=filters)
        resumidos = []
        for equipo in equipos:
            resumidos.append(
                EquipoResumidoPublic(
                    generacion=equipo.generacion,
                    nombre=equipo.nombre,
                    id=equipo.id,
                    cant_integrantes=len(equipo.integrantes),
                )
            )
        return resumidos

    def create_equipo(self, data: EquipoUpsert) -> Equipo:
        self.validate_generacion(data.id_generacion)

        equipo = self.equipo_repository.get_por_nombre(data.nombre)
        if equipo is not None:
            raise EquipoExists

        return self.equipo_repository.create(data)

    def update_equipo(self, equipo_id: int, data: EquipoUpsert) -> Equipo:
        self.validate_generacion(data.id_generacion)

        equipo = self.get_equipo_por_id(equipo_id)

        for integrante in equipo.integrantes:
            if all(
                generacion.id > data.id_generacion
                for generacion in integrante.pokemon.generaciones
            ):
                raise InvalidGeneration

        return self.equipo_repository.update(equipo_id, data)

    def delete_equipo(self, equipo_id: int) -> Equipo:
        return self.equipo_repository.delete(equipo_id)

    def add_integrante(self, equipo_id: int, data: EquipoIntegranteAdd) -> Integrante:
        equipo = self.get_equipo_por_id(equipo_id)

        if len(equipo.integrantes) >= 6:
            raise MaxIntegranteNumber

        integrante = self.integrante_repository.get_integrante_por_apodo(
            equipo_id, data.apodo
        )

        if integrante:
            raise InvalidPokemonIntegranteApodo

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

        return self.integrante_repository.create(equipo_id, data)

    def get_integrante(self, equipo_id: int, integrante_id: int) -> Integrante:
        integrante = self.integrante_repository.get(equipo_id, integrante_id)
        if integrante is None:
            raise InvalidPokemonIntegrate
        return integrante

    def add_movimiento_a_integrante(
        self, equipo_id: int, integrante_id: int, movimiento_id: int
    ) -> Integrante:
        new_movimiento = self.movimiento_repository.get(movimiento_id)

        if new_movimiento is None:
            raise MovimientoNotFound

        integrante = self.get_integrante(equipo_id, integrante_id)
        pokemon_movimiento_ids = self.pokemon_repository.get_unique_movimiento_ids(
            integrante.pokemon_id
        )

        if movimiento_id not in pokemon_movimiento_ids:
            raise InvalidPokemonMovimiento

        movimiento_ids = [movimiento.id for movimiento in integrante.movimientos]
        movimiento_ids.append(new_movimiento.id)

        data = EquipoIntegranteUpdate(
            apodo=integrante.apodo, movimientos=movimiento_ids
        )
        self.integrante_repository.update(equipo_id, integrante.id, data)
        return new_movimiento

    def update_integrante(
        self, equipo_id: int, integrante_id: int, data: EquipoIntegranteUpdate
    ) -> Integrante:
        integrante = self.get_integrante(equipo_id, integrante_id)

        pokemon_movimiento_ids = self.pokemon_repository.get_unique_movimiento_ids(
            integrante.pokemon_id
        )

        for movimiento_id in data.movimientos:
            if movimiento_id not in pokemon_movimiento_ids:
                raise InvalidPokemonMovimiento

        return self.integrante_repository.update(equipo_id, integrante.id, data)

    def delete_integrante(self, equipo_id: int, integrante_id: int) -> Integrante:
        integrante = self.get_integrante(equipo_id, integrante_id)
        return self.integrante_repository.delete(equipo_id, integrante.id)
