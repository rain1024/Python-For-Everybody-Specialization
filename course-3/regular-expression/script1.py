import re

text = "abc123XYZ456_!@#"

pattern = r'[a-z0-9]'
matches = re.findall(pattern, text)
print(f"Các ký tự khớp: {matches}")