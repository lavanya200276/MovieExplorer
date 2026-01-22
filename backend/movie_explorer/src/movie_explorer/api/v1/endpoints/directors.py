from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException

from movie_explorer.schemas.director import Director, DirectorCreate, DirectorUpdate
from movie_explorer.services.director_service import (
    list_directors,
    get_director,
    create_director,
    update_director,
    delete_director,
)

router = APIRouter(prefix="/directors", tags=["directors"])


@router.get("/", response_model=List[Director])
async def read_directors():
    return list_directors()


@router.post("/", response_model=Director, status_code=201)
async def create_new_director(payload: DirectorCreate):
    return create_director(payload)


@router.get("/{director_id}", response_model=Director)
async def read_director(director_id: UUID):
    director = get_director(director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director


@router.put("/{director_id}", response_model=Director)
async def replace_director(director_id: UUID, payload: DirectorUpdate):
    director = update_director(director_id, payload)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director


@router.delete("/{director_id}", status_code=204)
async def remove_director(director_id: UUID):
    deleted = delete_director(director_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Director not found")
    return None
