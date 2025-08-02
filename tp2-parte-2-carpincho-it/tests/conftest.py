from typing import Generator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

import alembic
from alembic.config import Config
from app.pokemon.router import router
from fastapi import FastAPI
from app.utils.database import seed_sqlite_database as seed
from app.utils.dependencies import get_session


@pytest.fixture
def sqlite_database() -> Generator[Engine, None, None]:
    """
    Initializes an in-memory sqlite database
    """
    DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)

    yield engine

    SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="session")
def seed_sqlite_database() -> Generator[Engine, None, None]:

    DATABASE_URL = "sqlite:///file:test_db?mode=memory&cache=shared&uri=true"

    # check_same_thread: False is needed due to the client fixture running in another thread
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

    # use migrations to get tables into database
    config = Config("alembic.ini")
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

    with engine.begin() as connection:
        config.attributes["connection"] = connection
        alembic.command.upgrade(config, "head")

    # seed the database
    seed(Session(engine))

    yield engine

    with engine.begin() as connection:
        config.attributes["connection"] = connection
        alembic.command.downgrade(config, "base")


@pytest.fixture
def session(seed_sqlite_database: Engine) -> Generator[Session, None, None]:
    """
    Yields a Session that is rolled back between test runs.
    """
    connection = seed_sqlite_database.connect()

    transaction = connection.begin()

    session = Session(bind=connection)
    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def client(session: Session) -> TestClient:
    # a new app is instanced to avoid seeding of a nonexistant database
    # when importing the real app
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[get_session] = lambda: session
    return TestClient(app)


@pytest.fixture
def mock_db() -> MagicMock:
    return MagicMock
