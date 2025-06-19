import socket

# Tạo một socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến máy chủ 'data.pr4e.org' qua cổng 80 (cổng HTTP mặc định)
mysock.connect(('data.pr4e.org', 80))

# Chuẩn bị lệnh GET theo đúng chuẩn HTTP
# Chú ý: \r\n\r\n là dấu hiệu để máy chủ biết là đã hết phần header của yêu cầu
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# Gửi lệnh đi
mysock.send(cmd)

# Vòng lặp để nhận dữ liệu về
# Máy chủ sẽ gửi dữ liệu về từng mảng 512 byte một
print("DỮ LIỆU THÔ TỪ MÁY CHỦ GỬI VỀ:\n")
while True:
    data = mysock.recv(512)
    # Nếu không nhận được gì nữa, kết thúc vòng lặp
    if len(data) < 1:
        break
    # In dữ liệu đã được giải mã (decode) ra màn hình
    print(data.decode(), end='')

# Đóng kết nối
mysock.close()