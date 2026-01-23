from sqlalchemy.orm import Session
import database
from datetime import date

def add_remaining_telugu_movies():
    db = Session(bind=database.engine)
    
    try:

        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        
        remaining_movies = [
            {
                "title": "A Aa",
                "release_year": 2016,
                "description": "A family entertainer about two contrasting personalities.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMTgxNjA1Njc2MV5BMl5BanBnXkFtZTgwNjE4NzQ2OTE@._V1_.jpg",
                "director_name": "Trivikram Srinivas",
                "actor_names": ["Nithiin", "Samantha Ruth Prabhu"],
                "genre_names": ["Romance", "Family"]
            },
            {
                "title": "Sarileru Neekevvaru",
                "release_year": 2020,
                "description": "A major helps a troubled family while on a mission.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BNzQ3NzU1NjgtMDQ1YS00MjNjLWI2M2QtZTVjZjY5ZDM0YTJjXkEyXkFqcGdeQXVyMTExNDQ2MTI@._V1_.jpg",
                "director_name": "Anil Ravipudi",
                "actor_names": ["Mahesh Babu", "Rashmika Mandanna"],
                "genre_names": ["Action", "Comedy"]
            },
            {
                "title": "Ala Vaikunthapurramuloo",
                "release_year": 2020,
                "description": "A young man discovers his true parentage.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BODQzOWFmZTctMzMzYy00ODhlLTllZjYtNDM0MTQ5YmY2Y2E5XkEyXkFqcGdeQXVyMTIyNzY1NzM1._V1_.jpg",
                "director_name": "Trivikram Srinivas",
                "actor_names": ["Allu Arjun", "Pooja Hegde"],
                "genre_names": ["Drama", "Family"]
            },
            {
                "title": "Rangasthalam",
                "release_year": 2018,
                "description": "A village story set in the 1980s.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BZjJlZDY5ZjEtMWI1ZS00YzM4LTkxMTMtMDU5NDY1YzY1MzExXkEyXkFqcGdeQXVyNjkwOTg4OTA@._V1_.jpg",
                "director_name": "Sukumar",
                "actor_names": ["Ram Charan", "Samantha Ruth Prabhu"],
                "genre_names": ["Drama", "Action"]
            },
            {
                "title": "Mirchi",
                "release_year": 2013,
                "description": "A man tries to unite two feuding families.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjExYTMyMDMtNGJkOS00YWNiLWEzZWYtY2Q3M2U3ZmZmN2RjXkEyXkFqcGdeQXVyNjE2NTgxOTE@._V1_.jpg",
                "director_name": "Koratala Siva",
                "actor_names": ["Prabhas", "Anushka Shetty"],
                "genre_names": ["Action", "Romance"]
            },
            {
                "title": "Dookudu",
                "release_year": 2011,
                "description": "An IPS officer goes undercover to expose corruption.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI2MDU5NTIzMV5BMl5BanBnXkFtZTgwNDQ4OTU0MDE@._V1_.jpg",
                "director_name": "Srinu Vaitla",
                "actor_names": ["Mahesh Babu", "Samantha Ruth Prabhu"],
                "genre_names": ["Action", "Comedy"]
            },
            {
                "title": "Gabbar Singh",
                "release_year": 2012,
                "description": "A police officer fights against local goons.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BOGEzOGM2YjYtNjRhYy00NzJmLWIzYjEtZDYyYTJjMzE5YzY5XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Harish Shankar",
                "actor_names": ["Prabhas", "Shruti Haasan"],
                "genre_names": ["Action", "Comedy"]
            },
            {
                "title": "Temper",
                "release_year": 2015,
                "description": "A corrupt cop transforms into an honest officer.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjE2MTMzODY3NV5BMl5BanBnXkFtZTgwMTY1ODY0NDE@._V1_.jpg",
                "director_name": "Boyapati Srinu",
                "actor_names": ["Jr. NTR", "Kajal Aggarwal"],
                "genre_names": ["Action", "Thriller"]
            },
            {
                "title": "Race Gurram",
                "release_year": 2014,
                "description": "Two brothers with contrasting personalities.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMTU3ZWY4ZTItZjVhYy00NzgyLWI2MDQtNjNiYzQ3NjkzNGI4XkEyXkFqcGdeQXVyNjE2NTgxOTE@._V1_.jpg",
                "director_name": "Surender Reddy",
                "actor_names": ["Allu Arjun", "Shruti Haasan"],
                "genre_names": ["Action", "Comedy"]
            },
            {
                "title": "Janatha Garage",
                "release_year": 2016,
                "description": "A mechanic fights for social justice.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BN2I4MzExZTctN2ZkYS00M2MxLWFjNjktYmU5ZTY5MDI1ZWVlXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Koratala Siva",
                "actor_names": ["Jr. NTR", "Samantha Ruth Prabhu"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "Khaidi No. 150",
                "release_year": 2017,
                "description": "A man fights against corporate agriculture.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI3MjE1NzMtNTU1MS00YzE4LWFhNjktZjUwZjNlOWM2YWU2XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Boyapati Srinu",
                "actor_names": ["Ram Charan", "Kajal Aggarwal"],
                "genre_names": ["Action", "Drama"]
            },
            {
                "title": "Jersey",
                "release_year": 2019,
                "description": "A failed cricketer makes a comeback.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjlmODQzMmItMzY5OS00ZTNiLWJjNDctZWZjYjMzZmJmZWQxXkEyXkFqcGdeQXVyMTExNDQ2MTI@._V1_.jpg",
                "director_name": "Trivikram Srinivas",
                "actor_names": ["Nithiin", "Shruti Haasan"],
                "genre_names": ["Drama", "Biographical"]
            },
            {
                "title": "Fidaa",
                "release_year": 2017,
                "description": "A love story between city and village.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjI5NjEyMzQtMDVkYS00ZGQ5LWE0MjYtNGJkYzNhZTFjMjRkXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Parasuram",
                "actor_names": ["Vijay Deverakonda", "Samantha Ruth Prabhu"],
                "genre_names": ["Romance", "Drama"]
            },
            {
                "title": "Attarintiki Daredi",
                "release_year": 2013,
                "description": "A man tries to reunite his estranged family.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMTU1Njc2MjQ3MF5BMl5BanBnXkFtZTgwNjEyNzQ0MDE@._V1_.jpg",
                "director_name": "Trivikram Srinivas",
                "actor_names": ["Prabhas", "Samantha Ruth Prabhu"],
                "genre_names": ["Comedy", "Family"]
            },
            {
                "title": "Pokiri",
                "release_year": 2006,
                "description": "An undercover cop infiltrates the underworld.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjc0NzQ4OTgtYWY1YS00NzJlLTg5OTYtYjgzMTA4NmI0YzU2XkEyXkFqcGdeQXVyNjE2NTgxOTE@._V1_.jpg",
                "director_name": "Boyapati Srinu",
                "actor_names": ["Mahesh Babu", "Keerthy Suresh"],
                "genre_names": ["Action", "Thriller"]
            },
            {
                "title": "Businessman",
                "release_year": 2012,
                "description": "A young man takes over Mumbai's underworld.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjIwNTQ3MzM5NV5BMl5BanBnXkFtZTgwNzEzMDY1MDE@._V1_.jpg",
                "director_name": "Boyapati Srinu",
                "actor_names": ["Mahesh Babu", "Kajal Aggarwal"],
                "genre_names": ["Action", "Thriller"]
            },
            {
                "title": "Magadheera",
                "release_year": 2009,
                "description": "A reincarnation love story.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BZDRjN2Y4M2ItNDU0NS00ZWRlLTk5ODQtMjczNWM2MTViZjRjXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "S. S. Rajamouli",
                "actor_names": ["Ram Charan", "Kajal Aggarwal"],
                "genre_names": ["Action", "Romance"]
            },
            {
                "title": "Eega",
                "release_year": 2012,
                "description": "A man reincarnated as a fly seeks revenge.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMTYxNDA2MDM2NV5BMl5BanBnXkFtZTcwNTE4OTAyOA@@._V1_.jpg",
                "director_name": "S. S. Rajamouli",
                "actor_names": ["Samantha Ruth Prabhu"],
                "genre_names": ["Fantasy", "Thriller"]
            },
            {
                "title": "Ninnu Kori",
                "release_year": 2017,
                "description": "A romantic drama about love and sacrifice.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjUzZDQzZTMtMmRhYy00ZWNlLWFhN2UtMjY0MzYwMWUxNjA1XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
                "director_name": "Trivikram Srinivas",
                "actor_names": ["Nithiin", "Keerthy Suresh"],
                "genre_names": ["Romance", "Drama"]
            },
            {
                "title": "Tholi Prema",
                "release_year": 2018,
                "description": "A college love story.",
                "poster_url": "https://m.media-amazon.com/images/M/MV5BMjIwOTI0MzE5OF5BMl5BanBnXkFtZTgwNzg4NDY4NDM@._V1_.jpg",
                "director_name": "Parasuram",
                "actor_names": ["Vijay Deverakonda", "Rashmika Mandanna"],
                "genre_names": ["Romance", "Comedy"]
            }
        ]
        

        for movie_data in remaining_movies:
            director = directors.get(movie_data["director_name"])
            if not director:
                print(f" Director not found: {movie_data['director_name']}")
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
            
            print(f" Added: {movie_data['title']} ({movie_data['release_year']})")
        
        db.commit()
        
        # Count total movies
        total_movies = db.query(database.Movie).count()
        
        
    except Exception as e:
        print(f" Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_remaining_telugu_movies()
