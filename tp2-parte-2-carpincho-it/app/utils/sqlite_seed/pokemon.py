import csv
from collections import defaultdict

from sqlmodel import Session, select

from app.pokemon.models.entity.generacion import Generacion
from app.pokemon.models.entity.movimiento import Movimiento
from app.pokemon.models.entity.pokemon import Evolucion, Habilidad, Pokemon
from app.pokemon.models.entity.tipo import Tipo
from app.pokemon.models.entity.estadistica import Estadistica


from app.utils.constants import (
    POKEMON,
    POKEMON_ABILITIES,
    POKEMON_EVOLUTIONS,
    POKEMON_GENERATION_FILEPATH,
    POKEMON_MOVES,
    POKEMON_STATS,
    POKEMON_TYPES,
)
from app.utils.images import get_pokemon_image_url


def load_pokemons(session: Session) -> None:
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
            for generacion_id in generaciones_ids:
                generacion = session.get(Generacion, generacion_id)
                generaciones_pokemon.append(generacion)

            pokemon = Pokemon(
                id=pokemon_id,
                nombre=row["identifier"],
                altura=row["height"],
                peso=row["weight"],
                generaciones=generaciones_pokemon,
                tipos=[],
                habilidades=[],
                estadisticas=None,
                evoluciones=[],
                movimientos_huevo=[],
                movimientos_nivel=[],
                movimientos_maquina=[],
            )

            session.add(pokemon)
    session.commit()


def load_pokemon_tipos(session: Session) -> None:
    """
    `load_tipos`, `load_debilidades`, `load_pokemon` must be called before this
    """

    pokemon_id_type_ids: dict[int, list[int]] = defaultdict(list)
    with open(POKEMON_TYPES, newline="") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            pokemon_id_type_ids[int(row["pokemon_id"])].append(int(row["type_id"]))

    for pokemon_id, pokemon_type_ids in pokemon_id_type_ids.items():
        pokemon = session.get(Pokemon, pokemon_id)
        # needed due to some asshole putting ids like 10001 in the file
        if pokemon:
            statement = select(Tipo).where(Tipo.id.in_(pokemon_type_ids))
            tipos = session.exec(statement).all()

            pokemon.tipos.extend(tipos)
            session.add(pokemon)

    session.commit()


def load_pokemon_habilidades(session: Session) -> None:
    """
    `load_habilidades` and `load_pokemon` must be called before this
    """
    pokemon_habiilidades: dict[int, list[int]] = defaultdict(list)
    habilidades = {}

    with open(POKEMON_ABILITIES, newline="") as abilities:
        csv_reader = csv.DictReader(abilities)
        for row in csv_reader:
            pokemon_habiilidades[int(row["pokemon_id"])].append(int(row["ability_id"]))

    for pokemon_id, habilidad_ids in pokemon_habiilidades.items():
        pokemon = session.get(Pokemon, pokemon_id)
        # needed due to some asshole putting ids like 10001 in the file
        if pokemon:
            statement = select(Habilidad).where(Habilidad.id.in_(habilidad_ids))

            habilidades = session.exec(statement).all()
            pokemon.habilidades.extend(habilidades)
            session.add(pokemon)

    session.commit()


def load_pokemon_estadisticas(session: Session) -> None:
    """
    `load_pokemon` must be called before this
    """

    pokemon_stats: dict[int, dict[int, int]] = defaultdict(dict)

    with open(POKEMON_STATS, newline="") as stats_file:
        csv_reader = csv.DictReader(stats_file)
        for row in csv_reader:
            pokemon_id = int(row["pokemon_id"])
            stat_id = int(row["stat_id"])
            base_stat = int(row["base_stat"])
            pokemon_stats[pokemon_id][stat_id] = base_stat

    for pokemon_id, stats in pokemon_stats.items():
        poke_stats = Estadistica(
            puntos_de_golpe=stats.get(1, 0),
            ataque=stats.get(2, 0),
            defensa=stats.get(3, 0),
            ataque_especial=stats.get(4, 0),
            defensa_especial=stats.get(5, 0),
            velocidad=stats.get(6, 0),
        )

        pokemon = session.get(Pokemon, pokemon_id)
        # needed due to some asshole putting ids like 10001 in the file
        if pokemon:
            pokemon.estadisticas = poke_stats
            session.add(pokemon)

    session.commit()


def load_pokemon_evoluciones(session: Session) -> None:
    """
    `load_pokemon` must be called before this
    """

    # we use a list because a pokemon can have multiple evolutions
    # at the same time, see eevee
    evolution_ids: dict[int, list[int]] = defaultdict(list)
    with open(POKEMON_EVOLUTIONS, newline="") as evolutions_file:
        csv_reader = csv.DictReader(evolutions_file)
        for row in csv_reader:
            pokemon_id = int(row["id"])
            evolution_id = int(row["evolution_id"])
            evolution_ids[pokemon_id].append(evolution_id)

    for pokemon_id, poke_evo_ids in evolution_ids.items():
        if len(poke_evo_ids) > 0:
            pokemon = session.get(Pokemon, pokemon_id)
            # needed due to some asshole putting ids like 10001 in the files
            if pokemon:
                statement = select(Pokemon).where(Pokemon.id.in_(poke_evo_ids))
                evo_pokes = session.exec(statement).all()
                evos = []

                for evo_poke in evo_pokes:
                    evo = Evolucion(
                        id=evo_poke.id,
                        pokemon_id=pokemon_id,
                        nombre=evo_poke.nombre,
                    )
                    evos.append(evo)

                if len(evos) > 0:
                    pokemon.evoluciones.extend(evos)
                    session.add(pokemon)

    session.commit()


def load_pokemon_movimientos(session: Session) -> None:
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

    for pokemon_id, movement_ids in movimientos_egg.items():
        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon:
            statement = select(Movimiento).where(Movimiento.id.in_(movement_ids))
            movimientos = session.exec(statement).all()

            pokemon.movimientos_huevo.extend(movimientos)

            session.add(pokemon)

    session.commit()

    for pokemon_id, movement_ids in movimientos_machine.items():
        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon:
            statement = select(Movimiento).where(Movimiento.id.in_(movement_ids))
            movimientos = session.exec(statement).all()

            pokemon.movimientos_maquina.extend(movimientos)

            session.add(pokemon)

    session.commit()

    for pokemon_id, movement_ids in movimientos_level.items():
        pokemon = session.get(Pokemon, pokemon_id)

        if pokemon:
            statement = select(Movimiento).where(Movimiento.id.in_(movement_ids))
            movimientos = session.exec(statement).all()

            pokemon.movimientos_nivel.extend(movimientos)

            session.add(pokemon)

    session.commit()
