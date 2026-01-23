from sqlalchemy.orm import Session
import database
from datetime import date

def add_final_hindi_movie():
    db = Session(bind=database.engine)
    
    try:
        # Get existing objects
        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}

        rakesh_roshan = database.Director(
            name="Rakesh Roshan",
            birth_date=date(1949, 9, 6),
            bio="Krrish series director"
        )
        db.add(rakesh_roshan)
        db.commit()
        
        # Update directors dictionary
        directors = {director.name: director for director in db.query(database.Director).all()}

        final_movie = {
            "title": "Krrish",
            "release_year": 2006,
            "description": "A young man discovers he has superpowers.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BYzQ5NGI2YmItNTQ2OS00ZDJjLTgzMmYtYmY2OTBhODQ4OGFkXkEyXkFqcGdeQXVyNjQ3ODkxMjE@._V1_.jpg",
            "director_name": "Rakesh Roshan",
            "actor_names": ["Hrithik Roshan"],
            "genre_names": ["Action", "Family"]
        }
        
        director = directors.get(final_movie["director_name"])
        
        movie = database.Movie(
            title=final_movie["title"],
            release_year=final_movie["release_year"],
            description=final_movie["description"],
            poster_url=final_movie["poster_url"],
            director_id=director.id
        )
        db.add(movie)
        db.flush()
        
        # Add actors
        for actor_name in final_movie["actor_names"]:
            actor = actors.get(actor_name)
            if actor:
                movie.actors.append(actor)
        
        # Add genres
        for genre_name in final_movie["genre_names"]:
            genre = genres.get(genre_name)
            if genre:
                movie.genres.append(genre)
        
        db.commit()
        
        # Final count
        total_movies = db.query(database.Movie).count()
      
        
    except Exception as e:
        print(f" Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_final_hindi_movie()
