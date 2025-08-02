from sqlmodel import Session

from app.pokemon.models.entity.tipo import Tipo
from app.pokemon.repository.tipo import TipoRepository


class TipoService:
    def __init__(self, session: Session):
        self.repository = TipoRepository(session)

    def get_all(self) -> list[Tipo]:
        return self.repository.get_all()
