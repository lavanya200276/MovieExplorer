from typing import Dict, List
from uuid import UUID, uuid4
from movie_explorer.schemas.director import Director, DirectorCreate, DirectorUpdate

_STORE: Dict[UUID, Director] = {}


def list_directors() -> List[Director]:
    return list(_STORE.values())


def get_director(director_id: UUID) -> Director | None:
    return _STORE.get(director_id)


def create_director(payload: DirectorCreate) -> Director:
    director_id = uuid4()
    director = Director(id=director_id, **payload.dict())
    _STORE[director_id] = director
    return director


def update_director(director_id: UUID, payload: DirectorUpdate) -> Director | None:
    if director_id not in _STORE:
        return None
    updated = Director(id=director_id, **payload.dict())
    _STORE[director_id] = updated
    return updated


def delete_director(director_id: UUID) -> bool:
    return _STORE.pop(director_id, None) is not None
