#!/usr/bin/env python3

# Simple ASCII Character Value Demonstration

print("=== ASCII Character Values Demo ===\n")

# Get the ASCII value of uppercase 'G'
char_g = 'G'
ascii_value_g = ord(char_g)
print(f"The ASCII value of '{char_g}' is: {ascii_value_g}")

# Answer to the quiz question
print(f"\nAnswer to the question: The decimal value for 'G' is {ascii_value_g}")

print("\n" + "="*40)
print("Other examples:")

# Show ASCII values for some other characters
characters = ['A', 'B', 'C', 'Z', 'a', 'g', 'z', '0', '9']

for char in characters:
    ascii_val = ord(char)
    print(f"'{char}' -> {ascii_val}")

print("\n" + "="*40)
print("Converting ASCII values back to characters:")

# Convert ASCII values back to characters
ascii_values = [65, 71, 97, 103, 48, 57]
for val in ascii_values:
    char = chr(val)
    print(f"{val} -> '{char}'")

print("\n" + "="*40)
print("Fun fact: ASCII values are in order!")
print("A-Z: 65-90")
print("a-z: 97-122") 
print("0-9: 48-57")
