from sqlmodel import Session
from app.pokemon.service.tipo import TipoService


class TestTiposService:
    def test_tipo_service_get_all(self, session: Session):
        service = TipoService(session)
        tipos = service.get_all()
        assert all(t.id for t in tipos)
