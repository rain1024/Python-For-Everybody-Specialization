import sqlite3

# Create in-memory SQLite database connection
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create students table
cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT,
        email TEXT UNIQUE
    )
''')

# Insert sample data
students_data = [
    ('Alice Johnson', 20, 'A', 'alice@example.com'),
    ('Bob Smith', 19, 'B', 'bob@example.com'),
    ('Carol Davis', 21, 'A', 'carol@example.com'),
    ('David Wilson', 18, 'C', 'david@example.com'),
    ('Eva Brown', 22, 'B', 'eva@example.com')
]

cursor.executemany('INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)', students_data)

# Commit the changes
conn.commit()

# Query and display all students
print("All Students:")
print("-" * 50)
cursor.execute('SELECT * FROM students')
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, Email: {row[4]}")

print("\n")

# Query students with grade 'A'
print("Students with grade 'A':")
print("-" * 30)
cursor.execute('SELECT name, age FROM students WHERE grade = ?', ('A',))
for row in cursor.fetchall():
    print(f"Name: {row[0]}, Age: {row[1]}")

print("\n")

# Count students by grade
print("Student count by grade:")
print("-" * 25)
cursor.execute('SELECT grade, COUNT(*) FROM students GROUP BY grade ORDER BY grade')
for row in cursor.fetchall():
    print(f"Grade {row[0]}: {row[1]} students")

print("\n")

# Find oldest student
print("Oldest student:")
print("-" * 15)
cursor.execute('SELECT name, age FROM students WHERE age = (SELECT MAX(age) FROM students)')
row = cursor.fetchone()
if row:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Close the connection
conn.close()

print("\nDatabase connection closed.")
