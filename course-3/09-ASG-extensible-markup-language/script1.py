import json

# 1. Dữ liệu gốc trong chương trình Python (giống như "chiếc bánh")
# Đây là một đối tượng dictionary
user_profile = {
    "username": "python_lover",
    "id": 123,
    "is_active": True,
    "courses": ["Python Basic", "Web Development"]
}

print(f"Kiểu dữ liệu ban đầu: {type(user_profile)}")
print("Dữ liệu gốc:", user_profile)
print("-" * 30)

# 2. SERIALIZATION: Chuyển dictionary thành một chuỗi JSON để gửi đi
# (Giống như "viết công thức ra giấy")
# hàm json.dumps() thực hiện việc này (dump string)
json_string = json.dumps(user_profile, indent=4) # indent=4 để in cho đẹp

print(f"Kiểu dữ liệu sau khi serialize: {type(json_string)}")
print("Dữ liệu đã serialize (chuỗi JSON):")
print(json_string)
print("-" * 30)

# 3. DESERIALIZATION: Giả sử máy khách nhận được chuỗi JSON này
# và muốn chuyển nó ngược lại thành dictionary để sử dụng
# (Giống như "đọc công thức và làm lại bánh")
# hàm json.loads() thực hiện việc này (load string)
recreated_profile = json.loads(json_string)

print(f"Kiểu dữ liệu sau khi deserialize: {type(recreated_profile)}")
print("Dữ liệu đã deserialize (quay về dictionary):", recreated_profile)

# Kiểm tra xem dữ liệu có giống ban đầu không
assert user_profile == recreated_profile
print("\n=> Dữ liệu sau khi phục hồi giống hệt ban đầu!")