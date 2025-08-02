from typing import Any

from sqlmodel import Session

from app.pokemon.models.entity.generacion import Generacion
from app.pokemon.repository.generacion import GeneracionRepository


class GeneracionService:
    def __init__(self, session: Session):
        self.repository = GeneracionRepository(session)

    def get_generations(self) -> list[Generacion]:
        return self.repository.get_all()
