import requests
import json # Thư viện json để in đẹp hơn

# --- PHẦN CẤU HÌNH ---
# Thay 'YOUR_API_KEY' bằng API Key thật của bạn
API_KEY = 'YOUR_API_KEY' 

# Địa chỉ bạn muốn tìm kiếm
address_to_find = '1600 Amphitheatre Parkway, Mountain View, CA'
# Thử một địa chỉ ở Việt Nam: 'Dinh Độc Lập, Quận 1, TP.HCM'

# URL gốc của Google Geocoding API
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

# --- XÂY DỰNG YÊU CẦU ---
# Tạo một dictionary chứa các tham số
# requests sẽ tự động mã hóa chúng vào URL
params = {
    'address': address_to_find,
    'key': API_KEY,
    'language': 'vi' # Yêu cầu kết quả trả về bằng tiếng Việt
}

print(f"Đang gửi yêu cầu đến Google API để tìm địa chỉ: '{address_to_find}'...")