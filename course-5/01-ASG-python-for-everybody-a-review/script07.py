# Demonstration of if-elif-else conditional logic
# This program shows why the order of conditions matters

print("=== If-Elif-Else Demonstration ===")
print()

# Test with different values of x
test_values = [1, 5, 15, 25]

for x in test_values:
    print(f"When x = {x}:")
    
    # The problematic code from the quiz
    if x < 2:
        print("  Below 2")
    elif x < 20:
        print("  Below 20")
    elif x < 10:  # This line will NEVER execute!
        print("  Below 10")
    else:
        print("  Something else")
    
    print()

print("=== Why 'Below 10' never prints ===")
print("The third condition 'x < 10' can never be reached because:")
print("- If x < 10, then x is also < 20, so the second condition catches it first")
print("- If x >= 20, then x < 10 is false")
print()

print("=== Corrected version ===")
print("Proper order: most specific conditions first")
print()

for x in test_values:
    print(f"When x = {x}:")
    
    # Corrected version with proper ordering
    if x < 2:
        print("  Below 2")
    elif x < 10:  # Now this can execute when 2 <= x < 10
        print("  Below 10")
    elif x < 20:  # This executes when 10 <= x < 20
        print("  Below 20")
    else:
        print("  Something else")
    
    print()
