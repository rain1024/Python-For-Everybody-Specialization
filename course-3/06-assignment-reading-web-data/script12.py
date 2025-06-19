# Ví dụ về cách Python 3 lưu trữ chuỗi (strings) bên trong
# Python 3 sử dụng Unicode để lưu trữ chuỗi

# 1. Chuỗi thông thường (ASCII)
text1 = "Hello"
print("1. Chuỗi ASCII:")
print(f"Chuỗi: {text1}")
print(f"Mã Unicode của từng ký tự:", [ord(c) for c in text1])
print()

# 2. Chuỗi có dấu tiếng Việt (Unicode)
text2 = "Xin chào"
print("2. Chuỗi Unicode tiếng Việt:")
print(f"Chuỗi: {text2}")
print(f"Mã Unicode của từng ký tự:", [ord(c) for c in text2])
print()

# 3. Chuỗi với emoji (Unicode)
text3 = "Python 🐍"
print("3. Chuỗi với emoji:")
print(f"Chuỗi: {text3}")
print(f"Mã Unicode của từng ký tự:", [ord(c) for c in text3])
print()

# 4. Chuyển đổi giữa các định dạng
text4 = "Xin chào 👋"
print("4. Chuyển đổi định dạng:")
print(f"Chuỗi gốc: {text4}")
print(f"UTF-8 bytes:", text4.encode('utf-8'))
print(f"UTF-16 bytes:", text4.encode('utf-16'))
