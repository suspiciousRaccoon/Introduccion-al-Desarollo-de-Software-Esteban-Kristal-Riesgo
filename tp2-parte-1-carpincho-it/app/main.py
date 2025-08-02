from fastapi import FastAPI
from app.pokemon.router import router
from app.utils.database import init_database, seed_database


def init_app():
    """
    Initializes a FastAPI app instance along with a seeded database
    """
    app = FastAPI()
    seed_database(init_database(app))
    return app


app = init_app()


@app.get("/healthcheck", include_in_schema=False)
def healthcheck() -> dict[str, str]:
    return {"status": "ok ฅ^•ﻌ•^ฅ"}


app.include_router(router)
