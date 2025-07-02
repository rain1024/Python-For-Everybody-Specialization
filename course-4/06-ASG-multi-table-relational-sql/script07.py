import sqlite3

def main():
    print("=== SQLite AUTOINCREMENT Demonstration ===\n")
    
    # Create in-memory database connection
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create Users table with AUTOINCREMENT primary key
    print("1. Creating Users table with AUTOINCREMENT...")
    cursor.execute('''
        CREATE TABLE Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            created_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert some users (without specifying user_id)
    print("2. Inserting users without specifying user_id...")
    users_data = [
        ('john_doe', 'john@example.com', 25),
        ('jane_smith', 'jane@example.com', 30),
        ('bob_wilson', 'bob@example.com', 28),
        ('alice_brown', 'alice@example.com', 22)
    ]
    
    cursor.executemany('''
        INSERT INTO Users (username, email, age) 
        VALUES (?, ?, ?)
    ''', users_data)
    
    # Display all users to show auto-incremented IDs
    print("3. Users after initial insert:")
    cursor.execute('SELECT * FROM Users ORDER BY user_id')
    users = cursor.fetchall()
    print(f"{'ID':<4} {'Username':<12} {'Email':<20} {'Age':<4} {'Created'}")
    print("-" * 60)
    for user in users:
        print(f"{user[0]:<4} {user[1]:<12} {user[2]:<20} {user[3]:<4} {user[4]}")
    print()
    
    # Delete a user in the middle
    print("4. Deleting user with ID 2 (jane_smith)...")
    cursor.execute('DELETE FROM Users WHERE user_id = 2')
    
    # Insert a new user to show AUTOINCREMENT continues from highest value
    print("5. Inserting new user after deletion...")
    cursor.execute('''
        INSERT INTO Users (username, email, age) 
        VALUES (?, ?, ?)
    ''', ('charlie_davis', 'charlie@example.com', 35))
    
    # Display users again
    print("6. Users after deletion and new insert:")
    cursor.execute('SELECT * FROM Users ORDER BY user_id')
    users = cursor.fetchall()
    print(f"{'ID':<4} {'Username':<12} {'Email':<20} {'Age':<4} {'Created'}")
    print("-" * 60)
    for user in users:
        print(f"{user[0]:<4} {user[1]:<12} {user[2]:<20} {user[3]:<4} {user[4]}")
    print()
    
    # Show the current AUTOINCREMENT value
    print("7. Checking AUTOINCREMENT sequence info...")
    cursor.execute("SELECT name, seq FROM sqlite_sequence WHERE name='Users'")
    seq_info = cursor.fetchone()
    if seq_info:
        print(f"Current AUTOINCREMENT sequence value for Users table: {seq_info[1]}")
    print()
    
    # Demonstrate explicit ID insertion (higher than current sequence)
    print("8. Inserting user with explicit high ID (10)...")
    cursor.execute('''
        INSERT INTO Users (user_id, username, email, age) 
        VALUES (?, ?, ?, ?)
    ''', (10, 'diana_white', 'diana@example.com', 27))
    
    # Insert another user without ID to show sequence updates
    print("9. Inserting another user without specifying ID...")
    cursor.execute('''
        INSERT INTO Users (username, email, age) 
        VALUES (?, ?, ?)
    ''', ('eve_green', 'eve@example.com', 24))
    
    # Final display
    print("10. Final Users table:")
    cursor.execute('SELECT * FROM Users ORDER BY user_id')
    users = cursor.fetchall()
    print(f"{'ID':<4} {'Username':<12} {'Email':<20} {'Age':<4} {'Created'}")
    print("-" * 60)
    for user in users:
        print(f"{user[0]:<4} {user[1]:<12} {user[2]:<20} {user[3]:<4} {user[4]}")
    print()
    
    # Show updated sequence value
    cursor.execute("SELECT name, seq FROM sqlite_sequence WHERE name='Users'")
    seq_info = cursor.fetchone()
    if seq_info:
        print(f"Final AUTOINCREMENT sequence value: {seq_info[1]}")
    
    print("\n=== Key AUTOINCREMENT Concepts Demonstrated ===")
    print("• AUTOINCREMENT ensures unique, incrementing primary keys")
    print("• IDs are assigned automatically when not specified")
    print("• Deleted IDs are NOT reused (gap at ID 2)")
    print("• Sequence continues from the highest ever used ID")
    print("• Explicit high ID insertion updates the sequence")
    print("• Next auto-generated ID comes after the highest used ID")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
