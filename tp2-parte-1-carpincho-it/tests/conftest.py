from typing import Any
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.utils.database import Database, create_database, seed_database


@pytest.fixture(scope="session")
def seeded_database() -> Database:
    """
    Creates and seeds a database from csv files in ./data
    """
    database = create_database()
    seed_database(database)
    return database


@pytest.fixture
def database(seeded_database: Database) -> Database:
    """
    Returns a cached `seeded_database` and rolls back mutable entries
    """
    database = seeded_database.copy()

    database["equipos"] = []

    return database


@pytest.fixture
def mock_db() -> MagicMock:
    return MagicMock


@pytest.fixture()
def client(database: Database) -> TestClient:
    app.state.database = database
    # the dependency acceses the apps state, there is no need to override it.
    return TestClient(app)
