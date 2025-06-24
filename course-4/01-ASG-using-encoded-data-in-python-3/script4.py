s1 = "Hello, world!"
s2 = "Xin chào, thế giới! 👋" # Bao gồm ký tự emoji (Unicode)

print(type(s1)) # Output: <class 'str'>
print(type(s2)) # Output: <class 'str'>

# Kiểm tra độ dài của chuỗi (số lượng ký tự Unicode)
print(len(s1)) # Output: 13
print(len(s2)) # Output: 22 (kể cả khoảng trắng và emoji)