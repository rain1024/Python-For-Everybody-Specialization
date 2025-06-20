import requests
from requests_oauthlib import OAuth1
import os

# --- Lấy credentials từ Developer Portal của X ---
# Tốt nhất là lưu chúng dưới dạng biến môi trường để bảo mật
# Ví dụ: os.environ.get("TWITTER_API_KEY")
api_key = "YOUR_API_KEY"  # Thay bằng API Key của bạn
api_secret_key = "YOUR_API_SECRET_KEY" # Thay bằng API Secret của bạn
access_token = "YOUR_ACCESS_TOKEN" # Thay bằng Access Token của bạn
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET" # Thay bằng Access Token Secret của bạn

# Kiểm tra xem credentials đã được điền chưa
if api_key == "YOUR_API_KEY":
    raise ValueError("Vui lòng thay thế các giá trị 'YOUR_..._KEY' bằng credentials thật từ X Developer Portal.")

# --- Tạo đối tượng xác thực OAuth1 ---
auth = OAuth1(api_key, api_secret_key, access_token, access_token_secret)

# --- Tạo nội dung tweet (payload) ---
# Endpoint để đăng tweet là API v2
url = "https://api.twitter.com/2/tweets"
payload = {"text": "Xin chào thế giới từ Python sử dụng requests và OAuth 1.0a! #Python"}

# --- Gửi yêu cầu POST ---
try:
    response = requests.post(url, auth=auth, json=payload)

    # --- Kiểm tra kết quả ---
    if response.status_code == 201:
        print("Đăng tweet thành công!")
        print("Dữ liệu trả về:")
        print(response.json())
    else:
        print(f"Lỗi khi đăng tweet: {response.status_code}")
        # In ra nội dung lỗi để dễ dàng gỡ rối
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Đã xảy ra lỗi kết nối: {e}")