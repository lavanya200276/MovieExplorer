from sqlalchemy.orm import Session
import database
from datetime import date

def complete_100_movies():
    db = Session(bind=database.engine)
    
    try:
        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}

        surender_reddy = database.Director(
            name="Surender Reddy",
            birth_date=date(1975, 8, 10),
            bio="Race Gurram and Kick director"
        )
        db.add(surender_reddy)
        db.commit()
        
        directors = {director.name: director for director in db.query(database.Director).all()}
        
        final_telugu_movie = {
            "title": "Race Gurram",
            "release_year": 2014,
            "description": "Two brothers with contrasting personalities.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTU3ZWY4ZTItZjVhYy00NzgyLWI2MDQtNjNiYzQ3NjkzNGI4XkEyXkFqcGdeQXVyNjE2NTgxOTE@._V1_.jpg",
            "director_name": "Surender Reddy",
            "actor_names": ["Allu Arjun", "Shruti Haasan"],
            "genre_names": ["Action", "Comedy"]
        }
        
        director = directors.get(final_telugu_movie["director_name"])
        
        movie = database.Movie(
            title=final_telugu_movie["title"],
            release_year=final_telugu_movie["release_year"],
            description=final_telugu_movie["description"],
            poster_url=final_telugu_movie["poster_url"],
            director_id=director.id
        )
        db.add(movie)
        db.flush()
        
        # Add actors
        for actor_name in final_telugu_movie["actor_names"]:
            actor = actors.get(actor_name)
            if actor:
                movie.actors.append(actor)
        
        # Add genres
        for genre_name in final_telugu_movie["genre_names"]:
            genre = genres.get(genre_name)
            if genre:
                movie.genres.append(genre)
        
        db.commit()
        
        # Final count
        total_movies = db.query(database.Movie).count()

        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    complete_100_movies()
