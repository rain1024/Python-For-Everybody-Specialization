import sqlite3

def main():
    # Create in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    print("=== SQLite JOIN Demo with Identical Column Names ===\n")
    
    # Create tables
    print("1. Creating tables...")
    
    # Students table (id, name)
    cursor.execute('''
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    
    # Courses table (id, name) - identical column names as Students
    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    
    # Enrollments table (junction table)
    cursor.execute('''
        CREATE TABLE Enrollments (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            enrollment_date TEXT,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES Students(id),
            FOREIGN KEY (course_id) REFERENCES Courses(id)
        )
    ''')
    
    print("Tables created successfully!\n")
    
    # Insert sample data
    print("2. Inserting sample data...")
    
    # Insert students
    students_data = [
        (1, 'Alice Johnson'),
        (2, 'Bob Smith'),
        (3, 'Charlie Brown'),
        (4, 'Diana Wilson'),
        (5, 'Eve Davis')
    ]
    cursor.executemany('INSERT INTO Students (id, name) VALUES (?, ?)', students_data)
    
    # Insert courses
    courses_data = [
        (1, 'Python Programming'),
        (2, 'Database Design'),
        (3, 'Web Development'),
        (4, 'Data Science'),
        (5, 'Machine Learning')
    ]
    cursor.executemany('INSERT INTO Courses (id, name) VALUES (?, ?)', courses_data)
    
    # Insert enrollments
    enrollments_data = [
        (1, 1, 1, '2024-01-15', 'A'),  # Alice -> Python Programming
        (2, 1, 2, '2024-01-16', 'A-'), # Alice -> Database Design
        (3, 2, 1, '2024-01-15', 'B+'), # Bob -> Python Programming
        (4, 2, 3, '2024-01-17', 'B'),  # Bob -> Web Development
        (5, 3, 2, '2024-01-16', 'A'),  # Charlie -> Database Design
        (6, 3, 4, '2024-01-18', 'A-'), # Charlie -> Data Science
        (7, 4, 1, '2024-01-15', 'B-'), # Diana -> Python Programming
        (8, 4, 4, '2024-01-18', 'A'),  # Diana -> Data Science
        (9, 4, 5, '2024-01-19', 'A+'), # Diana -> Machine Learning
    ]
    cursor.executemany('''INSERT INTO Enrollments 
                         (id, student_id, course_id, enrollment_date, grade) 
                         VALUES (?, ?, ?, ?, ?)''', enrollments_data)
    
    print("Sample data inserted successfully!\n")
    
    # Display individual tables
    print("3. Individual table contents:")
    print("\n--- Students Table ---")
    cursor.execute('SELECT * FROM Students')
    students = cursor.fetchall()
    print(f"{'ID':<5} {'Name':<15}")
    print("-" * 20)
    for student in students:
        print(f"{student[0]:<5} {student[1]:<15}")
    
    print("\n--- Courses Table ---")
    cursor.execute('SELECT * FROM Courses')
    courses = cursor.fetchall()
    print(f"{'ID':<5} {'Name':<20}")
    print("-" * 25)
    for course in courses:
        print(f"{course[0]:<5} {course[1]:<20}")
    
    print("\n--- Enrollments Table ---")
    cursor.execute('SELECT * FROM Enrollments')
    enrollments = cursor.fetchall()
    print(f"{'ID':<5} {'Student ID':<12} {'Course ID':<12} {'Date':<12} {'Grade':<8}")
    print("-" * 50)
    for enrollment in enrollments:
        print(f"{enrollment[0]:<5} {enrollment[1]:<12} {enrollment[2]:<12} {enrollment[3]:<12} {enrollment[4]:<8}")
    
    # Demonstrate JOIN operations with identical column names
    print("\n\n4. JOIN Operations with Identical Column Names:")
    
    # Example 1: Basic INNER JOIN with table aliases
    print("\n--- Example 1: Basic INNER JOIN (Student enrollments) ---")
    print("Using table aliases to handle identical column names:")
    query1 = '''
        SELECT 
            s.id AS student_id,
            s.name AS student_name,
            c.id AS course_id,
            c.name AS course_name,
            e.grade,
            e.enrollment_date
        FROM Students s
        INNER JOIN Enrollments e ON s.id = e.student_id
        INNER JOIN Courses c ON c.id = e.course_id
        ORDER BY s.name, c.name
    '''
    cursor.execute(query1)
    results1 = cursor.fetchall()
    
    print(f"{'Student ID':<12} {'Student Name':<15} {'Course ID':<11} {'Course Name':<18} {'Grade':<7} {'Date':<12}")
    print("-" * 85)
    for row in results1:
        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<11} {row[3]:<18} {row[4]:<7} {row[5]:<12}")
    
    # Example 2: LEFT JOIN to show students without enrollments
    print("\n--- Example 2: LEFT JOIN (All students, including those without enrollments) ---")
    query2 = '''
        SELECT 
            s.id AS student_id,
            s.name AS student_name,
            c.name AS course_name,
            e.grade
        FROM Students s
        LEFT JOIN Enrollments e ON s.id = e.student_id
        LEFT JOIN Courses c ON c.id = e.course_id
        ORDER BY s.name, c.name
    '''
    cursor.execute(query2)
    results2 = cursor.fetchall()
    
    print(f"{'Student ID':<12} {'Student Name':<15} {'Course Name':<20} {'Grade':<7}")
    print("-" * 55)
    for row in results2:
        course_name = row[2] if row[2] is not None else 'No Enrollment'
        grade = row[3] if row[3] is not None else 'N/A'
        print(f"{row[0]:<12} {row[1]:<15} {course_name:<20} {grade:<7}")
    
    # Example 3: Aggregation with JOINs
    print("\n--- Example 3: Aggregation - Students with enrollment counts ---")
    query3 = '''
        SELECT 
            s.id AS student_id,
            s.name AS student_name,
            COUNT(e.id) AS enrollment_count,
            AVG(CASE 
                WHEN e.grade = 'A+' THEN 4.3
                WHEN e.grade = 'A' THEN 4.0
                WHEN e.grade = 'A-' THEN 3.7
                WHEN e.grade = 'B+' THEN 3.3
                WHEN e.grade = 'B' THEN 3.0
                WHEN e.grade = 'B-' THEN 2.7
                ELSE 0.0
            END) AS gpa
        FROM Students s
        LEFT JOIN Enrollments e ON s.id = e.student_id
        GROUP BY s.id, s.name
        ORDER BY enrollment_count DESC, gpa DESC
    '''
    cursor.execute(query3)
    results3 = cursor.fetchall()
    
    print(f"{'Student ID':<12} {'Student Name':<15} {'Enrollments':<12} {'GPA':<8}")
    print("-" * 50)
    for row in results3:
        gpa = f"{row[3]:.2f}" if row[3] is not None else "N/A"
        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<12} {gpa:<8}")
    
    # Example 4: Complex JOIN with course popularity
    print("\n--- Example 4: Course popularity (enrollment counts) ---")
    query4 = '''
        SELECT 
            c.id AS course_id,
            c.name AS course_name,
            COUNT(e.id) AS student_count,
            GROUP_CONCAT(s.name, ', ') AS enrolled_students
        FROM Courses c
        LEFT JOIN Enrollments e ON c.id = e.course_id
        LEFT JOIN Students s ON s.id = e.student_id
        GROUP BY c.id, c.name
        ORDER BY student_count DESC, c.name
    '''
    cursor.execute(query4)
    results4 = cursor.fetchall()
    
    print(f"{'Course ID':<10} {'Course Name':<20} {'Students':<10} {'Enrolled Students':<30}")
    print("-" * 70)
    for row in results4:
        students = row[3] if row[3] is not None else 'No enrollments'
        print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {students:<30}")
    
    # Example 5: Self-referencing example - students in same courses
    print("\n--- Example 5: Students enrolled in the same courses ---")
    query5 = '''
        SELECT DISTINCT
            s1.id as student1_id,
            s1.name AS student1_name,
            s2.id as student2_id,
            s2.name AS student2_name,
            c.name AS shared_course
        FROM Students s1
        INNER JOIN Enrollments e1 ON s1.id = e1.student_id
        INNER JOIN Courses c ON c.id = e1.course_id
        INNER JOIN Enrollments e2 ON c.id = e2.course_id
        INNER JOIN Students s2 ON s2.id = e2.student_id
        WHERE s1.id < s2.id  -- Avoid duplicate pairs and self-pairs
        ORDER BY shared_course, s1.name, s2.name
    '''
    cursor.execute(query5)
    results5 = cursor.fetchall()
    
    print(f"{'Student 1':<15} {'Student 2':<15} {'Shared Course':<20}")
    print("-" * 50)
    for row in results5:
        print(f"{row[1]:<15} {row[3]:<15} {row[4]:<20}")
    
    print("\n\n5. Key Points about handling identical column names:")
    print("   • Use table aliases (e.g., 's' for Students, 'c' for Courses)")
    print("   • Qualify column names with table aliases (e.g., s.id, c.id)")
    print("   • Use column aliases in SELECT for clarity (e.g., s.id AS student_id)")
    print("   • Be explicit about which table's columns you're referencing")
    print("   • Consider renaming columns during table creation to avoid conflicts")
    
    # Close connection
    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
