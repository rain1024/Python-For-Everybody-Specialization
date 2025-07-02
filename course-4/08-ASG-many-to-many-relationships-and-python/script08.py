import sqlite3

def demonstrate_or_ignore():
    """
    Demonstrates the purpose of 'OR IGNORE' in SQL INSERT statements.
    OR IGNORE prevents duplicate rows from being inserted if a constraint would be violated.
    """
    
    # Create an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    
    # Create a Course table with title as a unique field
    cur.execute('''
        CREATE TABLE Course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("=== SQLite OR IGNORE Demonstration ===\n")
    
    # Insert some initial courses
    courses = ['Python Programming', 'Database Design', 'Web Development']
    
    print("1. Inserting initial courses:")
    for course in courses:
        cur.execute('INSERT INTO Course (title) VALUES (?)', (course,))
        print(f"   Inserted: {course}")
    
    # Show current courses in the database
    print("\n2. Current courses in database:")
    cur.execute('SELECT id, title FROM Course')
    for row in cur.fetchall():
        print(f"   ID: {row[0]}, Title: {row[1]}")
    
    print("\n3. Attempting to insert duplicate without OR IGNORE:")
    try:
        cur.execute('INSERT INTO Course (title) VALUES (?)', ('Python Programming',))
        print("   Success: Duplicate inserted")
    except sqlite3.IntegrityError as e:
        print(f"   Error: {e}")
    
    print("\n4. Attempting to insert duplicate WITH OR IGNORE:")
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', ('Python Programming',))
    print("   Success: No error occurred (duplicate was ignored)")
    
    print("\n5. Attempting to insert new course WITH OR IGNORE:")
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', ('Machine Learning',))
    print("   Success: New course was inserted")
    
    # Show final courses in the database
    print("\n6. Final courses in database:")
    cur.execute('SELECT id, title FROM Course')
    for row in cur.fetchall():
        print(f"   ID: {row[0]}, Title: {row[1]}")
    
    print("\n=== Summary ===")
    print("OR IGNORE makes sure that if a particular title is already in the table,")
    print("there are no duplicate rows inserted. It silently ignores the INSERT")
    print("operation when it would violate a UNIQUE constraint.")
    
    # Clean up
    conn.close()

def demonstrate_multiple_scenarios():
    """
    Additional demonstration showing various OR IGNORE scenarios
    """
    print("\n\n=== Additional OR IGNORE Scenarios ===\n")
    
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    
    # Create a more complex table
    cur.execute('''
        CREATE TABLE Student (
            id INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            course_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES Course (id)
        )
    ''')
    
    # Create Course table for foreign key reference
    cur.execute('''
        CREATE TABLE Course (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        )
    ''')
    
    # Insert a course
    cur.execute('INSERT INTO Course (id, name) VALUES (1, "Python")')
    
    print("1. Inserting students with OR IGNORE:")
    students = [
        (1, 'alice@email.com', 'Alice', 1),
        (2, 'bob@email.com', 'Bob', 1),
        (1, 'charlie@email.com', 'Charlie', 1),  # Duplicate ID
        (3, 'alice@email.com', 'Alice Clone', 1),  # Duplicate email
    ]
    
    for student in students:
        cur.execute('INSERT OR IGNORE INTO Student VALUES (?, ?, ?, ?)', student)
        print(f"   Attempted to insert: {student}")
    
    print("\n2. Actual students in database:")
    cur.execute('SELECT * FROM Student')
    for row in cur.fetchall():
        print(f"   {row}")
    
    print("\n   Notice: Only the first occurrence of each unique constraint was kept")
    
    conn.close()

if __name__ == "__main__":
    demonstrate_or_ignore()
    demonstrate_multiple_scenarios()
