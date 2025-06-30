class User:
    def __init__(self, first_name, last_name, email):
        self.email = email
        # Create 'fullname' attribute by combining first and last name
        self.fullname = f"{first_name} {last_name}"

# Create an object from the User class and store it in variable 'colleen'
colleen = User("Colleen", "Van Lent", "colleen@example.com")

# --- ACCESSING ATTRIBUTES ---

# Use dot notation to access and print the 'fullname' attribute
print("Using correct syntax:")
print(f"Full name: {colleen.fullname}")
print(f"Email: {colleen.email}")

# --- INCORRECT SYNTAX EXAMPLES ---
print("\nExamples of incorrect syntax that will cause errors:")
try:
    # This is dictionary syntax, not the usual way to access object attributes
    print(colleen['fullname'])
except TypeError as e:
    print(f"Error when using colleen['fullname']: {e}")

# Syntax '->' and '::' will cause SyntaxError in Python
# print(colleen->fullname) # Causes SyntaxError
# print(colleen::fullname) # Causes SyntaxError
print("Syntax '->' or '::' will prevent the program from running (SyntaxError).")