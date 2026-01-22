from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException

from movie_explorer.schemas.movie import Movie, MovieCreate, MovieUpdate
from movie_explorer.services.movie_service import (
    list_movies,
    get_movie,
    create_movie,
    update_movie,
    delete_movie,
)

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/", response_model=List[Movie])
async def read_movies():
    return list_movies()


@router.post("/", response_model=Movie, status_code=201)
async def create_new_movie(payload: MovieCreate):
    return create_movie(payload)


@router.get("/{movie_id}", response_model=Movie)
async def read_movie(movie_id: UUID):
    movie = get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.put("/{movie_id}", response_model=Movie)
async def replace_movie(movie_id: UUID, payload: MovieUpdate):
    movie = update_movie(movie_id, payload)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.delete("/{movie_id}", status_code=204)
async def remove_movie(movie_id: UUID):
    deleted = delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return None
