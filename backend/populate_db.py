from sqlalchemy.orm import Session
from datetime import date
import database
import crud
import schemas

# Create database tables
database.Base.metadata.create_all(bind=database.engine)

def populate_sample_data():
    db = Session(bind=database.engine)
    
    try:
        genres_data = [
            {"name": "Action", "description": "High-energy films with exciting sequences"},
            {"name": "Comedy", "description": "Films designed to make audiences laugh"},
            {"name": "Drama", "description": "Character-driven stories with emotional depth"},
            {"name": "Sci-Fi", "description": "Science fiction films exploring future concepts"},
            {"name": "Thriller", "description": "Suspenseful films that keep audiences on edge"},
            {"name": "Romance", "description": "Love stories and romantic relationships"},
            {"name": "Horror", "description": "Films designed to frighten and create suspense"},
            {"name": "Animation", "description": "Animated films for all ages"}
        ]
        
        genre_objects = []
        for genre_data in genres_data:
            genre = crud.create_genre(db, schemas.GenreCreate(**genre_data))
            genre_objects.append(genre)
        
        # Create directors
        directors_data = [
            {
                "name": "Christopher Nolan",
                "birth_date": date(1970, 7, 30),
                "bio": "British-American filmmaker known for his cerebral, often nonlinear storytelling",
                "photo_url": "https://example.com/nolan.jpg"
            },
            {
                "name": "Quentin Tarantino",
                "birth_date": date(1963, 3, 27),
                "bio": "American director known for his nonlinear narratives and pop culture references",
                "photo_url": "https://example.com/tarantino.jpg"
            },
            {
                "name": "Greta Gerwig",
                "birth_date": date(1983, 8, 4),
                "bio": "American actress and filmmaker known for coming-of-age stories",
                "photo_url": "https://example.com/gerwig.jpg"
            },
            {
                "name": "Denis Villeneuve",
                "birth_date": date(1967, 10, 3),
                "bio": "Canadian filmmaker known for his thoughtful science fiction films",
                "photo_url": "https://example.com/villeneuve.jpg"
            }
        ]
        
        director_objects = []
        for director_data in directors_data:
            director = crud.create_director(db, schemas.DirectorCreate(**director_data))
            director_objects.append(director)
        
        # Create actors
        actors_data = [
            {
                "name": "Leonardo DiCaprio",
                "birth_date": date(1974, 11, 11),
                "bio": "American actor known for his versatile performances",
                "photo_url": "https://example.com/dicaprio.jpg"
            },
            {
                "name": "Margot Robbie",
                "birth_date": date(1990, 7, 2),
                "bio": "Australian actress and producer",
                "photo_url": "https://example.com/robbie.jpg"
            },
            {
                "name": "Ryan Gosling",
                "birth_date": date(1980, 11, 12),
                "bio": "Canadian actor known for his diverse roles",
                "photo_url": "https://example.com/gosling.jpg"
            },
            {
                "name": "Timothée Chalamet",
                "birth_date": date(1995, 12, 27),
                "bio": "American-French actor known for dramatic roles",
                "photo_url": "https://example.com/chalamet.jpg"
            },
            {
                "name": "Zendaya",
                "birth_date": date(1996, 9, 1),
                "bio": "American actress and singer",
                "photo_url": "https://example.com/zendaya.jpg"
            },
            {
                "name": "Samuel L. Jackson",
                "birth_date": date(1948, 12, 21),
                "bio": "American actor known for his distinctive voice and presence",
                "photo_url": "https://example.com/jackson.jpg"
            },
            {
                "name": "Uma Thurman",
                "birth_date": date(1970, 4, 29),
                "bio": "American actress known for her work with Quentin Tarantino",
                "photo_url": "https://example.com/thurman.jpg"
            },
            {
                "name": "Christian Bale",
                "birth_date": date(1974, 1, 30),
                "bio": "British actor known for his method acting",
                "photo_url": "https://example.com/bale.jpg"
            }
        ]
        
        actor_objects = []
        for actor_data in actors_data:
            actor = crud.create_actor(db, schemas.ActorCreate(**actor_data))
            actor_objects.append(actor)
        
        # Create movies
        movies_data = [
            {
                "title": "Inception",
                "release_year": 2010,
                "description": "A thief who enters the dreams of others to steal their secrets must perform inception.",
                "poster_url": "https://example.com/inception.jpg",
                "director_id": director_objects[0].id,  # Nolan
                "actor_ids": [actor_objects[0].id, actor_objects[7].id],  # DiCaprio, Bale
                "genre_ids": [genre_objects[0].id, genre_objects[3].id, genre_objects[4].id]  # Action, Sci-Fi, Thriller
            },
            {
                "title": "Pulp Fiction",
                "release_year": 1994,
                "description": "Interconnected stories of Los Angeles criminals, fringe players, and underworld figures.",
                "poster_url": "https://example.com/pulpfiction.jpg",
                "director_id": director_objects[1].id,  # Tarantino
                "actor_ids": [actor_objects[5].id, actor_objects[6].id],  # Jackson, Thurman
                "genre_ids": [genre_objects[0].id, genre_objects[2].id, genre_objects[4].id]  # Action, Drama, Thriller
            },
            {
                "title": "Barbie",
                "release_year": 2023,
                "description": "Barbie and Ken are having the time of their lives in the colorful world of Barbie Land.",
                "poster_url": "https://example.com/barbie.jpg",
                "director_id": director_objects[2].id,  # Gerwig
                "actor_ids": [actor_objects[1].id, actor_objects[2].id],  
                "genre_ids": [genre_objects[1].id, genre_objects[5].id]  
            },
            {
                "title": "Dune",
                "release_year": 2021,
                "description": "Paul Atreides leads nomadic tribes in a revolt against the galactic emperor.",
                "poster_url": "https://example.com/dune.jpg",
                "director_id": director_objects[3].id,  
                "actor_ids": [actor_objects[3].id, actor_objects[4].id],  
                "genre_ids": [genre_objects[0].id, genre_objects[2].id, genre_objects[3].id] 
            },
            {
                "title": "The Dark Knight",
                "release_year": 2008,
                "description": "Batman must accept one of the greatest psychological and physical tests.",
                "poster_url": "https://example.com/darkknight.jpg",
                "director_id": director_objects[0].id,  
                "actor_ids": [actor_objects[7].id], 
                "genre_ids": [genre_objects[0].id, genre_objects[2].id, genre_objects[4].id] 
            }
        ]
        
        for movie_data in movies_data:
            crud.create_movie(db, schemas.MovieCreate(**movie_data))
        
        print("Sample data populated successfully!")
        
    except Exception as e:
        print(f"Error populating data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_sample_data()
