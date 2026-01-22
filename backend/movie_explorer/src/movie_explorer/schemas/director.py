from __future__ import annotations
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class DirectorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    bio: Optional[str] = None


class DirectorCreate(DirectorBase):
    pass


class DirectorUpdate(DirectorBase):
    pass


class DirectorInDB(DirectorBase):
    id: UUID


class Director(DirectorInDB):
    pass
