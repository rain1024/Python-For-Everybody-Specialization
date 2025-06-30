import sqlite3

def create_and_populate_table(cursor):
    """Tạo bảng students và thêm dữ liệu mẫu"""
    # Tạo bảng students
    cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT,
            email TEXT
        )
    ''')
    
    # Thêm dữ liệu mẫu
    students_data = [
        (1, 'Nguyễn Văn An', 20, 'A', 'an@example.com'),
        (2, 'Trần Thị Bình', 19, 'B', 'binh@example.com'),
        (3, 'Lê Văn Cường', 21, 'A', 'cuong@example.com'),
        (4, 'Phạm Thị Dung', 20, 'C', 'dung@example.com'),
        (5, 'Hoàng Văn Em', 18, 'B', 'em@example.com')
    ]
    
    cursor.executemany('''
        INSERT INTO students (id, name, age, grade, email) 
        VALUES (?, ?, ?, ?, ?)
    ''', students_data)

def show_all_students(cursor):
    """Hiển thị tất cả sinh viên"""
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("Danh sách sinh viên:")
    print("-" * 60)
    print(f"{'ID':<3} {'Tên':<15} {'Tuổi':<4} {'Lớp':<3} {'Email':<20}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<3} {row[1]:<15} {row[2]:<4} {row[3]:<3} {row[4]:<20}")
    print(f"Tổng số sinh viên: {len(rows)}")
    print()

def demo_delete_with_where():
    """Minh họa DELETE với WHERE clause"""
    print("=" * 70)
    print("DEMO 1: DELETE với WHERE clause")
    print("=" * 70)
    
    # Tạo kết nối mới
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Tạo và thêm dữ liệu
    create_and_populate_table(cursor)
    conn.commit()
    
    print("Dữ liệu ban đầu:")
    show_all_students(cursor)
    
    # DELETE với WHERE - chỉ xóa sinh viên có grade = 'C'
    print("Thực hiện: DELETE FROM students WHERE grade = 'C'")
    cursor.execute("DELETE FROM students WHERE grade = 'C'")
    affected_rows = cursor.rowcount
    conn.commit()
    
    print(f"Số dòng bị ảnh hưởng: {affected_rows}")
    print("\nDữ liệu sau khi xóa:")
    show_all_students(cursor)
    
    conn.close()

def demo_delete_without_where():
    """Minh họa DELETE không có WHERE clause"""
    print("=" * 70)
    print("DEMO 2: DELETE không có WHERE clause")
    print("=" * 70)
    
    # Tạo kết nối mới
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Tạo và thêm dữ liệu
    create_and_populate_table(cursor)
    conn.commit()
    
    print("Dữ liệu ban đầu:")
    show_all_students(cursor)
    
    # DELETE không có WHERE - xóa TẤT CẢ dữ liệu
    print("Thực hiện: DELETE FROM students")
    cursor.execute("DELETE FROM students")
    affected_rows = cursor.rowcount
    conn.commit()
    
    print(f"Số dòng bị ảnh hưởng: {affected_rows}")
    print("\nDữ liệu sau khi xóa:")
    show_all_students(cursor)
    
    conn.close()

def demo_delete_with_specific_condition():
    """Minh họa DELETE với điều kiện cụ thể khác"""
    print("=" * 70)
    print("DEMO 3: DELETE với điều kiện phức tạp")
    print("=" * 70)
    
    # Tạo kết nối mới
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Tạo và thêm dữ liệu
    create_and_populate_table(cursor)
    conn.commit()
    
    print("Dữ liệu ban đầu:")
    show_all_students(cursor)
    
    # DELETE với điều kiện phức tạp - xóa sinh viên tuổi >= 20
    print("Thực hiện: DELETE FROM students WHERE age >= 20")
    cursor.execute("DELETE FROM students WHERE age >= 20")
    affected_rows = cursor.rowcount
    conn.commit()
    
    print(f"Số dòng bị ảnh hưởng: {affected_rows}")
    print("\nDữ liệu sau khi xóa:")
    show_all_students(cursor)
    
    conn.close()

def main():
    print("MINH HỌA SỰ KHÁC BIỆT GIỮA DELETE CÓ WHERE VÀ KHÔNG CÓ WHERE")
    print("="*70)
    
    # Demo 1: DELETE với WHERE
    demo_delete_with_where()
    
    input("Nhấn Enter để tiếp tục...")
    
    # Demo 2: DELETE không có WHERE
    demo_delete_without_where()
    
    input("Nhấn Enter để tiếp tục...")
    
    # Demo 3: DELETE với điều kiện khác
    demo_delete_with_specific_condition()
    
    print("\n" + "="*70)
    print("KẾT LUẬN:")
    print("="*70)
    print("1. DELETE với WHERE clause:")
    print("   - Chỉ xóa những dòng thỏa mãn điều kiện")
    print("   - An toàn hơn, có kiểm soát")
    print("   - Có thể xóa 0, 1 hoặc nhiều dòng tùy điều kiện")
    print()
    print("2. DELETE không có WHERE clause:")
    print("   - Xóa TẤT CẢ dữ liệu trong bảng")
    print("   - Rất nguy hiểm, cần thận trọng")
    print("   - Bảng vẫn tồn tại nhưng rỗng")
    print()
    print("⚠️  LƯU Ý: Luôn sử dụng WHERE clause trừ khi bạn thực sự muốn xóa tất cả!")

if __name__ == "__main__":
    main()
