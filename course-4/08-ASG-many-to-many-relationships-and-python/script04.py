import sqlite3

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Create the Counts table
cur.execute('''
CREATE TABLE Counts (
    org TEXT,
    count INTEGER
)
''')

# Insert sample data
sample_data = [
    ('google.com', 45),
    ('apple.com', 32),
    ('microsoft.com', 28),
    ('facebook.com', 19),
    ('amazon.com', 67),
    ('google.com', 12),  # Another entry for google.com to show multiple records
    ('apple.com', 8)     # Another entry for apple.com
]

cur.executemany('INSERT INTO Counts (org, count) VALUES (?, ?)', sample_data)

print("=== SQLite Database Parameterized Query Demonstration ===\n")

# Display all data in the table
print("All data in Counts table:")
cur.execute('SELECT org, count FROM Counts')
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\n" + "="*50 + "\n")

# Demonstrate the parameterized query concept
def get_count_for_org(org):
    """Get count value for a specific organization using parameterized query"""
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    results = cur.fetchall()
    return results

# Test with different organizations
test_orgs = ['google.com', 'apple.com', 'netflix.com', 'microsoft.com']

for org in test_orgs:
    print(f"Searching for org: '{org}'")
    results = get_count_for_org(org)
    
    if results:
        print(f"  Found {len(results)} record(s):")
        for row in results:
            print(f"    count = {row[0]}")
    else:
        print("  No records found")
    print()

print("="*50 + "\n")

# Demonstrate aggregation - sum all counts for an organization
print("Sum of all counts per organization:")
cur.execute('''
SELECT org, SUM(count) as total_count 
FROM Counts 
GROUP BY org 
ORDER BY total_count DESC
''')

for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\n" + "="*50 + "\n")

# Demonstrate the exact query pattern from the user's example
print("Using the exact query pattern: cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))")
org = 'google.com'
print(f"Looking for org: {org}")

cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
results = cur.fetchall()

print(f"Results: {results}")

# Close the connection
conn.close()

print("\nDatabase connection closed.")
