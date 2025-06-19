import re

html_line = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

# 1. Sử dụng biểu thức chính quy đã chọn: href="(.+)"
# re.findall() tìm tất cả các lần xuất hiện của mẫu và trả về các nhóm chụp (capturing groups)
matches = re.findall(r'href="(.+)"', html_line)

if matches:
    extracted_url = matches[0]
    print(f"URL được trích xuất bằng href='(.+)': {extracted_url}")
else:
    print("Không tìm thấy URL với biểu thức href='(.+)'")

print("\n--- Thử các biểu thức khác để thấy sự khác biệt ---")

# 2. Thử với http://.* (lưu ý tính greedy)
matches_greedy = re.findall(r'http://.*', html_line)
if matches_greedy:
    print(f"Kết quả với http://.* (greedy): {matches_greedy}")
    # Kết quả sẽ là ['http://www.dr-chuck.com">here</a></p>']
    # Vì .* là greedy, nó sẽ khớp càng nhiều càng tốt cho đến cuối dòng.
else:
    print("Không tìm thấy với http://.*")

# 3. Thử với http://.*? (sử dụng non-greedy để chỉ lấy URL)
# Đây là cách tốt hơn nếu bạn muốn lấy bất kỳ URL nào bắt đầu bằng http:// và kết thúc bằng "
matches_non_greedy = re.findall(r'http://(.*?)"', html_line)
if matches_non_greedy:
    print(f"Kết quả với http://(.*?)\" (non-greedy): {matches_non_greedy}")
    # Kết quả sẽ là ['www.dr-chuck.com']
    # Bạn sẽ cần thêm 'http://' vào nếu muốn lấy đầy đủ URL
    # Hoặc điều chỉnh regex một chút: 'href="(http://.*?)"'
else:
    print("Không tìm thấy với http://(.*?)\"")

# Ví dụ tốt hơn để lấy URL đầy đủ và là non-greedy
matches_full_url_non_greedy = re.findall(r'href="(http://.*?)"', html_line)
if matches_full_url_non_greedy:
    print(f"Kết quả với href=\"(http://.*?)\" (non-greedy và đầy đủ): {matches_full_url_non_greedy}")
else:
    print("Không tìm thấy với href=\"(http://.*?)\"")


# 1. Sử dụng biểu thức chính quy đã chọn: href="(.+)"
# re.findall() tìm tất cả các lần xuất hiện của mẫu và trả về các nhóm chụp (capturing groups)
matches = re.findall(r'href=".+"', html_line)

if matches:
    extracted_url = matches[0]
    print(f"URL được trích xuất bằng href='.+': {extracted_url}")
else:
    print("Không tìm thấy URL với biểu thức href='(.+)'")