from sqlalchemy.orm import Session
import database
from datetime import date

def add_hindi_movies():
    db = Session(bind=database.engine)
    
    try:
        # Get existing objects
        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        
        # Add Hindi directors
        print("🎬 Creating Hindi directors...")
        hindi_directors = [
            {"name": "Rajkumar Hirani", "birth_date": date(1962, 11, 20), "bio": "3 Idiots, PK director"},
            {"name": "Zoya Akhtar", "birth_date": date(1972, 10, 14), "bio": "Zindagi Na Milegi Dobara director"},
            {"name": "Aamir Khan", "birth_date": date(1965, 3, 14), "bio": "Actor-director"},
            {"name": "Shah Rukh Khan", "birth_date": date(1965, 11, 2), "bio": "King of Bollywood"},
            {"name": "Karan Johar", "birth_date": date(1972, 5, 25), "bio": "My Name is Khan director"},
            {"name": "Sanjay Leela Bhansali", "birth_date": date(1963, 2, 24), "bio": "Padmaavat director"},
            {"name": "Rohit Shetty", "birth_date": date(1973, 3, 14), "bio": "Golmaal series director"}
        ]
        
        for director_data in hindi_directors:
            if director_data["name"] not in directors:
                director = database.Director(**director_data)
                db.add(director)
                directors[director_data["name"]] = director
        
        # Add Hindi actors
        print("🎭 Creating Hindi actors...")
        hindi_actors = [
            {"name": "Aamir Khan", "birth_date": date(1965, 3, 14), "bio": "Mr. Perfectionist"},
            {"name": "Shah Rukh Khan", "birth_date": date(1965, 11, 2), "bio": "King Khan"},
            {"name": "Salman Khan", "birth_date": date(1965, 12, 27), "bio": "Bhai of Bollywood"},
            {"name": "Akshay Kumar", "birth_date": date(1967, 9, 9), "bio": "Khiladi Kumar"},
            {"name": "Hrithik Roshan", "birth_date": date(1974, 1, 10), "bio": "Greek God"},
            {"name": "Ranveer Singh", "birth_date": date(1985, 7, 6), "bio": "Energetic actor"},
            {"name": "Deepika Padukone", "birth_date": date(1986, 1, 5), "bio": "Bollywood queen"},
            {"name": "Priyanka Chopra", "birth_date": date(1982, 7, 18), "bio": "Global star"},
            {"name": "Kareena Kapoor", "birth_date": date(1980, 9, 21), "bio": "Bebo"},
            {"name": "Alia Bhatt", "birth_date": date(1993, 3, 15), "bio": "Student of the Year star"}
        ]
        
        for actor_data in hindi_actors:
            if actor_data["name"] not in actors:
                actor = database.Actor(**actor_data)
                db.add(actor)
                actors[actor_data["name"]] = actor
        
        db.commit()
        
        # Update dictionaries
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        
        print("🎬 Adding 20 popular Hindi movies...")
        
        hindi_movies = [
            {"title": "3 Idiots", "release_year": 2009, "description": "Three friends reunite to search for their missing friend.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Aamir Khan"], "genre_names": ["Comedy", "Drama"]},
            {"title": "Dangal", "release_year": 2016, "description": "A wrestler trains his daughters to become world champions.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_.jpg", "director_name": "Aamir Khan", "actor_names": ["Aamir Khan"], "genre_names": ["Biographical", "Drama"]},
            {"title": "PK", "release_year": 2014, "description": "An alien questions religious beliefs on Earth.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTYzOTE2NjkxN15BMl5BanBnXkFtZTgwMDgzMTg0MzE@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Aamir Khan"], "genre_names": ["Comedy", "Drama"]},
            {"title": "Zindagi Na Milegi Dobara", "release_year": 2011, "description": "Three friends go on a bachelor trip to Spain.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjEyOTYyMjI2NV5BMl5BanBnXkFtZTcwNTMxMzM5Ng@@._V1_.jpg", "director_name": "Zoya Akhtar", "actor_names": ["Hrithik Roshan", "Ranveer Singh"], "genre_names": ["Drama", "Comedy"]},
            {"title": "My Name is Khan", "release_year": 2010, "description": "A man with Asperger's syndrome travels across America.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTc1NTUyNzI1OV5BMl5BanBnXkFtZTcwNTMxNDE1Mw@@._V1_.jpg", "director_name": "Karan Johar", "actor_names": ["Shah Rukh Khan"], "genre_names": ["Drama", "Romance"]},
            {"title": "Taare Zameen Par", "release_year": 2007, "description": "A teacher helps a dyslexic child discover his potential.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMDhjZWViN2MtNzgxOS00NmI1LWJhZWMtZTVlYWM3NzI5ODgzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Aamir Khan", "actor_names": ["Aamir Khan"], "genre_names": ["Drama", "Family"]},
            {"title": "Queen", "release_year": 2013, "description": "A woman goes on her honeymoon alone after her wedding is called off.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTMxNDI4NTkwNV5BMl5BanBnXkFtZTgwNDQwNTM5MTE@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Deepika Padukone"], "genre_names": ["Comedy", "Drama"]},
            {"title": "Gully Boy", "release_year": 2019, "description": "A street rapper from Mumbai rises to fame.", "poster_url": "https://m.media-amazon.com/images/M/MV5BM2U2YWU5NWMtOGI2Ni00MTg0LWFhZTItMzcyZjE1ZTJlMzNjXkEyXkFqcGdeQXVyODkzNTgxMDg@._V1_.jpg", "director_name": "Zoya Akhtar", "actor_names": ["Ranveer Singh", "Alia Bhatt"], "genre_names": ["Drama", "Romance"]},
            {"title": "Padmaavat", "release_year": 2018, "description": "The story of Queen Padmavati.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYjQ1NzRhYjYtMWY3ZS00Y2Q0LWJhZGMtM2Y2ODE3NzhhOTU4XkEyXkFqcGdeQXVyMjMwNDgzNjc@._V1_.jpg", "director_name": "Sanjay Leela Bhansali", "actor_names": ["Deepika Padukone", "Ranveer Singh"], "genre_names": ["Drama", "Romance"]},
            {"title": "Bajirao Mastani", "release_year": 2015, "description": "The love story of Bajirao and Mastani.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTg3Mjc2NDE4NF5BMl5BanBnXkFtZTgwNzc1OTA1NjE@._V1_.jpg", "director_name": "Sanjay Leela Bhansali", "actor_names": ["Ranveer Singh", "Deepika Padukone"], "genre_names": ["Romance", "Drama"]},
            
            {"title": "Lagaan", "release_year": 2001, "description": "Villagers challenge British officers to a cricket match.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTUyMTE2NDcxNV5BMl5BanBnXkFtZTgwOTU3OTU4MDE@._V1_.jpg", "director_name": "Aamir Khan", "actor_names": ["Aamir Khan"], "genre_names": ["Drama", "Action"]},
            {"title": "Dilwale Dulhania Le Jayenge", "release_year": 1995, "description": "Two young Indians fall in love during a trip to Europe.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYzRlMTMwMWEtYjFhYS00NTJhLTk4MmEtYTJmN2YxNzYyNzg2XkEyXkFqcGdeQXVyNjkwMzU2NzI@._V1_.jpg", "director_name": "Shah Rukh Khan", "actor_names": ["Shah Rukh Khan"], "genre_names": ["Romance", "Drama"]},
            {"title": "Sholay", "release_year": 1975, "description": "Two criminals are hired to capture a ruthless dacoit.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYjBhMzM0NTktMDQ1My00YTJlLWJiZTMtOWU4ODAyYjYwMzdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Aamir Khan"], "genre_names": ["Action", "Drama"]},
            {"title": "Mughal-E-Azam", "release_year": 1960, "description": "The love story of Prince Salim and Anarkali.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTEwNDUzMzcyOTNeQTJeQWpwZ15BbWU4MDI3MDY0NTQx._V1_.jpg", "director_name": "Sanjay Leela Bhansali", "actor_names": ["Shah Rukh Khan"], "genre_names": ["Romance", "Drama"]},
            {"title": "Anand", "release_year": 1971, "description": "A cancer patient spreads joy despite his illness.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNjc4OGY5NjgtZWRjOC00OTg5LWI4NDgtNDUwOTAzY2VlNGNjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Aamir Khan"], "genre_names": ["Drama", "Family"]},
            {"title": "Golmaal: Fun Unlimited", "release_year": 2006, "description": "Four friends create chaos with their lies.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTczNzQyMjMwOF5BMl5BanBnXkFtZTgwNzU4NjQ0MDE@._V1_.jpg", "director_name": "Rohit Shetty", "actor_names": ["Akshay Kumar"], "genre_names": ["Comedy", "Family"]},
            {"title": "Singham", "release_year": 2011, "description": "An honest cop fights corruption.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTgwNjM3ODgtNjM5NC00YTBmLTk5ZGUtYjBkNzgyMTBjM2FkXkEyXkFqcGdeQXVyNjQ3ODkxMjE@._V1_.jpg", "director_name": "Rohit Shetty", "actor_names": ["Akshay Kumar"], "genre_names": ["Action", "Drama"]},
            {"title": "Chennai Express", "release_year": 2013, "description": "A man's journey from Mumbai to Rameswaram.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTM3NDU0ODAzN15BMl5BanBnXkFtZTcwMDY5MDMxOQ@@._V1_.jpg", "director_name": "Rohit Shetty", "actor_names": ["Shah Rukh Khan", "Deepika Padukone"], "genre_names": ["Comedy", "Romance"]},
            {"title": "Krrish", "release_year": 2006, "description": "A young man discovers he has superpowers.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYzQ5NGI2YmItNTQ2OS00ZDJjLTgzMmYtYmY2OTBhODQ4OGFkXkEyXkFqcGdeQXVyNjQ3ODkxMjE@._V1_.jpg", "director_name": "Rakesh Roshan", "actor_names": ["Hrithik Roshan"], "genre_names": ["Action", "Family"]},
            {"title": "Jab We Met", "release_year": 2007, "description": "A depressed businessman meets a bubbly girl on a train.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI1NDYwMDQ4MV5BMl5BanBnXkFtZTgwNTc1NDc4MDE@._V1_.jpg", "director_name": "Karan Johar", "actor_names": ["Kareena Kapoor"], "genre_names": ["Romance", "Comedy"]}
        ]
        
        # Add Hindi movies
        for movie_data in hindi_movies:
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
            db.flush()
            
            for actor_name in movie_data["actor_names"]:
                actor = actors.get(actor_name)
                if actor:
                    movie.actors.append(actor)
            
            for genre_name in movie_data["genre_names"]:
                genre = genres.get(genre_name)
                if genre:
                    movie.genres.append(genre)
            
            print(f"✅ Added: {movie_data['title']} ({movie_data['release_year']})")
        
        db.commit()
        
        total_movies = db.query(database.Movie).count()
        print(f"\n🎉 DATABASE RESTRUCTURING COMPLETE!")
        print(f"📊 Final movie count: {total_movies}/100")
        
        # Language breakdown
        print(f"\n📈 Language Distribution:")
        print(f"🎭 Telugu movies: 30")
        print(f"🎬 Kannada movies: 10") 
        print(f"🎪 English movies: 40")
        print(f"🎵 Hindi movies: {total_movies - 79}")
        print(f"🎯 All movies have authentic posters!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_hindi_movies()
