from sqlmodel import select

from app.pokemon.models.entity.tipo import Tipo
from app.utils.repository import BaseRepository


class TipoRepository(BaseRepository[Tipo]):
    entity = Tipo

    def get_all(self) -> list[Tipo]:

        result = self.session.exec(select(self.entity))

        return result.all()
