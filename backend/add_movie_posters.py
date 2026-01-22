from sqlalchemy.orm import Session
import database
import random

def update_movie_posters():
    db = Session(bind=database.engine)
    
    try:
        # Get all movies from database
        movies = db.query(database.Movie).all()
        print(f"Found {len(movies)} movies to update with posters...")
        
        # Create a list of poster image URLs using Lorem Picsum
        # Using movie poster dimensions (300x450) with different seeds for variety
        base_poster_urls = [
            "https://picsum.photos/300/450?random=",
            "https://source.unsplash.com/300x450/?movie,poster,",
            "https://loremflickr.com/300/450/movie,cinema,",
        ]
        
        # Movie poster themes for more realistic images
        poster_themes = [
            "action", "drama", "comedy", "thriller", "romance", "adventure", 
            "mystery", "fantasy", "scifi", "horror", "western", "war",
            "biography", "musical", "animation", "documentary"
        ]
        
        updated_count = 0
        
        for i, movie in enumerate(movies):
            # Generate a unique poster URL for each movie
            # Use different services and themes for variety
            service_index = i % len(base_poster_urls)
            theme = poster_themes[i % len(poster_themes)]
            
            if service_index == 0:
                # Lorem Picsum with seed based on movie ID
                poster_url = f"https://picsum.photos/300/450?random={movie.id + 1000}"
            elif service_index == 1:
                # Unsplash with theme
                poster_url = f"https://source.unsplash.com/300x450/?{theme},cinema"
            else:
                # LoremFlickr with theme
                poster_url = f"https://loremflickr.com/300/450/{theme},movie"
            
            # Update the movie's poster URL
            movie.poster_url = poster_url
            updated_count += 1
            
            if updated_count % 25 == 0:
                print(f"Updated {updated_count} movie posters...")
        
        # Commit all changes
        db.commit()
        print(f"Successfully updated {updated_count} movies with poster images!")
        
        # Show some examples
        print("\nSample poster URLs:")
        for i, movie in enumerate(movies[:5]):
            print(f"- {movie.title}: {movie.poster_url}")
        
    except Exception as e:
        print(f"Error updating movie posters: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_movie_posters()
