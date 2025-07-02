import sqlite3

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Create Colors table
cur.execute('''
CREATE TABLE Colors (
    id INTEGER PRIMARY KEY,
    color_name TEXT
)
''')

# Create Sizes table  
cur.execute('''
CREATE TABLE Sizes (
    id INTEGER PRIMARY KEY,
    size_name TEXT
)
''')

# Insert sample data into Colors table
colors_data = [
    (1, 'Red'),
    (2, 'Blue'), 
    (3, 'Green')
]

cur.executemany('INSERT INTO Colors (id, color_name) VALUES (?, ?)', colors_data)

# Insert sample data into Sizes table
sizes_data = [
    (1, 'Small'),
    (2, 'Medium'),
    (3, 'Large')
]

cur.executemany('INSERT INTO Sizes (id, size_name) VALUES (?, ?)', sizes_data)

# Display individual tables
print("=== Colors Table ===")
cur.execute('SELECT * FROM Colors')
for row in cur.fetchall():
    print(f"ID: {row[0]}, Color: {row[1]}")

print("\n=== Sizes Table ===")
cur.execute('SELECT * FROM Sizes')
for row in cur.fetchall():
    print(f"ID: {row[0]}, Size: {row[1]}")

# Demonstrate JOIN without ON (Cartesian product)
print("\n=== JOIN without ON (Cartesian Product) ===")
print("This combines every color with every size:")
cur.execute('SELECT Colors.color_name, Sizes.size_name FROM Colors JOIN Sizes')

results = cur.fetchall()
for row in results:
    print(f"Color: {row[0]}, Size: {row[1]}")

print(f"\nTotal combinations: {len(results)}")
print("Note: JOIN without ON creates a Cartesian product")
print("Each row from Colors table is paired with each row from Sizes table")
print("Result count = Colors rows × Sizes rows = 3 × 3 = 9")

# Alternative syntax (CROSS JOIN - more explicit)
print("\n=== Alternative: CROSS JOIN (same result) ===")
cur.execute('SELECT Colors.color_name, Sizes.size_name FROM Colors CROSS JOIN Sizes')
cross_results = cur.fetchall()
print(f"CROSS JOIN also produces {len(cross_results)} combinations")

# Close the connection
conn.close()
