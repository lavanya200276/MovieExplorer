from __future__ import annotations
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ActorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    bio: Optional[str] = None


class ActorCreate(ActorBase):
    pass


class ActorUpdate(ActorBase):
    pass


class ActorInDB(ActorBase):
    id: UUID


class Actor(ActorInDB):
    pass
