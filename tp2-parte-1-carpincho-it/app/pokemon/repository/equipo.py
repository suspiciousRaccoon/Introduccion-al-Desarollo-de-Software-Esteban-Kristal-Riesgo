from app.pokemon.models.equipo import (
    Equipo,
    EquipoIntegranteAdd,
    EquipoIntegranteUpdate,
    EquipoResumido,
    EquipoUpsert,
    Integrante,
    PokemonEquipo,
)
from app.pokemon.models.movimiento import MovimientoResumido
from app.utils.types import Database


class EquipoRepository:
    def __init__(self, database: Database):
        self.database = database

    def get(self, equipo_id: int) -> Equipo | None:
        for equipo in self.database["equipos"]:
            if equipo.id == equipo_id:
                return equipo
        return None

    def get_por_nombre(self, nombre: str) -> Equipo | None:
        for equipo in self.database["equipos"]:
            if equipo.nombre.lower() == nombre.lower():
                return equipo

    def get_all(self) -> list[EquipoResumido]:
        return [
            EquipoResumido(
                id=equipo.id,
                nombre=equipo.nombre,
                generacion=equipo.generacion,
                cant_integrantes=len(equipo.integrantes),
            )
            for equipo in self.database["equipos"]
        ]

    def create(self, data: EquipoUpsert) -> Equipo:
        if self.get_por_nombre(data.nombre) is not None:
            raise ValueError("Ya existe un equipo con ese nombre")

        equipo_generacion = None
        for generacion in self.database["generaciones"]:
            if generacion.id == data.id_generacion:
                equipo_generacion = generacion

        if equipo_generacion is None:
            raise ValueError("Generación no encontrada")

        nuevo_id = (
            max([equipo.id for equipo in self.database["equipos"]], default=0) + 1
        )

        nuevo_equipo = Equipo(
            id=nuevo_id,
            nombre=data.nombre,
            generacion=equipo_generacion,
            integrantes=[],
        )
        self.database["equipos"].append(nuevo_equipo)
        return nuevo_equipo

    def update(self, equipo_id: int, data: EquipoUpsert) -> Equipo:
        nuevo_nombre = data.nombre
        nueva_generacion_id = data.id_generacion
        nueva_generacion = None
        equipo_a_actualizar = None

        for generacion in self.database["generaciones"]:
            if generacion.id == nueva_generacion_id:
                nueva_generacion = generacion

        if nueva_generacion is None:
            raise ValueError("Generación inválida")

        for equipo in self.database["equipos"]:
            if equipo.id == equipo_id:
                equipo_a_actualizar = equipo

                for integrante in equipo.integrantes:
                    pertenece_a_generacion = False
                    for generacion in integrante.pokemon.generaciones:
                        if generacion.id <= nueva_generacion_id:
                            pertenece_a_generacion = True
                            break
                    if not pertenece_a_generacion:
                        raise ValueError("El integrante no pertenece a la generacion")

            elif equipo.nombre.lower() == nuevo_nombre.lower():  # differing ids
                raise ValueError("Ya existe un equipo con ese nombre")

        if equipo_a_actualizar is None:
            raise ValueError("Equipo no encontrado")

        equipo_a_actualizar.nombre = nuevo_nombre
        equipo_a_actualizar.generacion = nueva_generacion
        return equipo_a_actualizar

    def delete(self, equipo_id: int) -> Equipo:
        for i, equipo in enumerate(self.database["equipos"]):
            if equipo.id == equipo_id:
                eliminado = self.database["equipos"].pop(i)
                return eliminado
        raise ValueError("Equipo no encontrado")


class IntegranteRepository:
    def __init__(self, database: Database):
        self.database = database

    def get(self, equipo_id: int, integrante_id: int) -> Integrante | None:
        for equipo in self.database["equipos"]:
            if equipo.id == equipo_id:
                for integrante in equipo.integrantes:
                    if integrante.id == integrante_id:
                        return integrante

    def create(self, equipo_id: int, data: EquipoIntegranteAdd) -> Integrante:
        for equipo in self.database["equipos"]:
            if equipo.id == equipo_id:
                if len(equipo.integrantes) >= 6:
                    raise ValueError("El equipo ya tiene 6 integrantes")
                nuevo_id = (
                    max([integrante.id for integrante in equipo.integrantes], default=0)
                    + 1
                )

                integrante_pokemon = None

                for pokemon in self.database["pokemons"]:
                    if pokemon.id == data.id_pokemon:
                        integrante_pokemon = pokemon

                if pokemon is None:
                    raise ValueError("El id_pokemon no es válido")

                pertenece_a_generacion = False
                integrante_generacion = None
                for generacion in integrante_pokemon.generaciones:
                    if generacion.id <= equipo.generacion.id:
                        pertenece_a_generacion = True
                        integrante_generacion = generacion
                        break

                if not pertenece_a_generacion:
                    raise ValueError("El integrante no pertenece a la generacion")

                pokemon_data = integrante_pokemon.model_dump()
                pokemon_data["generacion"] = integrante_generacion

                integrante_pokemon_resumido = PokemonEquipo(**pokemon_data)

                nuevo_integrante = Integrante(
                    id=nuevo_id,
                    apodo=data.apodo,
                    pokemon=integrante_pokemon_resumido,
                    movimientos=[],
                )

                equipo.integrantes.append(nuevo_integrante)
                return nuevo_integrante
        raise ValueError("Equipo no encontrado")

    def update(
        self, equipo_id: int, integrante_id: int, data: EquipoIntegranteUpdate
    ) -> Integrante:
        integrante = self.get(equipo_id, integrante_id)
        if integrante is None:
            raise ValueError("Integrante no encontrado")

        if len(data.movimientos) > 4:
            raise ValueError("Un integrante no puede tener mas de 4 movimientos")
        integrante.apodo = data.apodo

        movimientos = []

        for movimiento_id in data.movimientos:
            for movimiento in self.database["movimientos"]:
                if movimiento.id == movimiento_id:
                    movimientos.append(movimiento)

        if len(movimientos) != len(data.movimientos):
            raise ValueError("Movimiento id no válido")

        movimientos_resumidos = [
            MovimientoResumido(**movimiento.model_dump()) for movimiento in movimientos
        ]

        integrante.movimientos = movimientos_resumidos
        return integrante

    def delete(self, equipo_id: int, integrante_id: int) -> Integrante:
        for equipo in self.database["equipos"]:
            if equipo.id == equipo_id:
                for i, integrante in enumerate(equipo.integrantes):
                    if integrante.id == integrante_id:
                        eliminado = equipo.integrantes.pop(i)
                        return eliminado
        raise ValueError("Integrante no encontrado")
