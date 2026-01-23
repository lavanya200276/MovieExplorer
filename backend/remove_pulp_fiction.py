from sqlalchemy.orm import Session
import database

def remove_pulp_fiction():
    db = Session(bind=database.engine)
    
    try:
        pulp_fiction = db.query(database.Movie).filter(database.Movie.title.ilike('%pulp fiction%')).first()
        
        if pulp_fiction:
            db.delete(pulp_fiction)
            db.commit()
            total_movies = db.query(database.Movie).count()
        else:
            print(" Pulp Fiction movie not found in database")
            
    except Exception as e:
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    remove_pulp_fiction()
