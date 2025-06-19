import re

filename = input("Enter file name (default: regex_sum_2242323.txt): ").strip()
if not filename:
    filename = 'regex_sum_2242323.txt'

try:
    with open(filename, 'r') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    exit(1)

# Find all numbers using regex
numbers = re.findall(r'\d+', contents)

# Convert to integers and sum
numbers = [int(num) for num in numbers]
total = sum(numbers)

print(f"Sum: {total}")
