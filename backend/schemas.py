from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class GenreBase(BaseModel):
    name: str
    description: Optional[str] = None

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int

    class Config:
        from_attributes = True

class ActorBase(BaseModel):
    name: str
    birth_date: Optional[date] = None
    bio: Optional[str] = None
    photo_url: Optional[str] = None

class ActorCreate(ActorBase):
    pass

class Actor(ActorBase):
    id: int
    movies: List["MovieSummary"] = []

    class Config:
        from_attributes = True

class DirectorBase(BaseModel):
    name: str
    birth_date: Optional[date] = None
    bio: Optional[str] = None
    photo_url: Optional[str] = None

class DirectorCreate(DirectorBase):
    pass

class Director(DirectorBase):
    id: int
    movies: List["MovieSummary"] = []

    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    title: str
    release_year: Optional[int] = None
    description: Optional[str] = None
    poster_url: Optional[str] = None

class MovieCreate(MovieBase):
    director_id: Optional[int] = None
    actor_ids: List[int] = []
    genre_ids: List[int] = []

class MovieSummary(MovieBase):
    id: int

    class Config:
        from_attributes = True

class Movie(MovieBase):
    id: int
    director: Optional[Director] = None
    actors: List[Actor] = []
    genres: List[Genre] = []

    class Config:
        from_attributes = True
