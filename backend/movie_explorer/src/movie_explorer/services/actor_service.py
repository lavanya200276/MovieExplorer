from typing import Dict, List
from uuid import UUID, uuid4
from movie_explorer.schemas.actor import Actor, ActorCreate, ActorUpdate

_STORE: Dict[UUID, Actor] = {}


def list_actors() -> List[Actor]:
    return list(_STORE.values())


def get_actor(actor_id: UUID) -> Actor | None:
    return _STORE.get(actor_id)


def create_actor(payload: ActorCreate) -> Actor:
    actor_id = uuid4()
    actor = Actor(id=actor_id, **payload.dict())
    _STORE[actor_id] = actor
    return actor


def update_actor(actor_id: UUID, payload: ActorUpdate) -> Actor | None:
    if actor_id not in _STORE:
        return None
    updated = Actor(id=actor_id, **payload.dict())
    _STORE[actor_id] = updated
    return updated


def delete_actor(actor_id: UUID) -> bool:
    return _STORE.pop(actor_id, None) is not None
