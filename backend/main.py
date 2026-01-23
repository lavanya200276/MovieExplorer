from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn

import crud
import schemas
import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Movie Explorer API",
    description="API for exploring movies, actors, directors, and genres",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/movies/", response_model=List[schemas.Movie])
def read_movies(
    skip: int = 0,
    limit: int = Query(default=500, le=500),
    genre_id: Optional[int] = None,
    director_id: Optional[int] = None,
    actor_id: Optional[int] = None,
    release_year: Optional[int] = None,
    search: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    """Get movies with optional filtering by genre, director, actor, release year, or search term"""
    movies = crud.get_movies(
        db, skip=skip, limit=limit, genre_id=genre_id, director_id=director_id,
        actor_id=actor_id, release_year=release_year, search=search
    )
    return movies

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(database.get_db)):
    """Get a specific movie by ID"""
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(database.get_db)):
    """Create a new movie"""
    return crud.create_movie(db=db, movie=movie)

# Actor endpoints
@app.get("/actors/", response_model=List[schemas.Actor])
def read_actors(
    skip: int = 0,
    limit: int = Query(default=100, le=100),
    search: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    """Get actors with optional search"""
    actors = crud.get_actors(db, skip=skip, limit=limit, search=search)
    return actors

@app.get("/actors/{actor_id}", response_model=schemas.Actor)
def read_actor(actor_id: int, db: Session = Depends(database.get_db)):
    """Get a specific actor by ID"""
    db_actor = crud.get_actor(db, actor_id=actor_id)
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor

@app.post("/actors/", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(database.get_db)):
    """Create a new actor"""
    return crud.create_actor(db=db, actor=actor)

# Director endpoints
@app.get("/directors/", response_model=List[schemas.Director])
def read_directors(
    skip: int = 0,
    limit: int = Query(default=100, le=100),
    search: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    """Get directors with optional search"""
    directors = crud.get_directors(db, skip=skip, limit=limit, search=search)
    return directors

@app.get("/directors/{director_id}", response_model=schemas.Director)
def read_director(director_id: int, db: Session = Depends(database.get_db)):
    """Get a specific director by ID"""
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director

@app.post("/directors/", response_model=schemas.Director)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(database.get_db)):
    """Create a new director"""
    return crud.create_director(db=db, director=director)

# Genre endpoints
@app.get("/genres/", response_model=List[schemas.Genre])
def read_genres(
    skip: int = 0,
    limit: int = Query(default=100, le=100),
    db: Session = Depends(database.get_db)
):
    """Get all genres"""
    genres = crud.get_genres(db, skip=skip, limit=limit)
    return genres

@app.get("/genres/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(database.get_db)):
    """Get a specific genre by ID"""
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@app.post("/genres/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(database.get_db)):
    """Create a new genre"""
    return crud.create_genre(db=db, genre=genre)

@app.get("/")
def read_root():
    return {"message": "Welcome to Movie Explorer API", "docs": "/docs"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
