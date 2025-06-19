import requests

# Send a GET request to vnexpress.net
response = requests.get('https://vnexpress.net')

# Print all headers
print("Headers from vnexpress.net:")
for header, value in response.headers.items():
    print(f"{header}: {value}")
