import sqlite3

def create_database():
    """Create an in-memory SQLite database with three tables demonstrating many-to-many relationship"""
    
    # Create in-memory database
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    
    print("Creating tables...")
    
    # Create Actors table
    cur.execute('''
    CREATE TABLE Actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER
    )
    ''')
    
    # Create Movies table
    cur.execute('''
    CREATE TABLE Movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,
        genre TEXT
    )
    ''')
    
    # Create junction table for many-to-many relationship
    cur.execute('''
    CREATE TABLE Movies_Actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        actor_id INTEGER,
        role TEXT,
        FOREIGN KEY (movie_id) REFERENCES Movies (id),
        FOREIGN KEY (actor_id) REFERENCES Actors (id)
    )
    ''')
    
    return conn, cur

def insert_sample_data(cur):
    """Insert sample data into all three tables"""
    
    print("\nInserting sample data...")
    
    # Insert actors
    actors = [
        ('Leonardo DiCaprio', 1974),
        ('Kate Winslet', 1975),
        ('Morgan Freeman', 1937),
        ('Brad Pitt', 1963),
        ('Margot Robbie', 1990),
        ('Christian Bale', 1974)
    ]
    
    cur.executemany('INSERT INTO Actors (name, birth_year) VALUES (?, ?)', actors)
    
    # Insert movies
    movies = [
        ('Titanic', 1997, 'Romance/Drama'),
        ('The Wolf of Wall Street', 2013, 'Biography/Comedy'),
        ('Se7en', 1995, 'Crime/Thriller'),
        ('Fight Club', 1999, 'Drama'),
        ('The Shawshank Redemption', 1994, 'Drama'),
        ('The Dark Knight', 2008, 'Action/Crime')
    ]
    
    cur.executemany('INSERT INTO Movies (title, release_year, genre) VALUES (?, ?, ?)', movies)
    
    # Insert many-to-many relationships
    # Format: (movie_id, actor_id, role)
    movie_actors = [
        # Titanic (movie_id: 1)
        (1, 1, 'Jack Dawson'),    # Leonardo DiCaprio
        (1, 2, 'Rose DeWitt'),    # Kate Winslet
        
        # The Wolf of Wall Street (movie_id: 2)
        (2, 1, 'Jordan Belfort'), # Leonardo DiCaprio
        (2, 5, 'Naomi Lapaglia'), # Margot Robbie
        
        # Se7en (movie_id: 3)
        (3, 3, 'Detective Somerset'), # Morgan Freeman
        (3, 4, 'Detective Mills'),    # Brad Pitt
        
        # Fight Club (movie_id: 4)
        (4, 4, 'Tyler Durden'),    # Brad Pitt
        (4, 6, 'The Narrator'),   # Christian Bale
        
        # The Shawshank Redemption (movie_id: 5)
        (5, 3, 'Ellis Boyd Redding'), # Morgan Freeman
    ]
    
    cur.executemany('INSERT INTO Movies_Actors (movie_id, actor_id, role) VALUES (?, ?, ?)', movie_actors)
    
    print("Sample data inserted successfully!")

def demonstrate_queries(cur):
    """Demonstrate various queries showing many-to-many relationships"""
    
    print("\n" + "="*60)
    print("DEMONSTRATING MANY-TO-MANY RELATIONSHIP QUERIES")
    print("="*60)
    
    # Query 1: Show all actors in a specific movie
    print("\n1. All actors in 'Titanic':")
    print("-" * 40)
    cur.execute('''
    SELECT a.name, ma.role
    FROM Actors a
    JOIN Movies_Actors ma ON a.id = ma.actor_id
    JOIN Movies m ON ma.movie_id = m.id
    WHERE m.title = 'Titanic'
    ''')
    
    for row in cur.fetchall():
        print(f"   {row[0]} as {row[1]}")
    
    # Query 2: Show all movies for a specific actor
    print("\n2. All movies featuring Leonardo DiCaprio:")
    print("-" * 40)
    cur.execute('''
    SELECT m.title, m.release_year, ma.role
    FROM Movies m
    JOIN Movies_Actors ma ON m.id = ma.movie_id
    JOIN Actors a ON ma.actor_id = a.id
    WHERE a.name = 'Leonardo DiCaprio'
    ''')
    
    for row in cur.fetchall():
        print(f"   {row[0]} ({row[1]}) as {row[2]}")
    
    # Query 3: Show all actor-movie pairs
    print("\n3. Complete actor-movie relationships:")
    print("-" * 40)
    cur.execute('''
    SELECT a.name, m.title, ma.role
    FROM Actors a
    JOIN Movies_Actors ma ON a.id = ma.actor_id
    JOIN Movies m ON ma.movie_id = m.id
    ORDER BY a.name, m.title
    ''')
    
    for row in cur.fetchall():
        print(f"   {row[0]} in '{row[1]}' as {row[2]}")
    
    # Query 4: Count movies per actor
    print("\n4. Number of movies per actor:")
    print("-" * 40)
    cur.execute('''
    SELECT a.name, COUNT(ma.movie_id) as movie_count
    FROM Actors a
    LEFT JOIN Movies_Actors ma ON a.id = ma.actor_id
    GROUP BY a.id, a.name
    ORDER BY movie_count DESC, a.name
    ''')
    
    for row in cur.fetchall():
        print(f"   {row[0]}: {row[1]} movie(s)")
    
    # Query 5: Count actors per movie
    print("\n5. Number of actors per movie:")
    print("-" * 40)
    cur.execute('''
    SELECT m.title, COUNT(ma.actor_id) as actor_count
    FROM Movies m
    LEFT JOIN Movies_Actors ma ON m.id = ma.movie_id
    GROUP BY m.id, m.title
    ORDER BY actor_count DESC, m.title
    ''')
    
    for row in cur.fetchall():
        print(f"   {row[0]}: {row[1]} actor(s)")
    
    # Query 6: Find actors who worked together
    print("\n6. Actors who worked together in the same movie:")
    print("-" * 40)
    cur.execute('''
    SELECT DISTINCT a1.name, a2.name, m.title
    FROM Movies_Actors ma1
    JOIN Movies_Actors ma2 ON ma1.movie_id = ma2.movie_id AND ma1.actor_id < ma2.actor_id
    JOIN Actors a1 ON ma1.actor_id = a1.id
    JOIN Actors a2 ON ma2.actor_id = a2.id
    JOIN Movies m ON ma1.movie_id = m.id
    ORDER BY m.title
    ''')
    
    for row in cur.fetchall():
        print(f"   {row[0]} & {row[1]} in '{row[2]}'")

def show_table_structures(cur):
    """Display the structure of all tables"""
    
    print("\n" + "="*60)
    print("TABLE STRUCTURES")
    print("="*60)
    
    tables = ['Actors', 'Movies', 'Movies_Actors']
    
    for table in tables:
        print(f"\n{table} table structure:")
        print("-" * 30)
        cur.execute(f"PRAGMA table_info({table})")
        columns = cur.fetchall()
        for col in columns:
            nullable = "NOT NULL" if col[3] else "NULL"
            primary_key = " (PRIMARY KEY)" if col[5] else ""
            print(f"   {col[1]} {col[2]} {nullable}{primary_key}")

def main():
    """Main function to demonstrate many-to-many relationships"""
    
    print("SQLite Many-to-Many Relationship Demonstration")
    print("Tables: Actors, Movies, Movies_Actors (junction table)")
    print("="*60)
    
    # Create database and tables
    conn, cur = create_database()
    
    # Show table structures
    show_table_structures(cur)
    
    # Insert sample data
    insert_sample_data(cur)
    
    # Demonstrate various queries
    demonstrate_queries(cur)
    
    print("\n" + "="*60)
    print("Many-to-many relationship demonstration completed!")
    print("="*60)
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
