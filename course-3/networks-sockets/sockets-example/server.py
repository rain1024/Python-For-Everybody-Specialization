import socket

# Bước 1: Khai báo host và port
# Host là địa chỉ IP mà server sẽ lắng nghe.
# '127.0.0.1' là địa chỉ loopback (localhost), nghĩa là server chỉ chấp nhận kết nối từ chính máy này.
# Nếu bạn muốn server chấp nhận kết nối từ bất kỳ địa chỉ nào, hãy dùng '0.0.0.0' hoặc rỗng ''.
HOST = '127.0.0.1'
# Port là số cổng mà server sẽ lắng nghe. Chọn một số cổng trống (thường là > 1024 để tránh các cổng hệ thống).
PORT = 65432

# Bước 2: Tạo một đối tượng socket
# socket.AF_INET: Chỉ định rằng chúng ta sẽ sử dụng địa chỉ IPv4.
# socket.SOCK_STREAM: Chỉ định rằng chúng ta sẽ sử dụng TCP (Transmission Control Protocol),
#                     là một giao thức hướng kết nối (connection-oriented).
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bước 3: Gán địa chỉ (bind) cho socket
# Gán socket với một địa chỉ IP và một số cổng cụ thể.
try:
    server_socket.bind((HOST, PORT))
    print(f"Server lắng nghe trên {HOST}:{PORT}")
except socket.error as e:
    print(f"Lỗi khi gán địa chỉ socket: {e}")
    server_socket.close()
    exit()

# Bước 4: Lắng nghe kết nối đến (listen)
# Bắt đầu lắng nghe các kết nối đến. Đối số '5' là số lượng kết nối tối đa có thể xếp hàng đợi.
server_socket.listen(5)
print("Đang chờ kết nối từ client...")

# Bước 5: Chấp nhận kết nối và xử lý (accept and handle)
# Vòng lặp vô hạn để server luôn sẵn sàng chấp nhận các kết nối mới.
while True:
    # server_socket.accept() trả về một cặp:
    #   - conn: là một đối tượng socket mới đại diện cho kết nối với client.
    #   - addr: là địa chỉ (IP, port) của client đã kết nối.
    conn, addr = server_socket.accept()
    print(f"Đã kết nối từ: {addr}")

    try:
        # Gửi dữ liệu đến client
        message = "Chào mừng bạn đến với Server Python đơn giản!\n"
        # encode('utf-8') để chuyển chuỗi thành bytes trước khi gửi qua mạng
        conn.sendall(message.encode('utf-8'))

        # Có thể nhận dữ liệu từ client nếu muốn
        # data = conn.recv(1024) # Nhận tối đa 1024 bytes
        # if data:
        #     print(f"Client gửi: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Lỗi trong quá trình xử lý kết nối: {e}")
    finally:
        # Đóng kết nối với client hiện tại
        conn.close()
        print(f"Đã đóng kết nối với {addr}")

# Lưu ý: Trong ví dụ này, server sẽ chạy vô hạn. Để dừng, bạn cần nhấn Ctrl+C trong terminal.
# Trong ứng dụng thực tế, bạn sẽ có cơ chế thoát vòng lặp hoặc xử lý nhiều kết nối đồng thời (multithreading/asyncio).