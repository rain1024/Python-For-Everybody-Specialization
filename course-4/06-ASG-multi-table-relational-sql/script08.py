import sqlite3

def main():
    # Create an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    print("=== SQLite JOIN Demonstration ===\n")
    
    # Create Authors table
    cursor.execute('''
        CREATE TABLE Authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            bio TEXT
        )
    ''')
    
    # Create Posts table with foreign key reference to Authors
    cursor.execute('''
        CREATE TABLE Posts (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT,
            author_id INTEGER,
            views INTEGER DEFAULT 0,
            FOREIGN KEY (author_id) REFERENCES Authors (id)
        )
    ''')
    
    # Insert sample authors
    authors_data = [
        (1, 'Alice Johnson', 'alice@example.com', 'Tech blogger and software engineer'),
        (2, 'Bob Smith', 'bob@example.com', 'Data science enthusiast'),
        (3, 'Carol Davis', 'carol@example.com', 'Web development expert'),
        (4, 'David Wilson', 'david@example.com', 'Mobile app developer')
    ]
    
    cursor.executemany('INSERT INTO Authors (id, name, email, bio) VALUES (?, ?, ?, ?)', authors_data)
    
    # Insert sample posts
    posts_data = [
        (1, 'Introduction to Python', 'Python is a versatile programming language...', 1, 150),
        (2, 'Data Structures in Python', 'Understanding lists, dictionaries, and sets...', 1, 230),
        (3, 'Machine Learning Basics', 'Getting started with ML using Python...', 2, 180),
        (4, 'SQL vs NoSQL', 'Comparing relational and non-relational databases...', 2, 95),
        (5, 'CSS Grid Layout', 'Modern web layout techniques...', 3, 120),
        (6, 'React Hooks Explained', 'Understanding useState and useEffect...', 3, 200),
        # Note: No posts for David Wilson (id=4) to demonstrate LEFT JOIN
    ]
    
    cursor.executemany('INSERT INTO Posts (id, title, content, author_id, views) VALUES (?, ?, ?, ?, ?)', posts_data)
    
    print("Tables created and sample data inserted.\n")
    
    # Display individual tables first
    print("=== AUTHORS TABLE ===")
    cursor.execute('SELECT * FROM Authors')
    authors = cursor.fetchall()
    print(f"{'ID':<3} {'Name':<15} {'Email':<20} {'Bio':<30}")
    print("-" * 70)
    for author in authors:
        print(f"{author[0]:<3} {author[1]:<15} {author[2]:<20} {author[3]:<30}")
    
    print("\n=== POSTS TABLE ===")
    cursor.execute('SELECT * FROM Posts')
    posts = cursor.fetchall()
    print(f"{'ID':<3} {'Title':<25} {'Author ID':<10} {'Views':<8}")
    print("-" * 50)
    for post in posts:
        print(f"{post[0]:<3} {post[1]:<25} {post[3]:<10} {post[4]:<8}")
    
    # Demonstrate different types of JOINs
    print("\n" + "="*60)
    print("=== JOIN DEMONSTRATIONS ===")
    print("="*60)
    
    # 1. INNER JOIN - Shows only authors who have posts
    print("\n1. INNER JOIN - Authors with their posts:")
    print("-" * 50)
    cursor.execute('''
        SELECT Authors.name, Authors.email, Posts.title, Posts.views
        FROM Authors
        INNER JOIN Posts ON Authors.id = Posts.author_id
        ORDER BY Authors.name, Posts.views DESC
    ''')
    
    results = cursor.fetchall()
    print(f"{'Author':<15} {'Email':<20} {'Post Title':<25} {'Views':<8}")
    print("-" * 70)
    for row in results:
        print(f"{row[0]:<15} {row[1]:<20} {row[2]:<25} {row[3]:<8}")
    
    # 2. LEFT JOIN - Shows all authors, even those without posts
    print("\n2. LEFT JOIN - All authors and their posts (if any):")
    print("-" * 50)
    cursor.execute('''
        SELECT Authors.name, Authors.email, Posts.title, Posts.views
        FROM Authors
        LEFT JOIN Posts ON Authors.id = Posts.author_id
        ORDER BY Authors.name, Posts.views DESC
    ''')
    
    results = cursor.fetchall()
    print(f"{'Author':<15} {'Email':<20} {'Post Title':<25} {'Views':<8}")
    print("-" * 70)
    for row in results:
        post_title = row[2] if row[2] else "No posts"
        views = row[3] if row[3] else "N/A"
        print(f"{row[0]:<15} {row[1]:<20} {post_title:<25} {str(views):<8}")
    
    # 3. Aggregate with JOIN - Count posts per author
    print("\n3. Aggregate with JOIN - Post count per author:")
    print("-" * 40)
    cursor.execute('''
        SELECT Authors.name, COUNT(Posts.id) as post_count, 
               COALESCE(SUM(Posts.views), 0) as total_views
        FROM Authors
        LEFT JOIN Posts ON Authors.id = Posts.author_id
        GROUP BY Authors.id, Authors.name
        ORDER BY post_count DESC, total_views DESC
    ''')
    
    results = cursor.fetchall()
    print(f"{'Author':<15} {'Posts':<8} {'Total Views':<12}")
    print("-" * 40)
    for row in results:
        print(f"{row[0]:<15} {row[1]:<8} {row[2]:<12}")
    
    # 4. Advanced JOIN with WHERE clause
    print("\n4. JOIN with WHERE - Popular posts (>100 views):")
    print("-" * 50)
    cursor.execute('''
        SELECT Authors.name, Posts.title, Posts.views
        FROM Authors
        INNER JOIN Posts ON Authors.id = Posts.author_id
        WHERE Posts.views > 100
        ORDER BY Posts.views DESC
    ''')
    
    results = cursor.fetchall()
    print(f"{'Author':<15} {'Post Title':<25} {'Views':<8}")
    print("-" * 50)
    for row in results:
        print(f"{row[0]:<15} {row[1]:<25} {row[2]:<8}")
    
    # 5. Subquery with JOIN
    print("\n5. Authors with above-average post views:")
    print("-" * 40)
    cursor.execute('''
        SELECT DISTINCT Authors.name, Authors.email
        FROM Authors
        INNER JOIN Posts ON Authors.id = Posts.author_id
        WHERE Posts.views > (SELECT AVG(views) FROM Posts)
        ORDER BY Authors.name
    ''')
    
    results = cursor.fetchall()
    print(f"{'Author':<15} {'Email':<20}")
    print("-" * 40)
    for row in results:
        print(f"{row[0]:<15} {row[1]:<20}")
    
    # Calculate and show average views for context
    cursor.execute('SELECT AVG(views) FROM Posts')
    avg_views = cursor.fetchone()[0]
    print(f"\n(Average post views: {avg_views:.1f})")
    
    print("\n" + "="*60)
    print("=== JOIN CONCEPTS EXPLAINED ===")
    print("="*60)
    print("• INNER JOIN: Returns only matching records from both tables")
    print("• LEFT JOIN: Returns all records from left table + matching from right")
    print("• RIGHT JOIN: Returns all records from right table + matching from left")
    print("• FULL OUTER JOIN: Returns all records when there's a match in either table")
    print("\nNote: SQLite supports INNER JOIN and LEFT JOIN natively.")
    print("RIGHT JOIN can be simulated by swapping table order in LEFT JOIN.")
    
    # Close the database connection
    conn.close()
    print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()
