import sqlite3

def main():
    # Create an in-memory SQLite database
    # ':memory:' creates a temporary database that exists only in RAM
    connection = sqlite3.connect(':memory:')
    
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()
    
    print("=== SQLite Cursor.Execute() Demonstration ===\n")
    
    # 1. CREATE TABLE - Using cursor.execute()
    print("1. Creating Students table...")
    cursor.execute('''
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT,
            gpa REAL
        )
    ''')
    print("✓ Students table created successfully\n")
    
    # 2. INSERT DATA - Single insert using cursor.execute()
    print("2. Inserting single student record...")
    cursor.execute('''
        INSERT INTO Students (name, age, major, gpa)
        VALUES (?, ?, ?, ?)
    ''', ('Alice Johnson', 20, 'Computer Science', 3.8))
    print("✓ Single record inserted\n")
    
    # 3. INSERT MULTIPLE RECORDS - Using cursor.executemany()
    print("3. Inserting multiple student records...")
    students_data = [
        ('Bob Smith', 21, 'Mathematics', 3.6),
        ('Carol Davis', 19, 'Physics', 3.9),
        ('David Wilson', 22, 'Engineering', 3.4),
        ('Eva Brown', 20, 'Biology', 3.7)
    ]
    
    cursor.executemany('''
        INSERT INTO Students (name, age, major, gpa)
        VALUES (?, ?, ?, ?)
    ''', students_data)
    print("✓ Multiple records inserted\n")
    
    # 4. SELECT ALL - Using cursor.execute() for queries
    print("4. Retrieving all students...")
    cursor.execute('SELECT * FROM Students')
    all_students = cursor.fetchall()
    
    print("All Students:")
    print("-" * 60)
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Major':<15} {'GPA':<5}")
    print("-" * 60)
    for student in all_students:
        print(f"{student[0]:<5} {student[1]:<15} {student[2]:<5} {student[3]:<15} {student[4]:<5}")
    print()
    
    # 5. SELECT WITH CONDITIONS - Using parameters with cursor.execute()
    print("5. Finding students with GPA > 3.7...")
    cursor.execute('SELECT name, gpa FROM Students WHERE gpa > ?', (3.7,))
    high_gpa_students = cursor.fetchall()
    
    print("High GPA Students:")
    for student in high_gpa_students:
        print(f"  {student[0]} - GPA: {student[1]}")
    print()
    
    # 6. UPDATE RECORD - Using cursor.execute()
    print("6. Updating Alice's GPA...")
    cursor.execute('''
        UPDATE Students 
        SET gpa = ? 
        WHERE name = ?
    ''', (3.9, 'Alice Johnson'))
    
    # Check how many rows were affected
    print(f"✓ {cursor.rowcount} record(s) updated\n")
    
    # 7. COUNT RECORDS - Using cursor.execute() with aggregate functions
    print("7. Counting total students...")
    cursor.execute('SELECT COUNT(*) FROM Students')
    count = cursor.fetchone()[0]
    print(f"Total students: {count}\n")
    
    # 8. GROUP BY - Using cursor.execute() with grouping
    print("8. Students count by major...")
    cursor.execute('''
        SELECT major, COUNT(*) as count 
        FROM Students 
        GROUP BY major
        ORDER BY count DESC
    ''')
    major_counts = cursor.fetchall()
    
    print("Students by Major:")
    for major, count in major_counts:
        print(f"  {major}: {count} student(s)")
    print()
    
    # 9. DELETE RECORD - Using cursor.execute()
    print("9. Deleting students with GPA < 3.5...")
    cursor.execute('DELETE FROM Students WHERE gpa < ?', (3.5,))
    print(f"✓ {cursor.rowcount} record(s) deleted\n")
    
    # 10. FINAL COUNT - Show remaining students
    print("10. Final student list...")
    cursor.execute('SELECT name, gpa FROM Students ORDER BY gpa DESC')
    remaining_students = cursor.fetchall()
    
    print("Remaining Students (sorted by GPA):")
    for student in remaining_students:
        print(f"  {student[0]} - GPA: {student[1]}")
    print()
    
    # Commit changes (though not necessary for in-memory database)
    connection.commit()
    
    # Close the connection
    connection.close()
    print("✓ Database connection closed")
    print("\n=== Demonstration Complete ===")

def demonstrate_cursor_methods():
    """Additional demonstration of different cursor methods"""
    print("\n=== Additional Cursor Methods Demonstration ===\n")
    
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE Demo (
            id INTEGER PRIMARY KEY,
            value TEXT
        )
    ''')
    
    # Insert some data
    cursor.execute("INSERT INTO Demo (value) VALUES (?)", ("First",))
    cursor.execute("INSERT INTO Demo (value) VALUES (?)", ("Second",))
    cursor.execute("INSERT INTO Demo (value) VALUES (?)", ("Third",))
    
    print("1. fetchone() - Gets one record at a time:")
    cursor.execute("SELECT * FROM Demo")
    print(f"   First call: {cursor.fetchone()}")
    print(f"   Second call: {cursor.fetchone()}")
    print(f"   Third call: {cursor.fetchone()}")
    print(f"   Fourth call: {cursor.fetchone()}")  # This will be None
    print()
    
    print("2. fetchmany() - Gets specified number of records:")
    cursor.execute("SELECT * FROM Demo")
    print(f"   fetchmany(2): {cursor.fetchmany(2)}")
    print(f"   fetchmany(2): {cursor.fetchmany(2)}")  # Gets remaining
    print()
    
    print("3. fetchall() - Gets all remaining records:")
    cursor.execute("SELECT * FROM Demo")
    print(f"   fetchall(): {cursor.fetchall()}")
    print()
    
    connection.close()

if __name__ == "__main__":
    main()
    demonstrate_cursor_methods()
