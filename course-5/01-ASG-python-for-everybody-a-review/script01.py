#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple UTF-8 String Demonstration
This program shows how Python handles UTF-8 encoded strings
"""

def main():
    print("=== UTF-8 String Demonstration ===\n")
    
    # 1. Basic ASCII strings (subset of UTF-8)
    print("1. Basic ASCII strings:")
    ascii_string = "Hello, World!"
    print(f"   {ascii_string}")
    print(f"   Length: {len(ascii_string)} characters")
    print(f"   Encoded bytes: {ascii_string.encode('utf-8')}")
    print()
    
    # 2. International characters
    print("2. International characters:")
    international_strings = [
        "Hello in French: Bonjour",
        "Hello in Spanish: Hola",
        "Hello in German: Hallo",
        "Hello in Japanese: こんにちは",
        "Hello in Chinese: 你好",
        "Hello in Arabic: مرحبا",
        "Hello in Russian: Привет"
    ]
    
    for text in international_strings:
        print(f"   {text}")
        print(f"   UTF-8 bytes: {len(text.encode('utf-8'))} bytes")
    print()
    
    # 3. Special characters and symbols
    print("3. Special characters and symbols:")
    special_chars = "©️ ® ™ € £ ¥ ° ± × ÷ ∞ π α β γ"
    print(f"   {special_chars}")
    print(f"   Character count: {len(special_chars)}")
    print(f"   UTF-8 byte count: {len(special_chars.encode('utf-8'))}")
    print()
    
    # 4. Emojis (multi-byte UTF-8)
    print("4. Emojis (multi-byte UTF-8):")
    emojis = "😀 😃 😄 😁 😊 😍 🌟 🎉 🚀 🌈 ❤️ 🔥"
    print(f"   {emojis}")
    print(f"   Character count: {len(emojis)}")
    print(f"   UTF-8 byte count: {len(emojis.encode('utf-8'))}")
    print()
    
    # 5. Encoding and decoding demonstration
    print("5. Encoding and decoding:")
    original = "Python is awesome! 🐍"
    print(f"   Original string: {original}")
    
    # Encode to bytes
    encoded = original.encode('utf-8')
    print(f"   Encoded to UTF-8 bytes: {encoded}")
    print(f"   Byte length: {len(encoded)}")
    
    # Decode back to string
    decoded = encoded.decode('utf-8')
    print(f"   Decoded back to string: {decoded}")
    print(f"   Strings match: {original == decoded}")
    print()
    
    # 6. Working with different encodings
    print("6. Different encodings comparison:")
    text = "Café"
    print(f"   Original: {text}")
    
    encodings = ['utf-8', 'latin-1', 'ascii']
    for encoding in encodings:
        try:
            encoded = text.encode(encoding)
            print(f"   {encoding}: {encoded}")
        except UnicodeEncodeError as e:
            print(f"   {encoding}: Error - {e}")
    print()
    
    # 7. File operations with UTF-8
    print("7. File operations with UTF-8:")
    filename = "utf8_demo.txt"
    content = "UTF-8 test: Hello 世界 🌍"
    
    # Write UTF-8 content to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"   Written to {filename}: {content}")
    
    # Read UTF-8 content from file
    with open(filename, 'r', encoding='utf-8') as f:
        read_content = f.read()
    print(f"   Read from {filename}: {read_content}")
    print(f"   Content matches: {content == read_content}")
    
    # Clean up
    import os
    os.remove(filename)
    print(f"   Cleaned up: {filename} removed")
    print()
    
    print("=== End of UTF-8 Demonstration ===")

if __name__ == "__main__":
    main()
