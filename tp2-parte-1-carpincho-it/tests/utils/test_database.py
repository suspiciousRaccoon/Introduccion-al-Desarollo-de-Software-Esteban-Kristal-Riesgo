from fastapi import FastAPI

from app.utils.database import init_database


def test_init_database():
    app = FastAPI()
    init_database(app)
    assert app.state.database
