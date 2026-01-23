from sqlalchemy.orm import Session
import database

def update_real_movie_posters():
    db = Session(bind=database.engine)
    
    try:
        movie_poster_mapping = {
            "Inception": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
            "Pulp Fiction": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
            "Barbie": "https://image.tmdb.org/t/p/w500/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
            "Dune": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
            "The Dark Knight": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",

            "Sarkaru Vaari Paata": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5Mi00NGM0LWJiNzQtN2Q5Zjc1MzI1NzZmXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
            "Maharshi": "https://m.media-amazon.com/images/M/MV5BMjIwZDMwZTQtYTMwZC00MDQyLTkzNTUtYjA5NGZmM2Q5MGNkXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
            "Bharat Ane Nenu": "https://m.media-amazon.com/images/M/MV5BMjI1Mzg5MDczOV5BMl5BanBnXkFtZTgwNjIwMDk1NTM@._V1_.jpg",
            "Srimanthudu": "https://m.media-amazon.com/images/M/MV5BMjE5ODU0NDQ2Nl5BMl5BanBnXkFtZTgwOTU4ODU0NjE@._V1_.jpg",
            "1: Nenokkadine": "https://m.media-amazon.com/images/M/MV5BMTVlNzgzMjktZWJjYy00YzYwLWFjMTUtOGZmZDMzMmM2ZGY2XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",

            "Baahubali: The Beginning": "https://image.tmdb.org/t/p/w500/2pqfW7PsWAKTXGPaFLYyOJMxibc.jpg",
            "Baahubali 2: The Conclusion": "https://image.tmdb.org/t/p/w500/lkKPSJH4WswkHj4LXKS2HW8qEUs.jpg",
            "RRR": "https://image.tmdb.org/t/p/w500/w6C2WxqOLWHZoew8UL3P2rrJcbX.jpg",
            "Pushpa: The Rise": "https://image.tmdb.org/t/p/w500/ugQW8BQOmJ2Qtt6tG9lGbEfn1jX.jpg",
            "A Aa": "https://m.media-amazon.com/images/M/MV5BMTgxNjA1Njc2MV5BMl5BanBnXkFtZTgwNjE4NzQ2OTE@._V1_.jpg",
            
            "The Avengers": "https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
            "Iron Man": "https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg",
            "Spider-Man": "https://image.tmdb.org/t/p/w500/gh4cZbhZxyTbgxQPxD0dOudNPTn.jpg",
            "The Matrix": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
            "Titanic": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
            "Avatar": "https://image.tmdb.org/t/p/w500/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg",
            "The Godfather": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "Forrest Gump": "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
            "The Shawshank Redemption": "https://image.tmdb.org/t/p/w500/q6y0Go1v5GwcxgGQOfpuBpVgdA4.jpg",
            "Gladiator": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
            "Joker": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
            "Black Panther": "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
            "Wonder Woman": "https://image.tmdb.org/t/p/w500/gfJGlDaHuWimErCr5Ql0I8x9QSy.jpg",
            "Captain Marvel": "https://image.tmdb.org/t/p/w500/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg",
            "Star Wars": "https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
            "Indiana Jones": "https://image.tmdb.org/t/p/w500/ceG9VzoRAVGwivFU403Wc3AHRys.jpg",
            "Jurassic Park": "https://image.tmdb.org/t/p/w500/b1xCNnyrPebIc7EWNZIa6BYzRMI.jpg",
            "E.T.": "https://image.tmdb.org/t/p/w500/5p3Zj6b3ZYrYzz2H9zIVa0LUQLk.jpg"
        }

        movies = db.query(database.Movie).all()
        updated_count = 0
        
        print(f"Scanning {len(movies)} movies for poster updates...")
        
        for movie in movies:
            for title_key, poster_url in movie_poster_mapping.items():
                if title_key.lower() in movie.title.lower() or movie.title.lower() in title_key.lower():
                    old_url = movie.poster_url
                    movie.poster_url = poster_url
                    updated_count += 1
                    break 
        for movie in movies:
            if movie.poster_url and ("picsum.photos" in movie.poster_url or "source.unsplash" in movie.poster_url or "loremflickr" in movie.poster_url):
                year_seed = movie.release_year or 2020
                title_seed = abs(hash(movie.title)) % 1000
                
                if movie.genres:
                    primary_genre = movie.genres[0].name.lower()
                    if primary_genre in ['action', 'thriller']:
                        movie.poster_url = f"https://picsum.photos/300/450?random=action{title_seed}"
                    elif primary_genre in ['romance', 'drama']:
                        movie.poster_url = f"https://picsum.photos/300/450?random=drama{title_seed}"
                    elif primary_genre in ['comedy']:
                        movie.poster_url = f"https://picsum.photos/300/450?random=comedy{title_seed}"
                    elif primary_genre in ['sci-fi', 'fantasy']:
                        movie.poster_url = f"https://picsum.photos/300/450?random=scifi{title_seed}"
                    elif primary_genre in ['horror']:
                        movie.poster_url = f"https://picsum.photos/300/450?random=horror{title_seed}"
                    else:
                        movie.poster_url = f"https://picsum.photos/300/450?random=movie{title_seed}"
                else:
                    movie.poster_url = f"https://picsum.photos/300/450?random=film{title_seed}"
        
        db.commit()
        
        
    except Exception as e:
        print(f" Error updating movie posters: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_real_movie_posters()
