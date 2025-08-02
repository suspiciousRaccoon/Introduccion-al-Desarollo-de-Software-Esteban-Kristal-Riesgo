import csv
from typing import Any

from sqlmodel import Session

from app.pokemon.models.entity.generacion import Generacion
from app.utils.constants import GENERATION_NAMES, LOCALE_CODE


def load_generaciones(session: Session) -> None:
    generations = get_generaciones()
    session.add_all(generations)
    session.commit()


def get_generaciones() -> list[Generacion]:
    with open(GENERATION_NAMES, newline="") as type_names:
        generations = []

        generation_reader = csv.DictReader(type_names)
        for g_row in generation_reader:
            if g_row["local_language_id"] == LOCALE_CODE:
                generations.append(
                    Generacion(id=g_row["generation_id"], nombre=g_row["name"])
                )

        return generations
