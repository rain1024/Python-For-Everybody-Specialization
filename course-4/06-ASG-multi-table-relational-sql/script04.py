import sqlite3

def main():
    # Create an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    print("=== SQLite Lookup Table Demonstration ===\n")
    
    # Create the genres table (lookup table)
    cursor.execute('''
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')
    
    # Create the tracks table with foreign key to genres
    cursor.execute('''
        CREATE TABLE tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            duration INTEGER,  -- in seconds
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres (id)
        )
    ''')
    
    print("✓ Tables created successfully\n")
    
    # Insert sample data into genres table (lookup table)
    genres_data = [
        ('Rock',),
        ('Pop',),
        ('Jazz',),
        ('Classical',),
        ('Hip Hop',),
        ('Electronic',)
    ]
    
    cursor.executemany('INSERT INTO genres (name) VALUES (?)', genres_data)
    print("✓ Genres data inserted")
    
    # Display genres table
    print("\n--- Genres Table (Lookup Table) ---")
    cursor.execute('SELECT * FROM genres')
    genres = cursor.fetchall()
    for genre in genres:
        print(f"ID: {genre[0]}, Name: {genre[1]}")
    
    # Insert sample data into tracks table
    tracks_data = [
        ('Bohemian Rhapsody', 'Queen', 355, 1),  # Rock
        ('Billie Jean', 'Michael Jackson', 294, 2),  # Pop
        ('Take Five', 'Dave Brubeck', 324, 3),  # Jazz
        ('Eine kleine Nachtmusik', 'Mozart', 360, 4),  # Classical
        ('Lose Yourself', 'Eminem', 326, 5),  # Hip Hop
        ('One More Time', 'Daft Punk', 320, 6),  # Electronic
        ('Stairway to Heaven', 'Led Zeppelin', 482, 1),  # Rock
        ('Shape of You', 'Ed Sheeran', 233, 2),  # Pop
        ('Blue in Green', 'Miles Davis', 337, 3),  # Jazz
    ]
    
    cursor.executemany('INSERT INTO tracks (title, artist, duration, genre_id) VALUES (?, ?, ?, ?)', tracks_data)
    print("\n✓ Tracks data inserted")
    
    # Demonstrate various queries using the lookup table
    print("\n=== Query Examples ===\n")
    
    # 1. Simple join to show tracks with their genres
    print("1. All tracks with their genres:")
    cursor.execute('''
        SELECT tracks.title, tracks.artist, genres.name as genre, tracks.duration
        FROM tracks
        JOIN genres ON tracks.genre_id = genres.id
        ORDER BY tracks.title
    ''')
    results = cursor.fetchall()
    for track in results:
        print(f"   {track[0]} by {track[1]} - Genre: {track[2]} ({track[3]}s)")
    
    # 2. Count tracks by genre
    print("\n2. Number of tracks per genre:")
    cursor.execute('''
        SELECT genres.name, COUNT(tracks.id) as track_count
        FROM genres
        LEFT JOIN tracks ON genres.id = tracks.genre_id
        GROUP BY genres.id, genres.name
        ORDER BY track_count DESC
    ''')
    results = cursor.fetchall()
    for genre_stat in results:
        print(f"   {genre_stat[0]}: {genre_stat[1]} tracks")
    
    # 3. Find all Rock tracks
    print("\n3. All Rock tracks:")
    cursor.execute('''
        SELECT tracks.title, tracks.artist, tracks.duration
        FROM tracks
        JOIN genres ON tracks.genre_id = genres.id
        WHERE genres.name = 'Rock'
        ORDER BY tracks.duration DESC
    ''')
    results = cursor.fetchall()
    for track in results:
        print(f"   {track[0]} by {track[1]} ({track[2]}s)")
    
    # 4. Average track duration by genre
    print("\n4. Average track duration by genre:")
    cursor.execute('''
        SELECT genres.name, 
               ROUND(AVG(tracks.duration), 1) as avg_duration,
               COUNT(tracks.id) as track_count
        FROM genres
        JOIN tracks ON genres.id = tracks.genre_id
        GROUP BY genres.id, genres.name
        ORDER BY avg_duration DESC
    ''')
    results = cursor.fetchall()
    for genre_avg in results:
        print(f"   {genre_avg[0]}: {genre_avg[1]}s average ({genre_avg[2]} tracks)")
    
    # 5. Find genres with no tracks (demonstrate LEFT JOIN)
    print("\n5. Genres with no tracks:")
    cursor.execute('''
        SELECT genres.name
        FROM genres
        LEFT JOIN tracks ON genres.id = tracks.genre_id
        WHERE tracks.id IS NULL
    ''')
    results = cursor.fetchall()
    if results:
        for genre in results:
            print(f"   {genre[0]}")
    else:
        print("   (All genres have at least one track)")
    
    # 6. Demonstrate the benefit of lookup tables - add a new track
    print("\n6. Adding a new track with existing genre:")
    cursor.execute('INSERT INTO tracks (title, artist, duration, genre_id) VALUES (?, ?, ?, ?)',
                  ('Hotel California', 'Eagles', 391, 1))  # Rock genre
    
    cursor.execute('''
        SELECT tracks.title, tracks.artist, genres.name as genre
        FROM tracks
        JOIN genres ON tracks.genre_id = genres.id
        WHERE tracks.title = 'Hotel California'
    ''')
    result = cursor.fetchone()
    print(f"   Added: {result[0]} by {result[1]} - Genre: {result[2]}")
    
    # 7. Show the power of lookup tables - update genre name affects all tracks
    print("\n7. Updating genre name (affects all tracks with that genre):")
    print("   Changing 'Hip Hop' to 'Rap'...")
    cursor.execute("UPDATE genres SET name = 'Rap' WHERE name = 'Hip Hop'")
    
    cursor.execute('''
        SELECT tracks.title, tracks.artist, genres.name as genre
        FROM tracks
        JOIN genres ON tracks.genre_id = genres.id
        WHERE genres.name = 'Rap'
    ''')
    results = cursor.fetchall()
    for track in results:
        print(f"   {track[0]} by {track[1]} - Genre: {track[2]}")
    
    print("\n=== Lookup Table Benefits Demonstrated ===")
    print("✓ Data consistency: Genre names stored once in lookup table")
    print("✓ Storage efficiency: Foreign key references instead of repeated strings")
    print("✓ Easy updates: Change genre name once, affects all related tracks")
    print("✓ Data integrity: Foreign key constraints prevent invalid references")
    
    # Close the connection
    conn.close()
    print("\n✓ Database connection closed")

if __name__ == "__main__":
    main()
