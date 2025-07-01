import re

text1 = "Giá của sản phẩm là $19.99"

match3 = re.search(r'\$', text1)
if match3:
    print(f"Match found for '\\$' in text1: '{match3.group()}'")