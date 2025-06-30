import sqlite3

# Tạo kết nối đến SQLite memory database (dữ liệu sẽ mất khi chương trình kết thúc)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tạo bảng Users
cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER
    )
''')

# Chèn dữ liệu mẫu
users_data = [
    (1, 'Nguyen Van A', 'a@email.com', 25),
    (2, 'Tran Thi B', 'b@email.com', 30),
    (3, 'Le Van C', 'c@email.com', 28),
    (4, 'Pham Thi D', 'd@email.com', 22)
]

cursor.executemany('INSERT INTO Users (id, name, email, age) VALUES (?, ?, ?, ?)', users_data)
conn.commit()

# Hiển thị dữ liệu trước khi UPDATE
print("=== DỮ LIỆU TRƯỚC KHI UPDATE ===")
cursor.execute('SELECT * FROM Users')
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")

print("\n" + "="*50)

# VÍ DỤ 1: UPDATE theo ID
print("\n=== VÍ DỤ 1: UPDATE theo ID ===")
cursor.execute("UPDATE Users SET name='Nguyen Van An Moi' WHERE id = 1")
conn.commit()
print(f"Đã cập nhật {cursor.rowcount} dòng")

# VÍ DỤ 2: UPDATE theo tuổi
print("\n=== VÍ DỤ 2: UPDATE theo tuổi ===")
cursor.execute("UPDATE Users SET name='Nguyen Van Tre Tuoi' WHERE age < 25")
conn.commit()
print(f"Đã cập nhật {cursor.rowcount} dòng")

# VÍ DỤ 3: UPDATE nhiều trường cùng lúc
print("\n=== VÍ DỤ 3: UPDATE nhiều trường ===")
cursor.execute("UPDATE Users SET name='Le Van C Moi', email='c_moi@email.com' WHERE id = 3")
conn.commit()
print(f"Đã cập nhật {cursor.rowcount} dòng")

# VÍ DỤ 4: UPDATE với điều kiện phức tạp
print("\n=== VÍ DỤ 4: UPDATE với điều kiện phức tạp ===")
cursor.execute("UPDATE Users SET name='Nguyen Van Lon Tuoi' WHERE age >= 30 AND email LIKE '%@email.com'")
conn.commit()
print(f"Đã cập nhật {cursor.rowcount} dòng")

# Hiển thị dữ liệu sau khi UPDATE
print("\n=== DỮ LIỆU SAU KHI UPDATE ===")
cursor.execute('SELECT * FROM Users')
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")

# Đóng kết nối
conn.close()
print("\n=== HOÀN THÀNH ===")
