import re

text = "abbbbbc aac b cccc"

print(f"Original text: '{text}'")
print("-" * 30)

# Ví dụ 1: Sử dụng '+' (một hoặc nhiều lần)
# Tìm kiếm một 'a', theo sau là một hoặc nhiều 'b', sau đó là một 'c'
pattern_plus = r'ab+c'

print(f"Tìm kiếm mẫu '{pattern_plus}':")
matches_plus = re.findall(pattern_plus, text)
print(f"Kết quả khớp: {matches_plus}")
# Output: ['abbbbbc', 'abc']
# Giải thích:
# - 'abbbbbc' khớp vì có 'a', theo sau là nhiều 'b', rồi đến 'c'.
# - 'abc' khớp vì có 'a', theo sau là một 'b', rồi đến 'c'.
# - 'ac' (nếu có trong chuỗi) sẽ KHÔNG khớp vì không có ít nhất một 'b'.
print("-" * 30)

# Ví dụ 2: Sử dụng '*' (không hoặc nhiều lần)
# Tìm kiếm một 'a', theo sau là không hoặc nhiều 'b', sau đó là một 'c'
pattern_star = r'ab*c'

print(f"Tìm kiếm mẫu '{pattern_star}':")
matches_star = re.findall(pattern_star, text)
print(f"Kết quả khớp: {matches_star}")
# Output: ['abbbbbc', 'abc', 'ac'] (giả sử 'ac' có trong chuỗi)
# Giải thích (thêm 'ac' vào text để minh họa rõ hơn):
text_with_ac = "abbbbbc aac b cccc ac"
print(f"Original text (có thêm 'ac'): '{text_with_ac}'")