import sqlite3
import os

# Kết nối tới database SQLite (tạo file nếu chưa tồn tại)
# Remove the SQLite database file
if os.path.exists('people.db'):
    os.remove('people.db')
    print("SQLite database file 'people.db' has been removed.")
else:
    print("SQLite database file 'people.db' does not exist.")
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Tạo bảng people
cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE,
        phone TEXT,
        city TEXT
    )
''')

print("Bảng 'people' đã được tạo thành công!")

# Thêm một số dữ liệu mẫu
sample_data = [
    ('Nguyễn Văn A', 25, 'nva@email.com', '0123456789', 'Hà Nội'),
    ('Trần Thị B', 30, 'ttb@email.com', '0987654321', 'Hồ Chí Minh'),
    ('Lê Văn C', 28, 'lvc@email.com', '0345678901', 'Đà Nẵng'),
    ('Phạm Thị D', 35, 'ptd@email.com', '0567890123', 'Cần Thơ'),
    ('Hoàng Văn E', 22, 'hve@email.com', '0789012345', 'Hải Phòng')
]

cursor.executemany('''
    INSERT INTO people (name, age, email, phone, city)
    VALUES (?, ?, ?, ?, ?)
''', sample_data)

print("Đã thêm dữ liệu mẫu vào bảng!")

# Truy vấn và hiển thị dữ liệu
cursor.execute('SELECT * FROM people')
rows = cursor.fetchall()

print("\nDữ liệu trong bảng people:")
print("-" * 80)
print(f"{'ID':<5} {'Tên':<15} {'Tuổi':<5} {'Email':<20} {'Điện thoại':<12} {'Thành phố':<15}")
print("-" * 80)

for row in rows:
    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<5} {row[3]:<20} {row[4]:<12} {row[5]:<15}")

# Một số truy vấn khác
print("\n" + "="*50)
print("CÁC TRUY VẤN KHÁC:")
print("="*50)

# Đếm số người
cursor.execute('SELECT COUNT(*) FROM people')
count = cursor.fetchone()[0]
print(f"\nTổng số người: {count}")

# Tìm người theo tuổi
cursor.execute('SELECT * FROM people WHERE age > 25')
older_people = cursor.fetchall()
print(f"\nNhững người trên 25 tuổi ({len(older_people)} người):")
for person in older_people:
    print(f"  - {person[1]} ({person[2]} tuổi)")

# Tìm người theo thành phố
cursor.execute('SELECT * FROM people WHERE city = "Hà Nội"')
hanoi_people = cursor.fetchall()
print(f"\nNhững người ở Hà Nội ({len(hanoi_people)} người):")
for person in hanoi_people:
    print(f"  - {person[1]}")

# Sắp xếp theo tuổi
cursor.execute('SELECT name, age FROM people ORDER BY age DESC')
sorted_people = cursor.fetchall()
print(f"\nDanh sách sắp xếp theo tuổi (giảm dần):")
for person in sorted_people:
    print(f"  - {person[0]}: {person[1]} tuổi")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("\nHoàn thành! Database đã được lưu.")

# Remove the SQLite database file
if os.path.exists('people.db'):
    os.remove('people.db')
    print("SQLite database file 'people.db' has been removed.")
else:
    print("SQLite database file 'people.db' does not exist.")