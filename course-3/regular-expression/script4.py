import re

text = "cat hat bat rat mat cot hot dot"

print(f"Original text: '{text}'")
print("-" * 30)

# Ví dụ 1: Sử dụng '.' để khớp bất kỳ ký tự nào
# Giả sử bạn muốn tìm tất cả các từ có 3 chữ cái mà bắt đầu bằng một ký tự bất kỳ,
# sau đó là 'at'.
pattern = r'.at' # Regex: Bất kỳ ký tự nào theo sau bởi 'at'

print(f"Tìm kiếm mẫu: '{pattern}'")
matches = re.findall(pattern, text)
print(f"Các chuỗi khớp: {matches}")