from __future__ import annotations
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field


class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    year: Optional[int] = None
    actor_ids: List[UUID] = Field(default_factory=list)
    director_id: Optional[UUID] = None
    genre_ids: List[UUID] = Field(default_factory=list)


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class MovieInDB(MovieBase):
    id: UUID


class Movie(MovieInDB):
    pass
