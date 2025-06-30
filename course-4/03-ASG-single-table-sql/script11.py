import sqlite3

# Create a connection to an in-memory database
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Create a Users table
cur.execute('''
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
''')

# Insert some sample data
cur.execute("INSERT INTO Users (name, email) VALUES ('John Doe', 'john@example.com')")
cur.execute("INSERT INTO Users (name, email) VALUES ('Jane Smith', 'jane@example.com')")
cur.execute("INSERT INTO Users (name, email) VALUES ('Bob Johnson', 'bob@example.com')")
cur.execute("INSERT INTO Users (name, email) VALUES ('Alice Brown', 'alice@example.com')")
cur.execute("INSERT INTO Users (name, email) VALUES ('Charlie Wilson', 'charlie@example.com')")

# Commit the inserts
conn.commit()

# Demonstrate SELECT COUNT(*) FROM Users
print("=== SELECT COUNT(*) FROM Users ===")
cur.execute("SELECT COUNT(*) FROM Users")
result = cur.fetchone()
print(f"Total number of users: {result[0]}")

# Show all users for verification
print("\n=== All Users (for verification) ===")
cur.execute("SELECT * FROM Users")
users = cur.fetchall()
for user in users:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

# Close the connection
conn.close()
