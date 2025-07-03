# Python Dictionary Demonstration - Key/Value Pairs

print("=== Python Dictionary Demo ===")
print()

# 1. Creating an empty dictionary
student_info = {}
print("1. Created empty dictionary:", student_info)
print()

# 2. Adding key/value pairs
student_info['name'] = 'Alice'
student_info['age'] = 20
student_info['major'] = 'Computer Science'
student_info['gpa'] = 3.8

print("2. Added key/value pairs:")
print("   student_info =", student_info)
print()

# 3. Accessing values using keys
print("3. Accessing values by keys:")
print("   Name:", student_info['name'])
print("   Age:", student_info['age'])
print("   Major:", student_info['major'])
print("   GPA:", student_info['gpa'])
print()

# 4. Creating a dictionary with initial values
course_grades = {
    'Python': 'A',
    'Math': 'B+',
    'Physics': 'A-',
    'English': 'B'
}

print("4. Dictionary created with initial values:")
print("   course_grades =", course_grades)
print()

# 5. Demonstrating that keys are unique
print("5. Keys are unique - updating existing key:")
course_grades['Math'] = 'A'  # Update existing key
print("   Updated Math grade:", course_grades['Math'])
print("   course_grades =", course_grades)
print()

# 6. Checking if a key exists
print("6. Checking if keys exist:")
if 'Python' in course_grades:
    print("   'Python' key exists with value:", course_grades['Python'])
if 'Chemistry' in course_grades:
    print("   'Chemistry' key exists")
else:
    print("   'Chemistry' key does not exist")
print()

# 7. Getting all keys and values
print("7. Getting all keys and values:")
print("   All keys:", list(course_grades.keys()))
print("   All values:", list(course_grades.values()))
print("   All key-value pairs:", list(course_grades.items()))
print()

print("=== Dictionary Summary ===")
print("• Dictionaries store data as key/value pairs")
print("• Keys must be unique")
print("• Values can be accessed using their keys")
print("• Perfect for storing related information!")
