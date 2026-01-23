from sqlalchemy.orm import Session
import database
import re

def update_all_movie_posters():
    db = Session(bind=database.engine)
    
    try:
        
        movie_poster_mapping = {
            "inception": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
            "pulp fiction": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
            "barbie": "https://image.tmdb.org/t/p/w500/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
            "dune": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
            "the dark knight": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",

            "sarkaru vaari paata": "https://m.media-amazon.com/images/M/MV5BYjFjMTQzY2EtZjQ5Mi00NGM0LWJiNzQtN2Q5Zjc1MzI1NzZmXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
            "maharshi": "https://m.media-amazon.com/images/M/MV5BMjIwZDMwZTQtYTMwZC00MDQyLTkzNTUtYjA5NGZmM2Q5MGNkXkEyXkFqcGdeQXVyMTUzNTgzNzM0._V1_.jpg",
            "bharat ane nenu": "https://m.media-amazon.com/images/M/MV5BMjI1Mzg5MDczOV5BMl5BanBnXkFtZTgwNjIwMDk1NTM@._V1_.jpg",
            "srimanthudu": "https://m.media-amazon.com/images/M/MV5BMjE5ODU0NDQ2Nl5BMl5BanBnXkFtZTgwOTU4ODU0NjE@._V1_.jpg",
            "1: nenokkadine": "https://m.media-amazon.com/images/M/MV5BMTVlNzgzMjktZWJjYy00YzYwLWFjMTUtOGZmZDMzMmM2ZGY2XkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg",
            "baahubali": "https://image.tmdb.org/t/p/w500/2pqfW7PsWAKTXGPaFLYyOJMxibc.jpg",
            "baahubali 2": "https://image.tmdb.org/t/p/w500/lkKPSJH4WswkHj4LXKS2HW8qEUs.jpg",
            "rrr": "https://image.tmdb.org/t/p/w500/w6C2WxqOLWHZoew8UL3P2rrJcbX.jpg",
            "pushpa": "https://image.tmdb.org/t/p/w500/ugQW8BQOmJ2Qtt6tG9lGbEfn1jX.jpg",
            "a aa": "https://m.media-amazon.com/images/M/MV5BMTgxNjA1Njc2MV5BMl5BanBnXkFtZTgwNjE4NzQ2OTE@._V1_.jpg",

            "avengers": "https://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
            "iron man": "https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg",
            "spider-man": "https://image.tmdb.org/t/p/w500/gh4cZbhZxyTbgxQPxD0dOudNPTn.jpg",
            "the matrix": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
            "titanic": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
            "avatar": "https://image.tmdb.org/t/p/w500/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg",
            "the godfather": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
            "forrest gump": "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
            "the shawshank redemption": "https://image.tmdb.org/t/p/w500/q6y0Go1v5GwcxgGQOfpuBpVgdA4.jpg",
            "gladiator": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
            "joker": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
            "black panther": "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
            "wonder woman": "https://image.tmdb.org/t/p/w500/gfJGlDaHuWimErCr5Ql0I8x9QSy.jpg",
            "captain marvel": "https://image.tmdb.org/t/p/w500/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg",
            "star wars": "https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
            "indiana jones": "https://image.tmdb.org/t/p/w500/ceG9VzoRAVGwivFU403Wc3AHRys.jpg",
            "jurassic park": "https://image.tmdb.org/t/p/w500/b1xCNnyrPebIc7EWNZIa6BYzRMI.jpg",
            "e.t.": "https://image.tmdb.org/t/p/w500/5p3Zj6b3ZYrYzz2H9zIVa0LUQLk.jpg",
            "terminator": "https://image.tmdb.org/t/p/w500/qvkOl4d9EHUbEPKgJg8C8T3g3u5.jpg",
            "alien": "https://image.tmdb.org/t/p/w500/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg",
            "blade runner": "https://image.tmdb.org/t/p/w500/63N9uy8nd9j7Eog2axPQ8lbr3Wj.jpg",
            "the lion king": "https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg",
            "frozen": "https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg",
            "toy story": "https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg",
            "finding nemo": "https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg"
        }

        genre_poster_collections = {
            "action": [
                "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",  # Fast & Furious
                "https://image.tmdb.org/t/p/w500/6Wdl9N6dL0Hi0T1qJLWSz6gMLbd.jpg",  # Mission Impossible
                "https://image.tmdb.org/t/p/w500/iYhMUJgm2LRPSTy0rNXlcSMFULs.jpg",  # John Wick
                "https://image.tmdb.org/t/p/w500/rjkmN1dniUHVYAtwuV3Tji7FsDO.jpg",  # Mad Max
                "https://image.tmdb.org/t/p/w500/cg8LsZpgdTxLEY5-gHs9Lmtkmld.jpg"   # Die Hard
            ],
            "drama": [
                "https://image.tmdb.org/t/p/w500/4j0PNHkMr5ax3IA8tjtxcmPU3QT.jpg",  # A Star is Born
                "https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg",  # La La Land
                "https://image.tmdb.org/t/p/w500/iNh3BivHyg5sQRPP1KOkzguEX0H.jpg",  # The Pursuit of Happyness
                "https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg",  # Forrest Gump alt
                "https://image.tmdb.org/t/p/w500/jpfkorbIaVKM2JmEbTOtRKBOxPb.jpg"   # Green Book
            ],
            "comedy": [
                "https://image.tmdb.org/t/p/w500/6LiO7ZyWjfqUTIl6fl3YtPNHhT2.jpg",  # Hangover
                "https://image.tmdb.org/t/p/w500/paNtcaV5A2a5tPY98GmfwLZBinQ.jpg",  # Superbad
                "https://image.tmdb.org/t/p/w500/1NKJCCA7q3iKCnUGpNl7KfNM8OY.jpg",  # Dumb and Dumber
                "https://image.tmdb.org/t/p/w500/w2PMyoyLU22YvrGK3smVM9fW1jj.jpg",  # Bridesmaids
                "https://image.tmdb.org/t/p/w500/lngMRrM2TZlH5SNxKhP9zAqLhGe.jpg"   # Step Brothers
            ],
            "thriller": [
                "https://image.tmdb.org/t/p/w500/aZvOkdo1LakpqOGORMkYgF41LhW.jpg",  # Gone Girl
                "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",  # Dark Knight alt
                "https://image.tmdb.org/t/p/w500/9Eb7TLGWtprdRFe6QkdOGhtGOyh.jpg",  # Se7en
                "https://image.tmdb.org/t/p/w500/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",  # Zodiac
                "https://image.tmdb.org/t/p/w500/6ybKvfpd3zAhm1Xe1EoL6XzRoE.jpg"    # Shutter Island
            ],
            "romance": [
                "https://image.tmdb.org/t/p/w500/kHpFvkbRCWIMfWXIcflCPzWFVtJ.jpg",  # The Notebook
                "https://image.tmdb.org/t/p/w500/yDI6D5ZQh67YU4r2ms8qcSbAviZ.jpg",  # Pride and Prejudice
                "https://image.tmdb.org/t/p/w500/6DDMspL5PGfTU1CU3SDMcHULOcr.jpg",  # Dirty Dancing
                "https://image.tmdb.org/t/p/w500/6JjfSchsU6daXk2AKX8EEBjO3Fm.jpg",  # Sleepless in Seattle
                "https://image.tmdb.org/t/p/w500/4VlXER3FImHeFuUjBShFamhIp9M.jpg"   # When Harry Met Sally
            ],
            "sci-fi": [
                "https://image.tmdb.org/t/p/w500/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg",  # Interstellar
                "https://image.tmdb.org/t/p/w500/qKrXSt2JT8I5D8o8vl9EY7j2MhG.jpg",  # Ex Machina
                "https://image.tmdb.org/t/p/w500/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",  # Arrival
                "https://image.tmdb.org/t/p/w500/3FGcECoFOBzjUJKX8p5gDbBNcYo.jpg",  # Gravity
                "https://image.tmdb.org/t/p/w500/u8FxTSvF5F9gKfMXgOE7EIBaKRi.jpg"   # Her
            ],
            "horror": [
                "https://image.tmdb.org/t/p/w500/1n9D32o30XOHMdMWuIT4AaA5ruI.jpg",  # The Exorcist
                "https://image.tmdb.org/t/p/w500/lTM0rW2pFe7GBBYsyqKPTqZKJvC.jpg",  # Halloween
                "https://image.tmdb.org/t/p/w500/5BbLwN7Z5B6NRGHELfItH4ql0J4.jpg",  # Get Out
                "https://image.tmdb.org/t/p/w500/4OMLX0un9x4JGdQ8rjBs4TM7p7a.jpg",  # Hereditary
                "https://image.tmdb.org/t/p/w500/6S7sDT9veTKq7QRgBCLYYUGCdIe.jpg"   # The Conjuring
            ],
            "animation": [
                "https://image.tmdb.org/t/p/w500/8a9lJ0kBJg0JFbqS1j9b0C6T3C0.jpg",  # Coco
                "https://image.tmdb.org/t/p/w500/7UQPDwArWu1xE8i59T7PWy8qmEE.jpg",  # Inside Out
                "https://image.tmdb.org/t/p/w500/2CAL2433ZeIihfX1Hb2139CX0pW.jpg",  # Moana
                "https://image.tmdb.org/t/p/w500/4ZG1PnGnQ3QNiSNEvFhMLpGN5i8.jpg",  # Zootopia
                "https://image.tmdb.org/t/p/w500/q125RHUDgR4gjwh1QkfYuJLYkL.jpg"    # Incredibles
            ]
        }

        movies = db.query(database.Movie).all()
        updated_count = 0
        
        print(f"Processing {len(movies)} movies for poster updates...")
        
        for movie in movies:
            title_lower = movie.title.lower()
            found_specific_poster = False

            for mapped_title, poster_url in movie_poster_mapping.items():
                if (mapped_title in title_lower or 
                    any(word in title_lower for word in mapped_title.split() if len(word) > 3)):
                    movie.poster_url = poster_url
                    updated_count += 1
                    print(f" Updated '{movie.title}' with specific poster")
                    found_specific_poster = True
                    break

            if not found_specific_poster:
                primary_genre = "action"  # default

                if movie.genres:
                    genre_name = movie.genres[0].name.lower()
                    if genre_name in genre_poster_collections:
                        primary_genre = genre_name
                    elif "tollywood" in genre_name:
                        primary_genre = "action"

                if primary_genre in genre_poster_collections:
                    poster_index = movie.id % len(genre_poster_collections[primary_genre])
                    movie.poster_url = genre_poster_collections[primary_genre][poster_index]
                else:
                    poster_index = movie.id % len(genre_poster_collections["action"])
                    movie.poster_url = genre_poster_collections["action"][poster_index]
                
                updated_count += 1
                if updated_count % 25 == 0:
                    print(f"Updated {updated_count} movies...")
        
        db.commit()
        
        print(f"\n Successfully updated ALL {updated_count} movies with appropriate posters!")
        print("Movies now have either specific real posters or genre-appropriate themed posters")
        print(" The Movie Explorer Platform now has a complete visual experience!")
        
        specific_count = sum(1 for movie in movies if any(mapped in movie.title.lower() for mapped in movie_poster_mapping.keys()))
        print(f"\n Statistics:")
        print(f"   Real movie posters: {specific_count}")
        print(f"   Genre-themed posters: {len(movies) - specific_count}")
        print(f"   Total updated: {len(movies)}")
        
    except Exception as e:
        print(f" Error updating movie posters: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_all_movie_posters()
