import csv
from typing import Any

from app.pokemon.models.movimiento import Movimiento
from app.utils.constants import (
    LOCALE_CODE,
    MOVE_DAMAGE_CLASS_PROSE,
    MOVE_EFFECT_PROSE,
    MOVE_NAMES,
    MOVES,
)


def load_movimientos(database: dict[str, Any]) -> None:
    movement_effects = {}
    with open(MOVE_EFFECT_PROSE, newline="") as move_effects:
        move_effect_reader = csv.DictReader(move_effects)
        for m_row in move_effect_reader:
            movement_effects[m_row["move_effect_id"]] = m_row["short_effect"]

    movement_categories = {}
    with open(MOVE_DAMAGE_CLASS_PROSE, newline="") as file:
        move_category_reader = csv.DictReader(file)
        for row in move_category_reader:
            if row["local_language_id"] == LOCALE_CODE:
                movement_categories[row["move_damage_class_id"]] = row["name"]

    movement_names = {}
    with open(MOVE_NAMES, newline="") as file:
        move_names_reader = csv.DictReader(file)
        for row in move_names_reader:
            if row["local_language_id"] == LOCALE_CODE:
                movement_names[row["move_id"]] = row["name"]

    movimientos = []
    with open(MOVES) as movements_file:
        csv_reader = csv.DictReader(movements_file)
        for row in csv_reader:
            if row["power"].isnumeric():
                potencia = int(row["power"])
            else:
                potencia = 0

            if row["accuracy"].isnumeric():
                precision = int(row["accuracy"])
            else:
                precision = 0

            if row["pp"].isnumeric():
                pp = int(row["pp"])
            else:
                pp = 0

            # reemplazar por el metodo del repository cuando este listo
            for generacion in database["generaciones"]:
                if generacion.id == int(row["generation_id"]):
                    movimiento_generacion = generacion

            # reemplazar por el metodo del repository cuando este listo
            for tipo in database["tipos"]:
                if tipo.id == int(row["type_id"]):
                    movimiento_tipo = tipo

            movimientos.append(
                Movimiento(
                    id=int(row["id"]),
                    nombre=movement_names.get(row["id"]),
                    generacion=movimiento_generacion,
                    tipo=movimiento_tipo,
                    categoria=movement_categories.get(row["damage_class_id"], ""),
                    potencia=potencia,
                    precision=precision,
                    puntos_de_poder=pp,
                    efecto=movement_effects.get(row["effect_id"], ""),
                    pokemon_por_huevo=[],
                    pokemon_por_maquina=[],
                    pokemon_por_nivel=[],
                )
            )
    database["movimientos"] = movimientos
