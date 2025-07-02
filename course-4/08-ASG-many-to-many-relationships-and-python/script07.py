import sqlite3

def demonstrate_execute_vs_executescript():
    print("=== SQLite Memory Database Demonstration ===")
    print("Comparing execute() vs executescript() methods\n")
    
    # Create an in-memory database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    print("1. Using execute() method - Single statement only:")
    print("-" * 50)
    
    # Using execute() - can only run one statement at a time
    try:
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
        print("✓ Table 'users' created successfully")
        
        cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
        print("✓ First user inserted")
        
        cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com')")
        print("✓ Second user inserted")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Show current data
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(f"\nCurrent users: {results}")
    
    print("\n" + "="*60)
    print("2. Using executescript() method - Multiple statements:")
    print("-" * 50)
    
    # Clear the table first
    cursor.execute("DELETE FROM users")
    
    # Using executescript() - can run multiple statements separated by semicolons
    script = """
    INSERT INTO users (name, email) VALUES ('Alice Johnson', 'alice@example.com');
    INSERT INTO users (name, email) VALUES ('Bob Wilson', 'bob@example.com');
    INSERT INTO users (name, email) VALUES ('Carol Brown', 'carol@example.com');
    CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);
    INSERT INTO products (name, price) VALUES ('Laptop', 999.99);
    INSERT INTO products (name, price) VALUES ('Mouse', 29.99);
    """
    
    try:
        cursor.executescript(script)
        print("✓ Multiple statements executed successfully with executescript()")
        
        # Show users data
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(f"\nUsers table: {users}")
        
        # Show products data
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        print(f"Products table: {products}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*60)
    print("3. Demonstrating the key difference:")
    print("-" * 50)
    
    # This would fail with execute() but works with executescript()
    multiple_statements = """
    UPDATE users SET email = 'newemail@example.com' WHERE name = 'Alice Johnson';
    UPDATE products SET price = price * 0.9 WHERE name = 'Laptop';
    """
    
    print("Trying to run multiple statements with execute():")
    try:
        cursor.execute(multiple_statements)
        print("✓ Success with execute()")
    except Exception as e:
        print(f"✗ Failed with execute(): {e}")
    
    print("\nTrying to run multiple statements with executescript():")
    try:
        cursor.executescript(multiple_statements)
        print("✓ Success with executescript()")
        
        # Verify the updates
        cursor.execute("SELECT * FROM users WHERE name = 'Alice Johnson'")
        alice = cursor.fetchone()
        print(f"Alice's updated record: {alice}")
        
        cursor.execute("SELECT * FROM products WHERE name = 'Laptop'")
        laptop = cursor.fetchone()
        print(f"Laptop's updated record: {laptop}")
        
    except Exception as e:
        print(f"✗ Failed with executescript(): {e}")
    
    # Close the connection
    conn.close()
    
    print("\n" + "="*60)
    print("SUMMARY:")
    print("• execute() can only run ONE SQL statement at a time")
    print("• executescript() can run MULTIPLE SQL statements separated by semicolons")
    print("• executescript() is useful for running SQL scripts or batch operations")
    print("• Both methods work with in-memory databases (:memory:)")

if __name__ == "__main__":
    demonstrate_execute_vs_executescript()
