from sqlalchemy.orm import Session
import database
from datetime import date

def create_60_movies_with_posters():
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
            {"name": "Biographical", "description": "Biographical movies"},
            {"name": "Fantasy", "description": "Fantasy movies"}
        ]
        
        for genre_data in genres_data:
            genre = database.Genre(**genre_data)
            db.add(genre)
        
        # Create directors
        print("🎬 Creating directors...")
        directors_data = [
            # Telugu Directors
            {"name": "S. S. Rajamouli", "birth_date": date(1973, 10, 10), "bio": "Epic filmmaker known for Baahubali series"},
            {"name": "Trivikram Srinivas", "birth_date": date(1971, 11, 7), "bio": "Popular Telugu director"},
            {"name": "Sukumar", "birth_date": date(1970, 1, 11), "bio": "Director of Pushpa and Arya"},
            {"name": "Koratala Siva", "birth_date": date(1975, 6, 15), "bio": "Known for message-oriented films"},
            {"name": "Vamshi Paidipally", "birth_date": date(1978, 7, 27), "bio": "Director of Maharshi"},
            
            # Hindi Directors
            {"name": "Rajkumar Hirani", "birth_date": date(1962, 11, 20), "bio": "3 Idiots, PK director"},
            {"name": "Aamir Khan", "birth_date": date(1965, 3, 14), "bio": "Actor-director"},
            {"name": "Zoya Akhtar", "birth_date": date(1972, 10, 14), "bio": "Zindagi Na Milegi Dobara director"},
            {"name": "Karan Johar", "birth_date": date(1972, 5, 25), "bio": "My Name is Khan director"},
            {"name": "Sanjay Leela Bhansali", "birth_date": date(1963, 2, 24), "bio": "Padmaavat director"},
            
            # English Directors
            {"name": "Christopher Nolan", "birth_date": date(1970, 7, 30), "bio": "Inception, Dark Knight director"},
            {"name": "Steven Spielberg", "birth_date": date(1946, 12, 18), "bio": "Jaws, E.T. director"},
            {"name": "James Cameron", "birth_date": date(1954, 8, 16), "bio": "Titanic, Avatar director"},
            {"name": "Quentin Tarantino", "birth_date": date(1963, 3, 27), "bio": "Pulp Fiction director"},
            {"name": "Martin Scorsese", "birth_date": date(1942, 11, 17), "bio": "Goodfellas director"},
            {"name": "The Russo Brothers", "birth_date": date(1970, 2, 3), "bio": "Avengers directors"},
            {"name": "Ridley Scott", "birth_date": date(1937, 11, 30), "bio": "Gladiator director"},
            {"name": "David Fincher", "birth_date": date(1962, 8, 28), "bio": "Fight Club director"}
        ]
        
        for director_data in directors_data:
            director = database.Director(**director_data)
            db.add(director)
        
        # Create actors
        print("🎭 Creating actors...")
        actors_data = [
            # Telugu Actors
            {"name": "Prabhas", "birth_date": date(1979, 10, 23), "bio": "Baahubali star"},
            {"name": "Mahesh Babu", "birth_date": date(1975, 8, 9), "bio": "Prince of Tollywood"},
            {"name": "Allu Arjun", "birth_date": date(1982, 4, 8), "bio": "Stylish Star"},
            {"name": "Jr. NTR", "birth_date": date(1983, 5, 20), "bio": "Young Tiger"},
            {"name": "Ram Charan", "birth_date": date(1985, 3, 27), "bio": "Mega Power Star"},
            {"name": "Vijay Deverakonda", "birth_date": date(1989, 5, 9), "bio": "Arjun Reddy star"},
            {"name": "Samantha Ruth Prabhu", "birth_date": date(1987, 4, 28), "bio": "Leading actress"},
            {"name": "Anushka Shetty", "birth_date": date(1981, 11, 7), "bio": "Baahubali actress"},
            {"name": "Rashmika Mandanna", "birth_date": date(1996, 4, 5), "bio": "National crush"},
            {"name": "Pooja Hegde", "birth_date": date(1990, 10, 13), "bio": "Pan-Indian actress"},
            
            # Hindi Actors
            {"name": "Aamir Khan", "birth_date": date(1965, 3, 14), "bio": "Mr. Perfectionist"},
            {"name": "Shah Rukh Khan", "birth_date": date(1965, 11, 2), "bio": "King Khan"},
            {"name": "Ranveer Singh", "birth_date": date(1985, 7, 6), "bio": "Energetic actor"},
            {"name": "Deepika Padukone", "birth_date": date(1986, 1, 5), "bio": "Bollywood queen"},
            {"name": "Hrithik Roshan", "birth_date": date(1974, 1, 10), "bio": "Greek God"},
            {"name": "Alia Bhatt", "birth_date": date(1993, 3, 15), "bio": "Student of the Year star"},
            
            # English Actors
            {"name": "Leonardo DiCaprio", "birth_date": date(1974, 11, 11), "bio": "Titanic, Inception star"},
            {"name": "Tom Hanks", "birth_date": date(1956, 7, 9), "bio": "Forrest Gump star"},
            {"name": "Robert Downey Jr.", "birth_date": date(1965, 4, 4), "bio": "Iron Man"},
            {"name": "Scarlett Johansson", "birth_date": date(1984, 11, 22), "bio": "Black Widow"},
            {"name": "Christian Bale", "birth_date": date(1974, 1, 30), "bio": "Batman"},
            {"name": "Brad Pitt", "birth_date": date(1963, 12, 18), "bio": "Fight Club star"},
            {"name": "Morgan Freeman", "birth_date": date(1937, 6, 1), "bio": "Shawshank star"},
            {"name": "Will Smith", "birth_date": date(1968, 9, 25), "bio": "Men in Black star"}
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
        
        # 10 Telugu Movies with authentic posters
        print("🎬 Adding 10 Telugu movies with authentic posters...")
        telugu_movies = [
            {"title": "Baahubali: The Beginning", "release_year": 2015, "description": "A young man learns about his heritage and seeks to avenge his father's death.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYWVlMjVmNzctYzU3Yy00YWM0LWIzMzktOGNiYmZlZDI4MGNkXkEyXkFqcGdeQXVyMTExNDQ2MTI@._V1_.jpg", "director_name": "S. S. Rajamouli", "actor_names": ["Prabhas", "Anushka Shetty"], "genre_names": ["Action", "Drama"]},
            {"title": "Baahubali 2: The Conclusion", "release_year": 2017, "description": "The epic conclusion to the Baahubali saga.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMzQ4Nzc2MjA1NF5BMl5BanBnXkFtZTgwNDE2NDI1MTI@._V1_.jpg", "director_name": "S. S. Rajamouli", "actor_names": ["Prabhas", "Anushka Shetty"], "genre_names": ["Action", "Drama"]},
            {"title": "RRR", "release_year": 2022, "description": "A fictional story of two freedom fighters.", "poster_url": "https://m.media-amazon.com/images/M/MV5BODUwNDNjYzctODUxNy00ZTA2LWIyYTEtMDc5Y2E5ZjBmNTMzXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg", "director_name": "S. S. Rajamouli", "actor_names": ["Jr. NTR", "Ram Charan"], "genre_names": ["Action", "Drama"]},
            {"title": "Pushpa: The Rise", "release_year": 2021, "description": "A laborer's rise in the red sandalwood smuggling syndicate.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNjM2NjU2NDk0NF5BMl5BanBnXkFtZTgwMzQ2NzYwNDM@._V1_.jpg", "director_name": "Sukumar", "actor_names": ["Allu Arjun", "Rashmika Mandanna"], "genre_names": ["Action", "Thriller"]},
            {"title": "Arjun Reddy", "release_year": 2017, "description": "A surgeon's self-destructive journey after heartbreak.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYjM3MDg0NDktNjU3NC00YjhhLWI1NTItN2Q5ZGRhNThhZjgzXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg", "director_name": "Trivikram Srinivas", "actor_names": ["Vijay Deverakonda"], "genre_names": ["Drama", "Romance"]},
            {"title": "Maharshi", "release_year": 2019, "description": "A successful businessman returns to help farmers.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjIwZDMwZTQtYTMwZC00MDQyLTkzNTUtYjA5NGZmM2Q5MGNkXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg", "director_name": "Vamshi Paidipally", "actor_names": ["Mahesh Babu", "Pooja Hegde"], "genre_names": ["Drama", "Family"]},
            {"title": "Bharat Ane Nenu", "release_year": 2018, "description": "A young man becomes Chief Minister and fights corruption.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI1Mzg5MDczOV5BMl5BanBnXkFtZTgwNjIwMDk1NTM@._V1_.jpg", "director_name": "Koratala Siva", "actor_names": ["Mahesh Babu"], "genre_names": ["Drama", "Thriller"]},
            {"title": "Srimanthudu", "release_year": 2015, "description": "A billionaire adopts a village and transforms it.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjE5ODU0NDQ2Nl5BMl5BanBnXkFtZTgwOTU4ODU0NjE@._V1_.jpg", "director_name": "Koratala Siva", "actor_names": ["Mahesh Babu"], "genre_names": ["Drama", "Action"]},
            {"title": "Rangasthalam", "release_year": 2018, "description": "A village story set in the 1980s.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZjJlZDY5ZjEtMWI1ZS00YzM4LTkxMTMtMDU5NDY1YzY1MzExXkEyXkFqcGdeQXVyNjkwOTg4OTA@._V1_.jpg", "director_name": "Sukumar", "actor_names": ["Ram Charan", "Samantha Ruth Prabhu"], "genre_names": ["Drama", "Action"]},
            {"title": "Ala Vaikunthapurramuloo", "release_year": 2020, "description": "A young man discovers his true parentage.", "poster_url": "https://m.media-amazon.com/images/M/MV5BODQzOWFmZTctMzMzYy00ODhlLTllZjYtNDM0MTQ5YmY2Y2E5XkEyXkFqcGdeQXVyMTIyNzY1NzM1._V1_.jpg", "director_name": "Trivikram Srinivas", "actor_names": ["Allu Arjun", "Pooja Hegde"], "genre_names": ["Drama", "Family"]}
        ]
        
        # Add Telugu movies
        for movie_data in telugu_movies:
            director = directors.get(movie_data["director_name"])
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
            
            print(f"✅ Added Telugu: {movie_data['title']} ({movie_data['release_year']})")
        
        # 10 Hindi Movies with authentic posters
        print("\n🎬 Adding 10 Hindi movies with authentic posters...")
        hindi_movies = [
            {"title": "3 Idiots", "release_year": 2009, "description": "Three friends reunite to search for their missing friend.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Aamir Khan"], "genre_names": ["Comedy", "Drama"]},
            {"title": "Dangal", "release_year": 2016, "description": "A wrestler trains his daughters to become world champions.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_.jpg", "director_name": "Aamir Khan", "actor_names": ["Aamir Khan"], "genre_names": ["Biographical", "Drama"]},
            {"title": "PK", "release_year": 2014, "description": "An alien questions religious beliefs on Earth.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTYzOTE2NjkxN15BMl5BanBnXkFtZTgwMDkzMTg0MzE@._V1_.jpg", "director_name": "Rajkumar Hirani", "actor_names": ["Aamir Khan"], "genre_names": ["Comedy", "Drama"]},
            {"title": "Zindagi Na Milegi Dobara", "release_year": 2011, "description": "Three friends go on a bachelor trip to Spain.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjEyOTYyMjI2NV5BMl5BanBnXkFtZTcwNTMxMzM5Ng@@._V1_.jpg", "director_name": "Zoya Akhtar", "actor_names": ["Hrithik Roshan", "Ranveer Singh"], "genre_names": ["Drama", "Comedy"]},
            {"title": "My Name is Khan", "release_year": 2010, "description": "A man with Asperger's syndrome travels across America.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTc1NTUyNzI1OV5BMl5BanBnXkFtZTcwNTMxNDE1Mw@@._V1_.jpg", "director_name": "Karan Johar", "actor_names": ["Shah Rukh Khan"], "genre_names": ["Drama", "Romance"]},
            {"title": "Gully Boy", "release_year": 2019, "description": "A street rapper from Mumbai rises to fame.", "poster_url": "https://m.media-amazon.com/images/M/MV5BM2U2YWU5NWMtOGI2Ni00MTg0LWFhZTItMzcyZjE1ZTJlMzNjXkEyXkFqcGdeQXVyODkzNTgxMDg@._V1_.jpg", "director_name": "Zoya Akhtar", "actor_names": ["Ranveer Singh", "Alia Bhatt"], "genre_names": ["Drama", "Romance"]},
            {"title": "Padmaavat", "release_year": 2018, "description": "The story of Queen Padmavati.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYjQ1NzRhYjYtMWY3ZS00Y2Q0LWJhZGMtM2Y2ODE3NzhhOTU4XkEyXkFqcGdeQXVyMjMwNDgzNjc@._V1_.jpg", "director_name": "Sanjay Leela Bhansali", "actor_names": ["Deepika Padukone", "Ranveer Singh"], "genre_names": ["Drama", "Romance"]},
            {"title": "Bajirao Mastani", "release_year": 2015, "description": "The love story of Bajirao and Mastani.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTg3Mjc2NDE4NF5BMl5BanBnXkFtZTgwNzc1OTA1NjE@._V1_.jpg", "director_name": "Sanjay Leela Bhansali", "actor_names": ["Ranveer Singh", "Deepika Padukone"], "genre_names": ["Romance", "Drama"]},
            {"title": "Lagaan", "release_year": 2001, "description": "Villagers challenge British officers to a cricket match.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTUyMTE2NDcxNV5BMl5BanBnXkFtZTgwOTU3OTU4MDE@._V1_.jpg", "director_name": "Aamir Khan", "actor_names": ["Aamir Khan"], "genre_names": ["Drama", "Action"]},
            {"title": "Dilwale Dulhania Le Jayenge", "release_year": 1995, "description": "Two young Indians fall in love during a trip to Europe.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYzRlMTMwMWEtYjFhYS00NTJhLTk4MmEtYTJmN2YxNzYyNzg2XkEyXkFqcGdeQXVyNjkwMzU2NzI@._V1_.jpg", "director_name": "Karan Johar", "actor_names": ["Shah Rukh Khan"], "genre_names": ["Romance", "Drama"]}
        ]
        
        # Add Hindi movies
        for movie_data in hindi_movies:
            director = directors.get(movie_data["director_name"])
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
            
            print(f"✅ Added Hindi: {movie_data['title']} ({movie_data['release_year']})")
        
        db.commit()
        
        # Count after Telugu and Hindi
        current_count = db.query(database.Movie).count()
        print(f"\n📊 Movies added so far: {current_count}/60")
        print("🎯 Next: Adding 40 English movies...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_60_movies_with_posters()
