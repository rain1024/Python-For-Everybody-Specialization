import urllib.request

url = "https://vnexpress.net/" # Một URL ví dụ

try:
    with urllib.request.urlopen(url) as response:
        # Dữ liệu nhận được từ mạng là dạng bytes
        raw_bytes_data = response.read()
        print(f"Kiểu dữ liệu nhận được: {type(raw_bytes_data)}")
        print(f"Một phần dữ liệu dạng bytes: {raw_bytes_data[:100]}...") # In ra 100 byte đầu tiên

        # Để làm việc với dữ liệu này dưới dạng chuỗi văn bản, chúng ta phải decode nó
        # Hầu hết các trang web hiện đại đều sử dụng UTF-8
        text_data = raw_bytes_data.decode('utf-8')
        print(f"\nKiểu dữ liệu sau khi decode: {type(text_data)}")
        print(f"Một phần dữ liệu dạng chuỗi: {text_data[:200]}...") # In ra 200 ký tự đầu tiên
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")