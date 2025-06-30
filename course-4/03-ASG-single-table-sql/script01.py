# create a table using sqlite
import sqlite3
import os

# Connect to SQLite database (creates the file if it doesn't exist)
if os.path.exists('example.db'):
    os.remove('example.db')
    print("SQLite database file 'example.db' has been removed.")
else:
    print("SQLite database file 'example.db' does not exist.")
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        created_date TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert some sample data
sample_users = [
    ('John Doe', 'john@example.com', 30),
    ('Jane Smith', 'jane@example.com', 25),
    ('Bob Johnson', 'bob@example.com', 35),
    ('Alice Williams', 'alice@example.com', 28)
]

cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', sample_users)

# Commit the changes
conn.commit()

# Query the table to verify data was inserted
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("Users table contents:")
print("ID | Name | Email | Age | Created Date")
print("-" * 50)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

# Close the connection
conn.close()

print("\nTable created successfully and populated with sample data!")

import os

# Remove the SQLite database file
if os.path.exists('example.db'):
    os.remove('example.db')
    print("SQLite database file 'example.db' has been removed.")
else:
    print("SQLite database file 'example.db' does not exist.")

