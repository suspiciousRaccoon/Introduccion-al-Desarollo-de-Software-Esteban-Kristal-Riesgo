from typing import Any

from app.pokemon.models.generacion import Generacion
from app.pokemon.repository.generacion import GeneracionRepository
from app.utils.types import Database


class GeneracionService:
    def __init__(self, database: Database):
        self.database = database
        self.repository = GeneracionRepository(database)

    def get_generations(self) -> list[Generacion]:
        return self.repository.get_all()
