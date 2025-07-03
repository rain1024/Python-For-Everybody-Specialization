#!/usr/bin/env python3
"""
Simple demonstration of reading data from a URL and using decode() 
to convert bytes to strings in Python 3.

When reading data across the network in Python 3, the data comes as bytes.
The decode() method is used to convert these bytes to the internal string format.
"""

import urllib.request

def demonstrate_decode():
    """Demonstrate reading data from URL and converting bytes to string."""
    
    print("=== Demonstrating decode() method ===")
    print()
    
    # Read data from a simple URL
    url = "http://data.pr4e.org/romeo.txt"
    
    try:
        # Open the URL and read the data
        print(f"Reading data from: {url}")
        fhand = urllib.request.urlopen(url)
        
        # Read first few lines to demonstrate
        for i, line in enumerate(fhand):
            if i >= 3:  # Only show first 3 lines
                break
            
            print(f"Raw bytes (line {i+1}): {line}")
            print(f"Type: {type(line)}")
            
            # Convert bytes to string using decode()
            decoded_line = line.decode()
            print(f"Decoded string: {decoded_line.strip()}")
            print(f"Type after decode(): {type(decoded_line)}")
            print("-" * 50)
        
        fhand.close()
        
    except Exception as e:
        print(f"Error reading from URL: {e}")
        print()
        print("Let's demonstrate with a simple example instead:")
        
        # Simple demonstration with bytes
        raw_bytes = b"Hello, World!"
        print(f"Raw bytes: {raw_bytes}")
        print(f"Type: {type(raw_bytes)}")
        
        # Convert to string using decode()
        decoded_string = raw_bytes.decode()
        print(f"Decoded string: {decoded_string}")
        print(f"Type after decode(): {type(decoded_string)}")

if __name__ == "__main__":
    demonstrate_decode()
    
    print()
    print("=== Summary ===")
    print("In Python 3, when reading data from URLs:")
    print("• Data comes as bytes (b'...')")
    print("• Use decode() method to convert bytes to strings")
    print("• This is required for proper string manipulation")
    print()
    print("Answer to the quiz question: decode()")
