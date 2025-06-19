import urllib.request

# Chỉ cần một dòng để mở URL, thư viện sẽ tự làm các bước socket, connect, send
try:
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

    # --- Lấy thông tin HEADER ---
    print("--- THÔNG TIN HEADERS ---")
    headers = fhand.info()
    print(headers)

    # Lấy riêng header 'Content-Type'
    print("-> Loại nội dung (Content-Type):", headers.get('Content-Type'))
    print("-" * 30)

    # --- Đọc và in NỘI DUNG FILE (BODY) ---
    print("\n--- NỘI DUNG FILE ---")
    # Đối tượng fhand có thể được duyệt qua như một file bình thường
    char_count = 0
    for line in fhand:
        decoded_line = line.decode().strip()
        print(decoded_line)
        char_count += len(decoded_line)

    print("-" * 30)
    print(f"\nTổng số ký tự đã đọc: {char_count}")


except Exception as e:
    print("Đã xảy ra lỗi:", e)