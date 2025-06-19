import re

text = "Product ID: 12345. Price: 99.99$. Quantity: 0. Phone: (123) 456-7890."

print(f"Original text: '{text}'")
print("-" * 30)

# Mẫu: [0-9]+
# Khớp một hoặc nhiều chữ số liên tiếp.
pattern = r'[0-9]+'

print(f"Tìm kiếm mẫu '{pattern}':")
matches = re.findall(pattern, text)
print(f"Các chuỗi khớp: {matches}")
# Output: ['12345', '99', '99', '0', '123', '456', '7890']
# Giải thích:
# - '12345' được khớp vì là một chuỗi các chữ số.
# - '99' và '99' được khớp riêng biệt vì có dấu chấm ở giữa.
# - '0' được khớp.
# - '123', '456', '7890' được khớp riêng biệt vì có dấu ngoặc và dấu gạch ngang ở giữa.

print("-" * 30)

# So sánh với [0-9]* (Không hoặc nhiều chữ số)
pattern_star = r'[0-9]*'
print(f"Tìm kiếm mẫu '{pattern_star}':")
matches_star = re.findall(pattern_star, text)
# Kết quả sẽ rất dài vì nó sẽ khớp cả các chuỗi rỗng giữa các ký tự không phải số.
# Ví dụ: ['', '', '', '12345', '', '', '', '', '', '99', '', '99', '', '', '', '0', '', '', '', '123', '', '', '', '456', '', '7890', '', '', '']
# Đây là lý do tại sao [0-9]+ thường được ưu tiên hơn [0-9]* khi bạn muốn khớp ít nhất một số.
# Để kiểm tra, bạn có thể chạy:
# print(f"Các chuỗi khớp (với *): {matches_star}")
# Và sẽ thấy rất nhiều chuỗi rỗng.

print("-" * 30)

# Ví dụ về một biểu thức toán học
text_math = "2 * (3 + 5) / 4"
# Mẫu [0-9]+ sẽ chỉ khớp: ['2', '3', '5', '4']
print(f"Mẫu '{pattern}' trong '{text_math}': {re.findall(pattern, text_math)}")
