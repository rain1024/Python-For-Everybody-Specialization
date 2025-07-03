# Simple ASCII Conversion Demonstration
# Converting ASCII numbers to characters

# The ASCII values from the question
ascii_values = [108, 105, 115, 116]

print("ASCII Conversion Demo")
print("=" * 25)

# Convert each ASCII value to its character
print("ASCII values:", ascii_values)
print("Converted characters:")

word = ""
for value in ascii_values:
    char = chr(value)
    print(f"ASCII {value} = '{char}'")
    word += char

print(f"\nThe complete word is: '{word}'")

# Bonus: Show the reverse conversion
print("\nReverse conversion (char to ASCII):")
for char in word:
    print(f"'{char}' = ASCII {ord(char)}")
