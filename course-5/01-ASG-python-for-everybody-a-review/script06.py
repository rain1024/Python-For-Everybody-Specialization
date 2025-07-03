#!/usr/bin/env python3
"""
Demonstration of if-elif-else logic flow
This program shows why one of the conditions will never execute
"""

def test_conditions(x):
    """Test the if-elif-else conditions with a given value of x"""
    print(f"\nTesting with x = {x}")
    
    if x < 2:
        print("Below 2")
    elif x < 0:
        print("Negative")  # This will NEVER execute!
    else:
        print("Something else")

def simple_quiz_demo():
    """Simple demonstration of the exact quiz question"""
    print("=== QUIZ QUESTION DEMO ===")
    print("Code:")
    print("if x < 2 :")
    print("    print('Below 2')")
    print("elif x < 0 :")
    print("    print('Negative')")
    print("else :")
    print("    print('Something else')")
    print()
    
    # Test with different values
    test_values = [-10, -1, 0, 1, 1.5, 2, 5]
    for x in test_values:
        print(f"x = {x}:")
        if x < 2:
            print("  → Below 2")
        elif x < 0:
            print("  → Negative")
        else:
            print("  → Something else")

def main():
    print("=== If-Elif-Else Logic Demonstration ===")
    print("\nThe question: Which line will never print regardless of x?")
    print("Answer: 'Negative' will never print!")
    print("\nWhy? Because if x < 0, then x < 2 is also true.")
    print("The first condition (x < 2) catches all negative numbers first.")
    
    print("\n" + "="*50)
    print("Testing different values of x:")
    
    # Test various values to demonstrate
    test_values = [-5, -1, 0, 1, 2, 3, 10]
    
    for x in test_values:
        test_conditions(x)
    
    print("\n" + "="*50)
    simple_quiz_demo()
    
    print("\n" + "="*50)
    print("CONCLUSION:")
    print("The line 'print(\"Negative\")' will NEVER execute because:")
    print("1. If x is negative (x < 0), then x < 2 is also true")
    print("2. Python evaluates conditions in order")
    print("3. Once the first condition (x < 2) is true, it skips the rest")
    print("4. So negative numbers are caught by 'Below 2', not 'Negative'")

if __name__ == "__main__":
    main()
