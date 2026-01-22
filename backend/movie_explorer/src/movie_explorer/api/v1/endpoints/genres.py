from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException

from movie_explorer.schemas.genre import Genre, GenreCreate, GenreUpdate
from movie_explorer.services.genre_service import (
    list_genres,
    get_genre,
    create_genre,
    update_genre,
    delete_genre,
)

router = APIRouter(prefix="/genres", tags=["genres"])


@router.get("/", response_model=List[Genre])
async def read_genres():
    return list_genres()


@router.post("/", response_model=Genre, status_code=201)
async def create_new_genre(payload: GenreCreate):
    return create_genre(payload)


@router.get("/{genre_id}", response_model=Genre)
async def read_genre(genre_id: UUID):
    genre = get_genre(genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


@router.put("/{genre_id}", response_model=Genre)
async def replace_genre(genre_id: UUID, payload: GenreUpdate):
    genre = update_genre(genre_id, payload)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


@router.delete("/{genre_id}", status_code=204)
async def remove_genre(genre_id: UUID):
    deleted = delete_genre(genre_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Genre not found")
    return None
