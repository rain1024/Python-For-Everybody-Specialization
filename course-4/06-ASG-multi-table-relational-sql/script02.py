import sqlite3

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table with a primary key
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
)
''')

# Insert some sample data
students_data = [
    ('Alice Johnson', 'alice@email.com', 20),
    ('Bob Smith', 'bob@email.com', 22),
    ('Charlie Brown', 'charlie@email.com', 21),
    ('Diana Ross', 'diana@email.com', 19)
]

cursor.executemany('INSERT INTO students (name, email, age) VALUES (?, ?, ?)', students_data)

# Commit the changes
conn.commit()

print("=== All Students ===")
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")

print("\n=== Find Student by Primary Key ===")
cursor.execute('SELECT * FROM students WHERE id = ?', (2,))
student = cursor.fetchone()
if student:
    print(f"Found student: {student[1]} ({student[2]})")

print("\n=== Demonstrating Primary Key Uniqueness ===")
try:
    # Try to insert a duplicate primary key (this will fail)
    cursor.execute('INSERT INTO students (id, name, email, age) VALUES (?, ?, ?, ?)', 
                   (1, 'Test User', 'test@email.com', 25))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")
    print("Primary key must be unique!")

print("\n=== Auto-increment Demonstration ===")
cursor.execute('INSERT INTO students (name, email, age) VALUES (?, ?, ?)', 
               ('Eve Wilson', 'eve@email.com', 23))
conn.commit()

cursor.execute('SELECT * FROM students WHERE name = ?', ('Eve Wilson',))
new_student = cursor.fetchone()
print(f"New student auto-assigned ID: {new_student[0]}")

# Close the connection
conn.close()
print("\nDatabase connection closed.")
