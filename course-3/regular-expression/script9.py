import re

line_of_text = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
regex_pattern = r'\S+?@\S+'

print(f"Dòng văn bản: '{line_of_text}'")
print(f"Mẫu Regular Expression: '{regex_pattern}'")

# re.findall() sẽ tìm tất cả các chuỗi khớp với mẫu.
matches = re.findall(regex_pattern, line_of_text)

print(f"Kết quả khớp: {matches}")