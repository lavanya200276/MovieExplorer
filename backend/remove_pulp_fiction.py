from sqlalchemy.orm import Session
import database

def remove_pulp_fiction():
    db = Session(bind=database.engine)
    
    try:
        # Find Pulp Fiction movie
        pulp_fiction = db.query(database.Movie).filter(database.Movie.title.ilike('%pulp fiction%')).first()
        
        if pulp_fiction:
            print(f"Found movie: {pulp_fiction.title} (ID: {pulp_fiction.id})")
            
            # Remove the movie (relationships will be handled by cascade)
            db.delete(pulp_fiction)
            db.commit()
            
            print(f"✅ Successfully removed '{pulp_fiction.title}' from the database")
            
            # Check total movies count after deletion
            total_movies = db.query(database.Movie).count()
            print(f"📊 Total movies remaining: {total_movies}")
            
        else:
            print("❌ Pulp Fiction movie not found in database")
            
    except Exception as e:
        print(f"❌ Error removing Pulp Fiction: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    remove_pulp_fiction()
