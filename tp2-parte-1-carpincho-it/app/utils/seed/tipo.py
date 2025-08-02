import csv
from typing import Any

from app.pokemon.models.tipo import Tipo
from app.utils.constants import LOCALE_CODE, TYPE_NAMES


def load_tipos(database: dict[str, Any]) -> None:
    types = []
    with open(TYPE_NAMES, newline="") as type_names:
        type_reader = csv.DictReader(type_names)
        for t_row in type_reader:
            if t_row["local_language_id"] == LOCALE_CODE:
                types.append(Tipo(id=int(t_row["type_id"]), nombre=t_row["name"]))
    database["tipos"] = types
