def ascii_to_word(numbers):
    # Convert ASCII numbers to characters and join them
    word = ''.join(chr(num) for num in numbers)
    return word

# The sequence of ASCII numbers
ascii_numbers = [108, 105, 110, 101]

# Convert and print the result
result = ascii_to_word(ascii_numbers)
print(f"The ASCII numbers {ascii_numbers} represent the word: {result}")
