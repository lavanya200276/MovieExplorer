from sqlalchemy.orm import Session
import database
import random

def update_movie_posters():
    db = Session(bind=database.engine)
    
    try:

        movies = db.query(database.Movie).all()
        print(f"Found {len(movies)} movies to update with posters...")
        

        base_poster_urls = [
            "https://picsum.photos/300/450?random=",
            "https://source.unsplash.com/300x450/?movie,poster,",
            "https://loremflickr.com/300/450/movie,cinema,",
        ]

        poster_themes = [
            "action", "drama", "comedy", "thriller", "romance", "adventure", 
            "mystery", "fantasy", "scifi", "horror", "western", "war",
            "biography", "musical", "animation", "documentary"
        ]
        
        updated_count = 0
        
        for i, movie in enumerate(movies):

            service_index = i % len(base_poster_urls)
            theme = poster_themes[i % len(poster_themes)]
            
            if service_index == 0:

                poster_url = f"https://picsum.photos/300/450?random={movie.id + 1000}"
            elif service_index == 1:

                poster_url = f"https://source.unsplash.com/300x450/?{theme},cinema"
            else:

                poster_url = f"https://loremflickr.com/300/450/{theme},movie"

            movie.poster_url = poster_url
            updated_count += 1
            
            if updated_count % 25 == 0:
                print(f"Updated {updated_count} movie posters...")
        

        db.commit()
        for i, movie in enumerate(movies[:5]):
            print(f"- {movie.title}: {movie.poster_url}")
        
    except Exception as e:
        print(f"Error updating movie posters: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_movie_posters()
