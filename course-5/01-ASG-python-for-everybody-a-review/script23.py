#!/usr/bin/env python3
"""
Demonstration: Python Socket vs File Handle Differences
"""
import socket
import tempfile
import os

print("=== Python Socket vs File Handle Demonstration ===\n")

# 1. FILE HANDLE DEMONSTRATION
print("1. FILE HANDLE BEHAVIOR:")
print("-" * 30)

# Create a temporary file with some content
with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write("Hello from file!\nLine 2\nLine 3\n")
    temp_filename = temp_file.name

try:
    # Opening a file can fail (demonstrate error handling)
    with open(temp_filename, 'r') as file_handle:
        print("✓ File opened successfully")
        print("✓ File reads ALL content when requested:")
        content = file_handle.read()  # Reads all content at once
        print(f"  Content: {repr(content)}")
        
        # File handles are typically unidirectional for each open mode
        print("✗ Cannot write to file opened in read mode")
        
except FileNotFoundError:
    print("✗ File opening can fail if file doesn't exist")

finally:
    # Clean up
    os.unlink(temp_filename)

print("\n2. SOCKET DEMONSTRATION:")
print("-" * 30)

try:
    # Create a socket (this can also fail)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("✓ Socket created successfully")
    
    # Try to connect to a web server
    client_socket.connect(('httpbin.org', 80))
    print("✓ Socket connected successfully")
    
    # Send an HTTP request
    request = "GET /get HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"
    client_socket.send(request.encode())
    print("✓ Data sent through socket")
    
    # Socket does NOT read all data when opened - you must explicitly read
    print("✓ Socket requires explicit reading (doesn't read all data automatically):")
    
    # Read response in chunks
    response_data = b""
    chunk_count = 0
    while True:
        chunk = client_socket.recv(1024)  # Read in chunks
        if not chunk:
            break
        response_data += chunk
        chunk_count += 1
        if chunk_count <= 2:  # Show first few chunks
            print(f"  Chunk {chunk_count}: {len(chunk)} bytes received")
    
    print(f"  Total: {len(response_data)} bytes received in {chunk_count} chunks")
    print("✓ Same socket used for both sending AND receiving (bidirectional)")
    
except socket.error as e:
    print(f"✗ Socket operations can fail: {e}")
    
finally:
    client_socket.close()
    print("✓ Socket closed")

print("\n3. KEY DIFFERENCES SUMMARY:")
print("-" * 30)
print("File Handles:")
print("  • Read entire content when requested")
print("  • Usually unidirectional (read OR write per open)")
print("  • Work with local files")
print("  • Opening can fail if file doesn't exist")

print("\nSockets:")
print("  • Do NOT read all data when opened - must explicitly read")
print("  • Bidirectional (can read AND write on same socket)")
print("  • Work with network connections")
print("  • Opening/connecting can fail due to network issues")

print("\n✓ Answer to quiz: 'You can read and write using the same socket'")
print("  (Sockets are inherently bidirectional)")
