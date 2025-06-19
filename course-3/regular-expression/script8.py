import re

html_text = "<h1>Title 1</h1> <p>Paragraph 1</p> <h1>Title 2</h1>"

# --- Ví dụ 1: Greedy Quantifier '*' (Mặc định) ---
# Mục tiêu: Khớp từ <h1> mở đầu đến </h1> đóng cuối cùng.
# Vì '*' là greedy, nó sẽ cố gắng khớp càng nhiều càng tốt.
pattern_greedy = r'<h1>.*</h1>'

print(f"Text: '{html_text}'")
print(f"Mẫu Greedy: '{pattern_greedy}'")
matches_greedy = re.findall(pattern_greedy, html_text)
print(f"Kết quả khớp Greedy: {matches_greedy}")

print("-" * 50)

# --- Ví dụ 2: Non-Greedy Quantifier '*?' ---
# Mục tiêu: Khớp từ <h1> mở đầu đến </h1> đóng ĐẦU TIÊN mà nó gặp.
# Thêm '?' sau '*' để biến nó thành non-greedy.
pattern_non_greedy = r'<h1>.*?</h1>'

print(f"Mẫu Non-Greedy: '{pattern_non_greedy}'")
matches_non_greedy = re.findall(pattern_non_greedy, html_text)
print(f"Kết quả khớp Non-Greedy: {matches_non_greedy}")