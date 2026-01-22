from __future__ import annotations
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class GenreBase(BaseModel):
    name: str
    description: Optional[str] = None


class GenreCreate(GenreBase):
    pass


class GenreUpdate(GenreBase):
    pass


class GenreInDB(GenreBase):
    id: UUID


class Genre(GenreInDB):
    pass
