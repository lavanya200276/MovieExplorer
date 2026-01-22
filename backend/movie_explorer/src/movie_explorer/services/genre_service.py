from typing import Dict, List
from uuid import UUID, uuid4
from movie_explorer.schemas.genre import Genre, GenreCreate, GenreUpdate

_STORE: Dict[UUID, Genre] = {}


def list_genres() -> List[Genre]:
    return list(_STORE.values())


def get_genre(genre_id: UUID) -> Genre | None:
    return _STORE.get(genre_id)


def create_genre(payload: GenreCreate) -> Genre:
    genre_id = uuid4()
    genre = Genre(id=genre_id, **payload.dict())
    _STORE[genre_id] = genre
    return genre


def update_genre(genre_id: UUID, payload: GenreUpdate) -> Genre | None:
    if genre_id not in _STORE:
        return None
    updated = Genre(id=genre_id, **payload.dict())
    _STORE[genre_id] = updated
    return updated


def delete_genre(genre_id: UUID) -> bool:
    return _STORE.pop(genre_id, None) is not None
