import sqlite3
import os

DB_FILE = "production.db"

# --- Thiết lập môi trường ---
# Giả lập việc tạo CSDL và thêm dữ liệu
def setup_database():
    # Xóa file db cũ nếu có để chạy lại từ đầu
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Tạo bảng sản phẩm
    cursor.execute('''
        CREATE TABLE SanPham (
            id INTEGER PRIMARY KEY,
            ten_san_pham TEXT,
            so_luong_da_ban INTEGER
        )
    ''')
    # Thêm dữ liệu mẫu
    products = [
        ('Laptop Pro', 150),
        ('Chuột Gaming', 450),
        ('Bàn phím cơ', 320),
        ('Màn hình 4K', 120),
        ('Tai nghe chống ồn', 280)
    ]
    cursor.executemany('INSERT INTO SanPham (ten_san_pham, so_luong_da_ban) VALUES (?,?)', products)
    conn.commit()
    conn.close()
    print("✅ Đã thiết lập CSDL 'production.db' với dữ liệu mẫu.")

# ==============================================================================
# PHẦN 1: CÔNG VIỆC CỦA LẬP TRÌNH VIÊN (DEVELOPER)
# ==============================================================================
# Developer viết code này, nó sẽ là một phần của ứng dụng web hoặc di động.
# Họ không cần đăng nhập trực tiếp vào CSDL.

def get_top_selling_products(limit=3):
    """
    Hàm này là một phần của ứng dụng, được viết bởi Developer.
    Nó kết nối tới CSDL theo cách an toàn (dùng connection string của ứng dụng)
    và chỉ thực hiện một nhiệm vụ cụ thể.
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Câu lệnh SQL để lấy top sản phẩm
        query = "SELECT ten_san_pham, so_luong_da_ban FROM SanPham ORDER BY so_luong_da_ban DESC LIMIT ?"
        
        cursor.execute(query, (limit,))
        top_products = cursor.fetchall()
        
        return top_products
    except sqlite3.Error as e:
        print(f"Lỗi ứng dụng: {e}")
        return []
    finally:
        if conn:
            conn.close()

# ==============================================================================
# PHẦN 2: CÔNG VIỆC CỦA QUẢN TRỊ VIÊN CSDL (DBA)
# ==============================================================================
# DBA chạy một script riêng biệt để bảo trì, thường là chạy trực tiếp trên server.
# Script này có thể thực hiện những tác vụ ở mức hệ thống mà ứng dụng không làm.

def run_dba_maintenance_script():
    """
    Kịch bản này được DBA chạy trực tiếp để kiểm tra "sức khỏe" CSDL.
    Họ có quyền chạy các lệnh đặc biệt (ví dụ: PRAGMA trong SQLite)
    để xem thông tin hệ thống của CSDL.
    """
    print("\n--- Bắt đầu chạy kịch bản bảo trì của DBA ---")
    conn = None
    try:
        # DBA có thông tin đăng nhập trực tiếp
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        print("\n[DBA] Kiểm tra thông tin bảng 'SanPham':")
        # PRAGMA là lệnh đặc biệt của SQLite, DBA dùng nó để xem cấu trúc bảng
        cursor.execute("PRAGMA table_info(SanPham);")
        print(cursor.fetchall())

        print("\n[DBA] Kiểm tra kích thước ước tính của CSDL:")
        # Lấy số lượng trang và kích thước trang để ước tính dung lượng
        cursor.execute("PRAGMA page_count;")
        page_count = cursor.fetchone()[0]
        cursor.execute("PRAGMA page_size;")
        page_size = cursor.fetchone()[0]
        print(f"-> CSDL có {page_count} trang, mỗi trang {page_size} bytes. Tổng cộng ~{page_count * page_size / 1024} KB.")

    except sqlite3.Error as e:
        print(f"Lỗi script bảo trì: {e}")
    finally:
        if conn:
            conn.close()
    print("--- Kết thúc kịch bản bảo trì của DBA ---")


# --- CHẠY CHƯƠNG TRÌNH MINH HỌA ---
if __name__ == "__main__":
    # 1. Khởi tạo môi trường
    setup_database()

    # 2. Giả lập ứng dụng chạy tính năng của Developer
    print("\n--- Ứng dụng đang chạy tính năng 'Top sản phẩm'... ---")
    top_3 = get_top_selling_products(3)
    print("🏆 Top 3 sản phẩm bán chạy nhất:")
    for i, product in enumerate(top_3):
        print(f"  {i+1}. {product[0]} (đã bán: {product[1]})")

    # 3. Giả lập DBA thực hiện công việc bảo trì
    run_dba_maintenance_script()