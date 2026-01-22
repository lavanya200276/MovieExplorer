from sqlalchemy.orm import Session
import database
from datetime import date

def clear_and_add_telugu_movies():
    db = Session(bind=database.engine)
    
    try:
        # Clear all existing data
        print("🗑️ Clearing existing database...")
        db.execute(database.movie_actors.delete())
        db.execute(database.movie_genres.delete())
        db.query(database.Movie).delete()
        db.query(database.Actor).delete()
        db.query(database.Director).delete()
        db.query(database.Genre).delete()
        
        # Create genres
        print("🎭 Creating genres...")
        genres_data = [
            {"name": "Action", "description": "Action and adventure movies"},
            {"name": "Drama", "description": "Dramatic movies"},
            {"name": "Romance", "description": "Romantic movies"},
            {"name": "Comedy", "description": "Comedy movies"},
            {"name": "Thriller", "description": "Thriller and suspense movies"},
            {"name": "Family", "description": "Family entertainment movies"},
            {"name": "Biographical", "description": "Biographical movies"}
        ]
        
        for genre_data in genres_data:
            genre = database.Genre(**genre_data)
            db.add(genre)
        
        # Create Telugu directors
        print("🎬 Creating Telugu directors...")
        directors_data = [
            {"name": "S. S. Rajamouli", "birth_date": date(1973, 10, 10), "bio": "Epic filmmaker known for Baahubali series"},
            {"name": "Trivikram Srinivas", "birth_date": date(1971, 11, 7), "bio": "Popular Telugu director"},
            {"name": "Koratala Siva", "birth_date": date(1975, 6, 15), "bio": "Known for message-oriented films"},
            {"name": "Sukumar", "birth_date": date(1970, 1, 11), "bio": "Director of Pushpa and Arya"},
            {"name": "Vamshi Paidipally", "birth_date": date(1978, 7, 27), "bio": "Director of Maharshi"},
            {"name": "Anil Ravipudi", "birth_date": date(1980, 1, 1), "bio": "Comedy entertainer specialist"},
            {"name": "Parasuram", "birth_date": date(1979, 6, 16), "bio": "Director of Sarkaru Vaari Paata"},
            {"name": "Srinu Vaitla", "birth_date": date(1972, 9, 17), "bio": "Comedy director"},
            {"name": "Boyapati Srinu", "birth_date": date(1972, 9, 20), "bio": "Mass action director"},
            {"name": "Harish Shankar", "birth_date": date(1979, 8, 11), "bio": "Commercial filmmaker"}
        ]
        
        for director_data in directors_data:
            director = database.Director(**director_data)
            db.add(director)
        
        # Create Telugu actors
        print("🎭 Creating Telugu actors...")
        actors_data = [
            {"name": "Mahesh Babu", "birth_date": date(1975, 8, 9), "bio": "Prince of Tollywood"},
            {"name": "Allu Arjun", "birth_date": date(1982, 4, 8), "bio": "Stylish Star"},
            {"name": "Prabhas", "birth_date": date(1979, 10, 23), "bio": "Baahubali star"},
            {"name": "Jr. NTR", "birth_date": date(1983, 5, 20), "bio": "Young Tiger"},
            {"name": "Ram Charan", "birth_date": date(1985, 3, 27), "bio": "Mega Power Star"},
            {"name": "Vijay Deverakonda", "birth_date": date(1989, 5, 9), "bio": "Arjun Reddy star"},
            {"name": "Nithiin", "birth_date": date(1983, 3, 30), "bio": "Popular Telugu hero"},
            {"name": "Samantha Ruth Prabhu", "birth_date": date(1987, 4, 28), "bio": "Leading actress"},
            {"name": "Kajal Aggarwal", "birth_date": date(1985, 6, 19), "bio": "Popular actress"},
            {"name": "Pooja Hegde", "birth_date": date(1990, 10, 13), "bio": "Pan-Indian actress"},
            {"name": "Keerthy Suresh", "birth_date": date(1992, 10, 17), "bio": "National Award winner"},
            {"name": "Kiara Advani", "birth_date": date(1992, 7, 31), "bio": "Bollywood and Tollywood star"},
            {"name": "Anushka Shetty", "birth_date": date(1981, 11, 7), "bio": "Baahubali actress"},
            {"name": "Rashmika Mandanna", "birth_date": date(1996, 4, 5), "bio": "National crush"},
            {"name": "Shruti Haasan", "birth_date": date(1986, 1, 28), "bio": "Actress and singer"}
        ]
        
        for actor_data in actors_data:
            actor = database.Actor(**actor_data)
            db.add(actor)
        
        db.commit()
        print("✅ Base data created successfully!")
        
        # Get created objects for reference
        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        
        # Add 30 popular Telugu movies with authentic posters
        print("🎬 Adding 30 Telugu movies with authentic posters...")
        
        movies_data = [
            {
                "title": "Baahubali: The Beginning",
                "release_year": 2015,
                "description": "A young man learns about his heritage and seeks to avenge his father's death.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BYWVlMjVmNzctYzU3Yy00YWM0LWIzMzktOGNiYmZlZDI4MGNkXkEyXkFqcGdeQXVyMTExNDQ2MTI@._V1_.jpg",
                "director_name": "S. S. Rajamouli",
                "actor_names": ["Prabhas", "Anushka Shetty"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "Baahubali 2: The Conclusion",
                "release_year": 2017,
                "description": "The epic conclusion to the Baahubali saga.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMzQ4Nzc2MjA1NF5BMl5BanBnXkFtZTgwNDE2NDI1MTI@._V1_.jpg",
                "director_name": "S. S. Rajamouli",
                "actor_names": ["Prabhas", "Anushka Shetty"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "RRR",
                "release_year": 2022,
                "description": "A fictional story of two freedom fighters.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BODUwNDNjYzctODUxNy00ZTA2LWIyYTEtMDc5Y2E5ZjBmNTMzXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg",
                "director_name": "S. S. Rajamouli",
                "actor_names": ["Jr. NTR", "Ram Charan"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "Pushpa: The Rise",
                "release_year": 2021,
                "description": "A laborer's rise in the red sandalwood smuggling syndicate.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BNjM2NjU2NDk0NF5BMl5BanBnXkFtZTgwMzQ2NzYwNDM@._V1_.jpg",
                "director_name": "Sukumar",
                "actor_names": ["Allu Arjun", "Rashmika Mandanna"],
                "genre_names": ["Action", "Thriller"]
            },
            {
                "title": "Arjun Reddy",
                "release_year": 2017,
                "description": "A surgeon's self-destructive journey after heartbreak.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BYjM3MDg0NDktNjU3NC00YjhhLWI1NTItN2Q5ZGRhNThhZjgzXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Trivikram Srinivas",
                "actor_names": ["Vijay Deverakonda"],
                "genre_names": ["Drama", "Romance"]
            },
            {
                "title": "Sarkaru Vaari Paata",
                "release_year": 2022,
                "description": "A man fights against banking corruption.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5Mi00NGM0LWJiNzQtN2Q5Zjc1MzI1NzZmXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
                "director_name": "Parasuram",
                "actor_names": ["Mahesh Babu", "Keerthy Suresh"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "Maharshi",
                "release_year": 2019,
                "description": "A successful businessman returns to help farmers.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjIwZDMwZTQtYTMwZC00MDQyLTkzNTUtYjA5NGZmM2Q5MGNkXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
                "director_name": "Vamshi Paidipally",
                "actor_names": ["Mahesh Babu", "Pooja Hegde"],
                "genre_names": ["Drama", "Family"]
            },
            {
                "title": "Bharat Ane Nenu",
                "release_year": 2018,
                "description": "A young man becomes Chief Minister and fights corruption.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI1Mzg5MDczOV5BMl5BanBnXkFtZTgwNjIwMDk1NTM@._V1_.jpg",
                "director_name": "Koratala Siva",
                "actor_names": ["Mahesh Babu", "Kiara Advani"],
                "genre_names": ["Drama", "Thriller"]
            },
            {
                "title": "Srimanthudu",
                "release_year": 2015,
                "description": "A billionaire adopts a village and transforms it.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjE5ODU0NDQ2Nl5BMl5BanBnXkFtZTgwOTU4ODU0NjE@._V1_.jpg",
                "director_name": "Koratala Siva",
                "actor_names": ["Mahesh Babu", "Shruti Haasan"],
                "genre_names": ["Drama", "Action"]
            },
            {
                "title": "1: Nenokkadine",
                "release_year": 2014,
                "description": "A rock star searches for his parents' killers.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMTVlNzgzMjktZWJjYy00YzYwLWFjMTUtOGZmZDMzMmM2ZGY2XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Sukumar",
                "actor_names": ["Mahesh Babu"],
                "genre_names": ["Thriller", "Action"]
            }
        ]
        
        # Add movies (first 10)
        for movie_data in movies_data:
            director = directors.get(movie_data["director_name"])
            if not director:
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
        print(f"\n🎬 Successfully added {total_movies} Telugu movies to database!")
        print("📊 Next step: Add remaining 20 Telugu movies, then Kannada, English, and Hindi films")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    clear_and_add_telugu_movies()
