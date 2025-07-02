import sqlite3

def demonstrate_cursor_operations():
    """
    Demonstrate SQLite cursor operations with a Students table
    A cursor is an object that allows you to execute SQL commands
    and fetch data from the database.
    """
    
    # Create an in-memory SQLite database
    # ':memory:' creates a temporary database in RAM
    connection = sqlite3.connect(':memory:')
    
    # Create a cursor object
    # The cursor is what we use to execute SQL commands
    cursor = connection.cursor()
    
    print("=== SQLite Cursor Demonstration ===\n")
    
    # 1. CREATE TABLE using cursor
    print("1. Creating Students table...")
    cursor.execute('''
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT,
            email TEXT UNIQUE
        )
    ''')
    print("✓ Table created successfully\n")
    
    # 2. INSERT data using cursor
    print("2. Inserting student records...")
    
    # Single insert
    cursor.execute('''
        INSERT INTO Students (name, age, grade, email)
        VALUES (?, ?, ?, ?)
    ''', ('Alice Johnson', 20, 'A', 'alice@school.edu'))
    
    # Multiple inserts using executemany()
    students_data = [
        ('Bob Smith', 19, 'B+', 'bob@school.edu'),
        ('Carol Wilson', 21, 'A-', 'carol@school.edu'),
        ('David Brown', 18, 'B', 'david@school.edu'),
        ('Eve Davis', 22, 'A+', 'eve@school.edu')
    ]
    
    cursor.executemany('''
        INSERT INTO Students (name, age, grade, email)
        VALUES (?, ?, ?, ?)
    ''', students_data)
    
    # Commit the transaction
    connection.commit()
    print(f"✓ Inserted {cursor.rowcount + 1} student records\n")
    
    # 3. SELECT data using cursor
    print("3. Querying all students...")
    cursor.execute('SELECT * FROM Students')
    
    # Fetch all records
    all_students = cursor.fetchall()
    
    print("All Students:")
    print("-" * 60)
    print(f"{'ID':<3} {'Name':<15} {'Age':<3} {'Grade':<5} {'Email':<20}")
    print("-" * 60)
    
    for student in all_students:
        print(f"{student[0]:<3} {student[1]:<15} {student[2]:<3} {student[3]:<5} {student[4]:<20}")
    print()
    
    # 4. SELECT with WHERE clause
    print("4. Querying students with grade 'A' or better...")
    cursor.execute('''
        SELECT name, age, grade FROM Students 
        WHERE grade IN ('A', 'A+', 'A-')
        ORDER BY grade DESC
    ''')
    
    # Fetch records one by one using fetchone()
    print("Top Students:")
    print("-" * 30)
    while True:
        student = cursor.fetchone()
        if student is None:  # No more records
            break
        print(f"{student[0]} (Age: {student[1]}, Grade: {student[2]})")
    print()
    
    # 5. UPDATE data using cursor
    print("5. Updating a student's grade...")
    cursor.execute('''
        UPDATE Students 
        SET grade = ? 
        WHERE name = ?
    ''', ('A+', 'Bob Smith'))
    
    connection.commit()
    print(f"✓ Updated {cursor.rowcount} record(s)\n")
    
    # 6. COUNT and aggregate functions
    print("6. Getting statistics...")
    cursor.execute('SELECT COUNT(*) FROM Students')
    total_students = cursor.fetchone()[0]
    
    cursor.execute('SELECT AVG(age) FROM Students')
    avg_age = cursor.fetchone()[0]
    
    print(f"Total Students: {total_students}")
    print(f"Average Age: {avg_age:.1f} years\n")
    
    # 7. Using fetchmany() to get limited results
    print("7. Getting first 3 students using fetchmany()...")
    cursor.execute('SELECT name, email FROM Students ORDER BY name')
    first_three = cursor.fetchmany(3)
    
    for student in first_three:
        print(f"Name: {student[0]}, Email: {student[1]}")
    print()
    
    # 8. DELETE operation
    print("8. Removing students older than 21...")
    cursor.execute('DELETE FROM Students WHERE age > 21')
    connection.commit()
    print(f"✓ Deleted {cursor.rowcount} record(s)\n")
    
    # 9. Final count
    print("9. Final student count...")
    cursor.execute('SELECT COUNT(*) FROM Students')
    remaining_students = cursor.fetchone()[0]
    print(f"Remaining students: {remaining_students}\n")
    
    # 10. Show remaining students
    print("10. Remaining students:")
    cursor.execute('SELECT name, age, grade FROM Students ORDER BY age')
    remaining = cursor.fetchall()
    
    print("-" * 35)
    for student in remaining:
        print(f"{student[0]} (Age: {student[1]}, Grade: {student[2]})")
    
    # Important: Close cursor and connection
    cursor.close()
    connection.close()
    
    print("\n=== Cursor Operations Complete ===")
    print("\nKey Cursor Concepts Demonstrated:")
    print("• cursor.execute() - Execute single SQL command")
    print("• cursor.executemany() - Execute command with multiple parameter sets")
    print("• cursor.fetchone() - Fetch one record at a time")
    print("• cursor.fetchall() - Fetch all remaining records")
    print("• cursor.fetchmany(n) - Fetch n records")
    print("• cursor.rowcount - Number of affected rows")
    print("• connection.commit() - Save changes to database")
    print("• cursor.close() - Close the cursor")

def cursor_methods_demo():
    """
    Additional demonstration of cursor methods and properties
    """
    print("\n\n=== Additional Cursor Methods Demo ===\n")
    
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    
    # Create a simple table
    cursor.execute('''
        CREATE TABLE Demo (
            id INTEGER PRIMARY KEY,
            value TEXT
        )
    ''')
    
    # Insert some data
    cursor.execute("INSERT INTO Demo (value) VALUES ('First')")
    cursor.execute("INSERT INTO Demo (value) VALUES ('Second')")
    cursor.execute("INSERT INTO Demo (value) VALUES ('Third')")
    connection.commit()
    
    print("1. Using cursor as an iterator:")
    cursor.execute("SELECT * FROM Demo")
    for row in cursor:
        print(f"  ID: {row[0]}, Value: {row[1]}")
    
    print("\n2. Cursor description (column information):")
    cursor.execute("SELECT * FROM Demo")
    print(f"  Columns: {[desc[0] for desc in cursor.description]}")
    
    print("\n3. Using row factory for named access:")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Demo WHERE id = 2")
    row = cursor.fetchone()
    print(f"  Access by name: {row['value']}")
    print(f"  Access by index: {row[1]}")
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    demonstrate_cursor_operations()
    cursor_methods_demo()
