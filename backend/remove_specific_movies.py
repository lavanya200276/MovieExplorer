from sqlalchemy.orm import Session
import database

def remove_specific_movies():
    db = Session(bind=database.engine)
    
    try:
        movies_to_remove = [
            "Baahubali: The Beginning",
            "Baahubali 2: The Conclusion", 
            "Pushpa: The Rise",
            "Arjun Reddy",
            "Maharshi",
            "Bharat Ane Nenu",
            "Srimanthudu",
            "Rangasthalam",
            "Ala Vaikunthapurramuloo",
            "PK",
            "Zindagi Na Milegi Dobara",
            "My Name is Khan",
            "Gully Boy",
            "Padmaavat",
            "Bajirao Mastani",
            "Lagaan",
            "Dilwale Dulhania Le Jayenge",
            "Goodfellas",
            "Top Gun: Maverick"
        ]
     
        removed_count = 0
        for movie_title in movies_to_remove:
            movie = db.query(database.Movie).filter(database.Movie.title == movie_title).first()
            
            if movie:
                db.execute(database.movie_actors.delete().where(database.movie_actors.c.movie_id == movie.id))
                db.execute(database.movie_genres.delete().where(database.movie_genres.c.movie_id == movie.id))

                db.delete(movie)
                removed_count += 1
            else:
                print(f" Not found: {movie_title}")
        
        db.commit()
        
        remaining_movies = db.query(database.Movie).count()
        all_movies = db.query(database.Movie).all()
        for movie in all_movies:
            print(f"- {movie.title} ({movie.release_year})")
    except Exception as e:
        print(f" Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    remove_specific_movies()
