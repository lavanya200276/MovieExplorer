from sqlalchemy.orm import Session
import database
from datetime import date

def add_kannada_movies():
    db = Session(bind=database.engine)
    
    try:
        # Get existing objects for reference
        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        
        # Add Kannada directors
        print("🎬 Creating Kannada directors...")
        kannada_directors_data = [
            {"name": "Rishabh Shetty", "birth_date": date(1983, 7, 7), "bio": "Director of Kantara"},
            {"name": "Rishab Shetty", "birth_date": date(1983, 7, 7), "bio": "Kantara director and actor"},
            {"name": "Preetham Gubbi", "birth_date": date(1984, 1, 1), "bio": "Kannada filmmaker"},
            {"name": "Yogaraj Bhat", "birth_date": date(1972, 10, 8), "bio": "Mungaru Male director"},
            {"name": "Pawan Kumar", "birth_date": date(1980, 1, 1), "bio": "Lucia and U Turn director"}
        ]
        
        for director_data in kannada_directors_data:
            if director_data["name"] not in directors:
                director = database.Director(**director_data)
                db.add(director)
                directors[director_data["name"]] = director
        
        # Add Kannada actors
        print("🎭 Creating Kannada actors...")
        kannada_actors_data = [
            {"name": "Yash", "birth_date": date(1986, 1, 8), "bio": "KGF star"},
            {"name": "Puneeth Rajkumar", "birth_date": date(1975, 3, 17), "bio": "Power Star"},
            {"name": "Sudeep", "birth_date": date(1973, 9, 2), "bio": "Kiccha Sudeep"},
            {"name": "Darshan", "birth_date": date(1977, 2, 16), "bio": "Challenging Star"},
            {"name": "Ganesh", "birth_date": date(1980, 7, 2), "bio": "Golden Star"},
            {"name": "Srinidhi Shetty", "birth_date": date(1992, 10, 21), "bio": "KGF actress"},
            {"name": "Radhika Pandit", "birth_date": date(1984, 3, 7), "bio": "Popular Kannada actress"},
            {"name": "Deepika Padukone", "birth_date": date(1986, 1, 5), "bio": "Bollywood and Kannada star"}
        ]
        
        for actor_data in kannada_actors_data:
            if actor_data["name"] not in actors:
                actor = database.Actor(**actor_data)
                db.add(actor)
                actors[actor_data["name"]] = actor
        
        db.commit()
        print("✅ Kannada cast and crew created successfully!")
        
        # Update dictionaries with new entries
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        
        print("🎬 Adding 10 popular Kannada movies with authentic posters...")
        
        # 10 popular Kannada movies with real posters
        kannada_movies = [
            {
                "title": "KGF: Chapter 1",
                "release_year": 2018,
                "description": "A young man from the Bombay slums rises to power in the gold mines of Karnataka.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjIyOTI0MzU5NV5BMl5BanBnXkFtZTgwMDkzODA5NjM@._V1_.jpg",
                "director_name": "Preetham Gubbi",
                "actor_names": ["Yash", "Srinidhi Shetty"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "KGF: Chapter 2",
                "release_year": 2022,
                "description": "Rocky continues his rise to become the undisputed king of the Kolar Gold Fields.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BZjAzZDllM2ItZGY5Yi00ZDA1LThiOGYtMGI0MmY4ZWMyNzVjXkEyXkFqcGdeQXVyMTE0MzQwMjgz._V1_.jpg",
                "director_name": "Preetham Gubbi", 
                "actor_names": ["Yash", "Srinidhi Shetty"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "Kantara",
                "release_year": 2022,
                "description": "A tribal warrior's conflict with forest officers and local traditions.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5Mi00NGM0LWJiNzQtN2Q5Zjc1MzI1NzZmXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
                "director_name": "Rishabh Shetty",
                "actor_names": ["Rishab Shetty"],
                "genre_names": ["Drama", "Thriller"]
            },
            {
                "title": "Lucia",
                "release_year": 2013,
                "description": "A man with insomnia experiences vivid dreams that blur reality.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMTU3NzIyOTczOV5BMl5BanBnXkFtZTgwMjcwMTA1MDE@._V1_.jpg",
                "director_name": "Pawan Kumar",
                "actor_names": ["Sudeep"],
                "genre_names": ["Thriller", "Drama"]
            },
            {
                "title": "Mungaru Male",
                "release_year": 2006,
                "description": "A love triangle set in the coffee estates of Karnataka.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI1NzQwNzI2MV5BMl5BanBnXkFtZTgwMzYwMDA1MDE@._V1_.jpg",
                "director_name": "Yogaraj Bhat",
                "actor_names": ["Ganesh", "Pooja Hegde"],
                "genre_names": ["Romance", "Drama"]
            },
            {
                "title": "Kirik Party",
                "release_year": 2016,
                "description": "Engineering students navigate college life and friendship.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BNzI5YjRlY2QtZjE2YS00ZGU0LWE3NzktYzNjNWZhZjBjYWY2XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Rishab Shetty",
                "actor_names": ["Samantha Ruth Prabhu"],
                "genre_names": ["Comedy", "Drama"]
            },
            {
                "title": "Ulidavaru Kandanthe",
                "release_year": 2014,
                "description": "Multiple perspectives of the same incident unfold.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjE0Mzc1NjQtNGY5YS00YTkxLWI5NzYtZjE1ZjY5NDM3NDgxXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Rishab Shetty",
                "actor_names": ["Rishab Shetty"],
                "genre_names": ["Drama", "Thriller"]
            },
            {
                "title": "RangiTaranga",
                "release_year": 2015,
                "description": "A mysterious thriller set in the Western Ghats.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI4ODMyOTU2NV5BMl5BanBnXkFtZTgwMjUyMDA1NjE@._V1_.jpg",
                "director_name": "Preetham Gubbi",
                "actor_names": ["Sudeep"],
                "genre_names": ["Mystery", "Thriller"]
            },
            {
                "title": "Godhi Banna Sadharana Mykattu",
                "release_year": 2016,
                "description": "A son searches for his missing father with Alzheimer's.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BNzU2MTgzNDU1M15BMl5BanBnXkFtZTgwMzUwMDA1NjE@._V1_.jpg",
                "director_name": "Pawan Kumar",
                "actor_names": ["Puneeth Rajkumar"],
                "genre_names": ["Drama", "Family"]
            },
            {
                "title": "U Turn",
                "release_year": 2016,
                "description": "A journalist investigates accidents on a flyover.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMzI3OTA5NzI1NV5BMl5BanBnXkFtZTgwMzUwMDA1NjE@._V1_.jpg",
                "director_name": "Pawan Kumar",
                "actor_names": ["Samantha Ruth Prabhu"],
                "genre_names": ["Thriller", "Mystery"]
            }
        ]
        
        # Add the Kannada movies
        for movie_data in kannada_movies:
            director = directors.get(movie_data["director_name"])
            if not director:
                print(f"⚠️ Director not found: {movie_data['director_name']}")
                continue
                
            movie = database.Movie(
                title=movie_data["title"],
                release_year=movie_data["release_year"],
                description=movie_data["description"],
                poster_url=movie_data["poster_url"],
                director_id=director.id
            )
            db.add(movie)
            db.flush()  # Get the movie ID
            
            # Add actors
            for actor_name in movie_data["actor_names"]:
                actor = actors.get(actor_name)
                if actor:
                    movie.actors.append(actor)
            
            # Add genres
            for genre_name in movie_data["genre_names"]:
                genre = genres.get(genre_name)
                if genre:
                    movie.genres.append(genre)
            
            print(f"✅ Added: {movie_data['title']} ({movie_data['release_year']})")
        
        db.commit()
        
        # Count total movies
        total_movies = db.query(database.Movie).count()
        print(f"\n🎬 Successfully completed Kannada section!")
        print(f"📊 Total movies in database: {total_movies}")
        print("🎯 Next step: Add 40 English movies")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_kannada_movies()
