from app.pokemon.models.entity.generacion import Generacion
from app.utils.repository import BaseRepository


class GeneracionRepository(BaseRepository[Generacion]):
    entity = Generacion
