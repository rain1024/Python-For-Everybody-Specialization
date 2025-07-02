import sqlite3

# Create an in-memory SQLite database
print("=== SQLite Memory Database Demonstration ===\n")

# Connect to in-memory database
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Create a sample table
cur.execute('''
    CREATE TABLE Counts (
        id INTEGER PRIMARY KEY,
        org TEXT,
        count INTEGER
    )
''')

# Insert some sample data
sample_data = [
    ('google.com', 15),
    ('microsoft.com', 8),
    ('apple.com', 12),
    ('facebook.com', 6)
]

for org, count in sample_data:
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org, count))

conn.commit()

print("Sample data inserted into Counts table:")
cur.execute('SELECT * FROM Counts')
rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Org: {row[1]}, Count: {row[2]}")

print("\n" + "="*50)

# Demonstration 1: Query that returns results
print("\n1. Query that RETURNS results:")
cur.execute('SELECT count FROM Counts WHERE org = ?', ('google.com',))
row = cur.fetchone()
print(f"Result: {row}")
print(f"Type: {type(row)}")
if row:
    print(f"Count value: {row[0]}")

print("\n" + "-"*30)

# Demonstration 2: Query that returns NO results
print("\n2. Query that returns NO results:")
cur.execute('SELECT count FROM Counts WHERE org = ?', ('nonexistent.com',))
row = cur.fetchone()
print(f"Result: {row}")
print(f"Type: {type(row)}")
print(f"Is None? {row is None}")

print("\n" + "-"*30)

# Demonstration 3: The specific question scenario
print("\n3. Answering the quiz question:")
print("Code: cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))")
print("      row = cur.fetchone()")
print("When no rows match the WHERE clause:")

# Simulate the exact scenario from the question
cur.execute('SELECT count FROM Counts WHERE org = ?', ('xyz.com',))
row = cur.fetchone()
print(f"row = {row}")
print(f"The answer is: {row} (which is None)")

print("\n" + "-"*30)

# Additional demonstrations
print("\n4. Additional fetchone() behaviors:")

# Multiple results - fetchone() gets first
cur.execute('SELECT org FROM Counts WHERE count > 5')
row = cur.fetchone()
print(f"First result from multiple matches: {row}")

# fetchall() vs fetchone() comparison
print("\n5. fetchall() vs fetchone() comparison:")
cur.execute('SELECT org FROM Counts WHERE count > 10')
all_rows = cur.fetchall()
print(f"fetchall() result: {all_rows}")

cur.execute('SELECT org FROM Counts WHERE count > 10')
one_row = cur.fetchone()
print(f"fetchone() result: {one_row}")

print("\n" + "="*50)
print("SUMMARY:")
print("When fetchone() is called and no rows match the WHERE clause:")
print("- The result is None")
print("- None is a special Python value representing 'nothing'")
print("- This is different from an empty list [] or empty dictionary {}")
print("- You can check: if row is None: # handle no results")

# Close the connection
conn.close()
print("\nDatabase connection closed.")
