from sqlalchemy.orm import Session
from datetime import date
import random
import database
import crud
import schemas

# Create database tables
database.Base.metadata.create_all(bind=database.engine)

def add_more_content():
    db = Session(bind=database.engine)
    
    try:

        additional_genres = [
            {"name": "Fantasy", "description": "Magical and supernatural stories"},
            {"name": "Mystery", "description": "Puzzling crimes and investigations"},
            {"name": "Adventure", "description": "Exciting journeys and quests"},
            {"name": "War", "description": "Military conflicts and battles"},
            {"name": "Western", "description": "Stories set in the American Old West"},
            {"name": "Musical", "description": "Films featuring songs and dance"},
            {"name": "Biography", "description": "Life stories of real people"},
            {"name": "Documentary", "description": "Non-fiction films"},
        ]
        
        existing_genres = crud.get_genres(db)
        for genre_data in additional_genres:
            genre = crud.create_genre(db, schemas.GenreCreate(**genre_data))
            existing_genres.append(genre)
        
        additional_directors = [
            {"name": "Steven Spielberg", "birth_date": date(1946, 12, 18), "bio": "Legendary filmmaker"},
            {"name": "Martin Scorsese", "birth_date": date(1942, 11, 17), "bio": "Master of cinema"},
            {"name": "Ridley Scott", "birth_date": date(1937, 11, 30), "bio": "Visionary director"},
            {"name": "James Cameron", "birth_date": date(1954, 8, 16), "bio": "Sci-fi pioneer"},
            {"name": "Guillermo del Toro", "birth_date": date(1964, 10, 9), "bio": "Fantasy storyteller"},
            {"name": "Jordan Peele", "birth_date": date(1979, 2, 21), "bio": "Horror innovator"},
            {"name": "Patty Jenkins", "birth_date": date(1971, 7, 24), "bio": "Superhero director"},
            {"name": "Chloe Zhao", "birth_date": date(1982, 3, 31), "bio": "Naturalistic filmmaker"},
        ]
        
        existing_directors = crud.get_directors(db)
        for director_data in additional_directors:
            director = crud.create_director(db, schemas.DirectorCreate(**director_data))
            existing_directors.append(director)
        

        additional_actors = [
            {"name": "Robert Downey Jr.", "birth_date": date(1965, 4, 4), "bio": "Iron Man actor"},
            {"name": "Scarlett Johansson", "birth_date": date(1984, 11, 22), "bio": "Versatile actress"},
            {"name": "Tom Hanks", "birth_date": date(1956, 7, 9), "bio": "America's beloved actor"},
            {"name": "Meryl Streep", "birth_date": date(1949, 6, 22), "bio": "Greatest actress of her generation"},
            {"name": "Denzel Washington", "birth_date": date(1954, 12, 28), "bio": "Powerful dramatic actor"},
            {"name": "Viola Davis", "birth_date": date(1965, 8, 11), "bio": "Award-winning actress"},
            {"name": "Oscar Isaac", "birth_date": date(1979, 3, 9), "bio": "Character actor"},
            {"name": "Lupita Nyong'o", "birth_date": date(1983, 3, 1), "bio": "Rising star"},
        ]
        
        existing_actors = crud.get_actors(db)
        for actor_data in additional_actors:
            actor = crud.create_actor(db, schemas.ActorCreate(**actor_data))
            existing_actors.append(actor)
        

        movie_titles = [
            "The Last Kingdom", "Midnight Runner", "City of Dreams", "The Silent Hour",
            "Broken Wings", "Rising Storm", "The Golden Path", "Shadow Dance",
            "Electric Blue", "The Final Stand", "Whispers in Time", "Ocean's Edge",
            "The Hidden Truth", "Crimson Moon", "The Lost City", "Silver Screen",
            "The Dark Forest", "Emerald Fire", "The Endless Road", "Crystal Vision",
            "The Burning Sky", "Iron Will", "The Secret Garden", "Golden Hour",
            "The Wild Hunt", "Neon Nights", "The Sacred Mountain", "Blood Diamond",
            "The Glass House", "Thunder Road", "The Phantom Voice", "Starlight Express",
            "The Broken Chain", "Mystic River", "The Silver Lining", "Desert Storm",
            "The Purple Rain", "Ghost Protocol", "The Winter Soldier", "Summer Nights",
            "The Black Swan", "White Lightning", "The Red Dragon", "Blue Moon",
            "The Green Mile", "Orange Sunset", "The Yellow Brick Road", "Pink Flamingo",
        ]
        

        prefixes = ["The Amazing", "The Incredible", "The Spectacular", "The Magnificent", 
                   "The Extraordinary", "The Ultimate", "The Legendary", "The Epic"]
        suffixes = ["Returns", "Rises", "Begins", "Forever", "Reborn", "Unleashed", 
                   "Revolution", "Chronicles", "Legacy", "Origins"]
        

        all_movies = []
        for i in range(200):
            if i < len(movie_titles):
                title = movie_titles[i]
            elif i < len(movie_titles) * 2:
                title = f"{random.choice(prefixes)} {movie_titles[i - len(movie_titles)]}"
            else:
                base_title = random.choice(movie_titles)
                title = f"{base_title} {random.choice(suffixes)}"

            release_year = random.randint(1990, 2024)
            

            director = random.choice(existing_directors)
            

            num_actors = random.randint(2, 4)
            selected_actors = random.sample(existing_actors, min(num_actors, len(existing_actors)))
            

            num_genres = random.randint(1, 3)
            selected_genres = random.sample(existing_genres, min(num_genres, len(existing_genres)))

            descriptions = [
                f"A thrilling adventure set in {release_year}.",
                f"An epic tale of courage and determination.",
                f"A heartwarming story about love and friendship.",
                f"A gripping thriller that keeps you on the edge.",
                f"An inspiring journey of self-discovery.",
                f"A powerful drama about human relationships.",
                f"An action-packed adventure across time.",
                f"A beautiful story about overcoming obstacles.",
                f"A mysterious tale with unexpected twists.",
                f"An unforgettable journey through emotions.",
            ]
            
            movie_data = {
                "title": title,
                "release_year": release_year,
                "description": random.choice(descriptions),
                "poster_url": f"https://example.com/{title.lower().replace(' ', '-')}.jpg",
                "director_id": director.id,
                "actor_ids": [actor.id for actor in selected_actors],
                "genre_ids": [genre.id for genre in selected_genres]
            }
            
            movie = crud.create_movie(db, schemas.MovieCreate(**movie_data))
            all_movies.append(movie)
            
            if (i + 1) % 50 == 0:
                print(f"Added {i + 1} movies...")
        
        print(f"Successfully added {len(all_movies)} new movies!")
        print(f"Total movies in database: {len(crud.get_movies(db, limit=1000))}")
        
    except Exception as e:
        print(f"Error adding movies: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_more_content()
