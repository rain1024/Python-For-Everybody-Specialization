#!/usr/bin/env python3

import sqlite3

# Create an in-memory SQLite database
print("=== SQLite LIMIT Clause Demonstration ===\n")

# Connect to in-memory database
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Create a Counts table similar to the one in the SQL question
cur.execute('''
CREATE TABLE Counts (
    org TEXT PRIMARY KEY,
    count INTEGER
)
''')

# Insert sample data - more than 10 rows to demonstrate LIMIT
sample_data = [
    ('Google', 45),
    ('Microsoft', 38),
    ('Apple', 42),
    ('Amazon', 35),
    ('Meta', 28),
    ('Tesla', 33),
    ('Netflix', 25),
    ('Adobe', 22),
    ('IBM', 18),
    ('Oracle', 20),
    ('Salesforce', 15),
    ('Zoom', 12),
    ('Spotify', 14),
    ('Twitter', 16),
    ('LinkedIn', 19)
]

cur.executemany('INSERT INTO Counts (org, count) VALUES (?, ?)', sample_data)

print("1. First, let's see ALL data in the table:")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')
all_results = cur.fetchall()
for i, (org, count) in enumerate(all_results, 1):
    print(f"{i:2d}. {org:<12} - {count}")

print(f"\nTotal rows in table: {len(all_results)}")

print("\n" + "="*50)

print("\n2. Now let's use LIMIT 10 (the SQL from your question):")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
limited_results = cur.fetchall()

for i, (org, count) in enumerate(limited_results, 1):
    print(f"{i:2d}. {org:<12} - {count}")

print(f"\nRows returned with LIMIT 10: {len(limited_results)}")

print("\n" + "="*50)

print("\n3. Demonstrating different LIMIT values:")

# LIMIT 5
print("\nLIMIT 5:")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5')
for i, (org, count) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {org} - {count}")

# LIMIT 3
print("\nLIMIT 3:")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 3')
for i, (org, count) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {org} - {count}")

print("\n" + "="*50)

print("\n4. LIMIT without ORDER BY (shows first N rows as stored):")
cur.execute('SELECT org, count FROM Counts LIMIT 5')
for i, (org, count) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {org} - {count}")

print("\n" + "="*50)

print("\n5. LIMIT with different ORDER BY directions:")

print("\nASCENDING order with LIMIT 5 (lowest counts first):")
cur.execute('SELECT org, count FROM Counts ORDER BY count ASC LIMIT 5')
for i, (org, count) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {org} - {count}")

print("\nDESCENDING order with LIMIT 5 (highest counts first):")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5')
for i, (org, count) in enumerate(cur.fetchall(), 1):
    print(f"{i}. {org} - {count}")

print("\n" + "="*50)

print("\nKEY CONCEPTS DEMONSTRATED:")
print("• LIMIT clause restricts the number of rows returned")
print("• It works AFTER ORDER BY has sorted the results")
print("• LIMIT 10 returns the first 10 rows from the sorted result set")
print("• Without ORDER BY, LIMIT returns the first N rows as stored")
print("• LIMIT is useful for getting 'top N' or 'bottom N' results")

# Close the connection
conn.close()

print("\n=== End of Demonstration ===")
