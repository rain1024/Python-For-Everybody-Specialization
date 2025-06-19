import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

data = client_socket.recv(1024) # Nhận dữ liệu từ server
print(f"Server gửi: {data.decode('utf-8')}")

client_socket.close()