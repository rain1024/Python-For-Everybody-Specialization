import urllib.parse
import urllib.request

# 1. Định nghĩa URL gốc của API
base_url = 'http://maps.googleapis.com/maps/api/geocode/json'

# 2. Tạo một dictionary chứa các tham số chúng ta muốn gửi đi
# Chú ý có dấu cách và dấu phẩy trong địa chỉ
params = {
    'sensor': 'false',
    'address': 'Ann Arbor, MI' 
}

# 3. Sử dụng urllib.parse.urlencode() để "đóng gói" các tham số
encoded_params = urllib.parse.urlencode(params)

# In ra để xem kết quả "đóng gói"
print(f"Các tham số sau khi mã hóa: {encoded_params}")
# Output: Các tham số sau khi mã hóa: sensor=false&address=Ann+Arbor%2CMI

# 4. Nối URL gốc với các tham số đã được mã hóa để tạo URL cuối cùng
final_url = base_url + '?' + encoded_params

print(f"URL hoàn chỉnh để gửi đi: {final_url}")
