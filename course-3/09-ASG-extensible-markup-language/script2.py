########################
# Dictionary
########################
a = {
    "name": "John"
}
print(a)

########################
# Json
########################
import json
print(json.dumps(a))

########################
# XML
########################
import xml.etree.ElementTree as ET

# Tạo XML element
data = ET.Element("data")
name = ET.SubElement(data, "name")
name.text = "John"

# Tạo XML string
xml_string = ET.tostring(data, encoding='unicode')
print(xml_string)

########################
# HTTP Request
########################
import requests

url = "https://www.google.com"
response = requests.get("https://www.google.com")
print(f"Protocol: {response.url.split('://')[0]}")

########################
# TCP
########################
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
s.send(cmd)

print("Gói tin TCP đã được gửi:")
print(f"Địa chỉ đích: data.pr4e.org:80")
print(f"Nội dung gói tin: {cmd.decode()}")
print("-" * 50)

while True:
    data = s.recv(512)
    if len(data) < 1:
        break
    print("Dữ liệu nhận được:", data.decode(), end="")

s.close()


