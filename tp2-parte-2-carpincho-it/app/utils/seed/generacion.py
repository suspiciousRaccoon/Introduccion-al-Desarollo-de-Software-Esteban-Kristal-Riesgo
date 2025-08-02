import csv
from typing import Any

from app.pokemon.models.generacion import Generacion
from app.utils.constants import GENERATION_NAMES, LOCALE_CODE


def load_generaciones(database: dict[str, Any]):
    database["generaciones"] = get_generaciones()


def get_generaciones():
    with open(GENERATION_NAMES, newline="") as type_names:
        generations = []

        generation_reader = csv.DictReader(type_names)
        for g_row in generation_reader:
            if g_row["local_language_id"] == LOCALE_CODE:
                generations.append(
                    Generacion(id=g_row["generation_id"], nombre=g_row["name"])
                )

        return generations
