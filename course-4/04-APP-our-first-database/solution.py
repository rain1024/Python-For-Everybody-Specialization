import sqlite3

# Connect to SQLite in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the Ages table
cursor.execute('''CREATE TABLE IF NOT EXISTS Ages ( 
    name VARCHAR(128), 
    age INTEGER
)''')

# Delete any existing rows to ensure table is empty
cursor.execute('DELETE FROM Ages')

# Insert the specified rows
data = [
    ('Annalisa', 19),
    ('Libbi', 17),
    ('Veera', 17),
    ('Rehanna', 27),
    ('Zella', 16)
]

for name, age in data:
    cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', (name, age))

# Commit the changes
conn.commit()

# Run the required query to get hex values
cursor.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
results = cursor.fetchall()

# Print all results for verification
print("All hex values (ordered):")
for i, row in enumerate(results, 1):
    print(f"{i}. {row[0]}")

# Get the first row (smallest hex value)
first_hex = results[0][0]
print(f"\nFirst row hex value: {first_hex}")
print(f"Answer: {first_hex}")

# Close the database connection
conn.close()
