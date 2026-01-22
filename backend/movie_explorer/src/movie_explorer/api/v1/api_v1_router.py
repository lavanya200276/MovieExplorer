from fastapi import APIRouter

from movie_explorer.api.v1.endpoints.movie_explorer import router as movie_explorer_router
from movie_explorer.api.v1.endpoints.movies import router as movies_router
from movie_explorer.api.v1.endpoints.actors import router as actors_router
from movie_explorer.api.v1.endpoints.directors import router as directors_router
from movie_explorer.api.v1.endpoints.genres import router as genres_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(movie_explorer_router)
api_v1_router.include_router(movies_router)
api_v1_router.include_router(actors_router)
api_v1_router.include_router(directors_router)
api_v1_router.include_router(genres_router)
