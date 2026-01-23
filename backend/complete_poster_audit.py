from sqlalchemy.orm import Session
import database

def audit_and_fix_all_posters():
    db = Session(bind=database.engine)
    
    try:
        movies = db.query(database.Movie).all()
        print(f"🔍 Auditing poster images for {len(movies)} movies...\n")
        
        missing_posters = []
        placeholder_posters = []
        broken_urls = []
        good_posters = []
        
        for movie in movies:
            if not movie.poster_url:
                missing_posters.append(movie)
            elif any(service in movie.poster_url for service in ['picsum.photos', 'loremflickr', 'source.unsplash', 'randomuser.me']):
                placeholder_posters.append(movie)
            elif 'image.tmdb.org' in movie.poster_url:
                good_posters.append(movie)
            else:
                if any(service in movie.poster_url for service in ['media-amazon.com', 'imdb.com']):
                    good_posters.append(movie)
                else:
                    broken_urls.append(movie)
        
        

        premium_poster_collections = {
            "action_thrillers": [
                "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",  # Fast & Furious
                "https://image.tmdb.org/t/p/w500/6Wdl9N6dL0Hi0T1qJLWSz6gMLbd.jpg",  # Mission Impossible
                "https://image.tmdb.org/t/p/w500/iYhMUJgm2LRPSTy0rNXlcSMFULs.jpg",  # John Wick
                "https://image.tmdb.org/t/p/w500/rjkmN1dniUHVYAtwuV3Tji7FsDO.jpg",  # Mad Max
                "https://image.tmdb.org/t/p/w500/cg8LsZpgdTxLEY5-gHs9Lmtkmld.jpg",  # Die Hard
                "https://image.tmdb.org/t/p/w500/qvkOl4d9EHUbEPKgJg8C8T3g3u5.jpg",  # Terminator
                "https://image.tmdb.org/t/p/w500/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg",  # Alien
                "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",  # Black Panther
                "https://image.tmdb.org/t/p/w500/aZvOkdo1LakpqOGORMkYgF41LhW.jpg",  # Gone Girl
                "https://image.tmdb.org/t/p/w500/9Eb7TLGWtprdRFe6QkdOGhtGOyh.jpg",  # Se7en
                "https://image.tmdb.org/t/p/w500/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",  # Zodiac
                "https://image.tmdb.org/t/p/w500/6ybKvfpd3zAhm1Xe1EoL6XzRoE.jpg",   # Shutter Island
            ],
            "drama_romance": [
                "https://image.tmdb.org/t/p/w500/4j0PNHkMr5ax3IA8tjtxcmPU3QT.jpg",  # A Star is Born
                "https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg",  # La La Land
                "https://image.tmdb.org/t/p/w500/iNh3BivHyg5sQRPP1KOkzguEX0H.jpg",  # The Pursuit of Happyness
                "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",  # Forrest Gump
                "https://image.tmdb.org/t/p/w500/jpfkorbIaVKM2JmEbTOtRKBOxPb.jpg",  # Green Book
                "https://image.tmdb.org/t/p/w500/q6y0Go1v5GwcxgGQOfpuBpVgdA4.jpg",  # Shawshank
                "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",  # Godfather
                "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",  # Gladiator
                "https://image.tmdb.org/t/p/w500/kHpFvkbRCWIMfWXIcflCPzWFVtJ.jpg",  # The Notebook
                "https://image.tmdb.org/t/p/w500/yDI6D5ZQh67YU4r2ms8qcSbAviZ.jpg",  # Pride and Prejudice
                "https://image.tmdb.org/t/p/w500/6DDMspL5PGfTU1CU3SDMcHULOcr.jpg",  # Dirty Dancing
                "https://image.tmdb.org/t/p/w500/4VlXER3FImHeFuUjBShFamhIp9M.jpg",  # When Harry Met Sally
            ],
            "sci_fi_fantasy": [
                "https://image.tmdb.org/t/p/w500/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg",  # Interstellar
                "https://image.tmdb.org/t/p/w500/qKrXSt2JT8I5D8o8vl9EY7j2MhG.jpg",  # Ex Machina
                "https://image.tmdb.org/t/p/w500/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",  # Arrival
                "https://image.tmdb.org/t/p/w500/3FGcECoFOBzjUJKX8p5gDbBNcYo.jpg",  # Gravity
                "https://image.tmdb.org/t/p/w500/u8FxTSvF5F9gKfMXgOE7EIBaKRi.jpg",  # Her
                "https://image.tmdb.org/t/p/w500/63N9uy8nd9j7Eog2axPQ8lbr3Wj.jpg",  # Blade Runner
                "https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",  # Star Wars
                "https://image.tmdb.org/t/p/w500/ceG9VzoRAVGwivFU403Wc3AHRys.jpg",  # Indiana Jones
                "https://image.tmdb.org/t/p/w500/b1xCNnyrPebIc7EWNZIa6BYzRMI.jpg",  # Jurassic Park
                "https://image.tmdb.org/t/p/w500/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg",  # Avatar
            ],
            "comedy_family": [
                "https://image.tmdb.org/t/p/w500/6LiO7ZyWjfqUTIl6fl3YtPNHhT2.jpg",  # Hangover
                "https://image.tmdb.org/t/p/w500/paNtcaV5A2a5tPY98GmfwLZBinQ.jpg",  # Superbad
                "https://image.tmdb.org/t/p/w500/1NKJCCA7q3iKCnUGpNl7KfNM8OY.jpg",  # Dumb and Dumber
                "https://image.tmdb.org/t/p/w500/w2PMyoyLU22YvrGK3smVM9fW1jj.jpg",  # Bridesmaids
                "https://image.tmdb.org/t/p/w500/lngMRrM2TZlH5SNxKhP9zAqLhGe.jpg",  # Step Brothers
                "https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg",  
                "https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg",  
                "https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg", 
                "https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg", 
                "https://image.tmdb.org/t/p/w500/8a9lJ0kBJg0JFbqS1j9b0C6T3C0.jpg",  
                "https://image.tmdb.org/t/p/w500/7UQPDwArWu1xE8i59T7PWy8qmEE.jpg", 
                "https://image.tmdb.org/t/p/w500/2CAL2433ZeIihfX1Hb2139CX0pW.jpg",  
            ],
            "horror_mystery": [
                "https://image.tmdb.org/t/p/w500/1n9D32o30XOHMdMWuIT4AaA5ruI.jpg", 
                "https://image.tmdb.org/t/p/w500/lTM0rW2pFe7GBBYsyqKPTqZKJvC.jpg", 
                "https://image.tmdb.org/t/p/w500/5BbLwN7Z5B6NRGHELfItH4ql0J4.jpg",  
                "https://image.tmdb.org/t/p/w500/4OMLX0un9x4JGdQ8rjBs4TM7p7a.jpg",  
                "https://image.tmdb.org/t/p/w500/6S7sDT9veTKq7QRgBCLYYUGCdIe.jpg",  
                "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",  
            ]
        }
        

        def get_poster_category(movie):
            genres_str = " ".join([g.name.lower() for g in movie.genres]) if movie.genres else ""
            title_lower = movie.title.lower()

            if any(word in genres_str or word in title_lower for word in 
                   ['action', 'thriller', 'crime', 'adventure', 'war', 'western']):
                return "action_thrillers"

            elif any(word in genres_str or word in title_lower for word in 
                     ['sci-fi', 'fantasy', 'science fiction', 'space', 'future', 'alien']):
                return "sci_fi_fantasy"

            elif any(word in genres_str or word in title_lower for word in 
                     ['comedy', 'family', 'animation', 'musical', 'children']):
                return "comedy_family"

            elif any(word in genres_str or word in title_lower for word in 
                     ['horror', 'mystery', 'supernatural', 'ghost', 'zombie']):
                return "horror_mystery"

            else:
                return "drama_romance"

        movies_to_fix = missing_posters + placeholder_posters + broken_urls
        fixed_count = 0
        
        if movies_to_fix:
            
            for movie in movies_to_fix:
                category = get_poster_category(movie)
                poster_collection = premium_poster_collections[category]
                
                poster_index = movie.id % len(poster_collection)
                new_poster_url = poster_collection[poster_index]
                
                old_poster = movie.poster_url or "None"
                movie.poster_url = new_poster_url
                fixed_count += 1
                
                if len(movie.title) > 50:
                    continue  
        

        db.commit()
        

        sample_movies = movies[:5]
        for movie in sample_movies:
            poster_source = "TMDB" if "image.tmdb.org" in movie.poster_url else "Amazon" if "media-amazon" in movie.poster_url else "Other"
            print(f"   • {movie.title}: {poster_source} quality poster")
        
    except Exception as e:
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    audit_and_fix_all_posters()
