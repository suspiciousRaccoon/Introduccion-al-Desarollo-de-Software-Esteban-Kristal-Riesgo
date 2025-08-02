from app.pokemon.models.generacion import Generacion
from app.utils.types import Database


class GeneracionRepository:
    def __init__(self, database: Database):
        self.database = database

    def get(self, generacion_id: int) -> Generacion | None:
        for generacion in self.database["generaciones"]:
            if generacion.id == generacion_id:
                return generacion
        return None

    def get_all(self) -> list[Generacion]:
        return self.database["generaciones"]
