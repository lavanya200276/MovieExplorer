from sqlalchemy.orm import Session
import database

def remove_specific_movies():
    db = Session(bind=database.engine)
    
    try:
        # List of movies to remove
        movies_to_remove = [
            # Telugu movies to remove
            "Baahubali: The Beginning",
            "Baahubali 2: The Conclusion", 
            "Pushpa: The Rise",
            "Arjun Reddy",
            "Maharshi",
            "Bharat Ane Nenu",
            "Srimanthudu",
            "Rangasthalam",
            "Ala Vaikunthapurramuloo",
            
            # Hindi movies to remove
            "PK",
            "Zindagi Na Milegi Dobara",
            "My Name is Khan",
            "Gully Boy",
            "Padmaavat",
            "Bajirao Mastani",
            "Lagaan",
            "Dilwale Dulhania Le Jayenge",
            
            # English movies to remove
            "Goodfellas",
            "Top Gun: Maverick"
        ]
        
        print(f"🗑️ Removing {len(movies_to_remove)} specific movies from database...")
        
        removed_count = 0
        for movie_title in movies_to_remove:
            # Find the movie by title
            movie = db.query(database.Movie).filter(database.Movie.title == movie_title).first()
            
            if movie:
                # Remove associations first
                db.execute(database.movie_actors.delete().where(database.movie_actors.c.movie_id == movie.id))
                db.execute(database.movie_genres.delete().where(database.movie_genres.c.movie_id == movie.id))
                
                # Remove the movie
                db.delete(movie)
                removed_count += 1
                print(f"✅ Removed: {movie_title}")
            else:
                print(f"⚠️ Not found: {movie_title}")
        
        db.commit()
        
        # Check final count
        remaining_movies = db.query(database.Movie).count()
        print(f"\n📊 Movies removed: {removed_count}")
        print(f"📊 Movies remaining: {remaining_movies}")
        
        # Show remaining movies by language
        print(f"\n📋 Remaining movies in database:")
        all_movies = db.query(database.Movie).all()
        for movie in all_movies:
            print(f"- {movie.title} ({movie.release_year})")
        
        print(f"\n✅ Movie removal complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    remove_specific_movies()
