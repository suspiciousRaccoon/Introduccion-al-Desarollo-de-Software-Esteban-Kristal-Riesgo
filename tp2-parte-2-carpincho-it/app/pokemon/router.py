from fastapi import APIRouter

from app.pokemon.routes.equipos import router as team_router
from app.pokemon.routes.generaciones import router as generation_router
from app.pokemon.routes.movimientos import router as movement_router
from app.pokemon.routes.pokemons import router as pokemon_router
from app.pokemon.routes.tipo import router as tipo_router

router = APIRouter(prefix="/api")

router.include_router(generation_router, prefix="/generaciones")
router.include_router(movement_router, prefix="/movimientos")
router.include_router(pokemon_router, prefix="/pokemon")
router.include_router(team_router, prefix="/equipos")
router.include_router(tipo_router, prefix="/tipos")


@router.get("/healthcheck", include_in_schema=False)
def healthcheck() -> dict[str, str]:
    return {"status": "ok ฅ^•ﻌ•^ฅ"}
