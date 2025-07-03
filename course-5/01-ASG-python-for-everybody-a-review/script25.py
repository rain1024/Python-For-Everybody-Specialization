#!/usr/bin/env python3
"""
Simple JSON Demonstration Program
This program shows how JSON (JavaScript Object Notation) works
and demonstrates its relationship to JavaScript syntax.
"""

import json

def main():
    print("=== JSON Demonstration Program ===")
    print()
    
    # 1. Show what JSON looks like (JavaScript-like syntax)
    print("1. JSON Syntax (based on JavaScript object notation):")
    print("   JavaScript object: { name: 'John', age: 30, city: 'New York' }")
    print("   JSON format:       { \"name\": \"John\", \"age\": 30, \"city\": \"New York\" }")
    print()
    
    # 2. Create a Python dictionary (similar to JavaScript object)
    person = {
        "name": "Alice",
        "age": 25,
        "city": "San Francisco",
        "hobbies": ["reading", "swimming", "coding"],
        "is_student": False
    }
    
    print("2. Python dictionary:")
    print(f"   {person}")
    print()
    
    # 3. Convert Python dictionary to JSON string
    json_string = json.dumps(person, indent=2)
    print("3. Converting to JSON string:")
    print(json_string)
    print()
    
    # 4. Parse JSON string back to Python object
    parsed_data = json.loads(json_string)
    print("4. Parsing JSON back to Python:")
    print(f"   Name: {parsed_data['name']}")
    print(f"   Age: {parsed_data['age']}")
    print(f"   Hobbies: {parsed_data['hobbies']}")
    print()
    
    # 5. Show the answer to the quiz question
    print("5. Quiz Answer:")
    print("   Question: Which programming language serves as the basis for JSON syntax?")
    print("   Answer: JavaScript")
    print("   Explanation: JSON stands for 'JavaScript Object Notation'")
    print("   It uses the same syntax as JavaScript object literals.")
    print()
    
    # 6. Demonstrate JSON data types
    print("6. JSON supports these data types:")
    json_example = {
        "string": "Hello World",
        "number": 42,
        "float": 3.14,
        "boolean": True,
        "null_value": None,
        "array": [1, 2, 3, "four", 5.0],
        "object": {
            "nested": "value",
            "count": 10
        }
    }
    
    print(json.dumps(json_example, indent=2))

if __name__ == "__main__":
    main()
