#!/usr/bin/env python3
"""
SQLite Foreign Key Demonstration
Simple program showing relationship between Authors and Posts tables
"""

import sqlite3

def main():
    # Create in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Enable foreign key constraints (disabled by default in SQLite)
    cursor.execute('PRAGMA foreign_keys = ON')
    
    print("=== SQLite Foreign Key Demonstration ===\n")
    
    # Create Authors table
    cursor.execute('''
        CREATE TABLE Authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("✓ Authors table created")
    
    # Create Posts table with foreign key reference
    cursor.execute('''
        CREATE TABLE Posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (author_id) REFERENCES Authors (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        )
    ''')
    print("✓ Posts table created with foreign key constraint\n")
    
    # Insert sample authors
    authors_data = [
        ('Alice Johnson', 'alice@example.com'),
        ('Bob Smith', 'bob@example.com'),
        ('Carol Davis', 'carol@example.com')
    ]
    
    cursor.executemany('INSERT INTO Authors (name, email) VALUES (?, ?)', authors_data)
    print("✓ Sample authors inserted:")
    
    # Display authors
    cursor.execute('SELECT id, name, email FROM Authors')
    for row in cursor.fetchall():
        print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    
    print()
    
    # Insert sample posts
    posts_data = [
        ('Getting Started with Python', 'Python is a great programming language...', 1),
        ('Advanced SQL Techniques', 'Today we will explore complex SQL queries...', 1),
        ('Web Development Basics', 'HTML, CSS, and JavaScript fundamentals...', 2),
        ('Database Design Principles', 'Good database design is crucial...', 3),
        ('Python Data Structures', 'Lists, dictionaries, and sets in Python...', 1)
    ]
    
    cursor.executemany('INSERT INTO Posts (title, content, author_id) VALUES (?, ?, ?)', posts_data)
    print("✓ Sample posts inserted\n")
    
    # Demonstrate foreign key relationship with JOIN query
    print("=== Posts with Author Information (JOIN Query) ===")
    cursor.execute('''
        SELECT p.id, p.title, a.name as author_name, p.created_at
        FROM Posts p
        JOIN Authors a ON p.author_id = a.id
        ORDER BY p.created_at
    ''')
    
    for row in cursor.fetchall():
        print(f"Post ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Author: {row[2]}")
        print(f"Created: {row[3]}")
        print("-" * 40)
    
    # Show posts count per author
    print("\n=== Posts Count per Author ===")
    cursor.execute('''
        SELECT a.name, COUNT(p.id) as post_count
        FROM Authors a
        LEFT JOIN Posts p ON a.id = p.author_id
        GROUP BY a.id, a.name
        ORDER BY post_count DESC
    ''')
    
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} posts")
    
    # Demonstrate foreign key constraint enforcement
    print("\n=== Testing Foreign Key Constraints ===")
    
    try:
        # Try to insert post with non-existent author_id
        cursor.execute('INSERT INTO Posts (title, content, author_id) VALUES (?, ?, ?)', 
                      ('Invalid Post', 'This should fail', 999))
        print("❌ This shouldn't happen - foreign key constraint failed!")
    except sqlite3.IntegrityError as e:
        print(f"✓ Foreign key constraint working: {e}")
    
    # Demonstrate CASCADE DELETE
    print("\n=== Testing CASCADE DELETE ===")
    print("Before deletion:")
    cursor.execute('SELECT COUNT(*) FROM Posts WHERE author_id = 2')
    posts_count = cursor.fetchone()[0]
    print(f"Posts by author ID 2: {posts_count}")
    
    # Delete author - should cascade delete their posts
    cursor.execute('DELETE FROM Authors WHERE id = 2')
    
    print("After deleting author ID 2:")
    cursor.execute('SELECT COUNT(*) FROM Posts WHERE author_id = 2')
    posts_count = cursor.fetchone()[0]
    print(f"Posts by author ID 2: {posts_count}")
    print("✓ CASCADE DELETE working - posts were automatically deleted")
    
    # Show final state
    print("\n=== Final Database State ===")
    cursor.execute('SELECT COUNT(*) FROM Authors')
    authors_count = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM Posts')
    posts_count = cursor.fetchone()[0]
    print(f"Total Authors: {authors_count}")
    print(f"Total Posts: {posts_count}")
    
    # Close connection
    conn.close()
    print("\n✓ Database connection closed")

if __name__ == '__main__':
    main()
