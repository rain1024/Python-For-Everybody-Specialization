#!/usr/bin/env python3
"""
Simple demonstration: Where are variables stored in computer memory?

Answer: Variables are stored in MAIN MEMORY (RAM)
"""

print("=== Variable Storage Demonstration ===")
print()

# Create some variables
x = 123
name = "Alice"
temperature = 98.6
is_student = True

print("Creating variables:")
print(f"x = {x}")
print(f"name = '{name}'")
print(f"temperature = {temperature}")
print(f"is_student = {is_student}")
print()

print("Where are these variables stored?")
print("Answer: MAIN MEMORY (RAM)")
print()

print("Explanation:")
print("- When you create a variable like 'x = 123'")
print("- The computer stores this in Main Memory (RAM)")
print("- RAM is fast, temporary memory")
print("- Variables exist here while the program runs")
print("- When the program ends, variables are cleared from RAM")
print()

# Demonstrate memory addresses (where variables are stored)
print("Memory addresses (where variables are actually stored):")
print(f"x is stored at memory address: {id(x)}")
print(f"name is stored at memory address: {id(name)}")
print(f"temperature is stored at memory address: {id(temperature)}")
print()

print("These addresses are locations in Main Memory (RAM)!")
