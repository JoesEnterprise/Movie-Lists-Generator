import sqlite3
import os

def init_database():
    """Initialize the SQLite database with movies table"""
    db_path = 'movies.db'
    
    # Create connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create movies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        genre TEXT,
        year INTEGER,
        rating REAL
    )
    ''')
    
    # Add sample movies if table is empty
    cursor.execute("SELECT COUNT(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        sample_movies = [
            ("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "Drama", 1994, 9.3),
            ("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant youngest son.", "Crime, Drama", 1972, 9.2),
            ("The Dark Knight", "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological tests.", "Action, Crime, Drama", 2008, 9.0),
            ("Inception", "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea.", "Action, Sci-Fi, Thriller", 2010, 8.8),
            ("Pulp Fiction", "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", "Crime, Drama", 1994, 8.9),
            ("Forrest Gump", "The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.", "Drama, Romance", 1994, 8.8),
            ("The Matrix", "A computer programmer discovers that reality as he knows it is a simulation created by machines.", "Action, Sci-Fi", 1999, 8.7),
            ("Interstellar", "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", "Adventure, Drama, Sci-Fi", 2014, 8.6),
            ("The Lion King", "Lion prince Simba flees his kingdom after the death of his father, only to discover the truth about his past and his rightful place in the Circle of Life.", "Animation, Adventure, Drama", 1994, 8.5),
            ("Avengers: Endgame", "After the devastating events, the Avengers assemble once more to reverse Thanos' actions and restore balance to the universe.", "Action, Adventure, Drama", 2019, 8.4),
        ]
        
        cursor.executemany('''
        INSERT INTO movies (title, description, genre, year, rating)
        VALUES (?, ?, ?, ?, ?)
        ''', sample_movies)
        
        print(f"✓ Database initialized with {len(sample_movies)} sample movies!")
    else:
        print("✓ Database already exists with movies!")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
