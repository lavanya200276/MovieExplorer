from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException

from movie_explorer.schemas.actor import Actor, ActorCreate, ActorUpdate
from movie_explorer.services.actor_service import (
    list_actors,
    get_actor,
    create_actor,
    update_actor,
    delete_actor,
)

router = APIRouter(prefix="/actors", tags=["actors"])


@router.get("/", response_model=List[Actor])
async def read_actors():
    return list_actors()


@router.post("/", response_model=Actor, status_code=201)
async def create_new_actor(payload: ActorCreate):
    return create_actor(payload)


@router.get("/{actor_id}", response_model=Actor)
async def read_actor(actor_id: UUID):
    actor = get_actor(actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor


@router.put("/{actor_id}", response_model=Actor)
async def replace_actor(actor_id: UUID, payload: ActorUpdate):
    actor = update_actor(actor_id, payload)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor


@router.delete("/{actor_id}", status_code=204)
async def remove_actor(actor_id: UUID):
    deleted = delete_actor(actor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Actor not found")
    return None
