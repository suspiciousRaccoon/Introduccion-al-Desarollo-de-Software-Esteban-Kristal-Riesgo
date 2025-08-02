import csv
from sqlmodel import Session
from app.pokemon.models.entity.pokemon import Habilidad
from app.utils.constants import ABILITY_NAMES, LOCALE_CODE


def load_habilidades(session: Session) -> None:
    with open(ABILITY_NAMES, newline="") as abilities:
        csv_reader = csv.DictReader(abilities)
        for row in csv_reader:
            habilidad_id = int(row["ability_id"])
            if row["local_language_id"] == LOCALE_CODE:
                habilidad = Habilidad(id=habilidad_id, nombre=row["name"])
                session.add(habilidad)
    session.commit()
