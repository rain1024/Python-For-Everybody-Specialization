import sqlite3

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

print("=== Many-to-Many Relationship Demonstration ===")
print("Example: Students and Courses relationship")
print()

# Create Students table
cursor.execute('''
CREATE TABLE Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
''')

# Create Courses table  
cursor.execute('''
CREATE TABLE Courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    credits INTEGER
)
''')

# Create junction table for many-to-many relationship
# Note: We avoid AUTOINCREMENT primary key in junction tables
# The primary key is the combination of the two foreign keys
cursor.execute('''
CREATE TABLE StudentCourses (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
)
''')

print("✓ Tables created successfully")
print()

# Insert sample data
students_data = [
    (1, 'Alice Johnson', 'alice@email.com'),
    (2, 'Bob Smith', 'bob@email.com'),
    (3, 'Carol Davis', 'carol@email.com')
]

courses_data = [
    (1, 'Python Programming', 3),
    (2, 'Database Design', 4), 
    (3, 'Web Development', 3),
    (4, 'Data Science', 4)
]

# Insert students
cursor.executemany('INSERT INTO Students VALUES (?, ?, ?)', students_data)
print("✓ Students inserted:")
for student in students_data:
    print(f"  - {student[1]} ({student[2]})")
print()

# Insert courses
cursor.executemany('INSERT INTO Courses VALUES (?, ?, ?)', courses_data)
print("✓ Courses inserted:")
for course in courses_data:
    print(f"  - {course[1]} ({course[2]} credits)")
print()

# Create many-to-many relationships (enrollments)
enrollments = [
    (1, 1, '2024-01-15'),  # Alice -> Python Programming
    (1, 2, '2024-01-15'),  # Alice -> Database Design
    (1, 3, '2024-01-16'),  # Alice -> Web Development
    (2, 1, '2024-01-16'),  # Bob -> Python Programming
    (2, 4, '2024-01-17'),  # Bob -> Data Science
    (3, 2, '2024-01-17'),  # Carol -> Database Design
    (3, 3, '2024-01-18'),  # Carol -> Web Development
    (3, 4, '2024-01-18')   # Carol -> Data Science
]

cursor.executemany('INSERT INTO StudentCourses VALUES (?, ?, ?)', enrollments)
print("✓ Enrollments created")
print()

# Demonstrate queries for many-to-many relationships
print("=== Query Demonstrations ===")
print()

# 1. Find all courses for a specific student
print("1. Courses enrolled by Alice Johnson:")
cursor.execute('''
SELECT c.name, c.credits, sc.enrollment_date
FROM Students s
JOIN StudentCourses sc ON s.id = sc.student_id
JOIN Courses c ON sc.course_id = c.id
WHERE s.name = 'Alice Johnson'
''')

for row in cursor.fetchall():
    print(f"   - {row[0]} ({row[1]} credits) - Enrolled: {row[2]}")
print()

# 2. Find all students in a specific course
print("2. Students enrolled in 'Python Programming':")
cursor.execute('''
SELECT s.name, s.email, sc.enrollment_date
FROM Courses c
JOIN StudentCourses sc ON c.id = sc.course_id
JOIN Students s ON sc.student_id = s.id
WHERE c.name = 'Python Programming'
''')

for row in cursor.fetchall():
    print(f"   - {row[0]} ({row[1]}) - Enrolled: {row[2]}")
print()

# 3. Count enrollments per course
print("3. Enrollment count per course:")
cursor.execute('''
SELECT c.name, COUNT(sc.student_id) as enrollment_count
FROM Courses c
LEFT JOIN StudentCourses sc ON c.id = sc.course_id
GROUP BY c.id, c.name
ORDER BY enrollment_count DESC
''')

for row in cursor.fetchall():
    print(f"   - {row[0]}: {row[1]} students")
print()

# 4. Count courses per student
print("4. Courses per student:")
cursor.execute('''
SELECT s.name, COUNT(sc.course_id) as course_count
FROM Students s
LEFT JOIN StudentCourses sc ON s.id = sc.student_id
GROUP BY s.id, s.name
ORDER BY course_count DESC
''')

for row in cursor.fetchall():
    print(f"   - {row[0]}: {row[1]} courses")
print()

# 5. Find students taking more than 2 courses
print("5. Students taking more than 2 courses:")
cursor.execute('''
SELECT s.name, COUNT(sc.course_id) as course_count
FROM Students s
JOIN StudentCourses sc ON s.id = sc.student_id
GROUP BY s.id, s.name
HAVING COUNT(sc.course_id) > 2
''')

for row in cursor.fetchall():
    print(f"   - {row[0]}: {row[1]} courses")
print()

print("=== Junction Table Best Practices Demonstrated ===")
print("✓ No AUTOINCREMENT primary key in junction table")
print("✓ Composite primary key using both foreign keys")
print("✓ Minimal additional data (only enrollment_date)")
print("✓ Proper foreign key constraints")
print()

# Close the connection
conn.close()
print("✓ Database connection closed")
