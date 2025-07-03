# Python String Indexing Demonstration

# Example from the quiz question
zap = "hello there bob"
print("String:", zap)
print("Length:", len(zap))
print()

# Show each character with its index
print("Character positions:")
for i in range(len(zap)):
    print(f"Index {i}: '{zap[i]}'")
print()

# Answer the quiz question
print("Quiz Question: What does zap[4] print?")
print("Answer:", zap[4])
print()

# More examples of string indexing
print("More String Indexing Examples:")
text = "Python"
print(f"String: '{text}'")
print(f"First character (index 0): '{text[0]}'")
print(f"Second character (index 1): '{text[1]}'")
print(f"Last character (index -1): '{text[-1]}'")
print(f"Second to last (index -2): '{text[-2]}'")
print()

# Show what happens with different indices
print("Testing different indices:")
try:
    print(f"Index 5: '{text[5]}'")  # Last valid index
    print(f"Index 6: '{text[6]}'")  # This will cause an error
except IndexError as e:
    print(f"Index 6 caused an error: {e}")
print()

# Demonstrate that strings are zero-indexed
print("Remember: Python uses zero-based indexing!")
print("This means the first character is at index 0, not 1")
