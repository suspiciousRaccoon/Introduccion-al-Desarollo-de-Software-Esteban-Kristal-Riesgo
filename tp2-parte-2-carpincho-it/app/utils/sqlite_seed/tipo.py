from collections import defaultdict
import csv
from typing import Any

from sqlmodel import Session

from app.pokemon.models.entity.tipo import Debilidad, Tipo
from app.utils.constants import LOCALE_CODE, TYPE_EFFICACY, TYPE_NAMES


def load_tipos(session: Session) -> None:
    with open(TYPE_NAMES, newline="") as type_names:
        type_reader = csv.DictReader(type_names)
        for t_row in type_reader:
            if t_row["local_language_id"] == LOCALE_CODE:
                tipo = Tipo(id=int(t_row["type_id"]), nombre=t_row["name"])
                session.add(tipo)

    session.commit()


def load_debilidades(session: Session) -> None:
    with open(TYPE_EFFICACY, newline="") as type_efficacy:
        csv_reader = csv.DictReader(type_efficacy)
        for row in csv_reader:
            if row["damage_factor"] == "200":
                debilidad = Debilidad(
                    tipo_id=int(row["target_type_id"]),
                    debilidad_id=int(row["damage_type_id"]),
                )
                session.add(debilidad)

    session.commit()
