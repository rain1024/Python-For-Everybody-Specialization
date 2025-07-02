import sqlite3

def create_database():
    """Create an in-memory SQLite database with users table"""
    # Create connection to in-memory database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create users table with primary key and logical keys
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Primary Key
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,           -- Logical Key 1
            phone TEXT UNIQUE NOT NULL,           -- Logical Key 2  
            age INTEGER,
            city TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("✓ Users table created successfully")
    print("  - Primary Key: id (auto-increment)")
    print("  - Logical Key 1: email (unique)")
    print("  - Logical Key 2: phone (unique)")
    print()
    
    return conn, cursor

def insert_sample_data(cursor):
    """Insert sample users data"""
    users_data = [
        ('John', 'Doe', 'john.doe@email.com', '+1-555-0101', 28, 'New York'),
        ('Jane', 'Smith', 'jane.smith@email.com', '+1-555-0102', 32, 'Los Angeles'),
        ('Bob', 'Johnson', 'bob.johnson@email.com', '+1-555-0103', 25, 'Chicago'),
        ('Alice', 'Brown', 'alice.brown@email.com', '+1-555-0104', 29, 'Houston'),
        ('Charlie', 'Wilson', 'charlie.wilson@email.com', '+1-555-0105', 35, 'Phoenix')
    ]
    
    cursor.executemany('''
        INSERT INTO users (first_name, last_name, email, phone, age, city)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', users_data)
    
    print(f"✓ Inserted {len(users_data)} users into the database")
    print()

def demonstrate_primary_key_queries(cursor):
    """Demonstrate querying by primary key"""
    print("=== QUERYING BY PRIMARY KEY ===")
    
    # Query by primary key (id)
    cursor.execute("SELECT * FROM users WHERE id = ?", (3,))
    user = cursor.fetchone()
    if user:
        print(f"User with ID 3: {user[1]} {user[2]} - {user[3]}")
    
    # Query multiple users by primary key
    cursor.execute("SELECT id, first_name, last_name FROM users WHERE id IN (1, 2, 4)")
    users = cursor.fetchall()
    print(f"Users with IDs 1, 2, 4:")
    for user in users:
        print(f"  ID {user[0]}: {user[1]} {user[2]}")
    print()

def demonstrate_logical_key_queries(cursor):
    """Demonstrate querying by logical keys"""
    print("=== QUERYING BY LOGICAL KEYS ===")
    
    # Query by email (logical key)
    email = 'jane.smith@email.com'
    cursor.execute("SELECT id, first_name, last_name, phone FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    if user:
        print(f"User found by email '{email}':")
        print(f"  ID: {user[0]}, Name: {user[1]} {user[2]}, Phone: {user[3]}")
    
    # Query by phone (logical key)
    phone = '+1-555-0104'
    cursor.execute("SELECT id, first_name, last_name, email FROM users WHERE phone = ?", (phone,))
    user = cursor.fetchone()
    if user:
        print(f"User found by phone '{phone}':")
        print(f"  ID: {user[0]}, Name: {user[1]} {user[2]}, Email: {user[3]}")
    print()

def demonstrate_logical_key_constraints(cursor):
    """Demonstrate logical key uniqueness constraints"""
    print("=== LOGICAL KEY CONSTRAINTS DEMONSTRATION ===")
    
    try:
        # Try to insert user with duplicate email
        cursor.execute('''
            INSERT INTO users (first_name, last_name, email, phone, age, city)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Test', 'User', 'john.doe@email.com', '+1-555-9999', 30, 'Boston'))
        print("ERROR: This should not succeed!")
    except sqlite3.IntegrityError as e:
        print(f"✓ Email uniqueness constraint enforced: {e}")
    
    try:
        # Try to insert user with duplicate phone
        cursor.execute('''
            INSERT INTO users (first_name, last_name, email, phone, age, city)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Another', 'User', 'unique@email.com', '+1-555-0101', 30, 'Boston'))
        print("ERROR: This should not succeed!")
    except sqlite3.IntegrityError as e:
        print(f"✓ Phone uniqueness constraint enforced: {e}")
    
    print()

def show_all_users(cursor):
    """Display all users in the database"""
    print("=== ALL USERS IN DATABASE ===")
    cursor.execute("SELECT id, first_name, last_name, email, phone, age, city FROM users")
    users = cursor.fetchall()
    
    print(f"{'ID':<3} {'Name':<15} {'Email':<25} {'Phone':<15} {'Age':<3} {'City'}")
    print("-" * 80)
    for user in users:
        print(f"{user[0]:<3} {user[1] + ' ' + user[2]:<15} {user[3]:<25} {user[4]:<15} {user[5]:<3} {user[6]}")
    print()

def demonstrate_update_by_logical_key(cursor):
    """Demonstrate updating records using logical keys"""
    print("=== UPDATING BY LOGICAL KEYS ===")
    
    # Update user by email
    cursor.execute('''
        UPDATE users 
        SET city = ?, age = ? 
        WHERE email = ?
    ''', ('San Francisco', 33, 'jane.smith@email.com'))
    
    print("✓ Updated Jane Smith's city and age using email as logical key")
    
    # Verify the update
    cursor.execute("SELECT first_name, last_name, age, city FROM users WHERE email = ?", 
                  ('jane.smith@email.com',))
    user = cursor.fetchone()
    if user:
        print(f"  Updated record: {user[0]} {user[1]}, Age: {user[2]}, City: {user[3]}")
    print()

def main():
    """Main function to run the demonstration"""
    print("SQLite Memory Database - Primary Keys vs Logical Keys Demonstration")
    print("=" * 70)
    print()
    
    # Create database and table
    conn, cursor = create_database()
    
    # Insert sample data
    insert_sample_data(cursor)
    
    # Show all users
    show_all_users(cursor)
    
    # Demonstrate different types of queries
    demonstrate_primary_key_queries(cursor)
    demonstrate_logical_key_queries(cursor)
    demonstrate_update_by_logical_key(cursor)
    demonstrate_logical_key_constraints(cursor)
    
    # Show final state
    show_all_users(cursor)
    
    print("=== KEY CONCEPTS SUMMARY ===")
    print("1. PRIMARY KEY (id): Unique identifier, auto-generated, used internally")
    print("2. LOGICAL KEYS (email, phone): Business-meaningful unique identifiers")
    print("3. Logical keys are often used in real-world queries and updates")
    print("4. Both primary and logical keys enforce uniqueness constraints")
    print("5. Logical keys provide alternative ways to identify records")
    
    # Close connection
    conn.close()
    print("\n✓ Database connection closed")

if __name__ == "__main__":
    main()
