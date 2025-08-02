import csv
from collections import defaultdict

from app.pokemon.models.estadistica import Estadistica
from app.pokemon.models.movimiento import MovimientoResumido
from app.pokemon.models.pokemon import Evolucion, Habilidad, Pokemon, PokemonResumido
from app.pokemon.models.tipo import PokemonTipo
from app.utils.constants import (
    ABILITY_NAMES,
    LOCALE_CODE,
    POKEMON,
    POKEMON_ABILITIES,
    POKEMON_EVOLUTIONS,
    POKEMON_GENERATION_FILEPATH,
    POKEMON_MOVES,
    POKEMON_STATS,
    POKEMON_TYPES,
    TYPE_EFFICACY,
)
from app.utils.images import get_pokemon_image_url
from app.utils.types import Database


def load_pokemons(database: Database) -> None:
    pokemon_ids_generaciones = defaultdict(set)
    with open(POKEMON_GENERATION_FILEPATH, newline="") as pokemon_generations:
        generation_reader = csv.DictReader(pokemon_generations)
        for row in generation_reader:
            pokemon_ids_generaciones[int(row["pokemon_id"])].add(
                int(row["generation_id"])
            )

    with open(POKEMON, newline="") as pokemons:
        pokemon_reader = csv.DictReader(pokemons)
        for row in pokemon_reader:
            pokemon_id = int(row["id"])
            generaciones_ids = pokemon_ids_generaciones[pokemon_id]
            generaciones_pokemon = []
            for generacion in database["generaciones"]:
                if generacion.id in generaciones_ids:
                    generaciones_pokemon.append(generacion)

            pokemon = Pokemon(
                id=pokemon_id,
                nombre=row["identifier"],
                imagen=get_pokemon_image_url(pokemon_id),
                altura=row["height"],
                peso=row["weight"],
                generaciones=generaciones_pokemon,
                tipos=None,  # X
                habilidades=None,  # X
                estadisticas=None,  # X
                evoluciones=None,  # X
                movimientos_huevo=None,
                movimientos_nivel=None,
                movimientos_maquina=None,
                # movimientos_huevo=get_pokemon_movements_by_pokemon_id_and_method(pokemon_id, 2),
                # movimientos_nivel=get_pokemon_movements_by_pokemon_id_and_method(pokemon_id, 1),
                # movimientos_maquina=get_pokemon_movements_by_pokemon_id_and_method(pokemon_id, 4),
            )

            database["pokemons"].append(pokemon)


def load_pokemon_tipos(database: Database) -> None:
    pokemon_id_type_ids = defaultdict(list)
    with open(POKEMON_TYPES, newline="") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            pokemon_id_type_ids[int(row["pokemon_id"])].append(int(row["type_id"]))

    type_id_weak_to_type_ids = defaultdict(list)
    with open(TYPE_EFFICACY, newline="") as type_efficacy:
        csv_reader = csv.DictReader(type_efficacy)
        for row in csv_reader:
            if row["damage_factor"] == "200":
                type_id_weak_to_type_ids[int(row["target_type_id"])].append(
                    int(row["damage_type_id"])
                )

    for pokemon in database["pokemons"]:
        pokemon_id = pokemon.id
        pokemon_types = []
        pokemon_type_ids = pokemon_id_type_ids[pokemon_id]
        for pokemon_type_id in pokemon_type_ids:
            weak_ids = type_id_weak_to_type_ids.get(pokemon_type_id)
            weak_types = []
            for weak_id in weak_ids:
                # the first index has id 1
                weak_types.append(database["tipos"][weak_id - 1])
            nombre = database["tipos"][pokemon_type_id - 1].nombre
            pokemon_type = PokemonTipo(
                id=pokemon_type_id, nombre=nombre, debilidades=weak_types
            )
            pokemon_types.append(pokemon_type)
        pokemon.tipos = pokemon_types


def load_pokemon_habilidades(database: Database) -> None:
    habilidad_ids = defaultdict(list)
    habilidades = {}

    with open(POKEMON_ABILITIES, newline="") as abilities:
        csv_reader = csv.DictReader(abilities)
        for row in csv_reader:
            habilidad_ids[int(row["pokemon_id"])].append(int(row["ability_id"]))

    with open(ABILITY_NAMES, newline="") as abilities:
        csv_reader = csv.DictReader(abilities)
        for row in csv_reader:
            habilidad_id = int(row["ability_id"])
            if row["local_language_id"] == LOCALE_CODE:
                habilidades[habilidad_id] = Habilidad(
                    id=habilidad_id, nombre=row["name"]
                )

    for pokemon in database["pokemons"]:
        pokemon_id = pokemon.id
        pokemon_habilidad_ids = habilidad_ids.get(pokemon_id)
        pokemon_habilidades = []
        for pokemon_habilidad_id in pokemon_habilidad_ids:
            pokemon_habilidades.append(habilidades.get(pokemon_habilidad_id))

        pokemon.habilidades = pokemon_habilidades


def load_pokemon_estadisticas(database: Database) -> None:
    pokemon_stats: dict[int, dict[int, int]] = defaultdict(dict)

    with open(POKEMON_STATS, newline="") as stats_file:
        csv_reader = csv.DictReader(stats_file)
        for row in csv_reader:
            pokemon_id = int(row["pokemon_id"])
            stat_id = int(row["stat_id"])
            base_stat = int(row["base_stat"])
            pokemon_stats[pokemon_id][stat_id] = base_stat

    for pokemon in database["pokemons"]:
        stats = pokemon_stats.get(pokemon.id, {})
        pokemon.estadisticas = Estadistica(
            puntos_de_golpe=stats.get(1, 0),
            ataque=stats.get(2, 0),
            defensa=stats.get(3, 0),
            ataque_especial=stats.get(4, 0),
            defensa_especial=stats.get(5, 0),
            velocidad=stats.get(6, 0),
        )


def load_pokemon_evoluciones(database: Database) -> None:
    evolution_ids: dict[int, list[int]] = defaultdict(list)
    with open(POKEMON_EVOLUTIONS, newline="") as evolutions_file:
        csv_reader = csv.DictReader(evolutions_file)
        for row in csv_reader:
            pokemon_id = int(row["id"])
            evolution_id = int(row["evolution_id"])
            evolution_ids[pokemon_id].append(evolution_id)

    for pokemon in database["pokemons"]:
        evoluciones = []
        for evolution_id in evolution_ids.get(pokemon.id, []):
            try:
                evo_pokemon = database["pokemons"][evolution_id - 1]
                evoluciones.append(
                    Evolucion(
                        id=evo_pokemon.id,
                        nombre=evo_pokemon.nombre,
                        imagen=get_pokemon_image_url(evo_pokemon.id),
                    )
                )
            except IndexError:
                # handle incorrect entries
                continue

        pokemon.evoluciones = evoluciones


def load_pokemon_movimientos(database: Database) -> None:
    EGG = 2
    MACHINE = 4
    LEVEL = 1

    movimientos_egg: dict[int, set[int]] = defaultdict(set)
    movimientos_machine: dict[int, set[int]] = defaultdict(set)
    movimientos_level: dict[int, set[int]] = defaultdict(set)

    # loading all this into memory is fine
    with open(POKEMON_MOVES, newline="") as moves_file:
        csv_reader = csv.DictReader(moves_file)
        for row in csv_reader:
            pokemon_id = int(row["pokemon_id"])
            method_id = int(row["pokemon_move_method_id"])
            movimiento_id = int(row["move_id"])

            if method_id == EGG:
                movimientos_egg[pokemon_id].add(movimiento_id)
            elif method_id == MACHINE:
                movimientos_machine[pokemon_id].add(movimiento_id)
            elif method_id == LEVEL:
                movimientos_level[pokemon_id].add(movimiento_id)

    for pokemon in database["pokemons"]:
        pokemon_id = pokemon.id
        movimientos_huevo = []
        for movement_id in movimientos_egg.get(pokemon_id, []):
            movimiento = database["movimientos"][movement_id - 1]
            movimientos_huevo.append(
                MovimientoResumido(
                    id=movimiento.id,
                    nombre=movimiento.nombre,
                    generacion=movimiento.generacion,
                    tipo=movimiento.tipo,
                    categoria=movimiento.categoria,
                    potencia=movimiento.potencia,
                    precision=movimiento.precision,
                    puntos_de_poder=movimiento.puntos_de_poder,
                    efecto=movimiento.efecto,
                )
            )
            database["movimientos"][movement_id - 1].pokemon_por_huevo.append(
                PokemonResumido(**pokemon.model_dump())
            )
        pokemon.movimientos_huevo = movimientos_huevo

        movimientos_maquina = []
        for movement_id in movimientos_machine.get(pokemon_id, []):
            movimiento = database["movimientos"][movement_id - 1]
            movimientos_maquina.append(
                MovimientoResumido(
                    id=movimiento.id,
                    nombre=movimiento.nombre,
                    generacion=movimiento.generacion,
                    tipo=movimiento.tipo,
                    categoria=movimiento.categoria,
                    potencia=movimiento.potencia,
                    precision=movimiento.precision,
                    puntos_de_poder=movimiento.puntos_de_poder,
                    efecto=movimiento.efecto,
                )
            )
            database["movimientos"][movement_id - 1].pokemon_por_maquina.append(
                PokemonResumido(**pokemon.model_dump())
            )
        pokemon.movimientos_maquina = movimientos_maquina

        movimientos_nivel = []
        for movement_id in movimientos_level.get(pokemon_id, []):
            movimiento = database["movimientos"][movement_id - 1]
            movimientos_nivel.append(
                MovimientoResumido(
                    id=movimiento.id,
                    nombre=movimiento.nombre,
                    generacion=movimiento.generacion,
                    tipo=movimiento.tipo,
                    categoria=movimiento.categoria,
                    potencia=movimiento.potencia,
                    precision=movimiento.precision,
                    puntos_de_poder=movimiento.puntos_de_poder,
                    efecto=movimiento.efecto,
                )
            )
            database["movimientos"][movement_id - 1].pokemon_por_nivel.append(
                PokemonResumido(**pokemon.model_dump())
            )
        pokemon.movimientos_nivel = movimientos_nivel
