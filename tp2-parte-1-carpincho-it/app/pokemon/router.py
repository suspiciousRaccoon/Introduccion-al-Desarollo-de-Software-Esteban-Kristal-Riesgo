from fastapi import APIRouter
from app.pokemon.routes.generations import router as generation_router
from app.pokemon.routes.movements import router as movement_router
from app.pokemon.routes.pokemons import router as pokemon_router
from app.pokemon.routes.teams import router as team_router

router = APIRouter(prefix="/api")

router.include_router(generation_router, prefix="/generaciones")
router.include_router(movement_router, prefix="/movimientos")
router.include_router(pokemon_router, prefix="/pokemon")
router.include_router(team_router, prefix="/equipos")
