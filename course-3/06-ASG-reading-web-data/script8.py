import requests
from bs4 import BeautifulSoup

# Gửi request đến vnexpress.net
url = 'https://vnexpress.net'
response = requests.get(url)

# Tạo đối tượng BeautifulSoup để parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm tất cả thẻ 'a' (links)
all_links = soup('a')

# In ra tất cả các links
print(f'Tổng số links tìm thấy: {len(all_links)}\n')

# Lặp qua từng link và in ra href nếu có
for link in all_links:
    href = link.get('href')
    if href:  # Chỉ in ra những link có thuộc tính href
        print(href)
