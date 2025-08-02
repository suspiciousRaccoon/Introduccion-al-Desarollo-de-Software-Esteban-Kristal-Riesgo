from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session as SQLModelSession

from app.pokemon.router import router
from app.utils.database import ENGINE, seed_sqlite_database
from app.utils.dependencies import get_session

ORIGINS = [
    "http://localhost:5173",
    "https://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:8080",
    "http://127.0.0.1:5173",
    "https://127.0.0.1:5173",
    "http://127.0.0.1:8080",
    "https://127.0.0.1:8080",
]


def init_app():
    """
    Initializes a FastAPI app instance along with a seeded database
    Assumes a database with applied migrations is present
    """
    app = FastAPI()
    with SQLModelSession(ENGINE) as session:
        seed_sqlite_database(session)

    return app


app = init_app()


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
