import sqlite3
import uuid

def demonstrate_bad_practice():
    """
    BAD PRACTICE: Using email as primary key
    Problems:
    1. Emails can change over time
    2. Case sensitivity issues
    3. Length limitations
    4. Not truly immutable
    5. Performance issues with string comparisons
    """
    print("=" * 50)
    print("BAD PRACTICE: Using Email as Primary Key")
    print("=" * 50)
    
    # Create in-memory database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create table with email as primary key
    cursor.execute('''
        CREATE TABLE users_bad (
            email TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')
    
    # Insert some users
    users = [
        ('john@example.com', 'John Doe', 30),
        ('jane@example.com', 'Jane Smith', 25),
        ('bob@example.com', 'Bob Johnson', 35)
    ]
    
    cursor.executemany('INSERT INTO users_bad VALUES (?, ?, ?)', users)
    
    print("Original users:")
    cursor.execute('SELECT * FROM users_bad')
    for row in cursor.fetchall():
        print(f"Email: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    
    print("\n--- Problems with email as primary key ---")
    
    # Problem 1: Cannot handle email changes easily
    print("\n1. Trying to update John's email...")
    try:
        # This requires complex operations and can break foreign key relationships
        cursor.execute("UPDATE users_bad SET email = ? WHERE email = ?", 
                      ('john.doe@newcompany.com', 'john@example.com'))
        print("✗ Email updated, but this breaks any foreign key references!")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Problem 2: Case sensitivity issues
    print("\n2. Case sensitivity problems...")
    try:
        cursor.execute("INSERT INTO users_bad VALUES (?, ?, ?)", 
                      ('JOHN@EXAMPLE.COM', 'John Duplicate', 31))
        print("✗ Allowed duplicate email with different case!")
    except sqlite3.IntegrityError:
        print("✓ SQLite caught this, but many systems don't handle case properly")
    
    # Problem 3: Performance with string comparisons
    print("\n3. String primary keys are slower for joins and lookups")
    print("✗ Every comparison requires string matching instead of integer comparison")
    
    conn.close()

def demonstrate_good_practice():
    """
    GOOD PRACTICE: Using UUID as primary key
    Benefits:
    1. Immutable identifier
    2. Globally unique
    3. No collision risk
    4. Better for distributed systems
    5. Privacy-friendly (no sequential numbers)
    """
    print("\n" + "=" * 50)
    print("GOOD PRACTICE: Using UUID as Primary Key")
    print("=" * 50)
    
    # Create in-memory database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create table with UUID as primary key
    cursor.execute('''
        CREATE TABLE users_good (
            id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')
    
    # Insert some users with UUIDs
    users = [
        (str(uuid.uuid4()), 'john@example.com', 'John Doe', 30),
        (str(uuid.uuid4()), 'jane@example.com', 'Jane Smith', 25),
        (str(uuid.uuid4()), 'bob@example.com', 'Bob Johnson', 35)
    ]
    
    cursor.executemany('INSERT INTO users_good VALUES (?, ?, ?, ?)', users)
    
    print("Users with UUID primary keys:")
    cursor.execute('SELECT * FROM users_good')
    for row in cursor.fetchall():
        print(f"ID: {row[0][:8]}..., Email: {row[1]}, Name: {row[2]}, Age: {row[3]}")
    
    print("\n--- Benefits of UUID as primary key ---")
    
    # Benefit 1: Easy email updates
    print("\n1. Easy email updates while maintaining relationships...")
    cursor.execute('SELECT id FROM users_good WHERE email = ?', ('john@example.com',))
    john_id = cursor.fetchone()[0]
    
    cursor.execute("UPDATE users_good SET email = ? WHERE id = ?", 
                  ('john.doe@newcompany.com', john_id))
    print("✓ Email updated easily! Foreign key relationships remain intact.")
    
    # Benefit 2: No case sensitivity issues with primary key
    print("\n2. Primary key is case-insensitive UUID, email can have proper validation")
    print("✓ UUIDs don't have case sensitivity issues")
    
    # Benefit 3: Better for distributed systems
    print("\n3. UUIDs are perfect for distributed systems")
    print("✓ No collision risk when merging data from multiple sources")
    
    # Create a related table to show foreign key benefits
    cursor.execute('''
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            user_id TEXT,
            product TEXT,
            amount REAL,
            FOREIGN KEY (user_id) REFERENCES users_good (id)
        )
    ''')
    
    # Add some orders
    orders = [
        (str(uuid.uuid4()), john_id, 'Laptop', 999.99),
        (str(uuid.uuid4()), john_id, 'Mouse', 29.99)
    ]
    
    cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?)', orders)
    
    print("\n4. Foreign key relationships work perfectly:")
    cursor.execute('''
        SELECT u.name, u.email, o.product, o.amount 
        FROM users_good u 
        JOIN orders o ON u.id = o.user_id
    ''')
    
    for row in cursor.fetchall():
        print(f"✓ {row[0]} ({row[1]}) ordered {row[2]} for ${row[3]}")
    
    conn.close()

def demonstrate_additional_benefits():
    """
    Additional benefits and considerations
    """
    print("\n" + "=" * 50)
    print("ADDITIONAL CONSIDERATIONS")
    print("=" * 50)
    
    print("\nUUID Types and Performance:")
    print("• UUID4 (random): Most common, cryptographically secure")
    print("• UUID1 (timestamp + MAC): Sortable but may leak info")
    print("• UUID7 (timestamp + random): New standard, sortable and secure")
    
    print(f"\nExample UUIDs:")
    print(f"• UUID4: {uuid.uuid4()}")
    print(f"• UUID1: {uuid.uuid1()}")
    
    print("\nWhen to use each approach:")
    print("✓ UUID Primary Key:")
    print("  - Production applications")
    print("  - Distributed systems")
    print("  - When natural keys might change")
    print("  - APIs and microservices")
    
    print("\n✗ Natural Key (like email) as Primary Key:")
    print("  - Simple, single-user applications")
    print("  - Temporary/prototype systems")
    print("  - When absolutely sure the key will never change")
    
    print("\n⚡ Performance Notes:")
    print("• UUIDs are slightly larger (36 chars vs variable email length)")
    print("• String comparisons vs integer comparisons (if using INTEGER PK)")
    print("• Consider BINARY(16) storage for UUIDs in production for better performance")

if __name__ == "__main__":
    print("SQLite Primary Key Demonstration")
    print("Comparing Email vs UUID as Primary Keys")
    
    demonstrate_bad_practice()
    demonstrate_good_practice()
    demonstrate_additional_benefits()
    
    print("\n" + "=" * 50)
    print("CONCLUSION")
    print("=" * 50)
    print("While emails seem like natural identifiers, they make poor primary keys.")
    print("UUIDs provide stable, unique identifiers that don't change over time.")
    print("Use UUIDs for primary keys and keep emails as unique but updateable fields.")
