#!/usr/bin/env python3

# Demonstration: How strings are stored internally in Python 3
# Answer: Unicode (strings are stored as Unicode internally)

print("=== Python 3 String Storage Demonstration ===")
print()

# 1. Basic string - internally stored as Unicode
text = "Hello, World!"
print(f"Basic string: {text}")
print(f"Type: {type(text)}")
print()

# 2. Unicode characters from different languages
unicode_text = "Hello 世界 مرحبا こんにちは"
print(f"Unicode text: {unicode_text}")
print(f"Length: {len(unicode_text)} characters")
print()

# 3. Show individual Unicode code points
print("Unicode code points:")
for i, char in enumerate(unicode_text[:5]):  # First 5 chars
    print(f"  '{char}' -> U+{ord(char):04X}")
print()

# 4. Demonstrate encoding to bytes (external representation)
print("=== Encoding to bytes (external storage) ===")
text_bytes_utf8 = unicode_text.encode('utf-8')
text_bytes_utf16 = unicode_text.encode('utf-16')

print(f"UTF-8 bytes: {text_bytes_utf8}")
print(f"UTF-16 bytes: {text_bytes_utf16}")
print(f"UTF-8 length: {len(text_bytes_utf8)} bytes")
print(f"UTF-16 length: {len(text_bytes_utf16)} bytes")
print()

# 5. Show that Python 3 strings are Unicode by default
print("=== Python 3 strings are Unicode by default ===")
emoji = "🐍 Python 🚀"
print(f"Emoji string: {emoji}")
print(f"Unicode code points for emoji:")
for char in emoji:
    if ord(char) > 127:  # Non-ASCII characters
        print(f"  '{char}' -> U+{ord(char):04X}")
print()

# 6. Demonstrate the difference with bytes
print("=== String vs Bytes ===")
string_obj = "Hello"
bytes_obj = b"Hello"

print(f"String object: {string_obj} (type: {type(string_obj)})")
print(f"Bytes object: {bytes_obj} (type: {type(bytes_obj)})")
print(f"Are they equal? {string_obj == bytes_obj}")
print()

print("Conclusion: Python 3 strings are stored internally as Unicode!")
print("This allows seamless handling of international characters.")
