from sqlalchemy.orm import Session
import database
from datetime import date

def add_english_movies():
    db = Session(bind=database.engine)
    
    try:
        # Get existing objects
        genres = {genre.name: genre for genre in db.query(database.Genre).all()}
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}
        

        english_directors = [
            {"name": "Christopher Nolan", "birth_date": date(1970, 7, 30), "bio": "Inception, Dark Knight director"},
            {"name": "Quentin Tarantino", "birth_date": date(1963, 3, 27), "bio": "Pulp Fiction director"},
            {"name": "Martin Scorsese", "birth_date": date(1942, 11, 17), "bio": "Goodfellas director"},
            {"name": "Steven Spielberg", "birth_date": date(1946, 12, 18), "bio": "Jaws, E.T. director"},
            {"name": "James Cameron", "birth_date": date(1954, 8, 16), "bio": "Titanic, Avatar director"},
            {"name": "Ridley Scott", "birth_date": date(1937, 11, 30), "bio": "Gladiator director"},
            {"name": "David Fincher", "birth_date": date(1962, 8, 28), "bio": "Fight Club director"},
            {"name": "The Russo Brothers", "birth_date": date(1970, 2, 3), "bio": "Avengers directors"}
        ]
        
        for director_data in english_directors:
            if director_data["name"] not in directors:
                director = database.Director(**director_data)
                db.add(director)
                directors[director_data["name"]] = director
        

        english_actors = [
            {"name": "Leonardo DiCaprio", "birth_date": date(1974, 11, 11), "bio": "Titanic, Inception star"},
            {"name": "Tom Hanks", "birth_date": date(1956, 7, 9), "bio": "Forrest Gump star"},
            {"name": "Robert Downey Jr.", "birth_date": date(1965, 4, 4), "bio": "Iron Man"},
            {"name": "Scarlett Johansson", "birth_date": date(1984, 11, 22), "bio": "Black Widow"},
            {"name": "Christian Bale", "birth_date": date(1974, 1, 30), "bio": "Batman"},
            {"name": "Brad Pitt", "birth_date": date(1963, 12, 18), "bio": "Fight Club star"},
            {"name": "Morgan Freeman", "birth_date": date(1937, 6, 1), "bio": "Shawshank star"},
            {"name": "Will Smith", "birth_date": date(1968, 9, 25), "bio": "Men in Black star"}
        ]
        
        for actor_data in english_actors:
            if actor_data["name"] not in actors:
                actor = database.Actor(**actor_data)
                db.add(actor)
                actors[actor_data["name"]] = actor
        
        db.commit()
        
        # Update dictionaries
        directors = {director.name: director for director in db.query(database.Director).all()}
        actors = {actor.name: actor for actor in db.query(database.Actor).all()}

        
        english_movies = [
            {"title": "Inception", "release_year": 2010, "description": "A thief enters dreams to plant ideas.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Leonardo DiCaprio"], "genre_names": ["Action", "Thriller"]},
            {"title": "The Dark Knight", "release_year": 2008, "description": "Batman faces the Joker.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Christian Bale"], "genre_names": ["Action", "Drama"]},
            {"title": "Avengers: Endgame", "release_year": 2019, "description": "The final battle against Thanos.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg", "director_name": "The Russo Brothers", "actor_names": ["Robert Downey Jr.", "Scarlett Johansson"], "genre_names": ["Action", "Drama"]},
            {"title": "Titanic", "release_year": 1997, "description": "A love story aboard the doomed ship.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg", "director_name": "James Cameron", "actor_names": ["Leonardo DiCaprio"], "genre_names": ["Romance", "Drama"]},
            {"title": "The Shawshank Redemption", "release_year": 1994, "description": "Hope and friendship in prison.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Morgan Freeman"], "genre_names": ["Drama"]},
            {"title": "Forrest Gump", "release_year": 1994, "description": "Life is like a box of chocolates.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Tom Hanks"], "genre_names": ["Drama", "Comedy"]},
            {"title": "Gladiator", "release_year": 2000, "description": "A Roman general seeks revenge.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Ridley Scott", "actor_names": ["Christian Bale"], "genre_names": ["Action", "Drama"]},
            {"title": "Fight Club", "release_year": 1999, "description": "An insomniac forms an underground fight club.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNDIzNDU0YzEtYzE5Ni00ZjlkLTk5ZjgtNjM3NWE4YzA3Nzk3XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg", "director_name": "David Fincher", "actor_names": ["Brad Pitt"], "genre_names": ["Drama", "Thriller"]},
            {"title": "The Matrix", "release_year": 1999, "description": "Reality is not what it seems.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Will Smith"], "genre_names": ["Action", "Thriller"]},
            {"title": "Goodfellas", "release_year": 1990, "description": "The rise and fall of a mobster.", "poster_url": "https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjA4NDI4NTI4MjNmXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "director_name": "Martin Scorsese", "actor_names": ["Robert Downey Jr."], "genre_names": ["Drama", "Thriller"]},
            
            {"title": "Avatar", "release_year": 2009, "description": "Humans colonize an alien world.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg", "director_name": "James Cameron", "actor_names": ["Will Smith"], "genre_names": ["Action", "Drama"]},
            {"title": "Interstellar", "release_year": 2014, "description": "A journey through space and time.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Leonardo DiCaprio"], "genre_names": ["Drama", "Thriller"]},
            {"title": "The Godfather", "release_year": 1972, "description": "The aging patriarch transfers control.", "poster_url": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Morgan Freeman"], "genre_names": ["Drama"]},
            {"title": "Pulp Fiction", "release_year": 1994, "description": "Interconnected crime stories.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "director_name": "Quentin Tarantino", "actor_names": ["Brad Pitt"], "genre_names": ["Drama", "Thriller"]},
            {"title": "Iron Man", "release_year": 2008, "description": "A billionaire becomes a superhero.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Robert Downey Jr."], "genre_names": ["Action", "Drama"]},
            {"title": "Spider-Man: No Way Home", "release_year": 2021, "description": "Peter Parker's identity is revealed.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_.jpg", "director_name": "The Russo Brothers", "actor_names": ["Tom Hanks"], "genre_names": ["Action", "Drama"]},
            {"title": "Avengers: Infinity War", "release_year": 2018, "description": "The Avengers face Thanos.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_.jpg", "director_name": "The Russo Brothers", "actor_names": ["Robert Downey Jr.", "Scarlett Johansson"], "genre_names": ["Action", "Drama"]},
            {"title": "Black Panther", "release_year": 2018, "description": "The king of Wakanda protects his nation.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Scarlett Johansson"], "genre_names": ["Action", "Drama"]},
            {"title": "Top Gun: Maverick", "release_year": 2022, "description": "Maverick returns to train new pilots.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZWYzOGEwNTgtNWU3NS00ZTQ0LWJkODUtMmVhMjIwMjA1ZmQwXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Tom Hanks"], "genre_names": ["Action", "Drama"]},
            {"title": "Jurassic Park", "release_year": 1993, "description": "Dinosaurs are brought back to life.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Will Smith"], "genre_names": ["Action", "Thriller"]},

            {"title": "Star Wars: A New Hope", "release_year": 1977, "description": "A young farm boy joins the Rebellion.", "poster_url": "https://m.media-amazon.com/images/M/MV5BOTA5NjhiOTAtZWM0ZC00MWNhLThiMzEtZDFkOTk2OTU1ZDJkXkEyXkFqcGdeQXVyMTA4NDI1NTQx@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Will Smith"], "genre_names": ["Action", "Drama"]},
            {"title": "E.T. the Extra-Terrestrial", "release_year": 1982, "description": "A boy befriends an alien.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQwMzI1MzI4NF5BMl5BanBnXkFtZTcwNDI3NzIxMw@@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Tom Hanks"], "genre_names": ["Family", "Drama"]},
            {"title": "Jaws", "release_year": 1975, "description": "A giant shark terrorizes a beach town.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMmVmODY1MzEtYTMwZC00MzNhLWFkNDMtZjAwM2EwODUxZTA5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Morgan Freeman"], "genre_names": ["Thriller", "Action"]},
            {"title": "The Lion King", "release_year": 1994, "description": "A young lion prince reclaims his kingdom.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNjgtEWFkZmIzNzQ0YjY2XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Will Smith"], "genre_names": ["Family", "Drama"]},
            {"title": "Toy Story", "release_year": 1995, "description": "Toys come to life when humans aren't around.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Tom Hanks"], "genre_names": ["Family", "Comedy"]},
            {"title": "Finding Nemo", "release_year": 2003, "description": "A clownfish searches for his son.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZjMxYzExOWUtYWNkZi00NjI4LWIzNzQtNjg0MTI3MDI5MjNjXkEyXkFqcGdeQXVyNjE2MjQwNjc@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Will Smith"], "genre_names": ["Family", "Comedy"]},
            {"title": "Frozen", "release_year": 2013, "description": "A queen with ice powers and her sister.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Scarlett Johansson"], "genre_names": ["Family", "Comedy"]},
            {"title": "The Incredibles", "release_year": 2004, "description": "A family of superheroes comes out of hiding.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Robert Downey Jr."], "genre_names": ["Family", "Action"]},
            {"title": "Shrek", "release_year": 2001, "description": "An ogre's journey to rescue a princess.", "poster_url": "https://m.media-amazon.com/images/M/MV5BOGZhM2FhNTItODAzNi00YjA0LWEyN2UtNjJlYWQzYzU1MDg5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Will Smith"], "genre_names": ["Family", "Comedy"]},
            {"title": "Up", "release_year": 2009, "description": "An elderly man ties balloons to his house.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_.jpg", "director_name": "Steven Spielberg", "actor_names": ["Morgan Freeman"], "genre_names": ["Family", "Drama"]},

            {"title": "The Dark Knight Rises", "release_year": 2012, "description": "Batman's final battle.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Christian Bale"], "genre_names": ["Action", "Drama"]},
            {"title": "Batman Begins", "release_year": 2005, "description": "The origin of Batman.", "poster_url": "https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Christian Bale"], "genre_names": ["Action", "Drama"]},
            {"title": "Dunkirk", "release_year": 2017, "description": "The evacuation of Allied soldiers from Dunkirk.", "poster_url": "https://m.media-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Tom Hanks"], "genre_names": ["Action", "Drama"]},
            {"title": "Tenet", "release_year": 2020, "description": "A secret agent manipulates time.", "poster_url": "https://m.media-amazon.com/images/M/MV5BYzg0NGM2NjAtNmIxOC00MDJmLTg5ZmYtYzM0MTE4NWE2NzlhXkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Leonardo DiCaprio"], "genre_names": ["Action", "Thriller"]},
            {"title": "Memento", "release_year": 2000, "description": "A man with short-term memory loss seeks revenge.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktMzY4ZmI2NDAyNzYzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "director_name": "Christopher Nolan", "actor_names": ["Leonardo DiCaprio"], "genre_names": ["Thriller", "Drama"]},
            {"title": "Once Upon a Time in Hollywood", "release_year": 2019, "description": "1960s Hollywood and the Manson murders.", "poster_url": "https://m.media-amazon.com/images/M/MV5BOTg4ZTNkZmUtMzNlZi00YmFjLTk1MmUtNWQwNTM0YjcyNTNkXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_.jpg", "director_name": "Quentin Tarantino", "actor_names": ["Leonardo DiCaprio", "Brad Pitt"], "genre_names": ["Drama", "Comedy"]},
            {"title": "Kill Bill: Vol. 1", "release_year": 2003, "description": "A bride seeks revenge on her former associates.", "poster_url": "https://m.media-amazon.com/images/M/MV5BNzM3NDFhYTAtYmU5Mi00NGRmLTljYjgtMDkyODQ4MjNkMGY2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg", "director_name": "Quentin Tarantino", "actor_names": ["Scarlett Johansson"], "genre_names": ["Action", "Thriller"]},
            {"title": "Django Unchained", "release_year": 2012, "description": "A freed slave becomes a bounty hunter.", "poster_url": "https://m.media-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_.jpg", "director_name": "Quentin Tarantino", "actor_names": ["Leonardo DiCaprio"], "genre_names": ["Action", "Drama"]},
            {"title": "Inglourious Basterds", "release_year": 2009, "description": "Allied soldiers hunt Nazis in occupied France.", "poster_url": "https://m.media-amazon.com/images/M/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg", "director_name": "Quentin Tarantino", "actor_names": ["Brad Pitt"], "genre_names": ["Action", "Drama"]},
            {"title": "Reservoir Dogs", "release_year": 1992, "description": "A jewelry heist goes wrong.", "poster_url": "https://m.media-amazon.com/images/M/MV5BZmQzNGQwNjAtYWQ2Ni00NmI0LWI4NDEtNzg1M2I2NGEzN2ZmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", "director_name": "Quentin Tarantino", "actor_names": ["Brad Pitt"], "genre_names": ["Thriller", "Drama"]}
        ]
        
        # Add movies
        for movie_data in english_movies:
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
            db.flush()
            
            for actor_name in movie_data["actor_names"]:
                actor = actors.get(actor_name)
                if actor:
                    movie.actors.append(actor)
            
            for genre_name in movie_data["genre_names"]:
                genre = genres.get(genre_name)
                if genre:
                    movie.genres.append(genre)
            
            print(f" Added: {movie_data['title']} ({movie_data['release_year']})")
        
        db.commit()
        
        total_movies = db.query(database.Movie).count()
        
    except Exception as e:
        print(f" Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_english_movies()
