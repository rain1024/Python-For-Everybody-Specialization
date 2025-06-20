import requests
from datetime import datetime

# --- Thay thế bằng Bearer Token của bạn ---
bearer_token = "YOUR_BEARER_TOKEN"
if bearer_token == "YOUR_BEARER_TOKEN":
    raise ValueError("Vui lòng thay thế 'YOUR_BEARER_TOKEN' bằng credential thật từ X Developer Portal.")

def create_headers(token):
    """Tạo header xác thực."""
    return {"Authorization": f"Bearer {token}"}

def check_user_info_and_rate_limit(username):
    """
    Lấy thông tin người dùng và kiểm tra rate limit.
    """
    # Endpoint để lấy thông tin người dùng theo username
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = create_headers(bearer_token)
    
    try:
        response = requests.get(url, headers=headers)
        
        # Lấy thông tin rate limit từ headers của response
        # Dùng response.headers.get() để tránh lỗi nếu header không tồn tại
        limit = response.headers.get('x-rate-limit-limit')
        remaining = response.headers.get('x-rate-limit-remaining')
        reset_timestamp = response.headers.get('x-rate-limit-reset')
        
        print("--- Trạng Thái Rate Limit ---")
        if all([limit, remaining, reset_timestamp]):
            # Chuyển đổi timestamp sang định dạng ngày giờ dễ đọc
            reset_time = datetime.utcfromtimestamp(int(reset_timestamp)).strftime('%Y-%m-%d %H:%M:%S UTC')
            
            print(f"Giới hạn yêu cầu (Limit): {limit}")
            print(f"Số yêu cầu còn lại (Remaining): {remaining}")
            print(f"Thời gian reset (Reset): {reset_time} ({reset_timestamp})")
        else:
            print("Không tìm thấy thông tin rate limit trong header.")
        
        print("\n--- Kết Quả API ---")
        # Kiểm tra mã trạng thái của yêu cầu
        if response.status_code == 200:
            print("Yêu cầu thành công!")
            print("Dữ liệu người dùng:", response.json())
        elif response.status_code == 429:
            print("LỖI: Đã vượt quá giới hạn Rate Limit (Too Many Requests).")
            print("Vui lòng đợi đến thời gian reset để thử lại.")
        else:
            print(f"Lỗi: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Đã xảy ra lỗi kết nối: {e}")

# --- Sử dụng hàm ---
# Thay 'TwitterDev' bằng username bạn muốn kiểm tra
check_user_info_and_rate_limit('TwitterDev')