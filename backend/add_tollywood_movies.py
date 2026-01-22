from sqlalchemy.orm import Session
from datetime import date
import database
import crud
import schemas

def add_tollywood_movies():
    db = Session(bind=database.engine)
    
    try:
        # Add Tollywood/Telugu genre if it doesn't exist
        tollywood_genre = crud.create_genre(db, schemas.GenreCreate(
            name="Tollywood",
            description="Telugu cinema films from Andhra Pradesh and Telangana"
        ))
        
        # Get existing genres for combinations
        existing_genres = crud.get_genres(db)
        action_genre = next((g for g in existing_genres if g.name == "Action"), None)
        drama_genre = next((g for g in existing_genres if g.name == "Drama"), None)
        romance_genre = next((g for g in existing_genres if g.name == "Romance"), None)
        thriller_genre = next((g for g in existing_genres if g.name == "Thriller"), None)
        comedy_genre = next((g for g in existing_genres if g.name == "Comedy"), None)
        
        # Add Telugu actors
        tollywood_actors = [
            {
                "name": "Mahesh Babu",
                "birth_date": date(1975, 8, 9),
                "bio": "Prince of Tollywood, known for his versatile acting and charismatic screen presence",
                "photo_url": "https://picsum.photos/150/200?random=mahesh"
            },
            {
                "name": "Samantha Ruth Prabhu",
                "birth_date": date(1987, 4, 28),
                "bio": "Popular actress known for her performances in Telugu and Tamil films",
                "photo_url": "https://picsum.photos/150/200?random=samantha"
            },
            {
                "name": "Allu Arjun",
                "birth_date": date(1983, 4, 8),
                "bio": "Stylish Star known for his dancing skills and energetic performances",
                "photo_url": "https://picsum.photos/150/200?random=allu"
            },
            {
                "name": "Kajal Aggarwal",
                "birth_date": date(1985, 6, 19),
                "bio": "Leading actress in South Indian cinema",
                "photo_url": "https://picsum.photos/150/200?random=kajal"
            },
            {
                "name": "Prabhas",
                "birth_date": date(1979, 10, 23),
                "bio": "Pan-India star known for Baahubali series",
                "photo_url": "https://picsum.photos/150/200?random=prabhas"
            },
            {
                "name": "Jr. NTR",
                "birth_date": date(1983, 5, 20),
                "bio": "Young Tiger, versatile actor and dancer",
                "photo_url": "https://picsum.photos/150/200?random=ntr"
            },
            {
                "name": "Ram Charan",
                "birth_date": date(1985, 3, 27),
                "bio": "Mega Power Star, son of Chiranjeevi",
                "photo_url": "https://picsum.photos/150/200?random=ramcharan"
            },
            {
                "name": "Pooja Hegde",
                "birth_date": date(1990, 10, 13),
                "bio": "Popular actress in Telugu and Hindi films",
                "photo_url": "https://picsum.photos/150/200?random=pooja"
            },
            {
                "name": "Keerthy Suresh",
                "birth_date": date(1992, 10, 17),
                "bio": "National Award winning actress",
                "photo_url": "https://picsum.photos/150/200?random=keerthy"
            },
            {
                "name": "Kiara Advani",
                "birth_date": date(1992, 7, 31),
                "bio": "Popular actress in Hindi and Telugu films",
                "photo_url": "https://picsum.photos/150/200?random=kiara"
            },
            {
                "name": "Shruti Haasan",
                "birth_date": date(1986, 1, 28),
                "bio": "Actress and singer",
                "photo_url": "https://picsum.photos/150/200?random=shruti"
            },
            {
                "name": "Kriti Sanon",
                "birth_date": date(1990, 7, 27),
                "bio": "Bollywood and Tollywood actress",
                "photo_url": "https://picsum.photos/150/200?random=kriti"
            },
            {
                "name": "Anushka Shetty",
                "birth_date": date(1981, 11, 7),
                "bio": "Sweety known for Baahubali series",
                "photo_url": "https://picsum.photos/150/200?random=anushka"
            },
            {
                "name": "Rashmika Mandanna",
                "birth_date": date(1996, 4, 5),
                "bio": "National crush, popular in South Indian films",
                "photo_url": "https://picsum.photos/150/200?random=rashmika"
            },
            {
                "name": "Nithin",
                "birth_date": date(1983, 3, 30),
                "bio": "Popular Telugu actor",
                "photo_url": "https://picsum.photos/150/200?random=nithin"
            }
        ]
        
        actor_objects = []
        for actor_data in tollywood_actors:
            actor = crud.create_actor(db, schemas.ActorCreate(**actor_data))
            actor_objects.append(actor)
        
        # Add Telugu directors
        tollywood_directors = [
            {
                "name": "S. S. Rajamouli",
                "birth_date": date(1973, 10, 10),
                "bio": "Visionary director known for Baahubali and RRR",
                "photo_url": "https://picsum.photos/150/200?random=rajamouli"
            },
            {
                "name": "Trivikram Srinivas",
                "birth_date": date(1971, 11, 7),
                "bio": "Wizard of words, known for family entertainers",
                "photo_url": "https://picsum.photos/150/200?random=trivikram"
            },
            {
                "name": "Koratala Siva",
                "birth_date": date(1975, 6, 15),
                "bio": "Director known for message-oriented commercial films",
                "photo_url": "https://picsum.photos/150/200?random=koratala"
            },
            {
                "name": "Sukumar",
                "birth_date": date(1970, 1, 11),
                "bio": "Creative director known for innovative storytelling",
                "photo_url": "https://picsum.photos/150/200?random=sukumar"
            },
            {
                "name": "Vamshi Paidipally",
                "birth_date": date(1978, 8, 27),
                "bio": "Director known for emotional family dramas",
                "photo_url": "https://picsum.photos/150/200?random=vamshi"
            },
            {
                "name": "Anil Ravipudi",
                "birth_date": date(1980, 1, 1),
                "bio": "Comedy entertainer specialist",
                "photo_url": "https://picsum.photos/150/200?random=anil"
            },
            {
                "name": "Parasuram",
                "birth_date": date(1979, 6, 16),
                "bio": "Director known for commercial entertainers",
                "photo_url": "https://picsum.photos/150/200?random=parasuram"
            }
        ]
        
        director_objects = []
        for director_data in tollywood_directors:
            director = crud.create_director(db, schemas.DirectorCreate(**director_data))
            director_objects.append(director)
        
        # Mahesh Babu filmography and other Tollywood hits
        tollywood_movies = [
            # Mahesh Babu Movies (Recent and Popular)
            {
                "title": "Sarkaru Vaari Paata",
                "release_year": 2022,
                "description": "A commercial entertainer about a man who fights against corruption and banking fraud",
                "director": next(d for d in director_objects if d.name == "Parasuram"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Mahesh Babu"),
                    next(a for a in actor_objects if a.name == "Keerthy Suresh")
                ],
                "genres": [tollywood_genre, action_genre, drama_genre]
            },
            {
                "title": "Maharshi",
                "release_year": 2019,
                "description": "A successful CEO returns to his roots to help farmers and discovers the importance of agriculture",
                "director": next(d for d in director_objects if d.name == "Vamshi Paidipally"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Mahesh Babu"),
                    next(a for a in actor_objects if a.name == "Pooja Hegde")
                ],
                "genres": [tollywood_genre, drama_genre, action_genre]
            },
            {
                "title": "Bharat Ane Nenu",
                "release_year": 2018,
                "description": "A young man becomes the Chief Minister and works to eliminate corruption from the political system",
                "director": next(d for d in director_objects if d.name == "Koratala Siva"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Mahesh Babu"),
                    next(a for a in actor_objects if a.name == "Kiara Advani")
                ],
                "genres": [tollywood_genre, drama_genre, thriller_genre]
            },
            {
                "title": "A Aa",
                "release_year": 2016,
                "description": "A romantic family entertainer about two contrasting families and their children",
                "director": next(d for d in director_objects if d.name == "Trivikram Srinivas"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Nithin"),
                    next(a for a in actor_objects if a.name == "Samantha Ruth Prabhu")
                ],
                "genres": [tollywood_genre, romance_genre, comedy_genre]
            },
            {
                "title": "Srimanthudu",
                "release_year": 2015,
                "description": "A wealthy young man adopts a village and works to develop it while facing various challenges",
                "director": next(d for d in director_objects if d.name == "Koratala Siva"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Mahesh Babu"),
                    next(a for a in actor_objects if a.name == "Shruti Haasan")
                ],
                "genres": [tollywood_genre, drama_genre, action_genre]
            },
            {
                "title": "1: Nenokkadine",
                "release_year": 2014,
                "description": "A psychological thriller about a rock star who suffers from a rare memory disorder",
                "director": next(d for d in director_objects if d.name == "Sukumar"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Mahesh Babu"),
                    next(a for a in actor_objects if a.name == "Kriti Sanon")
                ],
                "genres": [tollywood_genre, thriller_genre, action_genre]
            },
            # Other Popular Tollywood Movies
            {
                "title": "Baahubali: The Beginning",
                "release_year": 2015,
                "description": "An epic tale of two brothers fighting for the throne of Mahishmati kingdom",
                "director": next(d for d in director_objects if d.name == "S. S. Rajamouli"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Prabhas"),
                    next(a for a in actor_objects if a.name == "Anushka Shetty")
                ],
                "genres": [tollywood_genre, action_genre, drama_genre]
            },
            {
                "title": "Baahubali 2: The Conclusion",
                "release_year": 2017,
                "description": "The epic conclusion revealing why Kattappa killed Baahubali",
                "director": next(d for d in director_objects if d.name == "S. S. Rajamouli"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Prabhas"),
                    next(a for a in actor_objects if a.name == "Anushka Shetty")
                ],
                "genres": [tollywood_genre, action_genre, drama_genre]
            },
            {
                "title": "RRR",
                "release_year": 2022,
                "description": "A fictional story about Indian freedom fighters Alluri Sitarama Raju and Komaram Bheem",
                "director": next(d for d in director_objects if d.name == "S. S. Rajamouli"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Jr. NTR"),
                    next(a for a in actor_objects if a.name == "Ram Charan")
                ],
                "genres": [tollywood_genre, action_genre, drama_genre]
            },
            {
                "title": "Pushpa: The Rise",
                "release_year": 2021,
                "description": "The story of a lorry driver who becomes a smuggler in the red sandalwood trade",
                "director": next(d for d in director_objects if d.name == "Sukumar"),
                "actors": [
                    next(a for a in actor_objects if a.name == "Allu Arjun"),
                    next(a for a in actor_objects if a.name == "Rashmika Mandanna")
                ],
                "genres": [tollywood_genre, action_genre, thriller_genre]
            }
        ]
        
        # Create movies with poster URLs
        created_movies = []
        for i, movie_data in enumerate(tollywood_movies):
            # Skip movies where actors/directors weren't found
            try:
                movie_create_data = {
                    "title": movie_data["title"],
                    "release_year": movie_data["release_year"],
                    "description": movie_data["description"],
                    "poster_url": f"https://picsum.photos/300/450?random={movie_data['title'].lower().replace(' ', '')}{i}",
                    "director_id": movie_data["director"].id,
                    "actor_ids": [actor.id for actor in movie_data["actors"]],
                    "genre_ids": [genre.id for genre in movie_data["genres"] if genre]
                }
                
                movie = crud.create_movie(db, schemas.MovieCreate(**movie_create_data))
                created_movies.append(movie)
                print(f"Added: {movie.title} ({movie.release_year})")
                
            except (AttributeError, StopIteration) as e:
                print(f"Skipping {movie_data['title']} due to missing data: {e}")
                continue
        
        print(f"\nSuccessfully added {len(created_movies)} Tollywood movies!")
        print("Tollywood content now available in the Movie Explorer!")
        
    except Exception as e:
        print(f"Error adding Tollywood movies: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_tollywood_movies()
