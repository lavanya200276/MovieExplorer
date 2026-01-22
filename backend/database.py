from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Association tables for many-to-many relationships
movie_actors = Table(
    'movie_actors',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

movie_genres = Table(
    'movie_genres',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_year = Column(Integer)
    description = Column(Text)
    poster_url = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))
    
    director = relationship("Director", back_populates="movies")
    actors = relationship("Actor", secondary=movie_actors, back_populates="movies")
    genres = relationship("Genre", secondary=movie_genres, back_populates="movies")

class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(Date)
    bio = Column(Text)
    photo_url = Column(String)
    
    movies = relationship("Movie", secondary=movie_actors, back_populates="actors")

class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(Date)
    bio = Column(Text)
    photo_url = Column(String)
    
    movies = relationship("Movie", back_populates="director")

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    
    movies = relationship("Movie", secondary=movie_genres, back_populates="genres")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
