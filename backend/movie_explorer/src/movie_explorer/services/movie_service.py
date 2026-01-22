from typing import Dict, List
from uuid import UUID, uuid4
from movie_explorer.schemas.movie import Movie, MovieCreate, MovieUpdate

_STORE: Dict[UUID, Movie] = {}


def list_movies() -> List[Movie]:
    return list(_STORE.values())


def get_movie(movie_id: UUID) -> Movie | None:
    return _STORE.get(movie_id)


def create_movie(payload: MovieCreate) -> Movie:
    movie_id = uuid4()
    movie = Movie(id=movie_id, **payload.dict())
    _STORE[movie_id] = movie
    return movie


def update_movie(movie_id: UUID, payload: MovieUpdate) -> Movie | None:
    if movie_id not in _STORE:
        return None
    updated = Movie(id=movie_id, **payload.dict())
    _STORE[movie_id] = updated
    return updated


def delete_movie(movie_id: UUID) -> bool:
    return _STORE.pop(movie_id, None) is not None
