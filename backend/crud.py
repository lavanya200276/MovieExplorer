from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
import database
import schemas

def get_movie(db: Session, movie_id: int):
    return db.query(database.Movie).filter(database.Movie.id == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, genre_id: Optional[int] = None, 
               director_id: Optional[int] = None, actor_id: Optional[int] = None, 
               release_year: Optional[int] = None, search: Optional[str] = None):
    query = db.query(database.Movie)
    
    if genre_id:
        query = query.filter(database.Movie.genres.any(id=genre_id))
    
    if director_id:
        query = query.filter(database.Movie.director_id == director_id)
    
    if actor_id:
        query = query.filter(database.Movie.actors.any(id=actor_id))
    
    if release_year:
        query = query.filter(database.Movie.release_year == release_year)
    
    if search:
        query = query.filter(
            or_(
                database.Movie.title.contains(search),
                database.Movie.description.contains(search)
            )
        )
    
    return query.offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = database.Movie(
        title=movie.title,
        release_year=movie.release_year,
        description=movie.description,
        poster_url=movie.poster_url,
        director_id=movie.director_id
    )
    
    # Add actors
    if movie.actor_ids:
        actors = db.query(database.Actor).filter(database.Actor.id.in_(movie.actor_ids)).all()
        db_movie.actors = actors
    
    # Add genres
    if movie.genre_ids:
        genres = db.query(database.Genre).filter(database.Genre.id.in_(movie.genre_ids)).all()
        db_movie.genres = genres
    
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_actor(db: Session, actor_id: int):
    return db.query(database.Actor).filter(database.Actor.id == actor_id).first()

def get_actors(db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
    query = db.query(database.Actor)
    
    if search:
        query = query.filter(database.Actor.name.contains(search))
    
    return query.offset(skip).limit(limit).all()

def create_actor(db: Session, actor: schemas.ActorCreate):
    db_actor = database.Actor(**actor.dict())
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor

def get_director(db: Session, director_id: int):
    return db.query(database.Director).filter(database.Director.id == director_id).first()

def get_directors(db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
    query = db.query(database.Director)
    
    if search:
        query = query.filter(database.Director.name.contains(search))
    
    return query.offset(skip).limit(limit).all()

def create_director(db: Session, director: schemas.DirectorCreate):
    db_director = database.Director(**director.dict())
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director

def get_genre(db: Session, genre_id: int):
    return db.query(database.Genre).filter(database.Genre.id == genre_id).first()

def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.Genre).offset(skip).limit(limit).all()

def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = database.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre
