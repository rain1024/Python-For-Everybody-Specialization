import sqlite3

# --- PHẦN LÝ THUYẾT ---
# Relation (quan hệ)   -> chính là Table (bảng)
# Attribute (thuộc tính) -> chính là Column (cột)
# Tuple (bộ)          -> chính là Row (hàng)

# Bước 2: Tạo kết nối tới cơ sở dữ liệu.
# Ở đây ta dùng ':memory:' để tạo một CSDL tạm thời trong bộ nhớ,
# nó sẽ biến mất khi chương trình kết thúc.
conn = sqlite3.connect(':memory:')

# Tạo một "con trỏ" (cursor) để thực thi các lệnh SQL
cursor = conn.cursor()

# Bước 3: Dùng lệnh CREATE TABLE để tạo bảng (Câu hỏi 2 & 6)
# Bảng 'HocVien' là một RELATION.
# Các cột 'id', 'ten', 'diem' là các ATTRIBUTES.
print("--- 1. Đang tạo bảng HocVien... ---")
cursor.execute('''
    CREATE TABLE HocVien (
        id INTEGER PRIMARY KEY,
        ten TEXT NOT NULL,
        diem REAL
    )
''')
print("✅ Tạo bảng thành công!")


# Bước 4: Dùng lệnh INSERT INTO để thêm dữ liệu (Câu hỏi 3)
# Mỗi lần INSERT là ta thêm một ROW (hay một TUPLE) vào bảng.
print("\n--- 2. Đang chèn dữ liệu học viên... ---")
hoc_vien_list = [
    (1, 'Trần Minh Anh', 8.5),
    (2, 'Lê Thị Bình', 9.0),
    (3, 'Nguyễn Văn Cường', 7.5),
    (4, 'Phạm Thuỳ Dung', 9.5)
]

cursor.executemany('INSERT INTO HocVien VALUES (?,?,?)', hoc_vien_list)
print("✅ Chèn dữ liệu thành công!")


# Bước 5: Dùng lệnh SELECT * để lấy tất cả dữ liệu (Câu hỏi 4)
print("\n--- 3. Lấy và hiển thị toàn bộ danh sách lớp: ---")
cursor.execute("SELECT * FROM HocVien")
all_students = cursor.fetchall() # Lấy tất cả các hàng kết quả

print("ID | Tên Học Viên      | Điểm")
print("---------------------------------")
for student in all_students:
    print(f"{student[0]:<2} | {student[1]:<17} | {student[2]}")


# Bước 6: Dùng ORDER BY để sắp xếp kết quả (Câu hỏi 5)
print("\n--- 4. Xếp hạng học viên theo điểm số từ cao đến thấp: ---")
cursor.execute("SELECT ten, diem FROM HocVien ORDER BY diem DESC")
ranked_students = cursor.fetchall()

print("Tên Học Viên      | Điểm")
print("---------------------------------")
for student in ranked_students:
    print(f"{student[0]:<17} | {student[1]}")


# Bước 7: Đóng kết nối khi đã hoàn thành
conn.close()