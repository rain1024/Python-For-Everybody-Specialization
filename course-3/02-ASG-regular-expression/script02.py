import re

text = "apple banana cherry date elderberry fig grape"

print(f"Original text: '{text}'")
print("-" * 30)

# Ví dụ 1: Tìm tất cả các từ có chữ 'a'
pattern1 = r'\b\w*a\w*\b' # Mẫu: một từ có chứa chữ 'a'

matches = re.findall(pattern1, text)
print(re.findall(pattern1, text))